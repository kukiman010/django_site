# Generated by Django 2.2.5 on 2019-09-15 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('body', models.TextField(blank=True, db_index=True)),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
