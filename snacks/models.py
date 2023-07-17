from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Snack(models.Model):
    title = models.CharField(max_length=64,help_text="Name of the Snack you want to add")
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(default="no desc available")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('snack_detail', args=[str(self.id)])