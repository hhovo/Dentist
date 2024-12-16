from django.urls import path # type: ignore
from . import views  # Ensure the views module is imported

urlpatterns = [
    path('', views.home, name='home'),  # Set as the default route
]