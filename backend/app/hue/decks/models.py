from django.db import models

class Deck(models.Model):
    name = models.CharField(max_length=50)

class Card(models.Model):
    text = models.CharField(max_length=255)
    deck = models.ManyToManyField(Deck, related_name='cards')