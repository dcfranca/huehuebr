from django.db import models

class Deck(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Card(models.Model):
    text = models.CharField(max_length=255)
    deck = models.ManyToManyField(Deck, related_name='cards')

    def __str__(self):
        return self.text