# Generated by Django 3.2.6 on 2021-08-20 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0004_alter_rental_return_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rental',
            name='customer',
        ),
        migrations.AddField(
            model_name='rental',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='rent.customer'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='rental',
            name='vehicle',
        ),
        migrations.AddField(
            model_name='rental',
            name='vehicle',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='rent.vehiclesize'),
            preserve_default=False,
        ),
    ]