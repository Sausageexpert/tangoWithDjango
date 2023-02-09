# Create URL patterns here
from . import views # the dot means same folder
from django.urls import path 
#app_name = 'tangyDjango'

urlpatterns = [
    path('index/',views.index, name='index'),
    path('', views.item, name='item'),
]

'''
the quotes would be empty for an empty path, index is the name of the path to views.index.
If something was in the quotations it would appear as tangyDjango/something in the localhost
'''
