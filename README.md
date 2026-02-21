# 📚 Library Management System API (Django REST Framework)

A secure backend API built using **Django**, **Django REST Framework (DRF)**, and **PostgreSQL**.

This project demonstrates:

- Django ORM
- JWT Authentication
- Role-based Permissions
- Pagination
- Filtering
- Search
- Clean API architecture

---

## 🚀 Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication (SimpleJWT)
- django-filter

---

## 🔐 Authentication (JWT)

### 🔑 Obtain Token

**POST** `/api/token/`

~~~json
{
  "username": "your_username",
  "password": "your_password"
}
~~~

Response:

~~~json
{
  "refresh": "refresh_token_here",
  "access": "access_token_here"
}
~~~

---

### 🔁 Refresh Access Token

**POST** `/api/token/refresh/`

~~~json
{
  "refresh": "your_refresh_token_here"
}
~~~

Response:

~~~json
{
  "access": "new_access_token_here"
}
~~~

---

### 🔒 Use Token in Requests

Add this in request headers:

~~~
Authorization: Bearer your_access_token
~~~

---

## 📚 Books API

Base URL:

~~~
/api/books/
~~~

---

### ✅ Get All Books (Paginated)

**GET** `/api/books/`

Response:

~~~json
{
  "count": 12,
  "next": "http://127.0.0.1:8000/api/books/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Django Basics",
      "auther": "William",
      "created_at": "2026-02-14T10:00:00Z"
    }
  ]
}
~~~

---

### 🔎 Filtering

Filter by author:

~~~
/api/books/?auther=William
~~~

---

### 🔍 Search

Search by title:

~~~
/api/books/?search=django
~~~

---

### ➕ Create Book (Admin Only)

**POST** `/api/books/`

~~~json
{
  "title": "Advanced Django",
  "auther": "William"
}
~~~

Response:

~~~json
{
  "id": 3,
  "title": "Advanced Django",
  "auther": "William"
}
~~~

Status Code: `201 Created`

---

### ✏️ Update Book (Admin Only)

**PATCH** `/api/books/1/`

~~~json
{
  "title": "Django Mastery"
}
~~~

---

### ❌ Delete Book (Admin Only)

**DELETE** `/api/books/1/`

Status Code: `204 No Content`

---

## 🛡 Permissions

- Only authenticated users can access the API.
- Only admin users can create, update, or delete books.
- Read operations are available to authenticated users.

---

## 📦 Setup Instructions

### 1️⃣ Clone Repository

~~~
git clone https://github.com/your-username/library-api.git
cd library-api
~~~

---

### 2️⃣ Create Virtual Environment

~~~
python -m venv venv
venv\Scripts\activate   (Windows)
~~~

---

### 3️⃣ Install Dependencies

~~~
pip install -r requirements.txt
~~~

---

### 4️⃣ Configure PostgreSQL in `settings.py`

~~~python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "library_db",
        "USER": "library_user",
        "PASSWORD": "your_password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
~~~

---

### 5️⃣ Run Migrations

~~~
python manage.py migrate
~~~

---

### 6️⃣ Create Superuser

~~~
python manage.py createsuperuser
~~~

---

### 7️⃣ Run Server

~~~
python manage.py runserver
~~~

---

## 📌 Features Implemented

- Django ORM
- ModelViewSet
- JWT Authentication
- Custom Permission Classes
- Pagination
- Filtering
- Search
- Proper HTTP status codes
- Clean project structure

---

## 🎯 Learning Outcomes

This project demonstrates practical understanding of:

- REST API design
- Authentication vs Authorization
- HTTP status codes
- Clean backend architecture
- Production-ready DRF setup

---

## 👨‍💻 Author

Suraj Patil  
Python Backend Developer
