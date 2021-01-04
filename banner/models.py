from django.db import models


class BannerHeader(models.Model):
    name= models.CharField(max_length=100, null=True, verbose_name='Title')
    image= models.ImageField(upload_to='banner/header', verbose_name='Image(730x90)')

    def  __str__(self):
        return self.name


class BannerSidebar(models.Model):
    name= models.CharField(max_length=100, null=True, verbose_name='Title')
    image= models.ImageField(upload_to='banner/sidebar', verbose_name='Image(300x300)')

    def  __str__(self):
        return self.name


class BannerFooter(models.Model):
    name= models.CharField(max_length=100, null=True, verbose_name='Title')
    image= models.ImageField(upload_to='banner/footer', verbose_name='Image(730x90)')

    def  __str__(self):
        return self.name