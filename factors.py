# Emission factors in kg CO2e
# Sources: UK DEFRA 2023 (transport), CEA India 2022 (electricity), Poore & Nemecek 2018 (food)

TRANSPORT_FACTORS = {
    "car": 0.170,       # kg CO2e per km (average petrol car)
    "bus": 0.103,       # kg CO2e per km
    "train": 0.035,     # kg CO2e per km
    "bike": 0.0,        # zero emissions
    "walk": 0.0,        # zero emissions
    "flight": 0.255,    # kg CO2e per km (short-haul)
}

ELECTRICITY_FACTOR = 0.82  # kg CO2e per kWh (India grid average)

FOOD_FACTORS = {
    "beef": 60.0,       # kg CO2e per kg of food
    "chicken": 6.9,     # kg CO2e per kg
    "vegetarian": 2.0,  # kg CO2e per meal
    "vegan": 1.5,       # kg CO2e per meal
}

WASTE_FACTOR = 0.5      # kg CO2e per kg of general waste