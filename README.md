# carbon-coach# 🌱 Carbon Coach

**DevFest 2026 Hackathon Submission**

Carbon Coach is an AI agent built with **Google ADK** that helps users measure, understand, and reduce their carbon footprint. Users can simply talk to the agent in plain language about their daily activities (travel, electricity, food), and it will calculate exact emissions, remember the session, and provide actionable tips with estimated savings.

## 🚀 Features (Core Requirements Met)

*   **Conversational Input:** Users describe activities naturally (e.g., "I travelled 12 km by bus today").
*   **Tool-Based Calculation:** The agent uses custom Python tools to convert activities into **kg CO₂e**. It never guesses numbers.
*   **Session Memory:** Remembers activities logged during the session. Users can ask "How am I doing today?" for a running total.
*   **Actionable Tips:** Provides personalized suggestions with exact estimated savings (e.g., "Swapping a chicken meal for a vegetarian meal saves 4.9 kg CO₂e").
*   **No Made-Up Numbers:** All math is handled by tools, verified by golden test cases.

## 🧠 Tech Stack

*   **Framework:** [Google Agent Development Kit (ADK)](https://github.com/google/adk-python)
*   **LLM Engine:** Groq (LLaMA 3.3 70B) via LiteLLM
*   **Language:** Python 3.13
*   **Environment:** VS Code / PowerShell (Windows)

## 🛠️ Emission Factors Used

To ensure accuracy, all calculations use established emission factors:
*   **Transport (per km):** Car (0.170), Bus (0.103), Train (0.035), Bike/Walk (0.0)
*   **Electricity:** 0.82 kg CO₂e per kWh (India grid average)
*   **Food (per kg/meal):** Beef (60.0), Chicken (6.9), Vegetarian (2.0), Vegan (1.5)

*(Sources: UK DEFRA 2023, CEA India 2022, Poore & Nemecek 2018)*

## 🧪 Evaluation & Accuracy

To prove the agent does not hallucinate math, we included a custom `test_math.py` script that runs golden evaluation cases against our emission factors. 

```bash
Running Carbon Coach Golden Math Tests...

✅ PASS: Bus travel (12km) = 1.236 kg CO2e
✅ PASS: Electricity (10kWh) = 8.2 kg CO2e
✅ PASS: Food (1kg beef) = 60.0 kg CO2e

All tests passed! No made-up numbers.