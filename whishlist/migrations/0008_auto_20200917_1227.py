# Generated by Django 3.1.1 on 2020-09-17 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whishlist', '0007_remove_item_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='whishlist_id',
            new_name='wishlist_id',
        ),
    ]
