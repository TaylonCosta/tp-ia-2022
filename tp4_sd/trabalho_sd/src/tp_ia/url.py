from tp_ia.views import pagina_contagem
from django.urls import path, include


urlpatterns = [
    path('pagina-contagem/', pagina_contagem, name='pagina-contagem')
    ]