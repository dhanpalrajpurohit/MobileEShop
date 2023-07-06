# Generated by Django 3.2 on 2021-05-17 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='author_details',
            fields=[
                ('author_id', models.AutoField(primary_key=True, serialize=False)),
                ('author_name', models.CharField(max_length=255)),
                ('author_image', models.ImageField(upload_to='media/author')),
            ],
        ),
    ]