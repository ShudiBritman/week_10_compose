from .data_interactor import *
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


class Contact(BaseModel):
    first_name: str
    last_name: str
    phone_number: str



app = FastAPI()

@app.get("/contacts/")
def get_contacts():
    return get_all_contacts()


@app.post("/contacts/")
def create_contact_api(contact: Contact):
    dict_contact = {
        "first_name": contact.first_name,
        "last_name": contact.last_name,
        "phone_number": contact.phone_number
    }
    return create_contact(dict_contact)


@app.put("/contacts/{id}")
def update_contact_api():
    return update_contact(id)


@app.delete("/contacts/{id}")
def delete_contact_api():
    delete_contact()
    return "Deletion was successful"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)



