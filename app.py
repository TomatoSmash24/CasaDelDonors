from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os
from flask_login import LoginManager, login_user

# login_manager = LoginManager()
app = Flask(__name__)
# login_manager.init_app(app)
# login_manager.login_view = 'join'



connect = sqlite3.connect("database.db")
connect.execute(
    "CREATE TABLE IF NOT EXISTS PARTICIPANTS (name TEXT, email TEXT, city TEXT, country TEXT, phone TEXT, password TEXT)"
)


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        with sqlite3.connect("database.db") as conn:
            user = conn.execute('''SELECT * FROM PARTICIPANTS WHERE email = (?)''', (email,))
            u = user.fetchall()

            if u[0][-1] == password:
                # Migrate to SQL_Alchemy to make this work
                # login_user(u)
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

        with sqlite3.connect("database.db") as users:
            cursor = users.cursor()
            cursor.execute(
                "INSERT INTO PARTICIPANTS (name,email,city,country,phone,password) VALUES (?,?,?,?,?,?)",
                (name, email, city, country, phone, password),
            )
            users.commit()
        return render_template("index.html")
    else:
        return render_template("join.html")


@app.route("/participants")
def participants():
    connect = sqlite3.connect("database.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM PARTICIPANTS")

    data = cursor.fetchall()
    return render_template("participants.html", data=data)


database = {"Sidharth": "696", "Syed": "123", "Vipul": "987"}


@app.route("/verify", methods=["GET", "POST"])
def verify():
    if request.method == "POST":
        name1 = request.form.get("username")
        pwd = request.form.get("password")
        if name1 is None or name1 not in database:
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
    # Do something with the file
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
