import mysql.connector

# ================= DATABASE CONNECTION =================

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Anshul@1234",   # ⚠️ Change this
        database="womensafety"            # ⚠️ Must be womensafety
    )

# ================= REGISTER USER =================

def register_user(name, email, password):

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

# ================= LOGIN USER =================

def login_user(email, password):

    db = get_db()
    cursor = db.cursor(dictionary=True)

    query = """
    SELECT * FROM users
    WHERE email = %s AND password = %s
    """

    cursor.execute(query, (email, password))
    user = cursor.fetchone()

    cursor.close()
    db.close()

    return user

# ================= GET USER BY ID =================

def get_user_by_id(user_id):

    db = get_db()
    cursor = db.cursor(dictionary=True)

    query = "SELECT * FROM users WHERE id = %s"

    cursor.execute(query, (user_id,))
    user = cursor.fetchone()

    cursor.close()
    db.close()

    return user

# ================= GET ALL USERS (ADMIN PANEL) =================

def get_all_users():

    db = get_db()
    cursor = db.cursor(dictionary=True)

    query = "SELECT * FROM users ORDER BY id DESC"

    cursor.execute(query)
    users = cursor.fetchall()

    cursor.close()
    db.close()

    return users

# ================= DELETE USER (OPTIONAL ADMIN FEATURE) =================

def delete_user(user_id):

    db = get_db()
    cursor = db.cursor()

    query = "DELETE FROM users WHERE id = %s"

    cursor.execute(query, (user_id,))
    db.commit()

    cursor.close()
    db.close()
