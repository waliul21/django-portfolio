# Generated by Django 3.2.4 on 2021-06-26 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tonmoy', '0011_delete_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('school', models.CharField(max_length=50)),
                ('collage', models.CharField(max_length=50)),
                ('university', models.CharField(max_length=50)),
                ('webdesign', models.CharField(max_length=50)),
                ('webdevelopment', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('time', models.IntegerField()),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]