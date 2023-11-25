# Generated by Django 4.2.7 on 2023-11-18 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Underwear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('name', models.TextField()),
                ('vendore_code', models.BigIntegerField()),
                ('price', models.IntegerField()),
                ('count', models.IntegerField()),
                ('sizes', models.ManyToManyField(to='store.size')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TShirtsAndTops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('name', models.TextField()),
                ('vendore_code', models.BigIntegerField()),
                ('price', models.IntegerField()),
                ('count', models.IntegerField()),
                ('sizes', models.ManyToManyField(to='store.size')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Trousers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('name', models.TextField()),
                ('vendore_code', models.BigIntegerField()),
                ('price', models.IntegerField()),
                ('count', models.IntegerField()),
                ('sizes', models.ManyToManyField(to='store.size')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShirtsAndBlouses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('name', models.TextField()),
                ('vendore_code', models.BigIntegerField()),
                ('price', models.IntegerField()),
                ('count', models.IntegerField()),
                ('sizes', models.ManyToManyField(to='store.size')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PantsuitsShortsSkirts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('name', models.TextField()),
                ('vendore_code', models.BigIntegerField()),
                ('price', models.IntegerField()),
                ('count', models.IntegerField()),
                ('sizes', models.ManyToManyField(to='store.size')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OverallsJacketsRaincoatsCardigans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('name', models.TextField()),
                ('vendore_code', models.BigIntegerField()),
                ('price', models.IntegerField()),
                ('count', models.IntegerField()),
                ('sizes', models.ManyToManyField(to='store.size')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Jeans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('name', models.TextField()),
                ('vendore_code', models.BigIntegerField()),
                ('price', models.IntegerField()),
                ('count', models.IntegerField()),
                ('sizes', models.ManyToManyField(to='store.size')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Jacket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('name', models.TextField()),
                ('vendore_code', models.BigIntegerField()),
                ('price', models.IntegerField()),
                ('count', models.IntegerField()),
                ('sizes', models.ManyToManyField(to='store.size')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Dresses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('name', models.TextField()),
                ('vendore_code', models.BigIntegerField()),
                ('price', models.IntegerField()),
                ('count', models.IntegerField()),
                ('sizes', models.ManyToManyField(to='store.size')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]