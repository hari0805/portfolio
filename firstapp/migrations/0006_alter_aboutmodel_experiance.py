# Generated by Django 4.0.6 on 2022-08-02 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_aboutmodel_experiance_aboutmodel_resume_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutmodel',
            name='Experiance',
            field=models.IntegerField(default=2),
        ),
    ]
