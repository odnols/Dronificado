from django.forms import ModelForm
from core.models import Carga, Viagem, Droneport, Rota, Contrato, Empresa, Drone


class FormEmpresa(ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'


class FormContrato(ModelForm):
    class Meta:
        model = Contrato
        fields = '__all__'


class FormCarga(ModelForm):
    class Meta:
        model = Carga
        fields = '__all__'


class FormDrone(ModelForm):
    class Meta:
        model = Drone
        fields = '__all__'


class FormDroneport(ModelForm):
    class Meta:
        model = Droneport
        fields = '__all__'


class FormRota(ModelForm):
    class Meta:
        model = Rota
        fields = '__all__'


class FormViagem(ModelForm):
    class Meta:
        model = Viagem
        fields = '__all__'