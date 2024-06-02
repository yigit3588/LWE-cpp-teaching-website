
import mysql.connector
from flask import Flask, render_template, request, redirect, url_for, session,jsonify
from model import *
from utils import *
from compiler import CppCodeCompiler
import os
import uuid
import re

app = Flask(__name__)
app.secret_key = 'sifrelebeni'

#http://localhost/
#http://localhost
@app.route("/")
def index():
    return render_template('index.html')

#http://localhost/register
@app.route("/register")
def register():
    return render_template('register.html')

#http://localhost/register-complated
@app.route("/register-complated" , methods=['POST'])
def register_complated():
    # email = request.form.get('email')
    name            = request.form.get('name')
    surname         = request.form.get('surname')
    email           = request.form.get('email')
    password        = request.form.get('password')
    password_again  = request.form.get('password_again')
    special_key     = str(uuid.uuid4())


    if password != password_again :
        #return redirect("/register")
        return render_template('register.html',  r_name = name, r_surname = surname, r_email = email, message="Passwords are not matching.")
    
    student = email_exist_check(email)

    if student is not None:
        return render_template('register.html',  r_name = name, r_surname = surname, r_email = email, message="This email is already exist.")


    add_student(name, surname, email, password, special_key)

    #return redirect("https://google.com")
    return redirect(url_for("login"))


#http://localhost/login
@app.route("/login")
def login():
    if session.get('is_login'):
        return redirect('/')
    return render_template('login.html')

@app.route('/forget-password')
def forget_password():
    return render_template('forget_password.html')

@app.route('/forget-password-send-email', methods=['POST'])
def forget_password_send_email():
    email       = request.form.get('email')
    student     = email_exist_check(email)
    print(student)
    if student == None:
        return redirect(url_for('forget_password', status=False))
    
    message = f"""
        <p>
            We have sent you this email regarding your password reset request.<br>
            You can continue the process by clinging on th link :<br>
            <a href="{request.url_root}new-password/{student.get('special_key')}">New Password</a>
        </p>
    """
    email_sender("LWE - RESET EMAIL", email, message)
    return redirect(url_for('password_email_send_info'))

@app.route('/password-email-send-info')
def password_email_send_info():
    return render_template('password_email_send_info.html')

@app.route('/new-password/<string:special_key>')
def new_password(special_key):
    student = get_student_by_special_key(special_key)
    if student == None:
        return render_template('change_password_timeout.html')
    return render_template("new_password.html", special_key=special_key)

@app.route("/new-password-completed", methods=['POST'])
def new_password_completed():

    special_key         = request.form.get('special_key')
    password            = request.form.get('password')
    password_again      = request.form.get('password_again')
    new_special_key     = str(uuid.uuid4())
    

    if password != password_again:
        return redirect(f'/new-password/{special_key}?status=false&message=New passwords are not matching !')
    
    update_password_by_special_key(password, special_key, new_special_key)
    
    return redirect(f'/new-password/{new_special_key}?status=true&message=Password Changed Successfully !')


#http://localhost/login-completed
@app.route("/login-completed", methods=['POST'])
def login_completed():

    email = request.form.get('email')
    password = request.form.get('password')

    student = student_check(email, password)
    
    if student is None :
        return redirect(url_for('login', email = email, message = "Invalid email or password"))
        #return render_template('login.html',r_email = email, message = "Invalid email or password")

    session['is_login'] = True
    session['id']       = student.get('id')
    session['name']     = student.get('name')   
    session['surname']  = student.get('surname')   
    session['type']     = student.get('type')
    return redirect('/')

@app.route("/logout")
def logout():
    session.clear()
    return redirect('/')

@app.route("/profile")
def profile():
    if not session.get('is_login'):
        return redirect('/')
    
    student = get_student_by_id(session.get('id'))
    #print(student)
    return render_template('profile.html', student = student)

