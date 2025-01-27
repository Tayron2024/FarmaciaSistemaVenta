import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Farmacia.settings')  # Asegúrate de que esto coincida con el nombre del directorio de tu proyecto.

application = get_wsgi_application()
