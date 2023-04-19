from django.db import models

# Create your models here.
operator_choices = [
    ('Airtel', 'Airtel'),
    ('Banglalink', 'Banglalink'),
    ('Grameenphone', 'Grameenphone'),
    ('Robi', 'Robi'),
    ('Teletalk', 'Teletalk'),
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