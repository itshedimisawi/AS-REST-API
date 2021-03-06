# Generated by Django 3.2.9 on 2021-11-13 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0017_alter_postimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='carmodel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carmodel', to='market.carmodel'),
        ),
        migrations.AlterField(
            model_name='postimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/photos'),
        ),
    ]
