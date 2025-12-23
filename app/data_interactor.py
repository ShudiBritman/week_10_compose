from sql.connection import get_connection



def create_contact(contact):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO contacts (first_name, last_name, phone_number)
        VALUES (%s, %s, %s)
    """
    cursor.execute(
        query,
        (
            contact["first_name"],
            contact["last_name"],
            contact["phone_number"]
        )
    )
    conn.commit()
    cursor.close()
    conn.close()
    return {
        "message": "add successful",
        "id": cursor.lastrowid
    }


def get_all_contacts():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    cursor.close()
    conn.close()
    return contacts


def update_contact(id, update):
    conn = get_connection()
    cursor = conn.cursor()

    fields = ", ".join([f"{key} = %s" for key in update.keys()])
    values = list(update.values())
    values.append(id)

    query = f"UPDATE contacts SET {fields} WHERE id = %s"
    cursor.execute(query, values)

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Update was successful"}



def delete_contact(id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM contacts WHERE id = %s", (id,))
    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Delete was successful"}


