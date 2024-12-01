from django.db import models

# Create your models here.

class Animal(models.Model):
    base_name = models.CharField(max_length=100)
    scientific_name =models.CharField(max_length=100)
    number = models.IntegerField()
    point = models.DecimalField(max_digits=100,decimal_places=5)

    CHANNEL_CHOICE = [
        ("forrest","Forrest"),
        ("land","Land"),
        ("sea","Sea"),
        ("sky","Sky"),
    ]
    channel = models.CharField(
        max_length=30,
        choices=CHANNEL_CHOICE,
        default="forrest",
    )

    created_date = models.DateTimeField(auto_now_add=True)

    def _str_(self) -> str:
        return "ชื่อพื้นเมือง: " + self.base_name + ", คะแนน" +str(self.point)