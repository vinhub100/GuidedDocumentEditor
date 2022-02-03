# Generated by Django 3.2.8 on 2022-02-03 11:34

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discription', models.CharField(max_length=256)),
                ('image', models.ImageField(upload_to='./imagestore')),
                ('date', models.CharField(max_length=8)),
            ],
            options={
                'verbose_name': 'photo',
                'verbose_name_plural': 'photos',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=64)),
                ('discription', models.CharField(max_length=256)),
                ('dp', models.CharField(max_length=256)),
                ('a_type', models.CharField(choices=[('P', 'PUBLISHED'), ('D', 'DRAFT')], max_length=1)),
                ('body', models.TextField()),
                ('creation_date', models.DateField(auto_now=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='heading', unique=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'article',
                'verbose_name_plural': 'articles',
                'ordering': ['-creation_date'],
            },
        ),
    ]
