# Generated by Django 3.1.6 on 2021-03-17 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20210317_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(blank=True, to='books.GenreSub'),
        ),
    ]
