from django.db import models


class Todo(models.Model):
    sarlavha = models.CharField(max_length=80)
    vaqt = models.DateTimeField(auto_now_add=True)
    batafsil_malumot = models.TextField()
    status = models.CharField(max_length=20, default="yangi")
    def __str__(self):
        return self.sarlavha

