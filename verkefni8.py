from bottle import *

from beaker.middleware import SessionMiddleware

#session er tíminn þar sem sum notkun browser forritið á vedsidu verða geymd a serverin
#adal munurin er ad cookies eru geymd a tolvu notandans og sessions a vedsidu serverin dar sem notandi get ekki sed dau



#ef cookies eru notud þá getur fólk séð þau og veðsidu eigandin þarf ekki geyma upplysingarnar

session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}
app = SessionMiddleware(app(), session_opts)

products = [{"pid": 1, "name": "Vara 1", "price": 1000},
            {"pid": 2, "name": "Vara 2", "price": 200},
            {"pid": 3, "name": "Vara 3", "price": 30},
            {"pid": 4, "name": "Vara 4", "price": 4}]

@route ("/")
def index():

    return template("index.tpl", products=products)

@route ("/cart")
def cart():
    session = request.environ.get("beaker.session")

    karfa = []
    for x in range(1,5):
        if x == 1:
            if session.get('1'):
                vara1 = session.get('1')
                karfa.append(vara1)

        elif x == 2:
            if session.get('2'):
                vara2 = session.get('2')
                karfa.append(vara2)

        elif x == 3:
            if session.get('3'):
                vara3 = session.get('3')
                karfa.append(vara3)

        elif x == 4:
            if session.get('4'):
                vara4 = session.get('4')
                karfa.append(vara4)

    print(karfa)
    return template("cart.tpl", karfa=karfa)

@route("/cart/add/<id:int>")
def add_to_cart(id):
    if id == 1:
        session = request.environ.get('beaker.session')
        session["1"] = "Vara 1"
        session.save()  # vistum session
        return redirect("/cart")
    elif id == 2:
        session = request.environ.get('beaker.session')
        session["2"] = "Vara 2"
        session.save()  # vistum session
        return redirect("/cart")
    elif id == 3:
        session = request.environ.get('beaker.session')
        session["3"] = "Vara 3"
        session.save()  # vistum session
        return redirect("/cart")
    elif id == 4:
        session = request.environ.get('beaker.session')
        session["4"] = "Vara 4"
        session.save()  # vistum session
        return redirect("/cart")

    #og svo framvegis
    else:
        return redirect("/")

@route("/cart/remove")
def remove_from_cart():
    session = request.environ.get('beaker.session')
    session.delete()
    return redirect("/cart")

@route('/static/<skra>')
def static_skrar(skra):
    return static_file(skra, root='./public/')


run(app = app,host='localhost', port=8080, debug=True)

