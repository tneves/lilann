#coding: utf-8

def index():
    # list all products
    # featured / gallery
    categories = db(db.category).select()
    products = db(db.product).select()

    #response.view = "alternate/myhome.html"
    return dict(category=categories, products=products)


    # objetos = [1,2,3]
    # import json
    # return json.dumps(dict(objetos=objetos))

    #return DIV(
    #            UL(
    #                LI(A("Hello")),
    #                LI(A("Google", _href="http://www.google.com"))
    #            )
    #           )
def user():
    pass
