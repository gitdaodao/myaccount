from django.db import models
from django.conf import settings

# Create your models here.

class Profile(models.Model):
    mobile=models.CharField('手机号',max_length=21,blank=True)
    photo=models.ImageField('图片',upload_to='users/%Y/%m/%d',blank=True)
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return f'用户名:{self.user.username}'