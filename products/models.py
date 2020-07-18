from django.db import models

# Create your models here.

class TileTest(models.Model):
    testval = models.CharField(max_length=10, default='test')

class TileColors(models.Model):
    color_is_active = models.BooleanField(default = True)
    color_name = models.CharField(max_length=30)
    color_name_rus = models.CharField(max_length=30)

    def __str__(self):
        return self.color_name_rus


class TileUsage(models.Model):
    usage_is_active = models.BooleanField(default = True)
    usage_type = models.CharField(max_length=30)
    usage_type_rus = models.CharField(max_length=30)

    def __str__(self):
        return self.usage_type_rus

class TileSurface(models.Model):
    surface_is_active = models.BooleanField(default = True)
    surface_type_rus = models.CharField(max_length=30)
    surface_type = models.CharField(max_length=30)

    def __str__(self):
        return self.surface_type_rus

class TileProduct(models.Model):
    tile_is_active = models.BooleanField(default = True)
    tile_name = models.CharField(max_length=30)
    img_url = models.URLField(default = 'http://www.amk-mosaic.ru/img/tiles/thumbs/25-fl-s-092.jpg')
    img_url_full_size = models.URLField(default = 'http://www.amk-mosaic.ru/img/tiles/thumbs/25-fl-s-092.jpg')
    tile_desc = models.CharField(max_length=250)
    tile_color = models.ManyToManyField('TileColors', related_name = 'colors')
    tile_usage = models.ManyToManyField('TileUsage', related_name = 'usage')
    tile_surface = models.ManyToManyField('TileSurface', related_name = 'surface')
    tile_chip_size = models.DecimalField(max_digits=5, decimal_places=2, default = 25)
    meters_in_box = models.DecimalField(max_digits=4, decimal_places=2,default=1)
    box_weight = models.DecimalField(max_digits=5, decimal_places=2,default=9.2)
    lists_in_box = models.PositiveIntegerField(default=10)
    price = models.PositiveIntegerField(default=0)
    color_qty = models.PositiveIntegerField(default=1)



    def __str__(self):
        return self.tile_name

    def get_color(self):
        return self.tile_color.values_list('color_name',flat=True)

class MessageModel(models.Model):
    customer_name = models.CharField(max_length=30)
    customer_phone = models.CharField(max_length=30)
    customer_message = models.TextField(max_length=350)
    customer_url = models.URLField(max_length=300)

    def __str__(self):
        return self.customer_name
