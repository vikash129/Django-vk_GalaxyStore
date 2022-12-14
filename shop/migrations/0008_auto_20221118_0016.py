# Generated by Django 3.2 on 2022-11-17 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_subcategory_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='sub_category',
            field=models.ManyToManyField(blank=True, related_name='sub_category', to='shop.SubCategory'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='shop/images/category__name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(blank=True, default=5, on_delete=django.db.models.deletion.CASCADE, to='shop.subcategory'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='products', to='shop.Product'),
        ),
    ]
