import mysql.connector
from datetime import datetime

thesis_db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="3588",
  database="thesis",
  auth_plugin='mysql_native_password'
)




def student_check(email , password):

    mycursor = thesis_db.cursor(dictionary=True)

    mycursor.execute("SELECT * FROM students WHERE email = %s AND password = %s", (email,password))
    student = mycursor.fetchone()

    mycursor.close()

    return student

def email_exist_check(email):

    mycursor = thesis_db.cursor(dictionary=True)

    # sql = "SELECT * FROM students WHERE email = %s"
    # val = (email,)
    mycursor.execute("SELECT * FROM students WHERE email = %s", (email,))
    student = mycursor.fetchone()
    mycursor.close()

    return student

def add_student(name, surname, email, password, special_key):

    mycursor = thesis_db.cursor()

    sql = "INSERT INTO students (name, surname, email, password, special_key) VALUES (%s, %s, %s, %s, %s)"
    val = (name, surname, email, password, special_key)

    mycursor.execute(sql, val)
    thesis_db.commit()

    mycursor.close()

def add_topic_db(title, content, slug):

    mycursor = thesis_db.cursor()

    sql = "INSERT INTO topics (title, content, slug) VALUES (%s, %s, %s)"
    val = (title, content, slug)

    mycursor.execute(sql, val)
    thesis_db.commit()

    mycursor.close()

def add_question_db(title, instructions, solution, test_case,results, slug):

    mycursor = thesis_db.cursor()

    sql = "INSERT INTO questions (title,instructions, solution, test_case, results, slug) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (title, instructions, solution, test_case, results, slug)

    mycursor.execute(sql, val)
    thesis_db.commit()

    mycursor.close()
    
def message_send_to_db(name_surname, email, message):
    mycursor = thesis_db.cursor()

    sql = "INSERT INTO messages (name_surname, email, message) VALUES (%s, %s, %s)"
    val = (name_surname, email, message)
    mycursor.execute(sql, val)
    thesis_db.commit()

    mycursor.close()

def get_student_by_id(id):
    mycursor = thesis_db.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM students WHERE id = %s", (id,))
    student = mycursor.fetchone()
    mycursor.close()

    return student

def get_student_by_email(email):
    mycursor = thesis_db.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM students WHERE email = %s", (email,))
    student = mycursor.fetchone()
    mycursor.close()

    return student

def get_student_by_special_key(special_key):
    mycursor = thesis_db.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM students WHERE special_key = %s", (special_key,))
    student = mycursor.fetchone()
    mycursor.close()

    return student

def get_solved_questions_by_student_id(student_id):
    mycursor = thesis_db.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM solved_questions WHERE student_id = %s", (student_id,))
    solved_questions = mycursor.fetchall()
    mycursor.close()
    return solved_questions

def get_solved_question_by_student_and_question_id(question_id, student_id):

    mycursor = thesis_db.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM solved_questions WHERE student_id = %s AND question_id = %s", (student_id, question_id))
    solved_question_answer = mycursor.fetchone()
    mycursor.close()
    return solved_question_answer    

def get_messages():
    mycursor = thesis_db.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM messages ORDER BY id DESC")
    messages = mycursor.fetchall()
    mycursor.close()

    return messages

def get_topics():
    mycursor = thesis_db.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM topics")
    topics = mycursor.fetchall()
    mycursor.close()

    return topics

def get_questions():
    mycursor = thesis_db.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM questions")
    questions = mycursor.fetchall()
    mycursor.close()

    return questions

def get_topic_by_id(id):
    mycursor = thesis_db.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM topics WHERE id = %s", (id,))
    topic = mycursor.fetchone()
    mycursor.close()

    return topic

def get_question_by_id(id):
    mycursor = thesis_db.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM questions WHERE id = %s", (id,))
    question = mycursor.fetchone()
    mycursor.close()

    return question

def update_topic(id, title, content, slug):
    mycursor = thesis_db.cursor()
    mycursor.execute("UPDATE topics SET title = %s, content = %s, slug = %s WHERE id = %s", 
                     (title, content, slug, id))
    thesis_db.commit()
    mycursor.close()

def update_question(id, title, instructions, solution, test_case, results, slug):
    mycursor = thesis_db.cursor()
    mycursor.execute("UPDATE questions SET title = %s, instructions = %s, solution = %s, test_case = %s,results = %s, slug = %s WHERE id = %s", 
                     (title, instructions, solution, test_case, results, slug, id))
    thesis_db.commit()
    mycursor.close()

def update_student(id, name, surname, email):
    mycursor = thesis_db.cursor()
    mycursor.execute("UPDATE students SET name = %s, surname = %s, email = %s WHERE id = %s", 
                     (name, surname, email, id))
    thesis_db.commit()
    mycursor.close()

def update_password_by_special_key(password, special_key, new_special_key):
    mycursor = thesis_db.cursor()
    mycursor.execute("UPDATE students SET password = %s, special_key= %s WHERE special_key = %s", 
                     (password, new_special_key, special_key))
    thesis_db.commit()
    mycursor.close()

def update_or_add_solved_question(student_id, question_id, code):
    #solved_quesiton = get_solved_question_by_student_and_question_id(student_id, question_id)
    mycursor = thesis_db.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM solved_questions WHERE student_id = %s AND question_id = %s", (student_id, question_id))
    solved_quesiton = mycursor.fetchone()
    mycursor.close()

    date = datetime.now()
    date = date.strftime("%Y-%m-%d %H:%M:%S")
    if solved_quesiton != None:
        mycursor = thesis_db.cursor()
        mycursor.execute("UPDATE solved_questions SET code = %s, `date` = %s WHERE student_id = %s AND question_id = %s ", 
                        (code, date, student_id, question_id))
        thesis_db.commit()
        mycursor.close()
    else:
        mycursor = thesis_db.cursor()
        sql = "INSERT INTO solved_questions (student_id, question_id, code, `date`) VALUES (%s, %s, %s, %s)"
        val = (student_id, question_id, code, date)
        mycursor.execute(sql, val)
        thesis_db.commit()
        mycursor.close()

def change_student_password(id,new_password):
    mycursor = thesis_db.cursor()
    mycursor.execute("UPDATE students SET password = %s WHERE id = %s",  (new_password, id))
    thesis_db.commit()
    mycursor.close()

def delete_topic_db(id):
    mycursor = thesis_db.cursor()
    mycursor.execute("DELETE from topics WHERE id = %s", (id,))
    thesis_db.commit()
    mycursor.close()

def delete_question_db(id):
    mycursor = thesis_db.cursor()
    mycursor.execute("DELETE from questions WHERE id = %s", (id,))
    thesis_db.commit()
    mycursor.close()
