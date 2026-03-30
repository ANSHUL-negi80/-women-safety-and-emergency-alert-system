from flask import Blueprint, render_template, session, redirect
import mysql.connector

# Create Blueprint
admin_bp = Blueprint("admin", __name__)

# ================= DATABASE CONNECTION =================

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Anshul@1234",   # ⚠️ Change this
        database="womensafety"            # ⚠️ Must be womensafety
    )

# ================= ADMIN DASHBOARD ROUTE =================

@admin_bp.route("/admin")
def admin_panel():

    # Optional Security (Only logged in users)
    if "user_id" not in session:
        return redirect("/login")

    db = get_db()
    cursor = db.cursor(dictionary=True)

    # Fetch Users
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    # Fetch Contacts
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()

    # Fetch SOS Logs
    cursor.execute("SELECT * FROM sos_logs ORDER BY id DESC")
    sos_logs = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template(
        "admin.html",
        users=users,
        contacts=contacts,
        sos_logs=sos_logs
    )
