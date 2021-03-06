# Generated by Django 3.2.6 on 2021-08-24 14:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilmRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='filmrate_requests_created', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FilmComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='filmcomment_requests_created', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='comments',
            field=models.ManyToManyField(to='films.FilmComment'),
        ),
        migrations.AddField(
            model_name='film',
            name='rate',
            field=models.ManyToManyField(to='films.FilmRate'),
        ),
    ]
