from flask import Blueprint, render_template, redirect, url_for, request

#Enter the Name of the File here
#Have to enter __name__ and then the name of the blueprint
views = Blueprint(__name__, "views")

@views.route("/")
def home():
    #Renders the Index Page
   return render_template("index.html")

@views.route("/level-1")
def level1():

    #request.form['userInput']
    #if request.method == "POST":
    #  user = request.form['userInput']
    #return redirect(url_for("level-1.html", name=user))
    return render_template("level-1.html", name="user")



@views.route("/level-2")
def level2():
    return render_template("level-2.html", name="user")

@views.route("/level-3")
def level3():
    return render_template("level-3.html", name="user")

@views.route("/level-3-alt")
def level3alt():
    return render_template("level-3-alt.html", name="user")


@views.route("/level-4")
def level4():
    return render_template("level-4.html", name="user")

#Ending Routes
@views.route("ending/home")
def endhome():
    return render_template("ending/home.html", name="user")

@views.route("ending/climb-tower")
def endtower():
    return render_template("ending/climb-tower.html", name="user")