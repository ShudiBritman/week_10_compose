from sql.connection import get_cursor

cursor = get_cursor()


def create_contact(contact):
    new_contact = cursor.execute("INSERET INTO contacts " \
    "(first_name, last_name, phone_number)" \
    f"VALUES({contact["first_name"]}, {contact["last_name"]}, {contact["phone_number"]})")
    cursor.commit()
    return {"massage": "add successful", "id": new_contact.id}

def get_all_contacts():
    contacts = cursor.execute("SELECT * FROM contacts")
    cursor.commit()
    return contacts

def update_contact(id, update):
    cursor.execute(f"UPDATE contacts SET  WHERE id = {id}")
    return {"massage": "Update was successful"}


def delete_contact(id):
    cursor.execute(f"DELETE FROM contacts WHERE id = {id}")