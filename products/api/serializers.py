from rest_framework import serializers

from rest_framework_recaptcha.fields import ReCaptchaField
from products.models import TileProduct, MessageModel,TileColors,TileUsage,TileSurface

""" class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TileProduct
        fields = '__all__' """

class ColorPropsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TileColors
        fields = ['color_name','color_name_rus']

class UsagePropsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TileUsage
        fields = ['usage_type','usage_type_rus']

class SurfacePropsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TileSurface
        fields = ['surface_type','surface_type_rus']

class PropertiesSerializer(serializers.Serializer):

    colors = ColorPropsSerializer(many=True)
    usages = UsagePropsSerializer(many=True)
    surfaces = SurfacePropsSerializer(many=True)



class ProductsSerializer(serializers.ModelSerializer):
    tile_color = serializers.StringRelatedField(many=True, read_only=True)
    tile_usage = serializers.StringRelatedField(many=True, read_only=True)
    tile_surface = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = TileProduct
        fields = ['id','tile_name', 'img_url','img_url_full_size', 'tile_color', 'color_qty', 'tile_usage', 'tile_surface', 'price' ]

class TileRecordSerializer(serializers.ModelSerializer):
    tile_color = serializers.StringRelatedField(many=True, read_only=True)
    tile_usage = serializers.StringRelatedField(many=True, read_only=True)
    tile_surface = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = TileProduct
        fields = '__all__'

class CaptchaSerializer(serializers.Serializer):
    # recaptcha = ReCaptchaField()
    id = serializers.IntegerField(read_only=True)
    customer_name = serializers.CharField(max_length=30)
    customer_phone = serializers.CharField(max_length=30)
    customer_message = serializers.CharField(max_length=350)
    customer_url = serializers.CharField(max_length=300)
    def create(self, validated_data):
        return MessageModel.objects.create(**validated_data)

    class Meta:
        model = MessageModel
        fields=['customer_name', 'customer_phone','customer_message','customer_url']
