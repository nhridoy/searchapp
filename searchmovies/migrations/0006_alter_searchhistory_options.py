# Generated by Django 3.2.6 on 2021-07-31 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchmovies', '0005_alter_searchhistory_search_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='searchhistory',
            options={'ordering': ('-search_date',), 'verbose_name_plural': 'Search Histories'},
        ),
    ]
