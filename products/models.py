from django.db import models

# Create your models here.
class Product(models.Model):
  id = models.AutoField(
    primary_key=True
  )

  genericName = models.TextField(
    max_length=1000,
    null=False,
    blank=False
  )
  
  name = models.TextField(
    max_length=1000,
    null=False,
    blank=False
  )
    
  category = models.TextField(
    max_length=1000,
    null=False,
    blank=False
  )
      
  location = models.TextField(
    max_length=1000,
    null=False,
    blank=False
  )

  created_at = models.DateTimeField(
    auto_now_add=True,
    null=False,
    blank=False
  )

  updated_at = models.DateTimeField(
    auto_now=True,
    null=False,
    blank=False
  )

  class Meta:
    db_table = 'products'