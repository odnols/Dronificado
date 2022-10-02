"""Drone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from core.views import home, Registrar, \
     menu_drone, menu_empresa, menu_contrato, menu_droneport, menu_rota, menu_viagem, menu_carga, \
     cadastro_empresa, listagem_empresas, atualiza_empresa, exclui_empresa, \
     cadastro_contrato, listagem_contratos, atualiza_contrato, exclui_contrato, \
     cadastro_carga, listagem_cargas, atualiza_carga, exclui_carga, \
     cadastro_drone, listagem_drones, atualiza_drone, exclui_drone, \
     cadastro_droneport, listagem_droneports, atualiza_droneport, exclui_droneport, \
     cadastro_rota, listagem_rotas, atualiza_rota, exclui_rota, \
     cadastro_viagem, listagem_viagens, atualiza_viagem, exclui_viagem, \
     mapa_drones, informacoes


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', Registrar.as_view(), name='url_registrar'),
    path('', home,  name='url_principal'),

    path('mapa_drones/', mapa_drones, name='url_mapa_drones'),
    path('informacoes/', informacoes, name='url_informacoes'),

    path('menu_carga/', menu_carga, name='url_menu_carga'),
    path('menu_contrato/', menu_contrato, name='url_menu_contrato'),
    path('menu_drone/', menu_drone, name='url_menu_drone'),
    path('menu_droneport/', menu_droneport, name='url_menu_droneport'),
    path('menu_empresa/', menu_empresa, name='url_menu_empresa'),
    path('menu_rota/', menu_rota, name='url_menu_rota'),
    path('menu_viagem/', menu_viagem, name='url_menu_viagem'),

    path('cadastro_empresa/', cadastro_empresa, name='url_cadastro_empresa'),
    path('listagem_empresas/', listagem_empresas, name='url_listagem_empresas'),
    path('atualiza_empresa/<int:id>/', atualiza_empresa, name='url_atualiza_empresa'),
    path('exclui_empresa/<int:id>/', exclui_empresa, name='url_exclui_empresa'),

    path('cadastro_contrato/', cadastro_contrato, name='url_cadastro_contrato'),
    path('listagem_contratos/', listagem_contratos, name='url_listagem_contratos'),
    path('atualiza_contrato/<int:id>/', atualiza_contrato, name='url_atualiza_contrato'),
    path('exclui_contrato/<int:id>/', exclui_contrato, name='url_exclui_contrato'),

    path('cadastro_carga/', cadastro_carga, name='url_cadastro_carga'),
    path('listagem_cargas/', listagem_cargas, name='url_listagem_cargas'),
    path('atualiza_carga/<int:id>/', atualiza_carga, name='url_atualiza_carga'),
    path('exclui_carga/<int:id>/', exclui_carga, name='url_exclui_carga'),

    path('cadastro_drone/', cadastro_drone, name='url_cadastro_drone'),
    path('listagem_drones/', listagem_drones, name='url_listagem_drones'),
    path('atualiza_drone/<int:id>/', atualiza_drone, name='url_atualiza_drone'),
    path('exclui_drone/<int:id>/', exclui_drone, name='url_exclui_drone'),

    path('cadastro_droneport/', cadastro_droneport, name='url_cadastro_droneport'),
    path('listagem_droneports/', listagem_droneports, name='url_listagem_droneports'),
    path('atualiza_droneport/<int:id>/', atualiza_droneport, name='url_atualiza_droneport'),
    path('exclui_droneport/<int:id>/', exclui_droneport, name='url_exclui_droneport'),

    path('cadastro_rota/', cadastro_rota, name='url_cadastro_rota'),
    path('listagem_rotas/', listagem_rotas, name='url_listagem_rotas'),
    path('atualiza_rota/<int:id>/', atualiza_rota, name='url_atualiza_rota'),
    path('exclui_rota/<int:id>/', exclui_rota, name='url_exclui_rota'),

    path('cadastro_viagem/', cadastro_viagem, name='url_cadastro_viagem'),
    path('listagem_viagens/', listagem_viagens, name='url_listagem_viagens'),
    path('atualiza_viagem/<int:id>/', atualiza_viagem, name='url_atualiza_viagem'),
    path('exclui_viagem/<int:id>/', exclui_viagem, name='url_exclui_viagem'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)