# Generated by Django 4.2 on 2024-02-20 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attractions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mustsee',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='attractions'),
        ),
    ]
