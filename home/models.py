from django.db import models

# Create your models here.
operator_choices = [
    ('Airtel', 'Airtel'),
    ('Banglalink', 'Banglalink'),
    ('Grameenphone', 'Grameenphone'),
    ('Robi', 'Robi'),
    ('Teletalk', 'Teletalk'),
]

choice=[
    ('1','One'),
    ('2','Two'),
    ('3','Three'),
    ('4','Four'),
    ('5','Five')
]

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    operator=models.CharField(max_length=12,choices=operator_choices)
    date = models.DateField()
    photo = models.ImageField(upload_to='contact/images',null=True,blank=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    name=models.CharField(max_length=122)
    Class=models.CharField(max_length=10,choices=choice)
    roll=models.IntegerField()
    birth_date=models.DateField()

    def __str__(self):
        return self.name
    

class Person(models.Model):
    name=models.CharField(max_length=122)
    Contact=models.ForeignKey(Contact,on_delete=models.CASCADE)

    def __str__(self):
        return self.name