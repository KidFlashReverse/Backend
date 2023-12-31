# Generated by Django 4.2.4 on 2023-11-28 00:22

from django.db import migrations, models
import geral.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('geral', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacao',
            fields=[
                ('id_publicao', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('endereco', models.CharField(max_length=254)),
                ('texto_explicativo', models.TextField()),
                ('valor', models.PositiveIntegerField(default=None, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=geral.models.upload_media)),
            ],
        ),
        migrations.DeleteModel(
            name='Produto',
        ),
        migrations.AlterModelManagers(
            name='usuario',
            managers=[
            ],
        ),
    ]
