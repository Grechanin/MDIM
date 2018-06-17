from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class Prices(models.Model):
    title = models.CharField(max_length=128, blank=True, null=True, default=None)
    short_description = RichTextUploadingField(blank=True, null=True, default=None)
    description = RichTextUploadingField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return ("%s") % self.title

    class Meta:
        verbose_name = 'Розділ "Ціни"'
        verbose_name_plural = 'Розділи "Ціни"'


class PriceCategory(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return ("%s") % self.name

    class Meta:
        verbose_name = 'Категорія ціни'
        verbose_name_plural = 'Категорії цін'


class ProiceCategoryDescription(models.Model):
    category = models.ForeignKey(PriceCategory, blank=True, null=True, default=None, on_delete=models.CASCADE)
    title = models.CharField(max_length=128, blank=True, null=True, default=None)
    description = RichTextUploadingField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return ("%s") % self.title

    class Meta:
        verbose_name = 'Опис категорії ціни'
        verbose_name_plural = 'Описи категорії ціни'