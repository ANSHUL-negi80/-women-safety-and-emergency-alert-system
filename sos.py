from altair import Latitude, Longitude
from flask import Blueprint, render_template, request, redirect, session
import mysql.connector

from models.sos_log import save_sos

# Create Blueprint
sos_bp = Blueprint("sos", __name__)

# ================= DATABASE CONNECTION =================

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Anshul@1234",   # ⚠️ Change this
        database="womensafety"            # ⚠️ Must be womensafety
    )

# ================= SOS PAGE (BUTTON UI) =================
google_maps_link = f"https://www.google.com/maps?q={Latitude},{Longitude}"


@sos_bp.route("/sos_page", methods=["GET", "POST"])
def sos_page():

    # If user not logged in
    if "user_id" not in session:
        return redirect("/login")

    if request.method == "POST":

        user_id = session["user_id"]

        # ⚠️ Temporary static location
        latitude = "30.2729"
        longitude = "78.0004"

        db = get_db()
        cursor = db.cursor()

        query = """
        INSERT INTO sos_logs (user_id, latitude, longitude)
        VALUES (%s, %s, %s)
        """

        cursor.execute(query, (user_id, latitude, longitude))
        db.commit()

        cursor.close()
        db.close()

        print("🚨 SOS SAVED IN DATABASE")

        return redirect("/dashboard")

    return render_template("sos.html")

# ================= SOS HISTORY PAGE =================

@sos_bp.route("/sos_history")
def sos_history():

    if "user_id" not in session:
        return redirect("/login")

    user_id = session["user_id"]

    db = get_db()
    cursor = db.cursor(dictionary=True)

    query = """
    SELECT * FROM sos_logs
    WHERE user_id = %s
    ORDER BY id DESC
    """

    cursor.execute(query, (user_id,))
    sos_list = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template(
        "sos_history.html",
        sos_list=sos_list
    )
@sos_bp.route("/live_location", methods=["POST"])
def live_location():
    data = request.get_json()

    lat = data["lat"]
    long = data["long"]

    save_sos(session["user_id"], lat, long)

    return {"status": "ok"}

