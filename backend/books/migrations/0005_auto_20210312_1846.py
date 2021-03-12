# Generated by Django 3.1.6 on 2021-03-12 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20210309_2222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('series_number', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='series',
            field=models.ManyToManyField(blank=True, to='books.Series'),
        ),
    ]
