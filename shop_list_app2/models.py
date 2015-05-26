from django.db import models

# Create your models here.
import datetime

#introducir contador de cambios
#introducir contador de productos

"""
Clase usuario
"""
class User(models.Model):
    email = models.EmailField(max_length=200,unique=True)
    password = models.CharField(max_length=200,blank=True)
    name = models.CharField(max_length=200,blank=True)
    last_name = models.CharField(max_length=200,blank=True)
    device = models.ManyToManyField('Phone',blank=True)
    active = models.BooleanField(default=True)
    avatar = models.ImageField(blank=True)
    friends = models.ManyToManyField("User",blank=True)
    created_at = models.DateTimeField(default=datetime.datetime.now, editable=False)
    modified_at = models.DateTimeField(default=datetime.datetime.now, editable=False, blank=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = datetime.datetime.today()
        self.modified_at = datetime.datetime.today()
        return super(User, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.id) + " - " + self.name + " " + self.last_name

    def getAllFriends(self):
        return self.friends.all()
    getAllFriends.short_description = 'Friends'

    def getFriendsActivate(self):
        return self.friends.all().filter(active=True)
    getAllFriends.short_description = 'Friends Act'

    def getFriendsDesactive(self):
        return self.friends.all().filter(active=False)
    getAllFriends.short_description = 'Friends DesAct'

    def getNumFriendsActive(self):
        return self.friends.all().filter(active=True).count()
    getNumFriendsActive.short_description = 'Num Friends Act'

    def getNumFriendsDesactive(self):
        return self.friends.all().filter(active=False).count()
    getNumFriendsDesactive.short_description = 'Num Friends DesAct'

    def getNumAllFriends(self):
        return self.friends.all().count()
    getNumAllFriends.short_description = 'Num Friends'

    def getDevices(self):
        return self.device.all()
    getDevices.short_description = 'Devices'

    def getNumDevices(self):
        return self.device.all().count()
    getNumDevices.short_description = 'Num devices'

    def getGroups(self):
        return self.group_set.all()
    getGroups.short_description = 'Groups'

    def getNumGroups(self):
        return self.group_set.all().count()
    getNumGroups.short_description = 'Num groups'


"""
Clase grupo
"""

class Group(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    orders = models.ManyToManyField("Order",blank=True)
    avatar = models.ImageField(blank=True)
    users = models.ManyToManyField("User",blank=True)
    created_at = models.DateTimeField(default=datetime.datetime.now, editable=False)
    modified_at = models.DateTimeField(default=datetime.datetime.now, editable=False, blank=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = datetime.datetime.today()
        self.modified_at = datetime.datetime.today()
        return super(Group, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.id) + " " + self.name

    def groupUsers(self):
        return self.users.all()
    groupUsers.short_description = "Users"

    def groupOrders(self):
        return self.orders.all()
    groupOrders.short_description = "Orders"

"""
Clase telefono
"""

class Phone(models.Model):

    KIND_OS = (
        ('iOS','iOS'),
        ('And','Android'),
        ('Moz','MozillaOS'),
        ('Win','Windows phone')
    )

    #Intentar meter mas datos del telefono, ver si se pueden extraer.

    id_device = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    os = models.CharField(max_length=3, choices=KIND_OS,blank=True)
    created_at = models.DateTimeField(default=datetime.datetime.now, editable=False)
    modified_at = models.DateTimeField(default=datetime.datetime.now, editable=False, blank=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = datetime.datetime.today()
        self.modified_at = datetime.datetime.today()
        return super(Phone, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.os + " " + self.id_device

    def users(self):
        return self.user_set.all()
    users.short_description = "User"

    def numUsers(self):
        return self.user_set.all().count()
    numUsers.short_description = "Num User"

"""
Clase listado
"""

class Order(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    items = models.ManyToManyField("Item",blank=True)
    created_at = models.DateTimeField(default=datetime.datetime.now, editable=False)
    modified_at = models.DateTimeField(default=datetime.datetime.now, editable=False, blank=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = datetime.datetime.today()
        self.modified_at = datetime.datetime.today()
        return super(Order, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.id) + " " + self.name

    def orderProducts(self):
        return self.items.all()
    orderProducts.short_description = "Products"

    def orderNumProducts(self):
        return self.items.all().count()
    orderProducts.short_description = "Num Products"

    def getGroups(self):
        return self.group_set.all()
    getGroups.short_description = 'Groups'

"""
Clase elemento
"""

class Item(models.Model):
    active = models.BooleanField(default=True)
    purchased = models.BooleanField(default=True)
    amount = models.PositiveIntegerField(default=0)
    product = models.ForeignKey("Product")
    created_at = models.DateTimeField(default=datetime.datetime.now, editable=False)
    modified_at = models.DateTimeField(default=datetime.datetime.now, editable=False, blank=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = datetime.datetime.today()
        self.modified_at = datetime.datetime.today()
        return super(Item, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.id)

    def getOrder(self):
        return self.order_set.all()
    getOrder.short_description = 'Order'



"""
Clase producto
"""

class Product(models.Model):

    UNITS = (
        ('kg','Kilogramos'),
        ('l','Litros')
    )

    name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    avatar = models.ImageField(blank=True)
    quantity = models.PositiveIntegerField(default= 0,blank=True)
    measure = models.CharField(max_length=3, choices=UNITS,blank=True)
    created_at = models.DateTimeField(default=datetime.datetime.now, editable=False)
    modified_at = models.DateTimeField(default=datetime.datetime.now, editable=False, blank=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = datetime.datetime.today()
        self.modified_at = datetime.datetime.today()
        return super(Product, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    #introducir funciona para introducir nuevas unidades. -> subclase

