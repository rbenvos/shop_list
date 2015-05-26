from django.db import models

# Create your models here.
import datetime


class User(models.Model):
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200,blank=True)
    id_tlf_and = models.CharField(max_length=200,blank=True)
    active = models.BooleanField(default=True)
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

class Product(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(default= True)
    created_at = models.DateTimeField(default=datetime.datetime.now, editable=False)
    modified_at = models.DateTimeField(default=datetime.datetime.now, editable=False, blank=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = datetime.datetime.today()
        self.modified_at = datetime.datetime.today()
        return super(User, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name