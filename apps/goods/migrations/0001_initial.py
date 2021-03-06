# Generated by Django 2.1.4 on 2020-06-27 20:33

import DjangoUeditor.models
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isDelete', models.BooleanField(default=False)),
                ('gtitle', models.CharField(max_length=20, unique=True, verbose_name='商品名称')),
                ('gpic', stdimage.models.StdImageField(default='goods/default.jpg', upload_to='goods/%Y/%m', verbose_name='商品图片')),
                ('gprice', models.DecimalField(decimal_places=2, max_digits=5, max_length=20, verbose_name='商品价格')),
                ('gunit', models.CharField(default='500g', max_length=20, verbose_name='单位重量')),
                ('gclick', models.IntegerField(default=1, verbose_name='点击量')),
                ('gjianjie', models.CharField(max_length=200, verbose_name='简介')),
                ('gkucun', models.IntegerField(verbose_name='库存')),
                ('gcontent', DjangoUeditor.models.UEditorField(default='', verbose_name='商品详情')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
            },
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isDelete', models.BooleanField(default=False)),
                ('tpic', stdimage.models.StdImageField(default='goods/default.jpg', upload_to='goods/%Y/%m', verbose_name='分类图标')),
                ('ttitle', models.CharField(max_length=20, verbose_name='分类')),
            ],
            options={
                'verbose_name': '商品类型',
                'verbose_name_plural': '商品类型',
            },
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.TypeInfo', verbose_name='分类'),
        ),
    ]
