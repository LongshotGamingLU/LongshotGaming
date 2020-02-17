# Generated by Django 3.0.2 on 2020-02-17 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('gamesWon', models.IntegerField()),
                ('gamesLost', models.IntegerField()),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.User')),
            ],
        ),
    ]