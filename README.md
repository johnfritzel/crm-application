# CRM Application - THRIVE CX

This project is a Customer Relationship Management (CRM) application built using Django for the backend and Bootstrap and JavaScript for the frontend. It provides a user-friendly interface for managing customer data and interactions.


### Features
- CRUD Operations: Create, Read, Update, and Delete customer records.
- Customer Management: Store and manage customer details, including contact information, notes, and preferences.
- Intuitive Interface: User-friendly interface with Bootstrap for easy navigation and data visualization.
- Responsive Design: Adapts to different screen sizes for optimal viewing on desktops, tablets, and mobile devices.
- Authentication: Secure user login and access control. (Note: Basic authentication implementation details are omitted for brevity)


### Technologies
- Backend: Django (Python web framework)
- Frontend:
  - HTML
  - CSS (Bootstrap)
  - JavaScript


### Prerequisites
- Python 3.12.2
- Django 5.0.3
- django-crispy-forms 1.14.0


### Installation
1. Clone this repository.
```
git clone https://github.com/johnfritzel/crm-application.git
```

2. Navigate to the project directory.
```
cd crm
```

3. Create a virtual environment.
```
python -m venv venv
```
```
venv\Scripts\activate # Windows
source venv/bin/activate  # Linux/macOS
```

4. Install required dependencies.
```
pip install -r requirements.txt
```

5. Apply database migrations.
```
python manage.py migrate
```

6. Create a superuser account (for initial login):
```
python manage.py createsuperuser
```
&nbsp; Enter your desired username, email, and password when prompted.

7. Run the development server:
```
python manage.py runserver
```
&nbsp; This will start the Django development server, typically accessible at http://127.0.0.1:8000/ in your web browser.


### Usage
1. Access the application in your web browser at http://127.0.0.1:8000/.
2. Login using the superuser credentials created earlier.
3. You can now start using the CRM to manage your customer data. Navigate through the application interface to explore various features like adding, viewing, editing, and deleting customer records.
