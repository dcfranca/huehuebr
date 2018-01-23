import DrillDownAPIView
from .models import Deck, Card

class DecksApi(DrillDownAPIView):
    """A GET API for Deck objects"""
    model = Deck

    MAX_RESULTS = 5000
    drilldowns = ['cards']

    def get_base_query(self):
        return Deck.objects.all()

class CardsApi(DrillDownAPIView):
    """A GET API for Deck objects"""
    model = Card

    MAX_RESULTS = 5000

    drilldowns = ['decks']

    def get_base_query(self):
        return Card.objects.all()