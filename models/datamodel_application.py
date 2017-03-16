# coding: utf-8

# definir objetos da app (Auth, Mail, Service)

from gluon.tools import Auth, Mail

auth = Auth(db, hmac_key=Auth.get_or_create_key())

# tabelas auth_user, auth_groups, auth_membership, auth_permission

# A tabela auth_user, tem por padrão os campos: nome, último nome, e-mail e senha
# Vamos adicionar mais campos a esta tabela
# auth.settings.extra_fields["auth_user"] = [CPF]

# auth.settings.registration_requires_verification = False
# auth.settings.registration_requires_approval = False
# auth.settings.reset_password_requires_verification = True

# CAPTCHA
#from gluon.tools import Recaptcha
#auth.settings.captcha = Recaptcha(request, 'PUBLIC_KEY', 'PRIVATE_KEY')

mail = Mail()
mail.settings.sender = config.mail.sender
mail.settings.server = config.mail.server
mail.settings.login = config.mail.login

auth.settings.mailer = mail

# auth.setting.login_field = 'cpf'
auth.define_tables()

# definir classes e funções da aplicação

# definir autenticação

# definir datamodel de autenticação

# definir e-mail de autenticação

# assinatura
