from flask import Blueprint, render_template, request, redirect, session
import mysql.connector

# Create Blueprint
auth_bp = Blueprint("auth", __name__)

# ================= DATABASE CONNECTION =================

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Anshul@1234",   # ⚠️ Change this
        database="womensafety"            # ⚠️ Must be womensafety
    )

# ================= REGISTER ROUTE =================

@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        db = get_db()
        cursor = db.cursor()

        query = """
        INSERT INTO users (name, email, password)
        VALUES (%s, %s, %s)
        """

        cursor.execute(query, (name, email, password))
        db.commit()

        cursor.close()
        db.close()

        return redirect("/login")

    return render_template("register.html")

# ================= LOGIN ROUTE =================

@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        db = get_db()
        cursor = db.cursor(dictionary=True)

        query = """
        SELECT * FROM users
        WHERE email=%s AND password=%s
        """

        cursor.execute(query, (email, password))
        user = cursor.fetchone()

        cursor.close()
        db.close()

        if user:
            session["user_id"] = user["id"]
            session["user_name"] = user["name"]

            return redirect("/dashboard")
        else:
            return "Invalid Email or Password"

    return render_template("login.html")

# ================= LOGOUT ROUTE =================

@auth_bp.route("/logout")
def logout():

    session.clear()
    return redirect("/login")
