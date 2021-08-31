# Generated by Django 3.2.6 on 2021-08-31 03:15

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
            name='SearchHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_keyword', models.CharField(max_length=264, verbose_name='Keyword')),
                ('search_results', models.IntegerField(verbose_name='Total Results')),
                ('search_date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_search_history', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Search Histories',
            },
        ),
    ]