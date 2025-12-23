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


def update_contact(contact_id, first_name=None, last_name=None, phone_number=None):
    conn = get_connection()
    cursor = conn.cursor()

    fields = []
    values = []

    if first_name is not None:
        fields.append("first_name = %s")
        values.append(first_name)

    if last_name is not None:
        fields.append("last_name = %s")
        values.append(last_name)

    if phone_number is not None:
        fields.append("phone_number = %s")
        values.append(phone_number)

    if not fields:
        return False

    query = f"UPDATE contacts SET {', '.join(fields)} WHERE id = %s"
    values.append(contact_id)

    cursor.execute(query, tuple(values))
    conn.commit()

    updated = cursor.rowcount

    cursor.close()
    conn.close()

    return updated > 0



def delete_contact(contcat_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE id = %s", (contcat_id,))
    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Delete was successful"}

