# Generated by Django 4.2.3 on 2023-09-22 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0012_adjustment_itemadjustment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemadjustment',
            name='adjustment',
        ),
        migrations.RemoveField(
            model_name='itemadjustment',
            name='user',
        ),
        migrations.DeleteModel(
            name='Adjustment',
        ),
        migrations.DeleteModel(
            name='ItemAdjustment',
        ),
    ]
