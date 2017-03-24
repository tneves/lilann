#coding: utf-8

# definir tabelas de objetos do sistema

# Category
# id, name, description

# Table, Field, define_table

db.define_table("category",
    Field("name", lenght=128, notnull=True, unique=True),
    Field("description", "text")
)
