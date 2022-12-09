from flask import Flask
#Imports the View Variable from the Views.py
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")


if __name__ == '__main__':
    app.run(debug=True, port=8000)

#Potential Ideas:

#User can go into another web page, pick up a sword and breastplate which is then counted in JavaScript/Python which will then allow them to defeat a Monster and unlock another route