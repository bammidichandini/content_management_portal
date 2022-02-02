# Generated by Django 3.0.5 on 2020-06-10 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_management_portal', '0013_auto_20200605_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='cleansolution',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='hint',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='prefilledcode',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='roughsolution',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='solutionapproach',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='testcase',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
