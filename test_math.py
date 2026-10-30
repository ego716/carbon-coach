from factors import TRANSPORT_FACTORS, ELECTRICITY_FACTOR, FOOD_FACTORS

def test_bus_math():
    # 12 km * 0.103 kg/km = 1.236 kg
    km = 12.0
    expected = 1.236
    result = TRANSPORT_FACTORS["bus"] * km
    assert round(result, 3) == expected, f"Failed: expected {expected}, got {result}"
    print(f"✅ PASS: Bus travel (12km) = {result} kg CO2e")

def test_electricity_math():
    # 10 kWh * 0.82 kg/kWh = 8.2 kg
    kwh = 10.0
    expected = 8.2
    result = ELECTRICITY_FACTOR * kwh
    assert round(result, 3) == expected, f"Failed: expected {expected}, got {result}"
    print(f"✅ PASS: Electricity (10kWh) = {result} kg CO2e")

def test_food_math():
    # 1 kg beef * 60.0 kg/kg = 60.0 kg
    kg = 1.0
    expected = 60.0
    result = FOOD_FACTORS["beef"] * kg
    assert round(result, 3) == expected, f"Failed: expected {expected}, got {result}"
    print(f"✅ PASS: Food (1kg beef) = {result} kg CO2e")

if __name__ == "__main__":
    print("Running Carbon Coach Golden Math Tests...\n")
    test_bus_math()
    test_electricity_math()
    test_food_math()
    print("\nAll tests passed! No made-up numbers.")