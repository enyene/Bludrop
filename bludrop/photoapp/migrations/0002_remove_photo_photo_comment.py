# Generated by Django 4.0.6 on 2022-07-29 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photoapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='photo',
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='photoapp.photo')),
            ],
        ),
    ]