@app.route("/profile-update", methods=['POST'])
def profile_update():
    id      = session.get('id')
    name    = request.form.get('name')
    surname = request.form.get('surname')
    email   = request.form.get('email')

    update_student(id, name, surname, email)

    #UPDATE students SET name = 'Tekin', surname = 'POLAT', email = 'tekin.polat@gmail.com' WHERE id = 2;


    return redirect(url_for('profile'))


@app.route("/change-password")
def change_password():
    return render_template('change_password.html')


@app.route("/change-password-completed", methods=['POST'])
def change_password_completed():
    id                      = session.get('id')
    current_password        = request.form.get('current_password')
    new_password            = request.form.get('new_password')
    new_password_again      = request.form.get('new_password_again')

    student = get_student_by_id(id)

    if student.get('password') != current_password:
        return redirect(url_for('change_password', message='Current password is wrong !'))
    
    if new_password != new_password_again:
        return redirect(url_for('change_password', message='New passwords are not matching !'))

    change_student_password(id, new_password)
    return redirect(url_for('profile', message= 'Password Changed Successfully !'))



@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/send-message", methods=['POST'])
def send_message():
    name_surname    = request.form.get('name_surname')
    email           = request.form.get('email')
    message         = request.form.get('message')
    message_send_to_db(name_surname, email, message)

    return redirect(url_for('about', message='Your message has been sent successfully'))



#admin
@app.route('/admin/messages')
def admin_read_messages():
    if session.get('type') != 'admin':
        return redirect('/')
    
    
    messages = get_messages()

    return render_template("admin/messages.html", messages=messages)


@app.route('/admin/topic-manager')
def  topic_manager():
    if session.get('type') != 'admin':
        return redirect('/')
    
    topics = get_topics()

    #print(topics)
    return render_template("admin/topics.html", topics=topics)


@app.route('/admin/add-topic')
def add_topic():
    if session.get('type') != 'admin':
        return redirect('/')
    return render_template('admin/topic_add.html')



@app.route('/admin/add-topic-completed', methods=['POST'])
def add_topic_completed():
    if session.get('type') != 'admin':
        return redirect('/')

    title       = request.form.get('title')
    content     = request.form.get('content')
    slug        = string_to_slug(title)

    add_topic_db(title, content, slug)
    return redirect('/admin/topic-manager')

@app.route('/admin/delete-topic/<int:id>')
def delete_topic(id):
    if session.get('type') != 'admin':
        return redirect('/')

    delete_topic_db(id)
    return redirect('/admin/topic-manager')

@app.route('/admin/edit-topic/<int:id>')
def edit_topic(id):
    if session.get('type') != 'admin':
        return redirect('/')    
    
    topic = get_topic_by_id(id)
    return render_template('admin/topic_edit.html', topic=topic)

@app.route('/admin/edit-topic-completed',methods=['POST'])
def edit_topic_completed():
    if session.get('type') != 'admin':
        return redirect('/')
    
    id          = request.form.get('id')
    title       = request.form.get('title')
    content     = request.form.get('content')
    slug        = string_to_slug(title)

    update_topic(id, title, content, slug)
    return redirect('/admin/topic-manager')

@app.route("/topics")
def topics():
    topics = get_topics()
    return render_template('topics.html', topics=topics)

@app.route('/topics/<string:slug>/<int:id>')
def show_topic(slug, id):
    topic = get_topic_by_id(id)
    topics = get_topics()
    return render_template('topic.html', topic=topic, topics=topics)

@app.route('/admin/question-manager')
def  question_manager():
    if session.get('type') != 'admin':
        return redirect('/')
    
    questions = get_questions()

    
    return render_template("admin/questions.html", questions=questions)

@app.route('/admin/add-question')
def add_question():
    if session.get('type') != 'admin':
        return redirect('/')
    return render_template('admin/question_add.html')

