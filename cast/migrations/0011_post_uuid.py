# Generated by Django 2.0.9 on 2018-11-19 12:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [("cast", "0010_blog_email")]

    operations = [
        migrations.AddField(
            model_name="post",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        )
    ]
