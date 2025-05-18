# 📬 Flask Notification Service

A lightweight RESTful API built with **Flask** to simulate sending notifications (Email, SMS, In-App) to users. This project is designed for internship-level demonstration of RESTful API development in Python using Flask.

---

## 🚀 Features

- ✅ Send notifications to users via API
- ✅ Get all notifications sent to a user
- ✅ Supports Email, SMS, and In-App notification types
- ✅ Uses SQLite for data persistence
- ✅ Logs simulated notification delivery to the console

---

## 🔧 Tech Stack

- **Python 3.8+**
- **Flask**
- **Flask-SQLAlchemy**
- **SQLite** (as the default database)

---

## 📁 Project Structure

notification_service/
├── app/
│ ├── init.py # App and DB initialization
│ ├── models.py # SQLAlchemy models
│ ├── routes.py # REST API endpoints
├── config.py # DB config
├── run.py # App runner
├── requirements.txt # Dependencies
└── README.md # This file

yaml
Copy
Edit

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/flask-notification-service.git
   cd flask-notification-service

--------------------------

Create and activate a virtual environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate          # Windows

------------------------------

Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt

---------------------------------

Run the Flask application:

bash
Copy
Edit
python run.py

-------------------------------

The API will be accessible at: http://127.0.0.1:5000

----------------------------------

🔌 API Endpoints:
➤ POST /notifications
Send a simulated notification to a user.

✅ Request Body (JSON)
json
Copy
Edit
{
  "user_id": "user123",
  "type": "email",          // "email", "sms", or "in-app"
  "content": "Hello! Welcome to the platform."
}

✅ Success Response
json
Copy
Edit
{
  "message": "Notification sent",
  "id": 1
}
➤ GET /users/<user_id>/notifications
Get all notifications sent to a specific user.

✅ Example
GET /users/user123/notifications

✅ Response
json
Copy
Edit
[
  {
    "id": 1,
    "type": "email",
    "content": "Hello! Welcome to the platform.",
    "status": "sent",
    "created_at": "2025-05-18T13:40:00"
  }
]

-----------------------------------------

📌 Assumptions
This is a simulation — no actual Email/SMS is sent.

Database used is SQLite (for simplicity).

No user authentication is implemented.

All data is stored and retrieved using RESTful endpoints.
