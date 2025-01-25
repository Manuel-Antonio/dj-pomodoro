from django.db import models

class PomodoroSession(models.Model):
    task_name = models.CharField(max_length=100)
    duration = models.IntegerField()
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.task_name} - {self.duration} min"