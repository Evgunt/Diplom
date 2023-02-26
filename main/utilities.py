
from easyauth.settings import ALLOWED_HOSTS, DEFAULT_FROM_EMAIL
from post_office import mail


# def send_docs(data):
#     if ALLOWED_HOSTS:
#         host = 'https://' + ALLOWED_HOSTS[0]
#     else:
#         host = 'http://127.0.0.1:8000'
#     file = data['name']+'.docs'
#     mail.send(
#         data['email'],
#         DEFAULT_FROM_EMAIL,
#         template='send_docs',
#         context=data,
#         priority='now',
#         attachments={
#             file: data['docs']
#         }
#     )
