from django.contrib import admin

# Dependencies
from client_admin.admin import ImageWidgetMixin  # TODO: Extract this one
from genericadmin.admin import GenericAdminModelAdmin, GenericTabularInline

from content_blocks.models import (JoinTable,
                                   ThreeColumn, TwoColumn, OneColumn, Quote)


class JoinTableInline(GenericTabularInline):
    model = JoinTable
    generic_fk_fields = [{
        'ct_field': 'content_block_type',
        'fk_field': 'content_block_id',
    }]

    extra = 0


class JoinTableAdmin(GenericAdminModelAdmin):
    inlines = [JoinTableInline, ]


class ContentBlockAdmin(ImageWidgetMixin, admin.ModelAdmin):
    list_display = ('__unicode__', 'used_on')


admin.site.register(ThreeColumn, ContentBlockAdmin)
admin.site.register(TwoColumn, ContentBlockAdmin)
admin.site.register(OneColumn, ContentBlockAdmin)
admin.site.register(Quote, ContentBlockAdmin)
