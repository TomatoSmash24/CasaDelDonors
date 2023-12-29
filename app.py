from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager, login_user, UserMixin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tomato'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' # type: ignore


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)


class Participant(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    city = db.Column(db.String(50))
    country = db.Column(db.String(50))
    phone = db.Column(db.String(20))
    password = db.Column(db.String(50))

    def __init__(self, name, email, city, country, phone, password):
        self.name = name
        self.email = email
        self.city = city
        self.country = country
        self.phone = phone
        self.password = password


with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return Participant.query.get(int(user_id))



@app.route("/index")
def index():
    return render_template("index.html")




@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = Participant.query.filter_by(email=email).first()

        if user and user.password == password:
            login_user(user)
            return redirect(url_for("home"))
    
    return render_template("login.html")


@app.route("/join", methods=["GET", "POST"])
def join():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        city = request.form["city"]
        country = request.form["country"]
        phone = request.form["phone"]
        password = request.form["password"]

        participant = Participant(
            name=name, email=email, city=city, country=country, phone=phone, password=password
        )
        db.session.add(participant)
        db.session.commit()
        return render_template("index.html")
    else:
        return render_template("join.html")


@app.route("/participants")
def participants():
    participants = Participant.query.all()
    return render_template("participants.html", data=participants)


database = {"Sidharth": "696", "Syed": "123", "Vipul": "987"}


@app.route("/verify", methods=["GET", "POST"])
def verify():
    if request.method == "POST":
        name1 = request.form.get("username")
        pwd = request.form.get("password")
        if name1 not in database:
            error_message = "Invalid username"
            return render_template("verify.html", error_message=error_message)
        elif database[name1] != pwd:
            error_message = "Invalid password"
            return render_template("verify.html", error_message=error_message)
        else:
            return redirect(url_for("participants", name=name1))
    else:
        return render_template("verify.html")


@app.route("/")
def home():
    return render_template("Home Page.html")


@app.route("/clothes")
def clothes():
    return render_template("clothes.html")


# start for toys
@app.route("/toys")
def toys():
    images = os.listdir("static/toys_images")
    return render_template("toys.html", images=images)


@app.route("/donate toys")
def donate():
    return render_template("toys_donate.html")


@app.route("/upload toy image")
def upload():
    return render_template("toys_upload.html")



@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]
    upload_folder = app.config["UPLOAD_FOLDER"]
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    file.save(os.path.join(str(upload_folder), str(file.filename)))

    return "File uploaded successfully"


@app.route("/toy_list")
def toy_list():
    return render_template("toy_list.html")


# end for toys


@app.route("/money")
def money():
    return render_template("money.html")


@app.route("/household")
def household():
    return render_template("household.html")


if __name__ == "__main__":
    app.run(debug=True)
