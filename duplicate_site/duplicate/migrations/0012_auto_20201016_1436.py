# Generated by Django 3.1.2 on 2020-10-16 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('duplicate', '0011_auto_20201015_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='collage',
            name='count_image',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='collage',
            name='main_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='current_collage', to='duplicate.customimage'),
        ),
    ]
