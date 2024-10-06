# Test login/register/logout with [agv-project](https://github.com/sondhg/agv-project) graphical user interface using this django server

## Setting Up the Database

To ensure you have the same database setup as this project, follow these steps:

### Prerequisites

- **PostgreSQL**: Make sure PostgreSQL is installed on your machine.
- **pgAdmin 4**: This is a web-based interface for managing PostgreSQL databases.

### Steps to Set Up the Database

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/sondhg/my-django-server.git
   cd my-django-server
   ```

2. **Set Up a Virtual Environment**:

   - Create a virtual environment to manage your project dependencies:

   ```bash
   python -m venv venv
   ```

   - Activate the virtual environment:

     - On Windows:

       ```bash
       venv\Scripts\activate
       ```

     - On macOS and Linux:

       ```bash
       source venv/bin/activate
       ```

   - Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. **Create a New Database in PostgreSQL**:

   - Open **pgAdmin 4**.
   - Right-click on the `Databases` node and select `Create > Database...`.
   - Enter a name for your database (e.g., `yt_django_auth`) and click `Save`.

4. **Configure Database Settings in Django**:

   - Open the `settings.py` file in your Django project.
   - Update the `DATABASES` setting with your PostgreSQL database details:

   ```python
   DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "yt_django_auth",  # Name of the database you created
        "USER": "root",  # PostgreSQL user you created
        "PASSWORD": "rootroot",  # Password for the user
        "HOST": "localhost",  # Or the server address
        "PORT": "5432",  # Default PostgreSQL port
    }
   }
   ```

5. **Apply Migrations**:

   - Run the following commands to apply migrations and set up the database schema:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

Now your database should be set up and ready to use with the Django REST framework code in this project.

## How to run django server

To run the Django server, follow these steps:

1. **Ensure the Virtual Environment is Activated**:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

2. **Start the Django Development Server**:

   ```bash
   python manage.py runserver
   ```

3. **Access the Server**:

   Open your web browser and go to `http://127.0.0.1:8000/`.

Now your backend, or Django server should be running and accessible at the specified URL. Run the frontend by following the README.md file from [agv-project](https://github.com/sondhg/agv-project) in combination with this, then you can test user authentication actions such as login, register and logout on the graphical user interface.
