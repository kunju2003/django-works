from django.urls import path
from . import views
urlpatterns=[
    path('sum/<int:a>/<int:b>',views.sum),
    
]