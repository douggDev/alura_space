# Generated by Django 5.0.3 on 2024-03-14 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('ESTRELA', 'Estrela'), ('GALÁXIA', 'Galáxia'), ('NEBULOSA', 'Nebulosa'), ('PLANETA', 'Planeta')], default='', max_length=100),
        ),
    ]
