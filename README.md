# 💰 Expense Tracker

A simple and beginner-friendly **Expense Tracker** application that helps users record, view, and manage their daily expenses. This project was built to practice CRUD operations and understand how data flows in a Django application.

---

## 🚀 Features

- Add new expenses (name, amount, date)
- View all recorded expenses
- Edit/update existing expenses
- Delete specific expenses
- Persistent data storage using a database (dbsqlite)
- Clean and simple user interface

---

## How to run locally
1. Clone the repo
2. Create a virtual environment: `python -m venv venv`
3. Activate the environment: 
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Start the server: `python manage.py runserver`