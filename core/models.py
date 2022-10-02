from django.db import models

# Create your models here.


class Empresa(models.Model):
    cnpj = models.CharField(max_length=18, blank=False, null=False)
    nome = models.CharField(max_length=100, blank=False, null=False)
    telefone = models.CharField(max_length=45, blank=False, null=False)
    cidade = models.CharField(max_length=100, blank=False, null=False)
    estado = models.CharField(max_length=45, blank=False, null=False)
    logradouro = models.CharField(max_length=100, blank=False, null=False)
    numeroRua = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    logo = models.ImageField(upload_to='logos_empresas', blank=True, null=True)

    def __str__(self):
        return self.cnpj + '(' + str(self.id) + ')'

    class Meta:
        verbose_name_plural = 'Empresas'


class Contrato(models.Model):
    valor = models.DecimalField(max_digits=20, decimal_places=2, blank=False, null=False)
    dataInicial = models.DateTimeField(auto_now_add=None)
    dataFinal = models.DateTimeField(auto_now_add=None)
    limiteEntregas = models.DecimalField(max_digits=10, decimal_places = 2, blank=False, null=False)
    id_empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)

    def __str__(self):
        return self.id_empresa + '(' + str(self.valor) + ')'

    class Meta:
        verbose_name_plural = 'Contratos'


class Carga(models.Model):
    notaFiscal = models.CharField(max_length=500, blank=False, null=False)
    carga = models.CharField(max_length=500, blank=False, null=False)
    peso = models.DecimalField(max_digits=100, decimal_places=2, blank=False, null=False)
    id_empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='fotos_cargas', blank=True, null=True)

    def __str__(self):
        return self.notaFiscal + '(' + str(self.id_empresa) + ')'

    class Meta:
        verbose_name_plural = 'Cargas'


class Drone(models.Model):
    prefixo = models.CharField(max_length=10, blank=False, null=False)
    localizacao = models.CharField(max_length=100, blank=False, null=False)
    peso = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    pesoMaximoSuportado = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    modeloDrone = models.CharField(max_length=150, blank=False, null=False)
    velocidadeMaxima = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    foto = models.ImageField(upload_to='fotos_drones', blank=True, null=True)

    def __str__(self):
        return self.prefixo + '(' + self.localizacao + ')'

    class Meta:
        verbose_name_plural = 'Drones'


class Droneport(models.Model):
    apelido = models.CharField(max_length=45, blank=False, null=False)
    localizacao = models.CharField(max_length=100, blank=False, null=False)
    capacidadeSuportada = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)

    def __str__(self):
        return self.apelido + '(' + self.localizacao + ')'

    class Meta:
        verbose_name_plural = 'Droneports'


class Rota(models.Model):
    apelido = models.CharField(max_length=100, blank=False, null=False)
    dronePorteInicial = models.ForeignKey('Droneport', on_delete=models.CASCADE)
    dronePorteFinal = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.apelido + '( Droneporte Inicial: '+ str(self.dronePorteInicial) +', Droneporte Final: '+ str(self.dronePorteFinal) +')'

    class Meta:
        verbose_name_plural = 'Rotas'


class Viagem(models.Model):
    carga_id = models.ForeignKey('Carga', on_delete=models.CASCADE)
    drone_prefixo = models.ForeignKey('Drone', on_delete=models.CASCADE)
    rota_id = models.ForeignKey('Rota', on_delete=models.CASCADE)

    def __str__(self):
        return self.id + '( Drone: ' + self.drone_prefixo + ', Rota: ' + self.rota_id + ')'

    class Meta:
        verbose_name_plural = 'Viagens'