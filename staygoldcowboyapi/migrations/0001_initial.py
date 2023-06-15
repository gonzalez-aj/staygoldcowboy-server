# Generated by Django 4.2.2 on 2023-06-15 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medium', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('creation_date', models.DateField()),
                ('image_url', models.URLField()),
                ('fan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='art_fan', to='staygoldcowboyapi.fan')),
                ('tag', models.ManyToManyField(related_name='art_tags', to='staygoldcowboyapi.tag')),
            ],
        ),
    ]
