# Generated by Django 4.2.5 on 2023-10-08 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_notes_namehash_hashtablenotes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hashtablenotes',
            name='notes',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.notes'),
        ),
    ]
