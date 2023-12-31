# Generated by Django 3.2.20 on 2023-09-06 07:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zohoapp', '0005_alter_bankcreation_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor_Credits_Bills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(blank=True, max_length=100, null=True)),
                ('source_supply', models.CharField(blank=True, max_length=100, null=True)),
                ('gst_number', models.CharField(blank=True, max_length=150, null=True)),
                ('vendor_email', models.CharField(max_length=250)),
                ('gst_treatment', models.CharField(max_length=100)),
                ('credit_note', models.CharField(blank=True, max_length=100, null=True)),
                ('order_no', models.CharField(blank=True, max_length=100, null=True)),
                ('vendor_date', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('sub_total', models.FloatField(blank=True, null=True)),
                ('igst', models.FloatField(blank=True, null=True)),
                ('cgst', models.FloatField(blank=True, null=True)),
                ('sgst', models.FloatField(blank=True, null=True)),
                ('tax_amount', models.FloatField(blank=True, null=True)),
                ('adjustment', models.FloatField(blank=True, null=True)),
                ('grand_total', models.FloatField(blank=True, null=True)),
                ('note', models.CharField(blank=True, max_length=255, null=True)),
                ('document', models.FileField(blank=True, null=True, upload_to='doc/Vendor_Credits_Bills')),
                ('comments', models.CharField(blank=True, max_length=255, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.company_details')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor_Credits_Bills_items_bills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(blank=True, max_length=100, null=True)),
                ('hsn', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('rate', models.FloatField(blank=True, null=True)),
                ('tax', models.FloatField(blank=True, null=True)),
                ('discount', models.FloatField(blank=True, null=True)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.company_details')),
                ('recur_bills', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.vendor_credits_bills')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='credits_comments_table',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.vendor_credits_bills'),
        ),
        migrations.AlterField(
            model_name='credits_doc_upload_table',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.vendor_credits_bills'),
        ),
        migrations.AlterField(
            model_name='credits_mail_table',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.vendor_credits_bills'),
        ),
    ]
