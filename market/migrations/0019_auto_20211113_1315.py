# Generated by Django 3.2.9 on 2021-11-13 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0018_auto_20211113_1257'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carmodel',
            old_name='title',
            new_name='make',
        ),
        migrations.RemoveField(
            model_name='carmodel',
            name='carmanifacturer',
        ),
        migrations.AddField(
            model_name='carmodel',
            name='model',
            field=models.CharField(default='S5', max_length=255),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='CarManifacturer',
        ),
    ]