# Generated by Django 3.0.5 on 2020-05-27 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content_management_portal', '0003_question_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='roughsolution',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='rough_solutions', to='content_management_portal.Question'),
            preserve_default=False,
        ),
    ]