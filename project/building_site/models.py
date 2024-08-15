# myapp/models.py

from django.db import models



class TextEntry(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content[:50]  # Връща първите 50 символа от текста
