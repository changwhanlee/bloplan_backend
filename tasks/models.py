from django.db import models
from django.conf import settings


class Platform(models.Model):

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='platforms'
    )
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.owner.username}의 {self.name}"
    
class Duty(models.Model):
    
    name = models.CharField(
        max_length=10,
    )
    
    def __str__(self):
        return self.name

class Task(models.Model):

    class TypeChoices(models.TextChoices):
        food = "food", "음식"
        stuff = "stuff", "물품"
        activity = "activity", "체험"    


    class StatusChoices(models.TextChoices):
        expired = "expired", "만료"
        in_progress = "in_progress", "진행중"
        completed = "completed", "완료"
        cancelled = "cancelled", "취소"
    
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    
    platform = models.ForeignKey(
        Platform,
        on_delete=models.CASCADE,
        related_name='tasks'
    )

    client = models.CharField(
        max_length=20,
    )

    task_name = models.CharField(
        max_length=20,
    )
    
    created_at = models.DateField()
    
    due_date = models.DateField()

    type = models.CharField(
        max_length=10,
        choices=TypeChoices.choices,
        default=TypeChoices.food,
    )   

    duty = models.ManyToManyField(
        Duty,
        related_name='tasks',
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.in_progress,
    )

    money = models.IntegerField(
        default=0,
    )

    note = models.TextField(
        max_length=100,
        blank=True,
    )

    
    def __str__(self):
        return f"{self.owner.username}의 {self.platform} 태스크"


