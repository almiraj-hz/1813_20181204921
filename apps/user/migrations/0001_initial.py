# Generated by Django 2.1.4 on 2020-06-27 20:33

import datetime
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adname', models.CharField(max_length=50, verbose_name='广告名称')),
                ('adimage', models.ImageField(upload_to='advert/%Y/%m', verbose_name='侧边广告图')),
                ('adurl', models.URLField(verbose_name='访问地址')),
                ('adindex', models.IntegerField(default=100, verbose_name='顺序')),
                ('ad_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('adtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.TypeInfo', verbose_name='广告类别')),
            ],
            options={
                'verbose_name': '侧边广告',
                'verbose_name_plural': '侧边广告',
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('image', models.ImageField(upload_to='banner/%Y/%m', verbose_name='轮播图')),
                ('url', models.URLField(verbose_name='访问地址')),
                ('index', models.IntegerField(default=100, verbose_name='顺序')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
            },
        ),
        migrations.CreateModel(
            name='GoodsBrowser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('browser_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='浏览时间')),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsInfo', verbose_name='商品ID')),
            ],
            options={
                'verbose_name': '用户浏览记录',
                'verbose_name_plural': '用户浏览记录',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20, unique=True, verbose_name='用户名')),
                ('upwd', models.CharField(max_length=40, verbose_name='用户密码')),
                ('uemail', models.EmailField(max_length=254, unique=True, verbose_name='邮箱')),
                ('avatar', stdimage.models.StdImageField(default='image/default.jpg', upload_to='image/%Y/%m', verbose_name='我的头像')),
                ('ushou', models.CharField(default='', max_length=20, verbose_name='收货地址')),
                ('uaddress', models.CharField(default='', max_length=100, verbose_name='地址')),
                ('uyoubian', models.CharField(default='', max_length=6, verbose_name='邮编')),
                ('uphone', models.CharField(default='', max_length=11, verbose_name='手机号')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
            },
        ),
        migrations.AddField(
            model_name='goodsbrowser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserInfo', verbose_name='用户ID'),
        ),
    ]
