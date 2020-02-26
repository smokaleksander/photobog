# Generated by Django 3.0.3 on 2020-02-26 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='imgs',
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='gallery',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='galleries.Gallery'),
            preserve_default=False,
        ),
    ]
