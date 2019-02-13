#import decimal
from decimal import Decimal
from django.db import models

# Create your models here.

''' List of fields needed
size
toppings - dropdown something
pizza type --->>(regular vs silican) no of toppings vs no of items
Extra/addition/specials
price
--------------

Before we start delivering any meals, we need to know:

Who ordered the meal
Where and when the meal should be delivered
What dishes are included in the order
What ingredients we need to fulfill the order
If the order has already been paid for

quant = Decimal('0.01')
'''
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Menu(models.Model):
    class_name = models.CharField(max_length=30)
    mtype = models.CharField(max_length=5, default='pasta')
    name = models.CharField(max_length=30)
    num_toppings = models.IntegerField()
    size = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    price_big = models.DecimalField(max_digits=5, decimal_places=2, null=True)

class Order(models.Model):
    user = models.CharField(max_length=60)
    items_in_menu = models.IntegerField()
    total = models.DecimalField(max_digits=5, decimal_places=2)
    items = models.CharField(max_length=1000)

class Carts(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    cart = models.CharField(max_length=1000)

"""
Menu(class_name='Regular Pizza', name='Cheese', num_toppings=0, size=True, price=12.20, price_big=17.45)
Menu(class_name='Regular Pizza', name='1 topping', num_toppings=1, size=True, price=13.20, price_big=19.45)
Menu(class_name='Regular Pizza', name='2 toppings', num_toppings=2, size=True, price=14.70, price_big=23.45)
Menu(class_name='Regular Pizza', name='3 toppings', num_toppings=3, size=True, price=15.70, price_big=17.45)
Menu(class_name='Regular Pizza', name='Special', num_toppings=30, size=True, price=17.25, price_big=25.45)

Menu(class_name='Sicilian Pizza', name='Cheese', num_toppings=0, size=True, price=23.45, price_big=37.70)
Menu(class_name='Sicilian Pizza', name='1 topping', num_toppings=1, size=True, price=25.45, price_big=39.70)
Menu(class_name='Sicilian Pizza', name='2 toppings', num_toppings=2, size=True, price=27.45, price_big=41.70)
Menu(class_name='Sicilian Pizza', name='3 toppings', num_toppings=3, size=True, price=28.45, price_big=43.70)
Menu(class_name='Sicilian Pizza', name='Special', num_toppings=30, size=True, price=29.45, price_big=44.70)
Menu(class_name='Subs', name='Cheese', num_toppings=0, size=True, price=6.50, price_big=7.95)
Menu(class_name='Subs', name='Italian', num_toppings=0, size=True, price=6.50, price_big=7.95)
Menu(class_name='Subs', name='Ham + Cheese', num_toppings=0, size=True, price=6.50, price_big=7.95)
Menu(class_name='Subs', name='Meatball', num_toppings=0, size=True, price=6.50, price_big=7.95)
Menu(class_name='Subs', name='Tuna', num_toppings=0, size=True, price=6.50, price_big=7.95)
Menu(class_name='Subs', name='Turkey', num_toppings=0, size=True, price=7.50, price_big=8.50)
Menu(class_name='Subs', name='Chicken Parmigiana', num_toppings=0, size=True, price=7.50, price_big=8.50)
Menu(class_name='Subs', name='Eggplant Parmigiana', num_toppings=0, size=True, price=6.50, price_big=7.95)
Menu(class_name='Subs', name='Steak', num_toppings=0, size=True, price=6.50, price_big=7.95)
Menu(class_name='Subs', name='Steak + Cheese', num_toppings=0, size=True, price=6.95, price_big=8.50)
Menu(class_name='Subs', name='Sausage, Peppers & Onions', num_toppings=0, size=True, price=8.50)
Menu(class_name='Subs', name='Hamburger', num_toppings=0, size=True, price=4.60, price_big=6.95)
Menu(class_name='Subs', name='Cheeseburger', num_toppings=0, size=True, price=5.10, price_big=7.45)
Menu(class_name='Subs', name='Fried Chicken', num_toppings=0, size=True, price=6.95, price_big=8.50)
Menu(class_name='Subs', name='Veggie', num_toppings=0, size=True, price=6.95, price_big=8.50)
Menu(class_name='Pasta', name='Baked Ziti w/Mozzarella', num_toppings=0, size=False, price=6.50)
Menu(class_name='Pasta', name='Baked Ziti w/Meatballs', num_toppings=0, size=False, price=8.75)
Menu(class_name='Pasta', name='Baked Ziti w/Chicken', num_toppings=0, size=False, price=9.75)
Menu(class_name='Salads', name='Garden Salad', num_toppings=0, size=False, price=6.25)
Menu(class_name='Salads', name='Greek Salad', num_toppings=0, size=False, price=8.25)
Menu(class_name='Salads', name='Antipasto', num_toppings=0, size=False, price=8.25)
Menu(class_name='Salads', name='Salad w/Tuna', num_toppings=0, size=False, price=8.25)
Menu(class_name='Dinner Platters', name='Garden Salad', num_toppings=0, size=True, price=35.00, price_big=60.00)
Menu(class_name='Dinner Platters', name='Greek Salad', num_toppings=0, size=True, price=45.00, price_big=70.00)
Menu(class_name='Dinner Platters', name='Antipasto', num_toppings=0, size=True, price=45.00, price_big=70.00)
Menu(class_name='Dinner Platters', name='Baked Ziti', num_toppings=0, size=True, price=35.00, price_big=60.00)
Menu(class_name='Dinner Platters', name='Meatball Parm', num_toppings=0, size=True, price=45.00, price_big=70.00)
Menu(class_name='Dinner Platters', name='Chicken Parm', num_toppings=0, size=True, price=45.00, price_big=80.00)
"""
























'''
class Pizza(models.Model):
    size = models.CharField(max_length=20)
    orderID = models.IntegerField()
    PizzaId = models.IntegerField()
    Amount = models.IntegerField()
    Price = models.DecimalField()
    SessionId = models.IntegerField()


class Topping(models.Model):
    name = models.CharField(max_length=50)
    base_price = models.DecimalField(max_digits=4,
                                     decimal_places=2,
                                     default=0.99)
    pizza = models.ForeignKey(Pizza, related_name="toppings")

    def __unicode__(self):
        return self.name

'''
'''
class Flavor(models.Model):
    name = models.CharField(max_length=24)
    base_price = models.DecimalField(max_digits=4,
                                     decimal_places=2,
                                     default=3.99)

    def __unicode__(self):
    return self.name


class Size(models.Model):
    name = models.CharField(max_length=24)
    base_price = models.DecimalField(max_digits=4,
                                     decimal_places=2,
                                     default=0.00)

    def __unicode__(self):
    return self.name


class Topping(models.Model):
    name = models.CharField(max_length=24)
    base_price = models.DecimalField(max_digits=4,
                                     decimal_places=2,
                                     default=0.99)

    def __unicode__(self):
    return self.name


class Pizza(models.Model):
    size = models.ForeignKey(Size, null=True)
    toppings = models.ManyToManyField(Topping, null=True)
    crust = models.ForeignKey(Flavor, null=True)
    base_price = models.DecimalField(max_digits=4,
                                     decimal_places=2,
                                     default=5.00)

    def save(self, *args, **kwargs):
    if not Pizza.objects.filter(id=self.id):
        super(Pizza, self).save(*args, **kwargs)
    else:
        price = Decimal('0.00')
        if self.size:
        price = self.size.base_price
        for topping in self.toppings.all():
        if topping.base_price:
            price = price + topping.base_price

        self.base_price = decimal.Decimal(str(price)).quantize(quant)
        super(Pizza, self).save(*args, **kwargs)

    def __unicode__(self):
    if self.size.name:
        name = self.size.name + " Pizza"
    else:
        name = "Pizza"
    for topping in self.toppings.all():
        if topping.name:
        name = name + ", " + topping.name
    return name


class Bread(models.Model):
    flavor = models.ForeignKey(Flavor)
    base_price = models.DecimalField(max_digits=4,
                                     decimal_places=2,
                                     default=4.00)

    def save(self, *args, **kwargs):
    self.base_price = Decimal(self.flavor.base_price).quantize(quant)
    super(Bread, self).save(*args, **kwargs)

    def __unicode__(self):
    return self.type


class Customer(models.Model):
    name = models.CharField(max_length=64)
    number = models.CharField(max_length=20)

    def __unicode__(self):
    return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer)
    date = models.DateField()
    pizzas = models.ManyToManyField(Pizza, blank=True)
    breads = models.ManyToManyField(Bread, blank=True)
    is_made = models.BooleanField(default=False)
    subtotal = models.DecimalField(max_digits=6,
                                   decimal_places=2,
                                   default=0.00)
    tax = models.DecimalField(max_digits=6,
                              decimal_places=2,
                              default=0.00)
    total = models.DecimalField(max_digits=6,
                                decimal_places=2,
                                default=0.00)

    def save(self, *args, **kwargs):
    if not Order.objects.filter(id=self.id):
        super(Order, self).save(*args, **kwargs)
    else:
        decimal.getcontext().rounding = decimal.ROUND_HALF_EVEN
        self.subtotal = Decimal('0.00')

        for pizza in self.pizzas.all():
        self.subtotal += pizza.base_price
        for topping in pizza.toppings.all():
            self.subtotal += topping.base_price

        for bread in self.breads.all():
        self.subtotal += bread.base_price

        self.tax = Decimal('0.06') * self.subtotal
        self.total = self.subtotal + self.tax
        self.subtotal = self.subtotal.quantize(quant)
        self.tax = self.tax.quantize(quant)
        self.total = self.total.quantize(quant)
        super(Order, self).save(*args, **kwargs)

    def __unicode__(self):
    return str(self.id)
'''
