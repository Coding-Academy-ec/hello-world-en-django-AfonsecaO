## Intenta hacer una solicitud GET a la página de hello world
#response = self.client.get('/mi_app/hello/')
#
## Verifica que la respuesta es 200 (OK)
#self.assertEqual(response.status_code, 200)
## Verifica que el contenido de la respuesta sea "¡Hola Mundo!"
#self.assertContains(response, "¡Hola Mundo!")

from django.http import HttpResponse

def test_hello_world(request):
    return HttpResponse("¡Hola Mundo!")