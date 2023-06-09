### 👉 Set Up for `Windows`

> Install modules via `VENV` (windows)

```
$ virtualenv env
$ .\env\Scripts\activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> Start the APP

```bash
$ python manage.py createsuperuser # create the admin
$ python manage.py runserver       # start the project
```

At this point, the app runs at `http://127.0.0.1:8000/`.

<br />

<br />

## Codebase Structure

The project is coded using a simple and intuitive structure presented below:

```bash
< PROJECT ROOT >
   |
   |-- core/
   |    |-- settings.py                   # Project Configuration
   |    |-- urls.py                       # Project Routing
   |
   |-- home/
   |    |-- views.py                      # APP Views
   |    |-- urls.py                       # APP Routing
   |    |-- models.py                     # APP Models
   |    |-- tests.py                      # Tests
   |    |-- templates/                    # Theme Customisation
   |         |-- pages                    #
   |              |-- custom-index.py     # Custom Dashboard
   |
   |-- requirements.txt                   # Project Dependencies
   |
   |-- env.sample                         # ENV Configuration (default values)
   |-- manage.py                          # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br />
