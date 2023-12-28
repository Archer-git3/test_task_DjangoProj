from django.db import models

class Item(models.Model):
    app_label = 'myapp'
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
