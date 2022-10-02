# Generated by Django 3.1.5 on 2021-01-05 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notaFiscal', models.CharField(max_length=500)),
                ('carga', models.CharField(max_length=500)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=100)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos_cargas')),
            ],
            options={
                'verbose_name_plural': 'Cargas',
            },
        ),
        migrations.CreateModel(
            name='Drone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefixo', models.CharField(max_length=10)),
                ('localizacao', models.CharField(max_length=100)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pesoMaximoSuportado', models.DecimalField(decimal_places=2, max_digits=10)),
                ('modeloDrone', models.CharField(max_length=150)),
                ('velocidadeMaxima', models.DecimalField(decimal_places=2, max_digits=10)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos_drones')),
            ],
            options={
                'verbose_name_plural': 'Drones',
            },
        ),
        migrations.CreateModel(
            name='Droneport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apelido', models.CharField(max_length=45)),
                ('localizacao', models.CharField(max_length=100)),
                ('capacidadeSuportada', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name_plural': 'Droneports',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=18)),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=45)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=45)),
                ('logradouro', models.CharField(max_length=100)),
                ('numeroRua', models.DecimalField(decimal_places=2, max_digits=10)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos_empresas')),
            ],
            options={
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='Rota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apelido', models.CharField(max_length=100)),
                ('dronePorte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.droneport')),
            ],
            options={
                'verbose_name_plural': 'Rotas',
            },
        ),
        migrations.CreateModel(
            name='Viagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carga_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.carga')),
                ('drone_prefixo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.drone')),
                ('rota_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.rota')),
            ],
            options={
                'verbose_name_plural': 'Viagens',
            },
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=20)),
                ('dataInicial', models.DateTimeField()),
                ('dataFinal', models.DateTimeField()),
                ('limiteEntregas', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.empresa')),
            ],
            options={
                'verbose_name_plural': 'Contratos',
            },
        ),
        migrations.AddField(
            model_name='carga',
            name='id_empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.empresa'),
        ),
    ]
