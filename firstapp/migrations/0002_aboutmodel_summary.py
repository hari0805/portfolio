# Generated by Django 4.0.3 on 2022-07-05 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutmodel',
            name='Summary',
            field=models.TextField(default='A small river named Duden flows by their place and \n             supplies it with the necessary regelialia. \n         It is a paradisematic country, in which roasted parts \n         of sentences fly into your mouth.\n', max_length=100),
        ),
    ]
