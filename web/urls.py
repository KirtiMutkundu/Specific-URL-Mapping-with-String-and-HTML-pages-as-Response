from django.urls import path
from web.views import *
app_name='nothing'
urlpatterns=[
    path('html/',html,name='html'),
]

