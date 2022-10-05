import datetime
from email.policy import default
from enum import unique
from pyexpat import model
from timeit import default_timer
from django.urls import reverse_lazy,reverse
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from randomslugfield import RandomSlugField
from django.contrib.auth.models import User
from django_line_notification.line_notify import Line




class RepairType(models.Model):
    repairTypeName = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.repairTypeName

class RepairDetail(models.Model):
    repairType = models.ForeignKey(RepairType, on_delete=models.CASCADE,default=1)
    repairDetail = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.repairDetail

class RepairStatus(models.Model):
    repairStatusName = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.repairStatusName



class RepairReview(models.Model):
    reviewName = models.CharField(max_length=500)
    reviewscore = models.CharField(max_length=1)
    
    
    def __str__(self):
        return self.reviewName


class Repair(models.Model):
    repairDetail = models.ForeignKey(RepairDetail, on_delete=models.CASCADE)
    repairStatus = models.ForeignKey(RepairStatus, on_delete=models.CASCADE,default=1)
    repairCause = models.TextField(max_length=500)
    repairDesc = models.TextField(max_length=500,default='Nothing')
    repairRequester= models.ForeignKey(User,on_delete=models.CASCADE,null=True, related_name='repairRequester')
    repairStaff= models.ForeignKey(User,on_delete=models.CASCADE,null=True, related_name='repairStaff')
    repairSummary = models.CharField(max_length=500,default='Nothing')
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    recieve_time = models.DateTimeField(blank=True,default='1992-11-03 23:09:42')
    work_time = models.DateTimeField(blank=True,default='1992-11-03 23:09:42')
    
    done_time = models.DateTimeField(blank=True,default='1992-11-03 23:09:42')
    repairRequestToken = models.CharField(max_length=100,default='-')
    repairReview = models.ForeignKey(RepairReview, on_delete=models.CASCADE,default=6)
    repairReviewDetail = models.TextField(max_length=500,default='รอการรีวิว',blank=True)
    review_time = models.DateTimeField(blank=True,default='1992-11-03 23:09:42')
    repairStaffForward = models.CharField(max_length=100,default='Nothing')
    forward_time = models.DateTimeField(blank=True,default='1992-11-03 23:09:42')
    
    slug = RandomSlugField(length=7)
    
    def save(self, *args, **kwargs):
        if self.repairStatus.id == 1:
            token = 'K4fGZ4VmVndAQQzbZVdxZZfey5nZUtacE9J0RVTN56e'
            line = Line(token)
            t1=self.repairDetail
            t2 = self.repairCause,'http://18.206.248.221:8000/repair/'
            send = line.send_msg(t1),line.send_msg(t2)
        elif self.repairStatus.id != 1:
            token = self.repairRequestToken 
            line = Line(token)
            t1 = " การขอรับบริการของคุณ "
            t2 = self.repairStatus,' แล้ว  :   http://18.206.248.221:8000/repair/allRepair/'
            send = line.send_msg(t1) ,line.send_msg(t2)
        #send = line.send_msg(self.repairStatus)   
        super(Repair, self).save(*args, **kwargs)  
        return send
        
    
    def __str__(self):
        name = self.repairCause
        return name

 



#    def save(self, *args, **kwargs):
#        if self.recieve_time != timezone.now() and self.done_time=='':
#            self.recieve_time = timezone.now()
#        elif not self.published and self.pub_date is not None:
#            self.pub_date = None
#        super(Repair, self).save(*args, **kwargs)

    
