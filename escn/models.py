from django.db import models
from .utils.encryption import encrypt_pin, decrypt_pin
# Create your models here.
class Gender(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
class State(models.Model):
    name  = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class RelationShip(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Accounts(models.Model):
    acc_number = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    dob = models.DateField()
    phone = models.PositiveBigIntegerField(unique=True)
    email = models.EmailField(unique=True)
    aadhar = models.PositiveBigIntegerField()
    address = models.TextField()
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="photos")
    gender = models.ForeignKey(Gender,on_delete=models.CASCADE)
    nomine = models.CharField(max_length=32)
    relation = models.ForeignKey(RelationShip,on_delete=models.CASCADE)
    pin = models.CharField(max_length=64 , default="0000")
    balance = models.FloatField(default=1000)
    
    def set_pin(self, raw_pin):
        self.pin = encrypt_pin(raw_pin)

    def get_pin(self):
        return decrypt_pin(self.pin)