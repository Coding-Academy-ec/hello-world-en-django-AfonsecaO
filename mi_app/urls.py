from django.urls import path
from .views import hello_world

urlpatterns = [
    # define la ruta para la vista hello_world.
    path ("mi_app/", hello_world)
    
]