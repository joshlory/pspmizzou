from django.db import models

class Committee(models.Model):
    name = models.CharField(max_length=127)
    
