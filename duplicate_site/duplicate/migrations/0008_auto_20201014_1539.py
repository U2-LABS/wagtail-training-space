# Generated by Django 3.1.2 on 2020-10-14 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('duplicate', '0007_customimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customimage',
            name='collage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='duplicate.collage'),
        ),
        migrations.AlterField(
            model_name='customimage',
            name='image',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='wagtailimages.image'),
        ),
    ]
