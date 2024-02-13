# Generated by Django 5.0 on 2024-02-07 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0007_alter_admin_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin123',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=12)),
            ],
            options={
                'db_table': 'ttmadmin123_table',
            },
        ),
    ]