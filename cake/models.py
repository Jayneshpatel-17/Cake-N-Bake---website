from django.db import models
from datetime import datetime

class userModel(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    contact = models.CharField(max_length=10 , default='Null')
    dob = models.DateField()
    password = models.CharField(max_length=15)
    cpassword = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.username
    
class category(models.Model):
    name = models.CharField(max_length=30)

    @staticmethod
    def get_all_categories():
        return category.objects.all()

    def __str__(self):
        return self.name
    
class product(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    category = models.ForeignKey(category, on_delete=models.CASCADE , default=1)
    description = models.TextField(max_length=250, default='')
    ingredients = models.TextField(max_length=500, default='')
    image = models.ImageField(upload_to='products/')
    date = models.DateTimeField(default=datetime.now)

    @staticmethod
    def get_all_products():
        return product.objects.all()

    @staticmethod
    def get_all_product_by_category_id(category_id):
        if category_id:
            return product.objects.filter(category=category_id)
        else:
            return product.get_all_products()

    def __str__(self):
        return self.name
    
class shape(models.Model):
    name = models.CharField(max_length=20)

    @staticmethod
    def get_all_shape():
        return shape.objects.all()

    def __str__(self):
        return self.name
    
class flavor(models.Model):
    name = models.CharField(max_length=20)

    @staticmethod
    def get_all_flavor():
        return flavor.objects.all()

    def __str__(self):
        return self.name
    
class cart(models.Model):
    username = models.CharField(max_length=50)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    image = models.ImageField(null=True , blank=True)
    weight = models.CharField(max_length=10,default='300g')
    quantity = models.PositiveIntegerField(default=1)
    price = models.IntegerField(default=0)
    shape = models.CharField(max_length=10,default='round')
    flavor = models.CharField(max_length=30,default=None)
    total = models.IntegerField(default=0)

    def total_price(self):
        return self.quantity * self.price

class review(models.Model):
    username = models.CharField(max_length=50)
    feedback = models.TextField(max_length=500)
    date = models.DateTimeField(default=datetime.now)

    @staticmethod
    def get_all_review():
        return review.objects.all()


STATUS_CHOICE = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
)  

class order(models.Model):
    username = models.CharField(max_length=50)
    delivery_name = models.CharField(max_length=50)
    contact = models.CharField(max_length=10 , default='Null')
    address = models.CharField(max_length=200)
    product = models.CharField(max_length=50)
    quantity = models.PositiveBigIntegerField(default=1)
    weight = models.CharField(max_length=10,default='300g')
    shape = models.CharField(max_length=20,default='round')
    flavor = models.CharField(max_length=20,default=None)
    image = models.ImageField(null=True , blank=True)
    price = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.now)
    status = models.CharField(max_length=50,default='Pending',choices=STATUS_CHOICE)

    @staticmethod
    def get_all_order():
        return order.objects.all()
    
class blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True , blank=True)
    blog = models.TextField(max_length=500)
    date = models.DateTimeField(default=datetime.now)

    @staticmethod
    def get_all_blog():
        return blog.objects.all()
    
class inquiry(models.Model):
    username = models.CharField(max_length=50)
    issue = models.TextField(max_length=500)
    ans = models.TextField(max_length=500)
    date = models.DateTimeField(default=datetime.now)

    @staticmethod
    def get_all_inquiry():
        return inquiry.objects.all()
