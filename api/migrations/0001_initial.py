# Generated by Django 4.0.5 on 2022-06-06 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=30)),
                ('ProductDetails', models.CharField(max_length=30)),
                ('productPrice', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerName', models.CharField(max_length=30)),
                ('mobileNo', models.CharField(max_length=30)),
                ('totalAmount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='SalesDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('unitPrice', models.FloatField()),
                ('total', models.FloatField()),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product')),
                ('salesId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.sales')),
            ],
        ),
    ]
