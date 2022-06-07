from .models import Sales,Product,SalesDetails
from rest_framework import serializers




class SalesDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SalesDetails
        fields = "__all__"  


class SalesSerializer(serializers.ModelSerializer):
    salesby = SalesDetailsSerializer(read_only=True,many=True)
    class Meta:
        model = Sales
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    productby = SalesDetailsSerializer(read_only=True,many=True)
    class Meta:
        model = Product
        fields = "__all__"   