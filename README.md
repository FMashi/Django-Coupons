# Django Coupon System

This Django project is designed to provide a comprehensive coupon system with authentication functionalities. It includes applications for user authentication and coupon management, all powered by Django's rest_framework.

### Key Features ⭐️

- **User Authentication**: token based authentication Provides token-based authentication for user registration, login, logout, and password reset functionalities.
- **coupon Management**: Allows companies to create, view, update, and delete coupons.
- **Coupon Usage Analytics**: Tracks coupon usage by users, recording the coupon, user, and usage datetime.
- **RESTful API**: Built with Django's rest_framework, offering robust API endpoints for seamless integration with frontend or other systems.

## Getting Started 🚀

To get started with the porject, follow these steps:

#### Prerequisites

**1. 🐍 Python**: Ensure you have Python installed. You can download Python from the [official Python website](https://www.python.org/downloads/).

**2. 🗂️ Install virtualenv**:
If you don't already have [virtualenv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) installed, you can install it using pip, which is Python's package manager. Open your terminal or command prompt and run:

    pip install virtualenv

If you are using Python 3, you can use pip3 instead of pip.

#### 📦 installation

**Clone the Repository:** Clone the project repository to your local machine:

    Clone the repository: git clone https://github.com/FMashi/Django-Coupons

**♻️ Activate the Virtual Environment:**

Depending on your operating system, the command to activate the virtual environment will vary:

##### Windows:

    venv\Scripts\activate

##### macOS and Linux:

    source venv/bin/activate

**🛠️ Install Dependencies:** Install the required Python packages and dependencies listed in the **requirements.txt** file:

    pip install -r requirements.txt

**🖇️ Apply Database Migrations:** Run database migrations to create the database schema:

    python manage.py makemigrations
    python manage.py migrate

**🪄 Running the Application:**

    python manage.py runserver

**✨ Access the API:** The application exposes its endpoints at [API](http://localhost:8000/api). You can use API clients like Postman or cURL to interact with the available endpoints

Authentication Endpoint: [Authentication](http://localhost:8000/auth), Please ensure to include the authentication token in the header of your requests when accessing authenticated endpoints.

### ✉️ Contact

📧 You can also reach out via email at: Fahadmashi@hotmail.com
