# Generated by Django 5.0.7 on 2024-07-18 13:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy_app', '0008_remove_cart_customer_remove_cart_medicine_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicine',
            old_name='sale_price',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='medicine',
            name='expiry_date',
        ),
        migrations.RemoveField(
            model_name='medicine',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='medicine',
            name='unit_price',
        ),
        migrations.RemoveField(
            model_name='pharmacist',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='pharmacist',
            name='username',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='city',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='email',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='supplier_id',
        ),
        migrations.AddField(
            model_name='medicine',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='pharmacist',
            name='employee_id',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='pharmacist',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='supplier',
            name='contact_info',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=20)),
                ('user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False)),
                ('transaction_id', models.CharField(max_length=100, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy_app.customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy_app.medicine')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy_app.order')),
            ],
        ),
    ]
