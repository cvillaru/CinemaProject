# Generated by Django 4.2.1 on 2023-05-30 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cinema', '0002_screen'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='age_rating',
            field=models.CharField(default='...', max_length=5),
        ),
        migrations.AddField(
            model_name='film',
            name='duration',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='film',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='screen',
            name='capacity',
            field=models.SmallIntegerField(default=0),
        ),
    ]