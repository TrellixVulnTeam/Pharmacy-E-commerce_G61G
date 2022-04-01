# Generated by Django 4.0.3 on 2022-04-01 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_tag_order_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tag',
        ),
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(to='myapp.tag'),
        ),
    ]