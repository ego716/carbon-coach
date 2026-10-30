from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.agents.callback_context import CallbackContext
from google.adk.models import LlmRequest

# Import all tools from tools.py
from .tools import (
    calculate_travel_emissions, 
    calculate_electricity_emissions, 
    calculate_food_emissions,
    log_activity,
    get_summary,
    suggest_reductions,
    get_weekly_summary
)

load_dotenv()

# Groq's gpt-oss model sends a "reasoning" field that Groq's API 
# strictly rejects if sent back in the chat history. 
# This callback strips it out before every model call.
def strip_reasoning_content(callback_context: CallbackContext, llm_request: LlmRequest):
    for content in llm_request.contents:
        if hasattr(content, "parts") and content.parts:
            content.parts = [
                p for p in content.parts 
                if not (hasattr(p, "thought") and p.thought)
            ]
    return None

# Initialize the Groq model
model = LiteLlm(model="groq/openai/gpt-oss-120b")

root_agent = Agent(
    name="carbon_coach",
    model=model,
    description="A carbon footprint coach for students.",
    instruction=(
        "You are Carbon Coach. Help users understand and reduce their carbon footprint.\n"
        "RULES:\n"
        "1. ALWAYS use the calculate tools to find emissions. NEVER guess or calculate numbers yourself.\n"
        "2. After calculating, ALWAYS use the log_activity tool to save it to memory.\n"
        "3. If the user asks for tips, use suggest_reductions tool.\n"
        "4. If the user asks about their week, use get_weekly_summary tool.\n"
        "5. Be concise and encouraging.\n"
    ),
    tools=[
        calculate_travel_emissions,
        calculate_electricity_emissions,
        calculate_food_emissions,
        log_activity,
        get_summary,
        suggest_reductions,
        get_weekly_summary
    ],
    before_model_callback=strip_reasoning_content,
)