# coding: utf-8

# conectar ao banco de dados

# db = DAL("uri", pool_size, check_reserved, migrate_enabled)
# exemplo -> db = DAL("mysql://usuário:senha@servidor/nome_do_banco", pool_size = 10, check_reserved = ["all"], migrate_enabled = True)

db = DAL(**config.db)
