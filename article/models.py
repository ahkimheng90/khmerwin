from django.db import models
from django.contrib.auth.models import  User
from ckeditor_uploader.fields import  RichTextUploadingField
from taggit.managers import TaggableManager




class Category(models.Model):
    title=models.CharField(max_length=250, verbose_name='Title', null=True)

    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'

    def __str__(self):
        return self.title


class Tag(models.Model):
    title=models.CharField(max_length=150, verbose_name='Tag', null=True)

    class Meta:
        verbose_name='Tag'
        verbose_name_plural='Tags'

    def __str__(self):
        return self.title


class Post(models.Model):
    title=models.CharField(max_length=250, verbose_name='Title', null=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category', null=True)
    thumbnail=models.ImageField(upload_to='articles/thumbnails/%Y/%m/%d', verbose_name='Thumbnail(850x550)', null=True)
    description=models.TextField(max_length=300, verbose_name='Description', blank=True, null=True)
    content=RichTextUploadingField(verbose_name='Content', null=True)
    author=models.ForeignKey(User,editable=False,on_delete=models.DO_NOTHING, null=True,blank=True)
    tags = TaggableManager()
    is_publish=models.BooleanField(default=True)
    publish_date=models.DateTimeField(auto_now_add=True, null=True)


    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'

    def __str__(self):
        return self.title