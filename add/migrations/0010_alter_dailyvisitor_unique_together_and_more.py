# Generated by Django 4.2.6 on 2023-10-27 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add', '0009_alter_dailyvisitor_visitor_count_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='dailyvisitor',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='dailyvisitor',
            name='visitor_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name='dailyvisitor',
            name='vistor',
        ),
        migrations.DeleteModel(
            name='vistor_user',
        ),
    ]