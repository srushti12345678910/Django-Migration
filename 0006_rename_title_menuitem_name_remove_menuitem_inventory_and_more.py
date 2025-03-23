# Generated by Django 5.1.5 on 2025-01-23 22:39

from django.db import migrations, models


class Migration(migrations.Migration):
    

    dependencies = [
        ('restaurant', '0005_menuitem_description'),
    ]
    

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='inventory',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='category',
            field=models.CharField(choices=[('Starter', 'Starter'), ('Main', 'Main'), ('Dessert', 'Dessert')], default='Starter', max_length=50),
        ),
    ]
