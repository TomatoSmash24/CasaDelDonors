from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

connect = sqlite3.connect("database.db")
connect.execute(
    "CREATE TABLE IF NOT EXISTS PARTICIPANTS (name TEXT, email TEXT, city TEXT, country TEXT, phone TEXT)"
)


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/join", methods=["GET", "POST"])
def join():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        city = request.form["city"]
        country = request.form["country"]
        phone = request.form["phone"]

        with sqlite3.connect("database.db") as users:
            cursor = users.cursor()
            cursor.execute(
                "INSERT INTO PARTICIPANTS (name,email,city,country,phone) VALUES (?,?,?,?,?)",
                (name, email, city, country, phone),
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


database = {"Sidharth": "696", "Syed Imad": "123", "VipulBSD": "987"}


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


@app.route("/toys")
def toys():
    return render_template("toys.html")


@app.route("/money")
def money():
    return render_template("money.html")


@app.route("/household")
def household():
    return render_template("household.html")


if __name__ == "__main__":
    app.run(debug=True)
