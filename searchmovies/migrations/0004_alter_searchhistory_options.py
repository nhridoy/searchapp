# Generated by Django 3.2.6 on 2021-08-30 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchmovies', '0003_alter_searchhistory_search_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='searchhistory',
            options={'ordering': ('search_date',), 'verbose_name_plural': 'Search Histories'},
        ),
    ]
