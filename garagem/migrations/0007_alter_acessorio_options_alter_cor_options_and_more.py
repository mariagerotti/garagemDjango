# Generated by Django 4.1.7 on 2023-03-31 18:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("garagem", "0006_veiculo"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="acessorio",
            options={"verbose_name_plural": "Acessorios"},
        ),
        migrations.AlterModelOptions(
            name="cor",
            options={"verbose_name_plural": "Cores"},
        ),
        migrations.AlterModelOptions(
            name="veiculo",
            options={"verbose_name_plural": "Veiculos"},
        ),
    ]