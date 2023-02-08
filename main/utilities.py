from cryptocode import encrypt, decrypt
import hashlib
from string import ascii_letters, digits
from random import sample
from django.core.signing import Signer

from easyauth.settings import ALLOWED_HOSTS, DEFAULT_FROM_EMAIL
from post_office import mail

signer = Signer()


# def getToken(password):
#     str = password[8] + password[3] + password[5] + password[1] + password[12]
#     token = hashlib.md5(str.encode('utf-8')).hexdigest()
#     lens = len(password)
#     token = token[1:lens]
#     return token
#
#
# def encode(data):
#     token = getToken(data.password)
#     data.first_name = encrypt(data.first_name, token)
#     data.last_name = encrypt(data.last_name, token)
#     data.midl_name = encrypt(data.midl_name, token)
#     data.phone = encrypt(data.phone, token)
#     data.dateBorn = encrypt(data.dateBorn, token)
#
#     return data
#     # for (index, dat) in data:
#     #     if index != 'password':
#     #         data2[index] = encrypt(dat, token)
#     # return data2
#
#
# def decode(data):
#     token = getToken(data.password)
#     data.first_name = decrypt(data.first_name, token)
#     data.last_name = decrypt(data.last_name, token)
#     data.midl_name = decrypt(data.midl_name, token)
#     data.phone = decrypt(data.phone, token)
#     data.dateBorn = decrypt(data.dateBorn, token)
#
#     return data
#     # for (index, dat) in data:
#     #     if index != 'password':
#     #         data2[index] = decrypt(dat, token)
#     # return data2
#
#
# def generate_password():
#     letters_and_digits = ascii_letters + digits
#     rand_string = ''.join(sample(letters_and_digits, 9))
#     return rand_string
#
#
# def send_password_notification(user):
#     user = decode(user)
#     if ALLOWED_HOSTS:
#         host = 'https://' + ALLOWED_HOSTS[0]
#     else:
#         host = 'http://127.0.0.1:8000'
#     mail.send(
#         user.email,
#         DEFAULT_FROM_EMAIL,
#         template='send_password_notification',
#         context={'user': user, 'host': host, 'sign': signer.sign(user.username)},
#         priority='now',
#     )
