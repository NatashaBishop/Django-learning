in the virtual environment, navigate to the folder where you would like to start the project and run this command: 

    django-admin startproject my_project
Django will create my_project (the name of your choice) with following structure@ 

    my_project
    manage.py
    my_project/
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
Navigate to  /my_project and run the Django Project: 

    python manage.py runserver 
Type 127.0.0.1:8000 in the  browser window address bar. 
To quit the server: 

    CTRL-BREAK.
navigate to /my_project, and run the command: 
   
    python manage.py startapp bartermonster #bartermonster is the name of application

If the server is still running, and you are not able to write commands, press [CTRL] [BREAK], or [CTRL] [C] to stop the server and you should be back in the virtual environment.  
Django will create a folder named bartermonster in my_project, with this content:  
    
    my_project
    manage.py
    my_project/
    bartermonster/
        migrations/
            __init__.py
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py


