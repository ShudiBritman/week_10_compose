from .data_interactor import *
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import uvicorn


class Contact(BaseModel):
    first_name: str
    last_name: str
    phone_number: str

class UpdateContactRequest(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None

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


@app.put("/contacts/{contact_id}")
def update_contact_api(contact_id: int, data: UpdateContactRequest):
    updated = update_contact(
        contact_id,
        data.first_name,
        data.last_name,
        data.phone_number
    )

    if not updated:
        raise HTTPException(status_code=404, detail="Contact not found")

    return {"message": "Update was successful"}


@app.delete("/contacts/{contcat_id}")
def delete_contact_api(contcat_id):
    delete_contact(contcat_id)
    return "Deletion was successful"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)



