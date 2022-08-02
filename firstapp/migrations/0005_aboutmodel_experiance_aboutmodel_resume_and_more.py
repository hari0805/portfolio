# Generated by Django 4.0.3 on 2022-07-06 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_alter_aboutmodel_managers_remove_aboutmodel_photo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutmodel',
            name='Experiance',
            field=models.IntegerField(default=2, max_length=10),
        ),
        migrations.AddField(
            model_name='aboutmodel',
            name='Resume',
            field=models.FileField(null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='aboutmodel',
            name='Address',
            field=models.CharField(default='Chennai', max_length=100),
        ),
        migrations.AlterField(
            model_name='aboutmodel',
            name='Phone_number',
            field=models.CharField(default='9988776655', max_length=10),
        ),
        migrations.AlterField(
            model_name='aboutmodel',
            name='Profile_photo',
            field=models.ImageField(default='default_profile.jpg', upload_to='media'),
        ),
    ]
