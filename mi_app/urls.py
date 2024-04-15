from django.urls import path
from .views import hello

urlpatterns = [
    # define la ruta para la vista hello_world.
    path ("app/", hello)
    
]