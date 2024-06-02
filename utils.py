import re
import yagmail 

def string_to_slug(s):
    slug = s.lower()
    slug = re.sub(r'[^a-z0-9\-]+', '-', slug)
    slug = slug.strip('-')
    slug = re.sub(r'[-]+', '-', slug)
    return slug


def email_sender(subject, to, message):
    yag = yagmail.SMTP('yigit3588@gmail.com','ldfi stst lfyy ebpg')
    yag.send(to, subject, message)




