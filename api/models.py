from django.db import models


# creating models for comapny

class companyapi(models.Model):
    company_id=models.AutoField(primary_key=True)
    name= models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=
                          (('IT','IT'),
                           ('Non IT','Non IT'),
                           ("Mobiles Phones",'Mobile Phones')
                           ))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.name + "," +self.location


class employee(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField(max_length=2)
    phone_number=models.IntegerField(max_length=20)
    position=models.CharField(max_length=50,choices=(
                                                       ('manager','Manager'),
                                                       ("Software developer","Software developer"),
                                                       ("product Manager","product manager"),
                                                       ("Team Leader","Team Leader")
                                                                                     ))
    address=models.TextField(max_length=200)

    company=models.ForeignKey(companyapi,on_delete=models.CASCADE)

