# Generated by Django 3.1.7 on 2021-03-20 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_twitter', '0005_auto_20210314_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='parent_tweet_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
