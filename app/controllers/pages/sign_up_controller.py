from flask import session, render_template, request, redirect
from app.models.Users import users
from ... import socketio
from ... import db
from app.controllers.auth import auth_controller





def sign_up(data):

    if data != None:

        # received login data
        print("l'utilisateur envoie les données d'inscription")

        # recup les données recus
        username = data['username']

        # check username already existe:pyt
        user_found = users.query.filter_by(name=username).first()

        if(user_found):
            print("nom déjà utilisé")
            socketio.emit('error', {'msg': "username already exist"})
            return

        else:
            data = users(username)
            db.session.add(data)
            db.session.commit()
            print("ok nom")
            return redirect('/')

    else:
        # l'utilisateur veux accèdé a la page d'inscription
        navbar = auth_controller.auth()
        content = render_template('pages/sign_up_page.html')
        return render_template("template.html", title="Inscription", navbar = navbar, content = content)