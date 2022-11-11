from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=100)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


# Home page Begin
class HeroSection(models.Model):
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="img/hero")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Hero Section'
        verbose_name_plural = 'Hero Sections'


class BannerSection(models.Model):
    first_title = models.CharField(max_length=50, verbose_name='Название первого баннера', help_text="Test help text", blank=True, null=True)
    first_photo = models.ImageField(upload_to="img/banner", blank=True, null=True)
    second_title = models.CharField(max_length=50, verbose_name='Название второго баннера', blank=True, null=True)
    second_photo = models.ImageField(upload_to="img/banner", blank=True, null=True)
    third_title = models.CharField(max_length=50, verbose_name='Название третьего баннера', blank=True, null=True)
    third_photo = models.ImageField(upload_to="img/banner", blank=True, null=True)

    def __str__(self):
        return self.first_title

    class Meta:
        verbose_name = 'Banner Section'
        verbose_name_plural = 'Banner Sections'


class NewSale(models.Model):
    last_sale = models.CharField(max_length=100, verbose_name='Прошлая скидка', blank=True, null=True)
    now_sale = models.CharField(max_length=100, verbose_name='Новая скидка', blank=True, null=True)
    future_sale = models.CharField(max_length=100, verbose_name='Скоро', blank=True, null=True)
    picture = models.ImageField(upload_to="img/sale")
    price = models.CharField(max_length=20, verbose_name='Цена включая скидку', blank=True, null=True)
    title = models.CharField(max_length=50, default='DEAL OF THE WEEK')
    name = models.CharField(max_length=100, verbose_name='Название акции')

    def __str__(self):
        return self.last_sale

    class Meta:
        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'


class LatestBlog(models.Model):
    author = models.CharField(max_length=50, verbose_name='Автор')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    photo = models.ImageField(upload_to="img/latest")
    date = models.DateTimeField(auto_now=True)
    content = models.TextField(verbose_name='Котнетн')
    contents = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'


class EmailForMailing(models.Model):
    email = models.EmailField()


class Mailing(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="img/mailing")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

# Home page End
