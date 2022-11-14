from django.contrib import admin
from .models import Item, ItemType
from django.utils.html import format_html


# Register your models here.


class ItemTypeInline(admin.StackedInline):
    model = Item
    extra = 0
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'type_name')
    search_fields = ['title']
    raw_id_fields = ['user']
    list_filter = ['status', 'type']

    @admin.display()
    def type_name(self, obj):
        if obj.type is not None:
            return obj.type.name
        return format_html(
            '<span style="color:gray;font-style: italic">Empty</span>',
        )
    

@admin.display(description='name')
def color_name(self):
    return format_html(
        '<span style="color: #ffb3b3;font-weight:bold">{}</span>',
        self.name.upper(),
    )

class ItemTypeAdmin(admin.ModelAdmin):
    list_display = ('id', color_name)
    search_fields = ['name']
    inlines = [ItemTypeInline]
    empty_value_display = 'unknown'

admin.site.register(Item, ItemAdmin)
admin.site.register(ItemType, ItemTypeAdmin)
