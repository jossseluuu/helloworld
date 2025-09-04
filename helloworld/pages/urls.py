# pages/urls.py
from .views import home_page_view
from django.urls import path, include

urlpatterns = [
    path("", home_page_view),
    path("", include("pages.urls"))
]
