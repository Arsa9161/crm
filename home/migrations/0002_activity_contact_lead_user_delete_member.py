# Generated by Django 4.2.1 on 2023-05-17 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.TextField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('owner', models.TextField(null=True)),
                ('status', models.TextField(null=True)),
                ('dateType', models.TextField(null=True)),
                ('createdDate', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contacted_name', models.TextField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('note', models.TextField(null=True)),
                ('type', models.TextField(null=True)),
                ('date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lead_name', models.TextField(max_length=255)),
                ('phone', models.IntegerField(null=True)),
                ('address', models.TextField(null=True)),
                ('monthlySale', models.TextField(null=True)),
                ('dailySale', models.TextField(null=True)),
                ('yearlySale', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255)),
                ('phone', models.IntegerField(null=True)),
                ('company', models.TextField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]