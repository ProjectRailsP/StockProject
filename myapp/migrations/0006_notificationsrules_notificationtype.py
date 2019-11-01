# Generated by Django 2.2.6 on 2019-10-27 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_notifications'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationsRules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('minChange', models.FloatField(null=True)),
                ('maxChange', models.FloatField(null=True)),
                ('action', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='NotificationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('notificationType', models.CharField(max_length=30)),
            ],
        ),
    ]