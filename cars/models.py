from django.db import models



class Car(models.Model):
    name = models.CharField(max_length= 20,null=False)
    model = models.CharField(max_length= 20,null=False)
    color = models.CharField(max_length= 20,null=False)
    is_active = models.BooleanField(default=True)
    year_of_model = models.IntegerField()
    year_of_sign = models.IntegerField()
    daily = models.FloatField()
    weekly = models.FloatField()
    monthly = models.FloatField()
    yearly = models.FloatField()
    main_pic = models.ImageField(upload_to='main_pics/', blank=False)
    second_pic = models.ImageField(upload_to='other_pics/', blank=True, null=True)
    third_pic = models.ImageField(upload_to='other_pics/', blank=True, null=True)
    fourth_pic = models.ImageField(upload_to='other_pics/', blank=True, null=True)
    fifth_pic = models.ImageField(upload_to='other_pics/', blank=True, null=True)
    
    def __str__(self):
        return self.name + " " + self.model + " " + self.color