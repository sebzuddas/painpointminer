from django.urls import path
from . import views

urlpatterns = [
    path('ping/', views.ping, name='ping'),
]


urlpatterns = [
    # ... other endpoints ...
    path('langflow/', views.langflow_chat, name='langflow_chat'),
]