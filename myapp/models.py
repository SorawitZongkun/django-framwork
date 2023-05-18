from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return "ชื่อ: " + self.name + ", อายุ: " + str(self.age) + " ปี"
