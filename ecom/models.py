from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name

# class Product(models.Model):
#     name=models.CharField(max_length=40)
#     product_image= models.ImageField(upload_to='product_image/',null=True,blank=True)
#     price = models.PositiveIntegerField()
#     description=models.CharField(max_length=500)
#     def __str__(self):
#         return self.name
    


    
from django.db import models

class Product(models.Model):
    class FairTradeValues(models.TextChoices):
        ENERGY_EFFICIENCY = "ENERGY_EFFICIENCY", "ENERGY_EFFICIENCY"
        RENEWABLE_ENERGY = "RENEWABLE_ENERGY", "RENEWABLE_ENERGY"
        FOREST_MANAGEMENT = "FOREST_MANAGEMENT", "FOREST_MANAGEMENT" 


    project_id = models.CharField(max_length=255, blank=True, unique=True)
    project_name = models.CharField(max_length=255, blank=True)
    voluntary_registry = models.CharField(max_length=255, blank=True)
    voluntary_status = models.CharField(max_length=255, blank=True)
    scope = models.CharField(max_length=255, blank=True)
    project_type = models.CharField(max_length=255, blank=True)
    reduction_removal = models.CharField(max_length=255, blank=True)
    methodology_protocol = models.CharField(max_length=255, blank=True)
    region = models.CharField(max_length=255, blank=True)
    documents = models.CharField(null=True, max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    state = models.CharField(null=True, max_length=255, blank=True)
    project_site_location = models.CharField(max_length=255, blank=True)
    project_developer = models.CharField(max_length=255, blank=True)
    total_credits_issued = models.IntegerField(blank=True ,default=0)
    total_credits_retired = models.IntegerField(blank=True,default=0)
    total_credits_remaining = models.IntegerField(blank=True,default=0)
    ccb_certifications = models.CharField(max_length=255, blank=True)
    project_owner = models.CharField(max_length=255, blank=True)
    offset_project_operator = models.CharField(max_length=255, blank=True)
    authorized_project_designee = models.CharField(max_length=255, blank=True, null=True)
    verifier = models.CharField(max_length=255, blank=True)
    registry_arb = models.CharField(max_length=255, blank=True)
    project_listed = models.CharField(max_length=255,blank=True)
    project_registered = models.CharField(max_length=255,blank=True)
    project_type = models.CharField(max_length=255, blank=True)
    registry_documents = models.CharField(max_length=255, blank=True)
    project_website = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=255, choices=FairTradeValues.choices, null=True, blank=True)
    #price = models.MoneyField(max_digits=14, decimal_places=2, default_currency='USD', help_text='Price of a tonne of carbon')
    image_url = models.URLField(default='', help_text='Url for ccompanying image of the project')

    def __str__(self):
        return self.project_name
    
    def compute_credit_price(self):
        A = {
            "ENERGY_EFFICIENCY" : 8.20 * 1.08 + 1.08,
            "RENEWABLE_ENERGY" : 8.10 * 1.08 + 1.08,
            "FOREST_MANAGEMENT" : 13 * 1.08 + 1.08
        }

        B = 12

        D = 35

        C = 0.05 * (A[self.category] + B + D)

        E = 1

        F = (A + B + C + D)

        if E < F:
            return (E-F) + (E-F) + (0.05 * E) 
        
        if E == F:
            return E + (0.05 * E)
        
        return F

       




        


    
    
    def save(self, *args, **kwargs):
        result = super().save(*args, **kwargs)
        self.price = self.compute_credit_price()
        return result


class Orders(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
    customer=models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
    product=models.ForeignKey('Product',on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    mobile = models.CharField(max_length=20,null=True)
    order_date= models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)


class Feedback(models.Model):
    name=models.CharField(max_length=40)
    feedback=models.CharField(max_length=500)
    date= models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name
    
class Wishlist(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.get_name} - {self.product.name} Wishlist"
