# Generated by Django 4.2.2 on 2023-06-28 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredients', models.CharField(max_length=200)),
                ('nutri_score', models.CharField(max_length=1)),
                ('name', models.CharField(max_length=25)),
                ('brand', models.CharField(max_length=25)),
                ('category', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='ProductPair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_product', models.CharField(max_length=200)),
                ('alternative_product', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('alternatives', models.ManyToManyField(to='search.productpair')),
            ],
        ),
        migrations.DeleteModel(
            name='Produit',
        ),
        migrations.AddField(
            model_name='productpair',
            name='user_rec',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.user'),
        ),
    ]
