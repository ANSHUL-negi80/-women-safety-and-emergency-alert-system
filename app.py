from flask import Flask, render_template, session, redirect

# ================= IMPORT ROUTES =================

from routes.auth import auth_bp
from routes.sos import sos_bp
from routes.admin import admin_bp
from routes.contact_routes import contact_bp


# ================= CREATE APP =================

app = Flask(__name__)

# ================= SECRET KEY =================

app.secret_key = "womensafety_secret_key"

# ================= REGISTER BLUEPRINTS =================

app.register_blueprint(auth_bp)
app.register_blueprint(sos_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(contact_bp)


# ================= HOME ROUTE =================

@app.route("/")
def home():
    return render_template("index.html")

# ================= DASHBOARD ROUTE =================

@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect("/login")

    return render_template("dashboard.html")

# ================= LOGOUT SAFETY =================

@app.route("/force_logout")
def force_logout():
    session.clear()
    return redirect("/login")

# ================= RUN SERVER =================

if __name__ == "__main__":
    app.run(debug=True)
