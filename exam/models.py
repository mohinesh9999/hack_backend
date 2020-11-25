from django.db import models
# import cloudinary
# from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
class test1(models.Model):
    test_id1= models.CharField(max_length=100,primary_key=True)
    theme1=models.CharField(max_length=100,blank=False)
    desc11=models.TextField(blank=False)
    noofstd=models.CharField(max_length=100,blank=False)
    start1=models.DateTimeField(blank=False)
    end1=models.DateTimeField(blank=False)
    qns=models.TextField(blank=False)
    def __str__(self):
        return str(self.theme1)
    def getv(self):
        return {"test_id1":self.test_id1,"theme":self.theme1,"desc11":self.desc11,"noofstd":self.noofstd,"start1":self.start1,"end1":self.end1,"qns":self.qns}
class questions1(models.Model):
    question_id1=models.CharField(max_length=100,primary_key=True)
    question1=models.TextField(blank=False)
    option1s=models.TextField(blank=False)
    ans=models.TextField(blank=False)
    def __str__(self):
        return str(self.question1)
    def getv(self):
        return {"qn_id":self.question_id1,"qn":self.question1,"options":self.option1s}