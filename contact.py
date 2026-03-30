import mysql.connector

# ================= DATABASE CONNECTION =================

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Anshul@1234",   # ⚠️ Change this
        database="womensafety"            # ⚠️ Must be womensafety
    )

# ================= ADD CONTACT =================

def add_contact(user_id, name, phone):

    db = get_db()
    cursor = db.cursor()

    query = """
    INSERT INTO contacts (user_id, name, phone)
    VALUES (%s, %s, %s)
    """

    cursor.execute(query, (user_id, name, phone))
    db.commit()

    cursor.close()
    db.close()

# ================= GET USER CONTACTS =================

def get_user_contacts(user_id):

    db = get_db()
    cursor = db.cursor(dictionary=True)

    query = """
    SELECT * FROM contacts
    WHERE user_id = %s
    """

    cursor.execute(query, (user_id,))
    data = cursor.fetchall()

    cursor.close()
    db.close()

    return data

# ================= GET ALL CONTACTS (ADMIN) =================

def get_all_contacts():

    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM contacts ORDER BY id DESC")
    data = cursor.fetchall()

    cursor.close()
    db.close()

    return data

# ================= DELETE CONTACT (OPTIONAL FEATURE) =================

def delete_contact(contact_id):

    db = get_db()
    cursor = db.cursor()

    query = "DELETE FROM contacts WHERE id = %s"

    cursor.execute(query, (contact_id,))
    db.commit()

    cursor.close()
    db.close()
