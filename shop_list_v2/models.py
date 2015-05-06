from django.db import models

# Create your models here.
import datetime

"""
Clase usuario
"""
class User(models.Model):
    email = models.EmailField(max_length=200,unique=True)
    password = models.CharField(max_length=200,blank=True)
    name = models.CharField(max_length=200,blank=True)
    last_name = models.CharField(max_length=200,blank=True)
    device = models.ForeignKey('Phone',blank=True)
    active = models.BooleanField(default=True)
    avatar = models.ImageField(blank=True)
    friends = models.ManyToManyField("self",blank=True)
    created_at = models.DateTimeField(default=datetime.datetime.now, editable=False)
    modified_at = models.DateTimeField(default=datetime.datetime.now, editable=False, blank=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = datetime.datetime.today()
        self.modified_at = datetime.datetime.today()
        return super(User, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.email

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
        return self.id_device

"""
Clase listado
"""

class Order(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    products = models.ManyToManyField("Product",blank=True)
    created_at = models.DateTimeField(default=datetime.datetime.now, editable=False)
    modified_at = models.DateTimeField(default=datetime.datetime.now, editable=False, blank=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = datetime.datetime.today()
        self.modified_at = datetime.datetime.today()
        return super(Order, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.id + " " + self.name

"""
Clase grupo
"""

class Group(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    id_order = models.ForeignKey("Order",blank=True)
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
        return self.id + " " + self.name
