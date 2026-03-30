import mysql.connector

# ================= DATABASE CONNECTION =================

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Anshul@1234",   # ⚠️ Change this
        database="womensafety"            # ⚠️ Must be womensafety
    )

# ================= SAVE SOS LOG =================

def save_sos(user_id, latitude, longitude):

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

# ================= GET USER SOS LOGS =================

def get_user_sos_logs(user_id):

    db = get_db()
    cursor = db.cursor(dictionary=True)

    query = """
    SELECT * FROM sos_logs
    WHERE user_id = %s
    ORDER BY id DESC
    """

    cursor.execute(query, (user_id,))
    data = cursor.fetchall()

    cursor.close()
    db.close()

    return data

# ================= GET ALL SOS LOGS (ADMIN) =================

def get_all_sos_logs():

    db = get_db()
    cursor = db.cursor(dictionary=True)

    query = """
    SELECT * FROM sos_logs
    ORDER BY id DESC
    """

    cursor.execute(query)
    data = cursor.fetchall()

    cursor.close()
    db.close()

    return data

# ================= DELETE SOS LOG (OPTIONAL) =================

def delete_sos_log(log_id):

    db = get_db()
    cursor = db.cursor()

    query = "DELETE FROM sos_logs WHERE id = %s"

    cursor.execute(query, (log_id,))
    db.commit()

    cursor.close()
    db.close()
