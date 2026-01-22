# Generated manually to add term fields to Committee

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0011_hansard_date_received_orderpaper_date_received_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='committee',
            name='begin_date',
            field=models.DateField(blank=True, help_text='Committee term begin date', null=True),
        ),
        migrations.AddField(
            model_name='committee',
            name='end_date',
            field=models.DateField(blank=True, help_text='Committee term end date', null=True),
        ),
    ]
