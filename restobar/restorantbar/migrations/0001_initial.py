# Generated by Django 4.2.1 on 2023-06-13 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_table', models.CharField(max_length=45)),
                ('capacite_table', models.CharField(max_length=45)),
                ('description_table', models.TextField()),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'tab',
            },
        ),
    ]
