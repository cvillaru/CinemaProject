# Generated by Django 4.2.1 on 2023-05-31 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cinema', '0003_film_age_rating_film_duration_film_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='screen',
            name='screen_number',
            field=models.PositiveIntegerField(default=0, unique=True),
        ),
        migrations.CreateModel(
            name='Showing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('showing_date', models.DateField(null=True)),
                ('showing_time', models.TimeField()),
                ('tickets_sold', models.SmallIntegerField(default=0)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='showing', to='Cinema.film')),
                ('screen', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='showing', to='Cinema.screen')),
            ],
        ),
    ]
