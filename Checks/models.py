from django.db import models
from django.contrib.auth.models import User
from  django.core.exceptions import ValidationError

class WorkSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)

    class Meta:
        db_table = 'work_sessions'

    def clean(self):
        if self.end_time and self.end_time <= self.start_time:
            raise ValidationError('La hora de fin debe ser posterior a la de inicio.')