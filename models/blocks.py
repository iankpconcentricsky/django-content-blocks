from content_blocks.models import ContentBlockInterface
from django.db import models

try:
    from ckeditor.fields import HTMLField as RichTextField
except ImportError:
    from ckeditor.fields import RichTextField


class ThreeColumn(ContentBlockInterface):
    template_name = '3-col.html'

    image1 = models.ImageField(upload_to='uploads/content_blocks')
    title1 = models.CharField(max_length=500, blank=True)
    body1 = RichTextField()
    image2 = models.ImageField(upload_to='uploads/content_blocks')
    title2 = models.CharField(max_length=500, blank=True)
    body2 = RichTextField()
    image3 = models.ImageField(upload_to='uploads/content_blocks')
    title3 = models.CharField(max_length=500, blank=True)
    body3 = RichTextField()

    class Meta:
        verbose_name_plural="Three column"
        app_label='content_blocks'


class TwoColumn(ContentBlockInterface):
    template_name = '2-col.html'

    title1 = models.CharField(max_length=500, blank=True)
    body1 = RichTextField()
    title2 = models.CharField(max_length=500, blank=True)
    body2 = RichTextField()

    class Meta:
        verbose_name_plural="Two column"
        app_label='content_blocks'


class OneColumn(ContentBlockInterface):
    template_name = '1-col.html'

    POSITION_CHOICES = (
        ('top', 'Top'),
        ('left', 'Left'),
        ('right', 'Right'),
        ('bottom', 'Bottom'),
    )

    image_position = models.CharField(max_length=10, choices=POSITION_CHOICES, default='bottom')
    image = models.ImageField(upload_to='uploads/modules')

    title = models.CharField(max_length=500)
    body = RichTextField()

    class Meta:
        verbose_name_plural="One column"
        app_label='content_blocks'


class Quote(ContentBlockInterface):
    template_name = 'quote.html'

    body = models.TextField()
    author = models.CharField(max_length=500)
    source = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural="Quote"
        app_label='content_blocks'
