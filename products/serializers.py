from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
  genericName = serializers.CharField(max_length=255, required=True)
  name = serializers.CharField(max_length=255, required=True)
  category = serializers.CharField(max_length=255, required=True)
  location = serializers.CharField(max_length=255, required=True)
  created_at = serializers.DateTimeField()
  updated_at = serializers.DateTimeField()

  def create(self, validated_data):
    # Once the request data has been validated, we can create a todo item instance in the database
    return Product.objects.create(
      genericName=validated_data.get('genericName'),
      name=validated_data.get('name'),
      category=validated_data.get('category'),
      location=validated_data.get('location')
    )

  def update(self, instance, validated_data):
     # Once the request data has been validated, we can update the todo item instance in the database
    instance.genericName = validated_data.get('genericName', instance.genericName)
    instance.name = validated_data.get('name', instance.name) 
    instance.category = validated_data.get('category', instance.category)
    instance.location = validated_data.get('location', instance.location)
    instance.save()
    return instance

  class Meta:
    model = Product
    fields = (
      'id',
      'genericName',
      'name',
      'category',
      'location',
      'created_at',
      'updated_at'
    )