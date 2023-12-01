from django.db import models


# Create your models here.
class PersonData(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    classroom_number = models.IntegerField()

    def __str__(self):
        return f"{self.name}: classroom {self.classroom_number} on age{self.age}"


class Schedule(models.Model):
    topic = models.CharField(max_length=50)
    date = models.DateField()
    start_title = models.TimeField(default=(00.00))
    classroom = models.ForeignKey(PersonData, on_delete=models.CASCADE, default=1)

class TaskDB(models.Model):
    task=models.CharField(max_length=50)
    priority=models.CharField(max_length=20)

    def __str__(self):
        return "%s %s"%(self.task, self.priority)