# Generated by Django 3.0.5 on 2020-06-24 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.IntegerField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_id', models.IntegerField(primary_key=True, serialize=False)),
                ('article_text', models.TextField(blank=True, null=True)),
                ('article_text2', models.TextField(blank=True, null=True)),
                ('article_text3', models.TextField(blank=True, null=True)),
                ('article_title', models.CharField(max_length=500, null=True)),
                ('article_logo', models.CharField(max_length=500, null=True)),
                ('author', models.CharField(max_length=500, null=True)),
                ('author_profile_link', models.CharField(max_length=500, null=True)),
                ('date', models.CharField(max_length=500, null=True)),
                ('article_summary', models.CharField(max_length=50000, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category')),
            ],
        ),
    ]
