# Generated by Django 2.1.2 on 2018-11-23 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_auto_20181120_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='number',
            field=models.IntegerField(default=1, verbose_name='分类数目'),
        ),
        migrations.AddField(
            model_name='tag',
            name='number',
            field=models.IntegerField(default=1, verbose_name='标签数目'),
        ),
    ]
