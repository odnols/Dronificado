from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from core.models import Contrato, Empresa, Droneport, Drone, Rota, Viagem, Carga
from core.forms import FormEmpresa, FormContrato, FormCarga, FormDrone, FormDroneport, FormRota, FormViagem

# Create your views here.
class Registrar(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


def home(request):
    contexto = {'acao': 'SpeedBird: Transporte por Drones'}
    return render(request, 'core/index.html', contexto)


def menu_carga(request):
    contexto = {'acao': 'SpeedBird: Cargas'}
    return render(request, 'core/menu_carga.html', contexto)


def menu_contrato(request):
    contexto = {'acao': 'SpeedBird: Contratos'}
    return render(request, 'core/menu_carga.html', contexto)


def menu_drone(request):
    contexto = {'acao': 'SpeedBird: Drones'}
    return render(request, 'core/menu_drone.html', contexto)


def menu_empresa(request):
    contexto = {'acao': 'SpeedBird: Empresas'}
    return render(request, 'core/menu_empresa.html', contexto)


def menu_droneport(request):
    contexto = {'acao': 'SpeedBird: Droneports'}
    return render(request, 'core/menu_droneport.html', contexto)


def menu_rota(request):
    contexto = {'acao': 'SpeedBird: Rotas'}
    return render(request, 'core/menu_rota.html', contexto)


def menu_viagem(request):
    contexto = {'acao': 'SpeedBird: Entregas'}
    return render(request, 'core/menu_viagem.html', contexto)


def mapa_drones(request):
    contexto = {'acao': 'Mapa de Drones'}
    return render(request, 'core/mapa_drones.html', contexto)


def informacoes(request):
    contexto = {'acao': 'Rotas - Informações'}
    return render(request, 'core/informacoes.html', contexto)


def cadastro_empresa(request):
    form = FormEmpresa(request.POST or None, request.FILES or None)
    contexto = {'form': form, 'acao': 'Cadastro de Empresa', 'caso': 'Cadastrar', 'redirect': '/menu_empresa/'}
    if form.is_valid():
        # Vindo pelo 2° ciclo
        form.save()
        messages.success(request, "Empresa cadastrada com sucesso")
        return redirect('url_listagem_empresas')
    else:
        # Vindo pelo 1° ciclo
        return render(request, 'core/cadastro.html', contexto)


def listagem_empresas(request):
    if request.POST:
        if request.POST['cnpj']:
            dados = Empresa.objects.filter(cnpj=request.POST['cnpj'])
        else:
            dados = Empresa.objects.all()
    else:
        dados = Empresa.objects.all()

    contexto = {'empresas': dados, 'acao': 'Lista de Empresas'}
    return render(request, 'core/listagem_empresas.html', contexto)


def atualiza_empresa(request, id):
    obj = Empresa.objects.get(id=id)
    form = FormEmpresa(request.POST or None, request.FILES or None, instance=obj)
    contexto = {'form': form, 'acao': 'Atualização de Empresa', 'caso': 'Atualizar', 'redirect': '/menu_empresa/'}

    if form.is_valid():
        form.save()
        messages.success(request, "Empresa ( "+ obj.nome +" ) atualizada com sucesso")
        return redirect('url_listagem_empresas')
    else:
        return render(request, 'core/cadastro.html', contexto)


def exclui_empresa(request, id):
    try:
        obj = Empresa.objects.get(id=id)
        contexto = {'valor': 'a empresa ( '+ obj.nome +' )', 'redirect': '/listagem_empresas/', 'acao': 'Excluir Empresa'}

        if request.method == 'POST':
            obj.delete()
            return redirect('url_listagem_empresas')
        else:
            return render(request, 'core/confirma_exclusao.html', contexto)
    except Exception as erro:
        return redirect('url_listagem_empresas')


def cadastro_contrato(request):
    form = FormContrato(request.POST or None, request.FILES or None)
    contexto = {'form': form, 'acao': 'Cadastro de Contrato', 'caso': 'Cadastrar', 'redirect': '/menu_empresa/'}
    if form.is_valid():
        # Vindo pelo 2° ciclo
        form.save()
        messages.success(request, "Contrato iniciado com sucesso")
        return redirect('url_listagem_contratos')
    else:
        # Vindo pelo 1° ciclo
        return render(request, 'core/cadastro.html', contexto)


def listagem_contratos(request):
    dados2 = []

    if request.POST:
        if request.POST['cnpj']:
            dados = Contrato.objects.all()
            dados2 = Empresa.objects.filter(cnpj=request.POST['cnpj'])
        else:
            dados = Contrato.objects.all()
            dados2 = Empresa.objects.all()

    else:
        dados = Contrato.objects.all()
        dados2 = Empresa.objects.all()

    contexto = {'contratos': dados, 'empresas': dados2, 'acao': 'Lista de Contratos'}
    return render(request, 'core/listagem_contratos.html', contexto)


def atualiza_contrato(request, id):
    obj = Contrato.objects.get(id=id)
    form = FormContrato(request.POST or None, request.FILES or None, instance=obj)
    contexto = {'form': form, 'acao': 'Atualização de Contrato', 'caso': 'Atualizar', 'redirect': '/menu_empresa/'}

    if form.is_valid():
        form.save()
        messages.success(request, "Contrato ( "+ str(obj.id_empresa) +" ) atualizado com sucesso")
        return redirect('url_listagem_contratos')
    else:
        return render(request, 'core/cadastro.html', contexto)


def exclui_contrato(request, id):
    try:
        obj = Contrato.objects.get(id=id)
        contexto = {'valor': 'contrato', 'redirect': '/listagem_contratos/', 'acao': 'Excluir Contrato'}

        if request.method == 'POST':
            obj.delete()
            return redirect('url_listagem_contratos')
        else:
            return render(request, 'core/confirma_exclusao.html', contexto)
    except Exception as erro:
        return redirect('url_listagem_contratos')


def cadastro_carga(request):
    form = FormCarga(request.POST or None, request.FILES or None)
    contexto = {'form': form, 'acao': 'Cadastro de Cargas', 'caso': 'Cadastrar', 'redirect': '/menu_viagem/'}
    if form.is_valid():
        # Vindo pelo 2° ciclo
        form.save()
        messages.success(request, "Carga cadastrada com sucesso")
        return redirect('url_listagem_cargas')
    else:
        # Vindo pelo 1° ciclo
        return render(request, 'core/cadastro.html', contexto)


def listagem_cargas(request):
    if request.POST:
        if request.POST['cnpj']:
            dados = Carga.objects.all()
            dados2 = Empresa.objects.filter(cnpj=request.POST['cnpj'])
        else:
            dados = Carga.objects.all()
            dados2 = Empresa.objects.all()
    else:
        dados = Carga.objects.all()
        dados2 = Empresa.objects.all()

    contexto = {'cargas': dados, 'acao': 'Lista de Cargas', 'empresas': dados2}
    return render(request, 'core/listagem_cargas.html', contexto)


def atualiza_carga(request, id):
    obj = Carga.objects.get(id=id)
    form = FormCarga(request.POST or None, request.FILES or None, instance=obj)
    contexto = {'form': form, 'acao': 'Atualização de Carga', 'caso': 'Atualizar', 'redirect': '/menu_viagem/'}

    if form.is_valid():
        form.save()
        messages.success(request, "Carga ( "+ obj.notaFiscal +" ) atualizada com sucesso")
        return redirect('url_listagem_cargas')
    else:
        return render(request, 'core/cadastro.html', contexto)


def exclui_carga(request, id):
    try:
        obj = Carga.objects.get(id=id)
        contexto = {'valor': 'a carga ( '+ obj.notaFiscal +' )', 'redirect': '/listagem_cargas/', 'acao': 'Excluir Carga'}

        if request.method == 'POST':
            obj.delete()
            return redirect('url_listagem_cargas')
        else:
            return render(request, 'core/confirma_exclusao.html', contexto)
    except Exception as erro:
        return redirect('url_listagem_cargas')


def cadastro_drone(request):
    form = FormDrone(request.POST or None, request.FILES or None)
    contexto = {'form': form, 'acao': 'Cadastro de Drone', 'caso': 'Cadastrar', 'redirect': '/menu_drone/'}
    if form.is_valid():
        # Vindo pelo 2° ciclo
        form.save()
        messages.success(request, "Drone cadastrado com sucesso")
        return redirect('url_listagem_drones')
    else:
        # Vindo pelo 1° ciclo
        return render(request, 'core/cadastro.html', contexto)


def listagem_drones(request):
    if request.POST:
        if request.POST['prefixo']:
            dados = Drone.objects.filter(prefixo=request.POST['prefixo'])
        else:
            dados = Drone.objects.all()
    else:
        dados = Drone.objects.all()

    contexto = {'drones': dados, 'acao': 'Lista de Drones'}
    return render(request, 'core/listagem_drones.html', contexto)


def atualiza_drone(request, id):
    obj = Drone.objects.get(id=id)
    form = FormDrone(request.POST or None, request.FILES or None, instance=obj)
    contexto = {'form': form, 'acao': 'Atualização de Drone', 'caso': 'Atualizar', 'redirect': '/menu_drone/'}

    if form.is_valid():
        form.save()
        messages.success(request, "Drone ( "+ obj.prefixo +" ) atualizado com sucesso")
        return redirect('url_listagem_drones')
    else:
        return render(request, 'core/cadastro.html', contexto)


def exclui_drone(request, id):
    try:
        obj = Drone.objects.get(id=id)
        contexto = {'valor': obj.prefixo, 'redirect': '/listagem_drones/', 'acao': 'Excluir Drone'}

        if request.method == 'POST':
            obj.delete()
            return redirect('url_listagem_drones')
        else:
            return render(request, 'core/confirma_exclusao.html', contexto)
    except Exception as erro:
        return redirect('url_listagem_drones')


def cadastro_droneport(request):
    form = FormDroneport(request.POST or None, request.FILES or None)
    contexto = {'form': form, 'acao': 'Cadastro de Droneport', 'caso': 'Cadastrar', 'redirect': '/menu_droneport/'}
    if form.is_valid():
        # Vindo pelo 2° ciclo
        form.save()
        messages.success(request, "Droneport cadastrado com sucesso")
        return redirect('url_listagem_droneports')
    else:
        # Vindo pelo 1° ciclo
        return render(request, 'core/cadastro.html', contexto)


def listagem_droneports(request):
    if request.POST:
        if request.POST['apelido']:
            dados = Droneport.objects.filter(apelido=request.POST['apelido'])
        else:
            dados = Droneport.objects.all()
    else:
        dados = Droneport.objects.all()

    contexto = {'droneports': dados, 'acao': 'Lista de Droneports'}
    return render(request, 'core/listagem_droneports.html', contexto)


def atualiza_droneport(request, id):
    obj = Droneport.objects.get(id=id)
    form = FormDroneport(request.POST or None, request.FILES or None, instance=obj)
    contexto = {'form': form, 'acao': 'Atualização de Droneport', 'caso': 'Atualizar', 'redirect': '/menu_droneport/'}

    if form.is_valid():
        form.save()
        messages.success(request, "Droneport ( "+ obj.apelido +" ) atualizado com sucesso")
        return redirect('url_listagem_droneports')
    else:
        return render(request, 'core/cadastro.html', contexto)


def exclui_droneport(request, id):
    try:
        obj = Droneport.objects.get(id=id)
        contexto = {'valor': 'o droneport ( '+ obj.apelido +' )', 'redirect': '/listagem_droneports/', 'acao': 'Excluir Droneport'}

        if request.method == 'POST':
            obj.delete()
            return redirect('url_listagem_droneports')
        else:
            return render(request, 'core/confirma_exclusao.html', contexto)
    except Exception as erro:
        return redirect('url_listagem_droneports')


def cadastro_rota(request):
    form = FormRota(request.POST or None, request.FILES or None)
    contexto = {'form': form, 'acao': 'Cadastro de Rota', 'caso': 'Cadastrar', 'redirect': '/menu_rota/'}
    if form.is_valid():
        # Vindo pelo 2° ciclo
        form.save()
        messages.success(request, "Rota cadastrada com sucesso")
        return redirect('url_listagem_rotas')
    else:
        # Vindo pelo 1° ciclo
        return render(request, 'core/cadastro.html', contexto)


def listagem_rotas(request):
    if request.POST:
        if request.POST['apelido']:
            dados = Rota.objects.filter(apelido=request.POST['apelido'])
        else:
            dados = Rota.objects.all()
    else:
        dados = Rota.objects.all()

    contexto = {'rotas': dados, 'acao': 'Lista de Rotas'}
    return render(request, 'core/listagem_rotas.html', contexto)


def atualiza_rota(request, id):
    obj = Rota.objects.get(id=id)
    form = FormRota(request.POST or None, request.FILES or None, instance=obj)
    contexto = {'form': form, 'acao': 'Atualização de Rota', 'caso': 'Atualizar', 'redirect': '/menu_rota/'}

    if form.is_valid():
        form.save()
        messages.success(request, "Rota ( "+ obj.apelido +" ) atualizada com sucesso")
        return redirect('url_listagem_rotas')
    else:
        return render(request, 'core/cadastro.html', contexto)


def exclui_rota(request, id):
    try:
        obj = Rota.objects.get(id=id)
        contexto = {'valor': 'a rota ( '+ obj.apelido +' )', 'redirect': '/listagem_rotas/', 'acao': 'Excluir Rota'}

        if request.method == 'POST':
            obj.delete()
            return redirect('url_listagem_rotas')
        else:
            return render(request, 'core/confirma_exclusao.html', contexto)
    except Exception as erro:
        return redirect('url_listagem_rotas')


def cadastro_viagem(request):
    form = FormViagem(request.POST or None, request.FILES or None)
    contexto = {'form': form, 'acao': 'Cadastro de Viagem', 'caso': 'Cadastrar', 'redirect': '/menu_viagem/'}
    if form.is_valid():
        # Vindo pelo 2° ciclo
        form.save()
        messages.success(request, "Entrega agendada com sucesso")
        return redirect('url_listagem_viagens')
    else:
        # Vindo pelo 1° ciclo
        return render(request, 'core/cadastro.html', contexto)


def listagem_viagens(request):
    if request.POST:
        if request.POST['notaFiscal']:
            dados = Viagem.objects.all()
            dados2 = Carga.objects.filter(notaFiscal=request.POST['notaFiscal'])
        else:
            dados = Viagem.objects.all()
            dados2 = Carga.objects.all()
    else:
        dados = Viagem.objects.all()
        dados2 = Carga.objects.all()

    contexto = {'viagens': dados, 'acao': 'Lista de Entregas', 'cargas': dados2}
    return render(request, 'core/listagem_viagens.html', contexto)


def atualiza_viagem(request, id):
    obj = Viagem.objects.get(id=id)
    form = FormViagem(request.POST or None, request.FILES or None, instance=obj)
    contexto = {'form': form, 'acao': 'Atualização de Entrega', 'caso': 'Atualizar', 'redirect': '/menu_viagem/'}

    if form.is_valid():
        form.save()
        messages.success(request, "Entrega ( "+ str(obj.id) +" ) atualizada com sucesso")
        return redirect('url_listagem_viagens')
    else:
        return render(request, 'core/cadastro.html', contexto)


def exclui_viagem(request, id):
    try:
        obj = Viagem.objects.get(id=id)
        contexto = {'valor': 'a entrega ( '+ str(obj.carga_id) +' )', 'redirect': '/listagem_viagens/', 'acao': 'Excluir Entrega'}

        if request.method == 'POST':
            obj.delete()
            return redirect('url_listagem_viagens')
        else:
            return render(request, 'core/confirma_exclusao.html', contexto)
    except Exception as erro:
        return redirect('url_listagem_viagens')