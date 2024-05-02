from django.db import models


class Column(models.Model):
    title = models.CharField(max_length=100)
    order = models.AutoField(primary_key=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name="cards")
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title
