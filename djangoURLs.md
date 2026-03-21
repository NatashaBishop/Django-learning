Create urls.py in the same folder as the views.py and type code:

          
                              
        from django.urls import path
        from . import views
        urlpatterns = [
            path('bartermonster/', views.members, name='bartermonster'), #bartermonster is app name
          ]
The urls.py file we created is specific for out application application

2 run server go 2 my_project folder (the top one) and execute command:

          python manage.py runserver

