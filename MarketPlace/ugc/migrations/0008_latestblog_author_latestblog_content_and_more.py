# Generated by Django 4.1.3 on 2022-11-09 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0007_latestblog_newsale_alter_bannersection_first_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='latestblog',
            name='author',
            field=models.CharField(default=1, max_length=50, verbose_name='Автор'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='latestblog',
            name='content',
            field=models.TextField(default=1, verbose_name='Котнетн'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='latestblog',
            name='contents',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='latestblog',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
    ]