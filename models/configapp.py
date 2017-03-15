#coding: utf-8

#import sys
#sys.path.insert(1, r"/home/tiago/Personal/www-dev/web2py")

from gluon.storage import Storage

config = Storage(
    db = Storage(),
    mail = Storage(),
    aut = Storage()
)

config.db.uri = "sqlite://lilaann.db"
config.db.pool_size = 0
config.db.check_reserved = ["all"]
config.db.migrate_enabled = True # desligar quando entrar em produção

config.mail.sender = "tiagojneves.eng@gmail.com"
config.mail.server = "logging" #"smtp.kdfnksdnf:25"
config.mail.login = "usuario:senha"

# definir configurações para banco de dados, autenticação e e-mail
# definir nível de acesso à visões genéricas
# criar/importar funções globais
