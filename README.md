# [Django Bootstrap 5](https://appseed.us/admin-dashboards/django-dashboard-volt) Volt

[Admin dashboard](https://appseed.us/admin-dashboards) generated by AppSeed in **[Django](https://appseed.us/admin-dashboards/django)** Framework. Volt Dashboard is a free and open source **[Bootstrap 5](https://appseed.us/admin-dashboards/django-dashboard-volt)** Admin Dashboard featuring over 100 components, 11 example pages and 3 plugins with Vanilla JS. There are more than 100 free Bootstrap 5 components included some of them being buttons, alerts, modals, datepickers and so on.

<br />


<br />

> Links

- [Django Bootstrap 5 Volt](https://appseed.us/admin-dashboards/django-dashboard-volt) - product page
- [Django Bootstrap 5 Volt](https://django-volt-dashboard.appseed-srv1.com/) - LIVE deployment
- [Django Bootstrap 5 Volt](https://docs.appseed.us/products/django-dashboards/volt) - product documentation

<br />

## Want more? Go PRO!

PRO versions include **Premium UI Kits**, Lifetime updates and **24/7 LIVE Support** (via [Discord](https://discord.gg/fZC6hup))

| [Django Datta PRO](https://appseed.us/admin-dashboards/django-dashboard-dattaable-pro) | [Django Soft PRO](https://appseed.us/product/django-soft-ui-dashboard-pro) | [Django Volt PRO](https://appseed.us/admin-dashboards/django-dashboard-volt-pro) |
| --- | --- | --- |
| [![Django Datta PRO](https://raw.githubusercontent.com/app-generator/django-dashboard-dattaable-pro/master/media/django-dashboard-dattaable-pro-screen.png)](https://appseed.us/admin-dashboards/django-dashboard-dattaable-pro) | [![Django Soft PRO](https://user-images.githubusercontent.com/51070104/123547150-3f176300-d768-11eb-9359-ad6611e19a3a.png)](https://appseed.us/product/django-soft-ui-dashboard-pro) | [![Django Volt PRO](https://raw.githubusercontent.com/app-generator/django-dashboard-volt-pro/master/media/django-dashboard-volt-pro-screen.png)](https://appseed.us/admin-dashboards/django-dashboard-volt-pro)

<br />
<br />

![Django Bootstrap 5 Volt - Template project provided by AppSeed.](https://raw.githubusercontent.com/app-generator/django-dashboard-volt/master/media/django-dashboard-volt-screen.png)

<br />

## How to use it

```bash
$ # Get the code
$ git clone https://github.com/app-generator/django-dashboard-volt.git
$ cd django-dashboard-volt
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install modules - SQLite Storage
$ pip3 install -r requirements.txt
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
$
$ # Start the app - custom port
$ # python manage.py runserver 0.0.0.0:<your_port>
$
$ # Access the web app in browser: http://127.0.0.1:8000/
```

> Note: To use the app, please access the registration page and create a new user. After authentication, the app will unlock the private pages.

<br />

## Code-base structure

The project is coded using a simple and intuitive structure presented bellow:

```bash
< PROJECT ROOT >
   |
   |-- core/                               # Implements app configuration
   |    |-- settings.py                    # Defines Global Settings
   |    |-- wsgi.py                        # Start the app in production
   |    |-- urls.py                        # Define URLs served by all apps/nodes
   |
   |-- apps/
   |    |
   |    |-- home/                          # A simple app that serve HTML files
   |    |    |-- views.py                  # Serve HTML pages for authenticated users
   |    |    |-- urls.py                   # Define some super simple routes  
   |    |
   |    |-- authentication/                # Handles auth routes (login and register)
   |    |    |-- urls.py                   # Define authentication routes  
   |    |    |-- views.py                  # Handles login and registration  
   |    |    |-- forms.py                  # Define auth forms (login and register) 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/                     # Templates used to render pages
   |         |-- includes/                 # HTML chunks and components
   |         |    |-- navigation.html      # Top menu component
   |         |    |-- sidebar.html         # Sidebar component
   |         |    |-- footer.html          # App Footer
   |         |    |-- scripts.html         # Scripts common to all pages
   |         |
   |         |-- layouts/                   # Master pages
   |         |    |-- base-fullscreen.html  # Used by Authentication pages
   |         |    |-- base.html             # Used by common pages
   |         |
   |         |-- accounts/                  # Authentication pages
   |         |    |-- login.html            # Login page
   |         |    |-- register.html         # Register page
   |         |
   |         |-- home/                      # UI Kit Pages
   |              |-- index.html            # Index page
   |              |-- 404-page.html         # 404 page
   |              |-- *.html                # All other pages
   |
   |-- requirements.txt                     # Development modules - SQLite storage
   |
   |-- .env                                 # Inject Configuration via Environment
   |-- manage.py                            # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br />

> The bootstrap flow

- Django bootstrapper `manage.py` uses `core/settings.py` as the main configuration file
- `core/settings.py` loads the app magic from `.env` file
- Redirect the guest users to Login page
- Unlock the pages served by *app* node for authenticated users

<br />



<br />

## Credits & Links

- [Django](https://www.djangoproject.com/) - The official website
- [Boilerplate Code](https://appseed.us/boilerplate-code) - Index provided by **AppSeed**
- [Boilerplate Code](https://github.com/app-generator/boilerplate-code) - Index published on Github

<br />

---
[Django Bootstrap 5](https://appseed.us/admin-dashboards/django-dashboard-volt) Volt - Provided by **AppSeed [App Generator](https://appseed.us/app-generator)**.
