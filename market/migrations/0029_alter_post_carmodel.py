# Generated by Django 3.2.9 on 2021-12-08 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0028_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='carmodel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='carmodel', to='market.carmodel'),
        ),
    ]