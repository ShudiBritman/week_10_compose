Project goal

Store contact records in a MySQL database

Expose RESTful HTTP endpoints to support full CRUD operations (Create, Read, Update, Delete)

Run the application using Docker containers orchestrated with Docker Compose

Ensure data persistence by using Docker volumes


## Project Overview

- Store contact records in a MySQL database  
- Expose RESTful HTTP endpoints to support full CRUD operations (Create, Read, Update, Delete)  
- Run the application inside Docker containers using Docker Compose  
- Persist database data using Docker volumes  

---

## Running the Project

The project is managed using **Docker Compose**, which defines all required services in a `docker-compose.yml` file.

### Start the project

From the root directory of the project, run:

```bash
docker compose up --build
```
This command will:

Build the application image

Start the API service and the MySQL database

Create and attach persistent volumes automatically

Run in detached mode (optional)
```
docker compose up -d --build
```
Docker Compose Configuration

All services (API server and MySQL database), including networking, environment variables, exposed ports, and volumes, are defined in the docker-compose.yml file.



endpoints 

| Method | Endpoint | Description | Request Body | Response |
| :---- | :---- | :---- | :---- | :---- |
| GET | `/contacts` | Get all contacts | None | List of all contacts |
| POST | `/contacts` | Create new contact | Contact data | Success message \+ ID |
| PUT | `/contacts/{id}` | Update existing contact | Updated fields | Success message |
| DELETE | `/contacts/{id}` | Delete contact | None | Success message |