@app.route('/admin/add-question-completed', methods=['POST'])  
def add_question_completed():
    if session.get('type') != 'admin':
        return redirect('/')

    title               = request.form.get('title')
    instructions        = request.form.get('instructions')
    solution            = request.form.get('solution')
    test_case           = request.form.get('test_case')
    slug                = string_to_slug(title)

    add_question_db(title, instructions, solution, test_case, slug)

    return redirect('/admin/question-manager')

@app.route('/admin/delete-question/<int:id>')
def delete_question(id):
    if session.get('type') != 'admin':
        return redirect('/')

    delete_question_db(id)
    return redirect('/admin/question-manager')

@app.route('/admin/edit-question/<int:id>')
def edit_question(id):
    if session.get('type') != 'admin':
        return redirect('/')    
    
    question = get_question_by_id(id)
    return render_template('admin/question_edit.html', question=question)

@app.route('/admin/edit-question-completed',methods=['POST'])
def edit_question_completed():
    if session.get('type') != 'admin':
        return redirect('/')
    
    id                  = request.form.get('id')
    title               = request.form.get('title')
    instructions        = request.form.get('instructions')
    solution            = request.form.get('solution')
    test_case           = request.form.get('test_case')
    slug                = string_to_slug(title)

    update_question(id, title, instructions, solution, test_case, slug)
    return redirect('/admin/question-manager')


@app.route("/questions")
def questions():
    solved_questions_id = []
    if session.get('is_login'):
        solved_questions = get_solved_questions_by_student_id(session.get('id'))
        for solved_question in solved_questions:
            solved_questions_id.append(solved_question.get('question_id'))

        
    questions = get_questions()
    return render_template('questions.html', questions=questions, solved_questions_id=solved_questions_id)

@app.route('/question/<string:slug>/<int:id>')
def question(slug, id):
    if not session.get('is_login'):
        return redirect('/')
    
    solved_question = get_solved_question_by_student_and_question_id(id, session.get('id'))
    question = get_question_by_id(id)

    if solved_question != None:
        question['solution'] = solved_question.get('code')

    return render_template('question.html',question=question)

@app.route('/solved-questions-completed',methods=['POST'])
def solved_questions_completed():
    question_id     = request.form.get('question_id')
    original_code   = request.form.get('code')

    filename = f"std-id-{session.get('id')}-question-id-{question_id}"

    question = get_question_by_id(question_id)

    cpp_code = CppCodeCompiler(f"{original_code}\n{question.get('test_case')}", filename)
    cpp_compiled_code = cpp_code.run_cpp_code()

    if cpp_compiled_code[0] != '':
        print(cpp_compiled_code[0])
        return jsonify(message= re.sub(r'\r\n|\n', '<br>', cpp_compiled_code[0]) , status=False)

    output_code     = [ result for result in re.split(r"\r\n|\n",cpp_compiled_code[1]) if result.strip() != '']
    expected_code   = [ result for result in re.split(r"\r\n|\n",question.get('results'))  if result.strip() != '' ]


    #delete compiled files
    
    os_type = '.exe' if os.name == 'nt' else '.out'
    os.remove(f"cpp-files/{filename}.cpp")
    os.remove(f"{filename}{os_type}")

    is_all_test_equal = True
    message = '<ul class="list-group">'
    for (output, expected) in zip(output_code, expected_code):
        if output == expected:
            message += f"""<li class="list-group-item text-success">
                <i class="fa-regular fa-circle-check"></i> {output} == {expected}
            </li>"""
        else:
            is_all_test_equal = False
            message += f"""<li class="list-group-item text-danger">
                <i class="fa-regular fa-circle-xmark"></i> {output} != {expected}
            </li>"""
    message += '</ul>'

    if is_all_test_equal:
        update_or_add_solved_question(session.get('id'), question_id, original_code)

    return jsonify(message=message, status=True)
app.run(host="0.0.0.0", port=80, debug=True)



