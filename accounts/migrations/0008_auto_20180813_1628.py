# Generated by Django 2.0.7 on 2018-08-13 08:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20180813_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='uid',
            field=models.CharField(default=uuid.UUID('4af6a822-4a7c-4f30-9392-087012e79db4'), max_length=40),
        ),
    ]