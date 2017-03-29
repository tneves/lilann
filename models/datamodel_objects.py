#coding: utf-8

# definir tabelas de objetos do sistema

# Category
# id, name, description

# Table, Field, define_table

db.define_table("category",
    #Field("cod_cat", "id"),
    Field("name", length=128, notnull=True, unique=True),
    Field("description", "text"),
    Field("picture", "upload"),
    # migrate = False,
    # primary_key = ["cod_cat", "name"]
)

# Product
# id, name, category, description, qtd, origin, unit_price,
# total_price, tax_price, picture, thumbnail, barcode (signature)

db.define_table("product",
    Field("name", notnull=True),
    Field("category", "reference category"),
    Field("description", "text"),
    Field("qtd", "integer", notnull=True),
    Field("origin", "string"),
    Field("unit_price", "double"),
    Field("total_price", "double"), # computed fields
    # campo virtual tax_price

)

origins = {"BR": 1.0, "JP": 1.2, "EUA": 1.8, "UK": 1.5}
