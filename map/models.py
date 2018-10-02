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

    #Отображение названия модели в админке
    def __str__(self):
        return(self.name)
    
#Поле
class Field(models.Model):
    title = models.CharField(max_length=9)
    square = models.FloatField()
    cultureID = models.ForeignKey(Culture, on_delete=models.CASCADE)
    process = models.ForeignKey(Process,default=1, on_delete=models.CASCADE)

    #Отображение названия модели в админке
    def __str__(self):
        return (self.title)




