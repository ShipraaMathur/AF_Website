# Generated by Django 3.1.4 on 2021-01-06 17:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0029_auto_20210106_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='art_type',
            field=models.CharField(choices=[('Sketches', 'Sketches'), ('Doodles', 'Doodles'), ('Anime', 'Anime'), ('Abstract', 'Abstract'), ('Portrait', 'Portrait'), ('Nature', 'Nature'), ('Digital', 'Digital'), ('Other', 'Other')], max_length=20, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 6, 17, 33, 21, 177139, tzinfo=utc)),
        ),
    ]
