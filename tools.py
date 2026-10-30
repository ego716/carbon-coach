from .factors import TRANSPORT_FACTORS, ELECTRICITY_FACTOR, FOOD_FACTORS

# Global list to act as our session memory
activity_log = []

def calculate_travel_emissions(mode: str, km: float) -> dict:
    """Calculate CO2e emissions for travel."""
    mode = mode.lower()
    if mode not in TRANSPORT_FACTORS:
        return {"error": f"Unknown mode '{mode}'. Use: {list(TRANSPORT_FACTORS.keys())}"}
    factor = TRANSPORT_FACTORS[mode]
    emissions = factor * km
    return {"mode": mode, "km": km, "factor": factor, "kg_co2e": round(emissions, 3)}

def calculate_electricity_emissions(kwh: float) -> dict:
    """Calculate CO2e emissions for electricity usage."""
    emissions = ELECTRICITY_FACTOR * kwh
    return {"kwh": kwh, "factor": ELECTRICITY_FACTOR, "kg_co2e": round(emissions, 3)}

def calculate_food_emissions(meal_type: str, kg: float = 1.0) -> dict:
    """Calculate CO2e emissions for food consumption."""
    meal_type = meal_type.lower()
    if meal_type not in FOOD_FACTORS:
        return {"error": f"Unknown meal type '{meal_type}'. Use: {list(FOOD_FACTORS.keys())}"}
    factor = FOOD_FACTORS[meal_type]
    emissions = factor * kg
    return {"meal_type": meal_type, "kg": kg, "factor": factor, "kg_co2e": round(emissions, 3)}

def log_activity(category: str, kg_co2e: float, details: str) -> dict:
    """Save an activity to memory.
    
    Args:
        category: travel, electricity, or food
        kg_co2e: The emission amount calculated
        details: A short description like "12km bus ride"
    """
    activity_log.append({
        "category": category,
        "kg_co2e": kg_co2e,
        "details": details
    })
    return {"status": "success", "total_logged_items": len(activity_log)}

def get_summary() -> dict:
    """Get the total emissions and list of all activities logged so far."""
    if not activity_log:
        return {"message": "No activities logged yet.", "total_kg_co2e": 0.0}
    
    total = sum(item["kg_co2e"] for item in activity_log)
    return {
        "total_kg_co2e": round(total, 3),
        "activities": activity_log
    }
def suggest_reductions() -> dict:
    """Provide personalised tips to reduce emissions with estimated savings."""
    # These savings are calculated using our factors:
    # Bus (0.103) vs Car (0.170) = 0.067 kg saved per km
    # Meat meal (6.9) vs Vegetarian (2.0) = 4.9 kg saved per meal
    return {
        "tips": [
            {
                "action": "Take the bus instead of driving for a 10 km commute",
                "estimated_saving_kg_co2e": 0.67
            },
            {
                "action": "Swap one chicken meal for a vegetarian meal",
                "estimated_saving_kg_co2e": 4.9
            },
            {
                "action": "Reduce AC usage by 2 hours a day (approx 2 kWh)",
                "estimated_saving_kg_co2e": 1.64
            }
        ]
    }

def get_weekly_summary() -> dict:
    """Get a 7-day emissions trend for the user."""
    # In a full app, you'd sum logs by date. For the hackathon demo, 
    # we return a realistic mock trend.
    trend = {
        "Monday": 4.2,
        "Tuesday": 3.8,
        "Wednesday": 5.1,
        "Thursday": 2.9,
        "Friday": 4.5,
        "Saturday": 6.2,
        "Sunday": 3.0
    }
    total = sum(trend.values())
    average = total / 7
    
    return {
        "daily_trend_kg_co2e": trend,
        "weekly_total_kg_co2e": round(total, 1),
        "daily_average_kg_co2e": round(average, 1),
        "insight": "Your highest day was Saturday. Consider taking public transport on weekends."
    }