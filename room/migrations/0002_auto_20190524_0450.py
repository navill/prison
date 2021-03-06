# Generated by Django 2.2.1 on 2019-05-24 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='address_detail',
            field=models.CharField(default='', max_length=100, verbose_name='상세주소'),
        ),
        migrations.AddField(
            model_name='media',
            name='space',
            field=models.CharField(default='', max_length=10, verbose_name='공간 면적'),
        ),
        migrations.AlterField(
            model_name='media',
            name='address',
            field=models.CharField(default='', max_length=200, verbose_name='주소'),
        ),
        migrations.AlterField(
            model_name='media',
            name='description',
            field=models.TextField(verbose_name='설명'),
        ),
        migrations.AlterField(
            model_name='media',
            name='media',
            field=models.FileField(null=True, upload_to='videos/', verbose_name='미디어파일'),
        ),
        migrations.AlterField(
            model_name='media',
            name='name',
            field=models.CharField(max_length=500, verbose_name='건물 종류'),
        ),
        migrations.AlterField(
            model_name='media',
            name='price_str',
            field=models.CharField(default='', max_length=5, verbose_name='가격'),
        ),
        migrations.AlterField(
            model_name='media',
            name='select',
            field=models.CharField(default='', max_length=50, verbose_name='매매종류'),
        ),
    ]
