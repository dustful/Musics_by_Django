# Generated by Django 2.0.3 on 2018-03-30 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0006_auto_20180331_0252'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='lyrics',
            field=models.TextField(blank=True, null=True),
        ),
    ]
