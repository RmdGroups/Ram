# Generated by Django 3.1 on 2020-08-23 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('idno', models.IntegerField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=30)),
            ],
        ),
    ]
