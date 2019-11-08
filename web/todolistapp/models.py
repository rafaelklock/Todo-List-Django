from django.db import models

# Create your models here.
from django.urls import reverse


class Todo(models.Model):
    todo = models.CharField(max_length=100, help_text='Obrigatorio preencher o todo')
    done = models.BooleanField(default=False)
    created_at = models.DateField(auto_now=True)
    closed_at = models.DateTimeField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('todolistapp:todo_list', kwargs={'pk': self.pk})

    def __str__(self):
        return self.todo



