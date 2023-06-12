class Airport:
    def __init__(self, airport):
        self.id = airport['id']
        self.iata = airport['iata']
        self.icao = airport['icao']
        self.name = airport['name']
        self.location = airport['location']
        self.country = airport['country']
        self.timezone = airport['timezone']
        self.hub = airport['hub']
        self.notes = airport['notes']
        self.lat = airport['lat']
        self.lon = airport['lon']
        self.ground_handling_cost = airport['ground_handling_cost']
        self.fuel_100ll_cost = airport['fuel_100ll_cost']
        self.fuel_jeta_cost = airport['fuel_jeta_cost']
        self.fuel_mogas_cost = airport['fuel_mogas_cost']
