# Generated by Django 4.1 on 2023-08-27 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RApp', '0006_alter_seprofile_sellcerti'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seprofile',
            name='sellcerti',
            field=models.FileField(default='test.pdf', upload_to='Attachments/'),
        ),
    ]
