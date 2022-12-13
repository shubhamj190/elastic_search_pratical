from rest_framework import serializers
from ecommerce.inventory.models import *


class AllCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model=Category
        fields=["name","slug","is_active"]
        read_only=True


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model= Product
        fields=["name","web_id"]
        read_only=True

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields=["name"]

class ProductMediaSerializer(serializers.ModelSerializer):
    img_url=serializers.SerializerMethodField()
    class Meta:
        model=Media
        fields=["img_url","alt_text"]

    def get_img_url(self, obj):
        return obj.img_url.url
class ProductAttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductAttributeValue
        depth=2
        exclude=["id"]
        read_only=True

class ProductInventorySerializer(serializers.ModelSerializer):
    brand=BrandSerializer(read_only=True)
    product=ProductSerializer(many=False, read_only=True)
    media=ProductMediaSerializer(many=True, read_only=True)
    attributes=ProductAttributeValueSerializer(source="attribute_values",many=True)

    class Meta:
        model=ProductInventory
        fields=[
            "id",
            "sku",
            "store_price",
            "is_default",
            "brand",
            "product",
            "is_on_sale",
            "weight",
            "media",
            "attributes",
            "product_type"
        ]
        read_only=True