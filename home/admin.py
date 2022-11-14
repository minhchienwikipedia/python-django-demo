from django.contrib import admin
from .models import Item, ItemType

# Register your models here.


class ItemTypeInline(admin.StackedInline):
    model = Item
    extra = 0
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status')
    search_fields = ['title']
    raw_id_fields = ['user']
    

class ItemTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ['name']
    inlines = [ItemTypeInline]

admin.site.register(Item, ItemAdmin)
admin.site.register(ItemType, ItemTypeAdmin)
