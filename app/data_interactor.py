from sql.connection import get_connection



def create_contact(first_name, last_name, phone_number):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO contacts (first_name, last_name, phone_number)
        VALUES (%s, %s, %s)
    """
    cursor.execute(query, (first_name, last_name, phone_number))
    conn.commit()
    new_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return new_id


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



def delete_contact(contact_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE id=%s", (contact_id,))
    conn.commit()
    deleted = cursor.rowcount > 0
    cursor.close()
    conn.close()
    return deleted

