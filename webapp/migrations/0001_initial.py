# Generated by Django 3.2.9 on 2022-03-23 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('Id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Product_Name', models.CharField(max_length=200)),
                ('Category', models.CharField(default='', max_length=30)),
                ('Color', models.CharField(max_length=50)),
                ('Full_Description', models.TextField(default='')),
                ('Price', models.FloatField()),
                ('Product_Image', models.ImageField(default='NoImage', upload_to='Product_Images/')),
            ],
        ),
    ]
