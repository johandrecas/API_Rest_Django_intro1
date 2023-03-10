from django.urls import path
from .views import book


# como funciona esto explique parte por parte :



urlpatterns=[
    path('',book,name='book'),

]