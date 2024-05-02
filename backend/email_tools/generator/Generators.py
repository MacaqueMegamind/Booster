from coolname import generate
import string
import secrets


def generate_login(length=3):
    return ''.join(x.capitalize() for x in generate(length))


def generate_password(length=16):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(all_characters) for i in range(length))
    return password
