from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.views.generic import TemplateView

# from .serializers import MonografiaSerializers
# from .api import MonografiaApi
from monografia.views import Index,  CreateAccount
from django.contrib.auth import views as auth_views

from tp_ia.views import pagina_contagem, write

urlpatterns = [

    path('auth/', include([
        path('create/', CreateAccount, name='user-create'),
        path('cadastro/', CreateAccount, name='user-registro')
    ])),

    path('', Index, name='index'),
    path('pagina-contagem/', pagina_contagem, name='pagina-contagem'),
    path('gera-tabela/', write, name='gera')

]