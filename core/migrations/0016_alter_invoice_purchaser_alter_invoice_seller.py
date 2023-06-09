# Generated by Django 4.0.4 on 2023-04-22 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_remove_invoice_amount_product_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='purchaser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchaser_invoices', to='core.user'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller_invoices', to='core.user'),
        ),
    ]
