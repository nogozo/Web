# Generated by Django 3.0.7 on 2020-08-09 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_trending'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homec',
            fields=[
                ('homec_id', models.IntegerField(primary_key=True, serialize=False)),
                ('homec_title', models.CharField(max_length=500, null=True)),
                ('homec_logo', models.CharField(max_length=500, null=True)),
                ('homec_url', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Homel',
            fields=[
                ('homel_id', models.IntegerField(primary_key=True, serialize=False)),
                ('homel_title', models.CharField(max_length=500, null=True)),
                ('homel_logo', models.CharField(max_length=500, null=True)),
                ('homel_date', models.CharField(max_length=500, null=True)),
                ('homel_url', models.IntegerField()),
            ],
        ),
    ]
