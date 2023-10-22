# Token Authentication

---

### To setup the project locally, follow these steps:

-   To set up a virtual environment, run: `python3 -m venv venv`
-   Then activate the virtual environment with: `source venv/bin/activate`
-   Install the dependencies with: `pip install -r requirements.txt`
-   Then run: `python manage.py migrate`
-   Then run the server with: `python manage.py runserver`
-   The endpoint in the app are the following:
    -   Registering a user: `/api/users/register/`
    -   Getting auth token: `/api/users/token/`
    -   Retrieving or updating user: `/api/users/me/`
    -   Logging out: `/api/users/logout/`
