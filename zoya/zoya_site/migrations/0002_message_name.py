# Generated by Django 3.2 on 2022-09-15 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoya_site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='name',
            field=models.CharField(default='nowa wiadomość', max_length=125),
            preserve_default=False,
        ),
    ]