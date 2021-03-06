# Generated by Django 3.2.4 on 2021-06-27 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tonmoy', '0016_education'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='email',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='present_location',
        ),
        migrations.AddField(
            model_name='contact',
            name='author_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='contact',
            name='facebook',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='github',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='gmail',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='instra',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='linkdin',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='youtube',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(blank=True),
        ),
    ]
