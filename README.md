# Client-Management-System

CMS is an Agent portal which allow agent to add customer either manually(one at a time) or using a csv file.

For Live Demo: https://client-management-system-bp.herokuapp.com/

## Requirements
To be able to run CMS you have to meet following requirements:

Python (3.6, 3.7, 3.8)

Django (3.x)

## 📖 Installation
```
$ git clone https://github.com/aayushkumar0795/Client-Management-System.git
$ cd client_management_system/
$ pipenv install
$ pipenv shell
```

## 🚀 Configuration
```
# Run Migrations
(client_management_system) $ python manage.py migrate

# Create a Superuser:
(client_management_system) $ python manage.py createsuperuser

# Load site with Dummy data:
(client_management_system) $ python manage.py load_dummy_data

# Confirm everything is working:
(client_management_system) $ python manage.py runserver

# Load the site at http://127.0.0.1:8000
```

## ⭐️ Add-ons

CMS supports multiple languages. English and Spanish to be specific.

To see Spanish version of the website, install Locale Switcher for chrome and select spanish.
(https://chrome.google.com/webstore/detail/locale-switcher/kngfjpghaokedippaapkfihdlmmlafcc)
