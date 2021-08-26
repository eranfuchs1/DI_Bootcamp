# Generated by Django 3.2.6 on 2021-08-19 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_date', models.DateField(auto_now_add=True)),
                ('return_date', models.DateField()),
                ('customer', models.ManyToManyField(to='rent.Customer')),
                ('vehicle', models.ManyToManyField(to='rent.Vehicle')),
            ],
        ),
    ]