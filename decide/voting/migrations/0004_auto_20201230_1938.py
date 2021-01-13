# Generated by Django 2.0 on 2020-12-30 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0003_auto_20180605_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='type',
            field=models.IntegerField(choices=[(1, 'Unique Answer'), (2, 'Preference answer')], default='1', verbose_name='Answer type'),
        ),
        migrations.AddField(
            model_name='questionoption',
            name='preference',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='questionoption',
            name='option',
            field=models.CharField(max_length=200),
        ),
    ]