# Generated by Django 2.1.5 on 2019-01-11 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clean_blog_app', '0003_auto_20190111_1412'),
    ]

    operations = [
        migrations.CreateModel(
            name='post_part_two',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('discriptions', models.TextField()),
                ('bquote', models.CharField(max_length=250)),
                ('pTwo', models.TextField()),
            ],
        ),
    ]
