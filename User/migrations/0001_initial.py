# Generated by Django 3.0.3 on 2020-03-02 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userId', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
