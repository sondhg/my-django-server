# Use this Django server in combination with [agv-frontend](https://github.com/sondhg/agv-frontend)

## Setting Up the Database

To ensure you have the same database setup as this project, follow these steps:

### Required installations

- **PostgreSQL**
- **pgAdmin 4**: Interface to interact with databases. This already came with PostgreSQL when you install it.

### Set up PostgreSQL Database

1. **Clone my code**:

   ```bash
   git clone https://github.com/sondhg/my-django-server.git
   cd my-django-server
   ```

2. **Set Up a Virtual Environment**:

   - Create a virtual environment (named "venv") to manage Python dependency packages:

   ```bash
   python -m venv venv
   ```

   - Activate the venv:

     - Windows:

       ```bash
       venv\Scripts\activate
       ```

     - macOS and Linux:

       ```bash
       source venv/bin/activate
       ```

   - Install packages:

     ```bash
     pip install -r requirements.txt
     ```

   - Check packages list to see if installation is successful:

     ```bash
     pip list
     ```

3. **Create a New Database in PostgreSQL**:

   - Open **pgAdmin 4**.
   - Right-click on the `Databases` node and select `Create > Database...`.
   - Enter a name for your database (e.g., `yt_django_auth`) and click `Save`.

4. **Configure Database Settings in Django**:

   - Open the `settings.py` file in your Django project.
   - Update the `DATABASES` setting with your PostgreSQL database details:

   If you don't wanna change anything, just name the database name `yt_django_auth` and keep this code:

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

   ```bash
   cd agv_backend
   python manage.py makemigrations
   python manage.py migrate
   ```

   > Note: agv_backend in the `cd agv_backend` command is the parent folder that includes the manage.py file, not the child folder with the same name.

Now your database should be set up and ready to use with the Django REST Framework code.

## How to run Django server

1. **Ensure the venv is Activated**:

   > If you use VSCode integrated terminal, venv should already be activated.

2. **Start the Django Development Server**:

   ```bash
   python manage.py runserver
   ```

Now your backend, or Django server should be running on port 8000. In combination with this, run my ReactJS frontend by following the README.md file from [agv-frontend](https://github.com/sondhg/agv-frontend). Now your fullstack web app is ready.
