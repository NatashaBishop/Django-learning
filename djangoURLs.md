Create urls.py in the same folder as the views.py and type code:

          
                              
        from django.urls import path
        from . import views
        urlpatterns = [
            path('members/', views.members, name='members'),
          ]
The urls.py file we created is specific for out application application
