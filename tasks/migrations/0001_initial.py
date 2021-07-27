# Generated by Django 3.1.13 on 2021-07-27 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('priority', models.CharField(choices=[('express', 'express'), ('moderate', 'moderate'), ('optional', 'optional')], default='moderate', max_length=10)),
                ('status', models.CharField(choices=[('undone', 'undone'), ('done', 'done')], default='undone', max_length=10)),
            ],
        ),
    ]