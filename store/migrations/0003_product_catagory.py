# Generated by Django 4.0.2 on 2022-02-27 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_catagory_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='catagory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.catagory'),
        ),
    ]
