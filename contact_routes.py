from flask import Blueprint, render_template, request, redirect, session
from models.contact import add_contact, get_user_contacts, delete_contact

contact_bp = Blueprint("contact", __name__)

# ================= ADD CONTACT =================

@contact_bp.route("/add_contacts", methods=["GET", "POST"])
def add_contacts():

    if "user_id" not in session:
        return redirect("/login")

    if request.method == "POST":

        name = request.form["name"]
        phone = request.form["phone"]

        add_contact(session["user_id"], name, phone)

        return redirect("/my_contacts")

    return render_template("add_contacts.html")

# ================= VIEW CONTACT LIST =================

@contact_bp.route("/my_contacts")
def my_contacts():

    if "user_id" not in session:
        return redirect("/login")

    contacts = get_user_contacts(session["user_id"])

    return render_template("my_contacts.html", contacts=contacts)

# ================= DELETE CONTACT =================

@contact_bp.route("/delete_contact/<int:contact_id>")
def delete_contact_route(contact_id):

    if "user_id" not in session:
        return redirect("/login")

    delete_contact(contact_id)

    return redirect("/my_contacts")
