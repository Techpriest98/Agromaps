from django.db import models

# Create your models here.

#Процес
class Process(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return(self.name)

#Агро культура
class Culture(models.Model):
    name = models.CharField(max_length=9)
    color = models.CharField(max_length=7, default="#cccccc")

    #Отображение названия модели в админке
    def __str__(self):
        return(self.name)
    
#Поле
class Field(models.Model):
    title = models.CharField(max_length=16)
    square = models.FloatField()
    polygon =  models.CharField(max_length=256, default="")

    #Отображение названия модели в админке
    def __str__(self):
        return (self.title)

#Посів поля
class SeedProcess(models.Model):
    seedDate = models.DateField(auto_now_add=True)
    harvestDate = models.DateField()
    field = models.ForeignKey(Field,default=1, on_delete=models.CASCADE)
    culture =  models.ForeignKey(Culture, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return(str(self.seedDate))


