from .subfleet import Subfleet

class Rank:
    def __init__(self, data):
        self.name = data['name']
        self.subfleets = [Subfleet(subfleet) for subfleet in data['subfleets']]