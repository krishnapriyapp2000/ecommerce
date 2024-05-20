# Generated by Django 5.0.1 on 2024-01-22 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_category_customer_order_products_delete_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paymethod',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='paystatus',
            field=models.BooleanField(default=False),
        ),
    ]