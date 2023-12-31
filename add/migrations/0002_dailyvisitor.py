# Generated by Django 4.2.6 on 2023-10-27 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('add', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyVisitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('visitor_count', models.PositiveIntegerField(default=0)),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='add.ad')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='add.location')),
            ],
        ),
    ]
