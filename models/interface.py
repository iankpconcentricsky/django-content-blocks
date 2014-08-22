from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models


class JoinTable(models.Model):
    """
    A Many-to-Many table which joins ContentBlocks with any Model in the system.
    """
    position = models.PositiveIntegerField(default=1)

    # Any Model in the system (except this one) can have a Content Block
    content_type = models.ForeignKey(ContentType,
        related_name='content_set',
        # TODO Make this configurable within settings.py
        limit_choices_to=~models.Q(app_label='content_blocks')
    )
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    # Any "Content Block" Model (except the JoinTable Model which isn't a Block)
    content_block_type = models.ForeignKey(ContentType,
        related_name='content_block_set',
        limit_choices_to=models.Q(
            models.Q(app_label='content_blocks'), ~models.Q(model='jointable')
        )
    )
    content_block_id = models.PositiveIntegerField()
    content_block = generic.GenericForeignKey('content_block_type',
                                              'content_block_id')

    class Meta:
        ordering = ['position']
        app_label='content_blocks'


class ContentBlockInterface(models.Model):
    """
    To define your own Block layout, inherit from this abstract Model.
    Defines the set of fields and methods common to all ContentBlock Models.
    """
    content_block_title = models.CharField(max_length=1024)  # TODO: name this differently? section_title?
    content_blocks = generic.GenericRelation(JoinTable,
                                             content_type_field="content_block_type",
                                             object_id_field="content_block_id")

    def __unicode__(self):
        return self.content_block_title

    @property
    def used_on(self):
        return ", ".join(map(lambda x: unicode(x.content_object),
                             self.content_blocks.all()))

    class Meta:
        abstract=True
        app_label='content_blocks'
