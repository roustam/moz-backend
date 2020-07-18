from django.contrib import admin
from products.models import TileProduct, TileColors, TileSurface,TileUsage,MessageModel

#class for tilerecords

class TileProductAdmin(admin.ModelAdmin):
    fields = ['tile_name', 'tile_desc', 'price', 'color_qty']
    list_display = ('tile_name', 'get_tile_color', 'get_tile_usage','get_tile_surface','price')
    search_fields =('tile_name', 'tile_desc','price')
    def get_tile_color(self,obj):
        color_list=[]
        for item in obj.tile_color.all():
            color_list.append(item.color_name_rus )
        return color_list

    def get_tile_usage(self,obj):
        usage_list=[]
        for item in obj.tile_usage.all():
            usage_list.append(item.usage_type_rus)
        return usage_list

    def get_tile_surface(self,obj):
        surface_list=[]
        for item in obj.tile_surface.all():
            surface_list.append(item.surface_type_rus)
        return surface_list


admin.site.register(TileProduct, TileProductAdmin)
admin.site.register(TileColors)
admin.site.register(TileSurface)
admin.site.register(TileUsage)
admin.site.register(MessageModel)
