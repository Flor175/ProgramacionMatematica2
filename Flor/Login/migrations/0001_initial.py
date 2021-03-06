# Generated by Django 2.1.7 on 2019-03-31 23:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_carnet', models.CharField(blank=True, max_length=9, null=True, unique=True)),
                ('cui', models.CharField(blank=True, max_length=13, null=True, unique=True)),
                ('profesion', models.CharField(choices=[('1', 'Matemática'), ('2', 'Física')], default='1', max_length=100)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
