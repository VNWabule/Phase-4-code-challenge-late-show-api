# 📺 Late Show API

A Flask-based RESTful API for managing guests, episodes, and appearances on a fictional Late Show. This project includes user registration, login, and token-based authentication.

---

## 🧰 Setup Instructions

### Prerequisites

- Python 3.8+
- PostgreSQL
- pip / virtualenv

1. **Clone the Repo**
    ```bash
    git clone git@github.com:VNWabule/Phase-4-code-challenge-late-show-api.git
    cd Phase-4-code-challenge-late-show-api

2. **Create a Virtual Environment & Activate**
    ```bash
    pipenv install && pipenv shell

3. **Install Dependencies**
    ```bash
    pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary pipenv shell

---

## 🚀 How to Run

1. **Create the Database**
    ```bash
    createdb late_show_db

2. **Run Migrations**
    ```bash
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade

3. **Seed the Database**
    ```bash
    python -m server.seed

4. **Start the Server**
    ```bash
    flask run

---

## 🔐 Auth Flow

1. **POST /register**
- Request
    ```json
    {
    "username": "johndoe",
    "password": "securepassword"
    }

- Response
    ```json
    {
    "id": 1,
    "username": "johndoe"
    }

2. **POST /login**
- Request
    ```json
    {
    "username": "johndoe",
    "password": "securepassword"
    }

- Response
    ```json
    {
    "token": "eyJhbGciOiJIUzI1NiIs..."
    }
    
- ✅ Copy the token and include it in the Authorization header for protected routes.

---

## 🧭 Route List & Sample Requests

1. **GET /guests**
    ```json
    [
    {
        "id": 1,
        "name": "Zendaya",
        "occupation": "Actor"
    },
    {
        "id": 2,
        "name": "Elon Musk",
        "occupation": "Entrepreneur"
    },
    {
        "id": 3,
        "name": "Billie Eilish",
        "occupation": "Musician"
    }
    ]

2. **GET /episodes**
    ```json
    [
    {
        "date": "2023-11-10",
        "id": 1,
        "number": 101
    }
    ]

3. **GET /episodes/1**
    ```json
    {
    "appearances": [
        {
        "guest": {
            "id": 1,
            "name": "Zendaya",
            "occupation": "Actor"
        },
        "id": 1,
        "rating": 5
        },
        {
        "guest": {
            "id": 2,
            "name": "Elon Musk",
            "occupation": "Entrepreneur"
        },
        "id": 2,
        "rating": 4
        }
    ],
    "date": "Fri, 10 Nov 2023 00:00:00 GMT",
    "id": 1,
    "number": 101
    }

4. **POST /appearance (Protected)**
- Headers
    ```http
    Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
    Content-Type: application/json

- Request
    ```json
    {
    "guest_id": 1,
    "episode_id": 1,
    "rating": 5
    }

- Response
    ```json
    {
    "id": 1,
    "guest_id": 1,
    "episode_id": 1,
    "rating": 5
    }

---

## 🧪 Postman Usage Guide

1. **Register/Login**
- Use POST /register or POST /login with raw JSON in body.
- Copy the returned token.

2. **Authenticated Requests**
- Add the following to Headers:
    ```makefile
    Key: Authorization
    Value: Bearer <your_token>

3. **Example Sequence**
- Register user
- Login and copy token
- Add a new appearance using POST /appearances with token in header















