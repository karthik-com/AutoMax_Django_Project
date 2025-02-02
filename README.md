# AutoMax_Django_Project
AutoMax - Best Deal for your car
This web application provides best deals for the buyer and the seller.
It is a Django based web project using Python, HTML, CSS, and BootStrap.

Steps to start your django project:
1. Install django using command prompt
     pip install Django
2. Start a project
     django-admin startproject automax
3. Change directory to automax
     cd automax
4. Create apps
     python manage.py startapp main
     python manage.py startapp users
5. Add apps to INSTALLED_APPS variable in automax/settings.py
6. (Optional)(Recommended) Create virtual environment
     pip install virtualenv
     virtualenv env_name
     env_name\Scripts\activate
7. Install django again in virtual environment. Also install required modules in virtual environment.
