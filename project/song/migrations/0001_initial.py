# Generated by Django 3.0.4 on 2020-03-27 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Geet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(null=True, upload_to='logo/')),
                ('title', models.CharField(max_length=200)),
                ('artist', models.CharField(blank=True, max_length=200)),
                ('album', models.CharField(blank=True, max_length=200)),
                ('year', models.IntegerField(blank=True)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('fav', models.BooleanField(default='False')),
                ('track', models.FileField(null=True, upload_to='track/')),
            ],
        ),
    ]
