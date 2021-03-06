# Generated by Django 2.2.7 on 2019-11-07 09:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='date_of_died',
            new_name='date_of_death',
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.UUIDField(default=uuid.UUID('976d9b8b-7c2f-4e07-9879-78d7f1d2fe11'), help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False),
        ),
    ]
