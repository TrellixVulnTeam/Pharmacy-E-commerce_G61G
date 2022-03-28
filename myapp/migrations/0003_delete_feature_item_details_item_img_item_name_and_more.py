# Generated by Django 4.0.3 on 2022-03-28 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_feature'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Feature',
        ),
        migrations.AddField(
            model_name='item',
            name='details',
            field=models.TextField(default='My products details', max_length=500),
        ),
        migrations.AddField(
            model_name='item',
            name='img',
            field=models.ImageField(null=True, upload_to='products/'),
        ),
        migrations.AddField(
            model_name='item',
            name='name',
            field=models.CharField(default='My product name', max_length=100),
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, default='45', max_digits=10),
        ),
    ]
