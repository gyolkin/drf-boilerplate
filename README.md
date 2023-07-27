# Django REST Framework boilerplate

## Getting started

1. Clone the repository

    ```bash
    git clone https://github.com/gyolkin/drf-boilerplate.git
    ```

2. Access the project's folder

    ```bash
    cd drf-boilerplate
    ```

3. Make it your own repository

    ```bash
    rm -rf .git
    git init
    ```

4. Initialize virtual environment

    ```bash
    py -m venv env
    ```

5. Activate the virtual environment

    ```bash
    . env/Scripts/activate
    ```

6. Install dependencies

    ```bash
    pip install -r requirements.txt
    ```

7. Start the development server

    ```bash
    python manage.py runserver
    ```

8. Prepare for production

    ```bash
    python manage.py collectstatic
    ```

**Good luck with your project!**