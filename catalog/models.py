from django.db import models
from django.urls import reverse
import uuid


class Admin(models.Model):
    admin_id = models.CharField(max_length=255, unique=True, primary_key=True)
    admin_fname = models.CharField(max_length=100)
    admin_lname = models.CharField(max_length=100)
    admin_username = models.CharField(max_length=100, unique=True)
    admin_password = models.CharField(max_length=255)
    personal_info = models.ForeignKey("PersonalInfo", on_delete=models.CASCADE)

    def __str__(self):
        return self.admin_id

class PersonalInfo(models.Model):
    personal_info_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    personal_info_fname = models.CharField(max_length=100)
    personal_info_lname = models.CharField(max_length=100)
    personal_info_email = models.EmailField(unique=True)

    def __str__(self):
        return self.personal_info_id


class Events(models.Model):
    event_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    event_name = models.CharField(max_length=100)
    event_url = models.URLField()

    def __str__(self):
        return self.event_id

class Neighborhood(models.Model):
    neighborhood_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    neighborhood_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.neighborhood_id

class PropertyType(models.Model):
    property_type_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    property_type_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.property_type_id

class PriceRange(models.Model):
    price_range_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    price_range_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.price_range_id

class Property(models.Model):
    status_choice = [
        ('available', 'Available'),
        ('pending', 'Pending'),
        ('sold', 'Sold'),
    ]

    property_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    property_street = models.CharField(max_length=255)
    property_city = models.CharField(max_length=100)
    property_state = models.CharField(max_length=100)
    property_zipcode = models.CharField(max_length=20)
    property_price = models.DecimalField(max_digits=10, decimal_places=2)
    property_description = models.TextField()
    property_status = models.CharField(max_length=10, choices=status_choice, default='available')
    property_date_added = models.DateField(auto_now_add=True)
    property_date_sold = models.DateField(null=True, blank=True)
    property_is_featured = models.BooleanField(default=False)
    property_is_visible = models.BooleanField(default=True)
    property_type_id = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    neighborhood_id = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    price_range_id = models.ForeignKey(PriceRange, on_delete=models.CASCADE)

    def __str__(self):
        return self.property_street

class Photo(models.Model):
    photo_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    photo_url = models.URLField()
    photo_description = models.TextField()
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE)

    def __str__(self):
        return self.photo_id

class SearchLog(models.Model):
    search_log_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    search_date = models.DateTimeField(auto_now_add=True)
    property_type_id = models.ForeignKey(PropertyType, null = True, blank = True, on_delete=models.SET_NULL)
    neighborhood_id = models.ForeignKey(Neighborhood, null = True, blank = True, on_delete=models.SET_NULL)
    price_range_id = models.ForeignKey(PriceRange, null = True, blank = True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.search_log_id



class OwnerProfile(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    bio = models.TextField()
    image = models.ImageField(upload_to='owner_profiles/')

    def __str__(self):
        return self.name


