# Generated by Django 2.0 on 2021-01-17 02:57

import django.core.validators
from django.db import migrations, models
import voting.models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0004_voting_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_options',
            field=models.PositiveIntegerField(choices=[(1, 'Simple question'), (2, 'Preference question')], default=1),
        ),
        migrations.AddField(
            model_name='question',
            name='yes_no_question',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='questionoption',
            name='pref_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='voting',
            name='link',
            field=models.CharField(blank=True, default='', max_length=30, null=True, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Sólo se permiten letras y números.')]),
        ),
        migrations.AlterField(
            model_name='voting',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True, validators=[voting.models.end_date_past]),
        ),
    ]
