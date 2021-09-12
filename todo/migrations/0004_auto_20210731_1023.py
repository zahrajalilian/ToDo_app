# Generated by Django 3.2.5 on 2021-07-31 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20210730_1954'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['-due_date_time']},
        ),
        migrations.AlterField(
            model_name='todo',
            name='category',
            field=models.CharField(choices=[('MHW', 'maktab home work'), ('IDS', 'improve django skill'), ('RE', 'react exe'), ('UD', 'undecided')], default='UD', max_length=100),
        ),
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.CharField(choices=[('HIGH', 'HIGH'), ('MIDDLE', 'MIDDLE'), ('LOW', 'LOW')], default='LOW', max_length=200),
        ),
    ]