# Generated by Django 3.1.2 on 2020-10-13 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('duplicate', '0004_auto_20201013_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='customimage',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
