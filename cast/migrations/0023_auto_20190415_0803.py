# Generated by Django 2.2 on 2019-04-15 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cast', '0022_chaptermark'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='chaptermark',
            unique_together={('audio', 'start')},
        ),
    ]
