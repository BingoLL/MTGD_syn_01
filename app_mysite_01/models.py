from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=100,verbose_name='添加分类')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='分类'
        verbose_name_plural='分类'

class Tag(models.Model):
    name=models.CharField(max_length=100,verbose_name='添加标签项')

    class Meta:
        verbose_name='标签'
        verbose_name_plural='标签'

    def __str__(self):
        return self.name

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES=(('draft','Draft'),('published','Published'),)
    title=models.CharField(max_length=250,verbose_name='文章标题')
    post_thumb=models.ImageField(upload_to='photos/thumbs/%Y/%m/%d/',blank=True,null=True,verbose_name='文章缩略图',help_text='请上传186*90像素图片，用于本文章缩略图')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='类别')
    tags=models.ManyToManyField(Tag,blank=True,verbose_name='标签',help_text='标签数量控制在四个以内')
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='mysite_posts',verbose_name='作者')
    body=RichTextUploadingField(default='',verbose_name='正文')
    publish=models.DateTimeField(default=timezone.now,verbose_name='发布时间')
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='published',verbose_name='文章状态')
    views=models.PositiveIntegerField(default=0,verbose_name='默认阅读数量')
    objects=models.Manager()
    published=PublishedManager()

    class Meta:
        ordering=('-created_time',)
        verbose_name='文章'
        verbose_name_plural='文章'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('mysite:post_detail',args=[self.id,])

    def views_count(self):
        self.views += 1
        self.save(update_fields=['views'])


class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments',verbose_name='评论所属文章')
    reader_name=models.CharField(max_length=80,null=True,verbose_name='读者名字')
    body=models.TextField(verbose_name='评论内容')
    created_time=models.DateTimeField(auto_now_add=True,verbose_name='评论时间')
    active=models.BooleanField(default=True,verbose_name='是否可用')

    class Meta:
        ordering=('created_time',)
        verbose_name='评论'
        verbose_name_plural='评论'

    def __str__(self):
        return '{}评论了文章《{}》'.format(self.reader_name,self.post)



#about.html,此页面四个选项卡
class AboutSite(models.Model):
    body=RichTextUploadingField(default='',verbose_name='关于本站正文')
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('created_time',)
        verbose_name='关于本站'
        verbose_name_plural='关于本站'

class AboutMe(models.Model):
    body=RichTextUploadingField(default='',verbose_name='关于作者正文')
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('created_time',)
        verbose_name='关于作者'
        verbose_name_plural='关于作者'

class FriendWeb(models.Model):
    logo_pic=models.ImageField(upload_to='photos/friend_log/%Y/%m/%d/',verbose_name='友情链接logo图片',help_text='请上传120*40像素logo')
    friend_web_name=models.CharField(max_length=80,verbose_name='网站名字')
    web_address=models.CharField(max_length=100,verbose_name='网址')
    created=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)

    class Meta:
        ordering=('created',)
        verbose_name='友情链接'
        verbose_name_plural='友情链接'

    def __str__(self):
        return self.friend_web_name

class MessageBoard(models.Model):
    reader_name=models.CharField(max_length=80,null=True,verbose_name='昵称')
    body=models.TextField(verbose_name='欢迎留言')
    created_time=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)

    class Meta:
        ordering=('-created_time',)
        verbose_name_plural='留言'
        verbose_name='留言'


class webSettings(models.Model):
    web_name=models.CharField(max_length=250,verbose_name='网站名称')
    web_footer_body=RichTextUploadingField(verbose_name='网站底部信息')
    created=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)

    class Meta:
        ordering=('-created',)
        verbose_name='网站基本信息设置'
        verbose_name_plural='网站基本信息设置'

