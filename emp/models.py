from django.db import models
from PIL import Image



from randomslugfield import RandomSlugField
from django.contrib.auth.models import User

# Create your models here.
class EmpUser(models.Model):
    empCID = models.CharField(max_length=13)
    empUser =models.OneToOneField(User, on_delete=models.CASCADE,default=1)
    #pub_date = models.DateTimeField('date published')
    empDepartment = models.CharField(max_length=200,default=1)
    departmentPhone = models.CharField(max_length=10,default='-')
    empPhone = models.CharField(max_length=10,default='-')
    empLineToken = models.CharField(max_length=100,default='-')
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')

    def __str__(self):
        return self.empCID
    
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)