# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cart(models.Model):
    product = models.OneToOneField('MedicineInventory', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'cart'


class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=45)
    total_quantity = models.IntegerField()
    total_price = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'order'


class OrderDetails(models.Model):
    order = models.ForeignKey('Order', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('MedicineInventory', models.DO_NOTHING, blank=True, null=True)
    product_name = models.CharField(max_length=45, blank=True, null=True)
    quantity = models.IntegerField()
    price_per_unit = models.ForeignKey('MedicineInventory', models.DO_NOTHING, db_column='price_per_unit', related_name='orderdetails_price_per_unit_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_details'


class MedicineInventory(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=45, blank=True, null=True)
    unit = models.CharField(max_length=45, blank=True, null=True)
    product_price = models.IntegerField(blank=True, null=True)
    unit_type = models.CharField(max_length=45, blank=True, null=True)
    big_box_quantity = models.IntegerField(blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    Manufacturer = models.CharField(max_length = 45, blank=True, null=True)
    pending_quantity = models.IntegerField(default=0)
    class Meta:
        managed = False
        db_table = 'products'
