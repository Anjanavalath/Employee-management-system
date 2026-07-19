# Employee Management System

A Flask-based Employee Management System developed using Python, Flask, SQLAlchemy, Bootstrap, and MySQL.

## Features

- Add Employee
- View Employee List
- Update Employee
- Delete Employee
- Search Employees
- Filter by Department
- Filter by Salary Range
- Sort by Name, Salary, Department, Email, and ID
- Pagination
- Responsive Bootstrap UI

## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- MySQL
- Bootstrap 5
- HTML5
- Jinja2

## Project Structure

```
Flask-Development
│
├── app
│   ├── models
│   ├── routes
│   ├── templates
│   └── static
│
├── config.py
├── app.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Employee-Management-System.git
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure the MySQL database in `config.py`.

Run the application:

```bash
python app.py
```

## Future Improvements

- Authentication
- User Roles
- Dashboard
- Charts
- Export PDF
- REST API

## Author

Anjana Sudheesh