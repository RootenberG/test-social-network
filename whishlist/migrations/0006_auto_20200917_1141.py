# Generated by Django 3.1.1 on 2020-09-17 11:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('whishlist', '0005_auto_20200917_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
