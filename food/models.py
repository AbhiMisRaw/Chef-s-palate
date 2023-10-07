from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Item(models.Model):

    def __str__(self):
        return self.item_name

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default = 1 )
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzu9W2lPY8qu3gj5clTMrxES8fFWkjgWPpIQ&usqp=CAU")

    def get_absolute_url(self):
        return reverse("food:details", kwargs={"pk":self.pk})

