# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor_uploader.fields
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='关于作者正文', default='')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '关于作者',
                'verbose_name_plural': '关于作者',
                'ordering': ('created_time',),
            },
        ),
        migrations.CreateModel(
            name='AboutSite',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='关于本站正文', default='')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '关于本站',
                'verbose_name_plural': '关于本站',
                'ordering': ('created_time',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='添加分类', max_length=100)),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('reader_name', models.CharField(null=True, verbose_name='读者名字', max_length=80)),
                ('body', models.TextField(verbose_name='评论内容')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('active', models.BooleanField(verbose_name='是否可用', default=True)),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
                'ordering': ('created_time',),
            },
        ),
        migrations.CreateModel(
            name='FriendWeb',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('logo_pic', models.ImageField(upload_to='photos/friend_log/%Y/%m/%d/', verbose_name='友情链接logo图片', help_text='请上传120*40像素logo')),
                ('friend_web_name', models.CharField(verbose_name='网站名字', max_length=80)),
                ('web_address', models.CharField(verbose_name='网址', max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': '友情链接',
                'verbose_name_plural': '友情链接',
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='MessageBoard',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(null=True, verbose_name='昵称', max_length=80)),
                ('body', models.TextField(verbose_name='欢迎留言')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': '留言',
                'verbose_name_plural': '留言',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(verbose_name='文章标题', max_length=250)),
                ('post_thumb', models.ImageField(null=True, upload_to='photos/thumbs/%Y/%m/%d/', verbose_name='文章缩略图', help_text='请上传186*90像素图片，用于本文章缩略图', blank=True)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='正文', default='')),
                ('publish', models.DateTimeField(verbose_name='发布时间', default=django.utils.timezone.now)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(verbose_name='文章状态', choices=[('draft', 'Draft'), ('published', 'Published')], max_length=10, default='published')),
                ('views', models.PositiveIntegerField(verbose_name='默认阅读数量', default=0)),
                ('author', models.ForeignKey(related_name='mysite_posts', verbose_name='作者', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(to='mysite.Category', verbose_name='类别')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'ordering': ('-created_time',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='添加标签项', max_length=100)),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.CreateModel(
            name='WebSettings',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('web_name', models.CharField(verbose_name='网站名称', max_length=250)),
                ('web_footer_body', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='网站底部信息')),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': '网站基本信息设置',
                'verbose_name_plural': '网站基本信息设置',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='mysite.Tag', verbose_name='标签', help_text='标签数量控制在四个以内', blank=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(related_name='comments', verbose_name='评论所属文章', to='mysite.Post'),
        ),
    ]
