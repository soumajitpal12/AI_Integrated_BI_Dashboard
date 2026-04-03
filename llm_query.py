import google.generativeai as genai
import os
from dotenv import load_dotenv
import json
import re

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_sql(user_query):

    prompt = f"""
You are an AI BI assistant.

Database table: customers

Columns:
age
monthly_income
daily_internet_hours
smartphone_usage_years
social_media_hours
online_payment_trust_score
tech_savvy_score
monthly_online_orders
monthly_store_visits
avg_online_spend
avg_store_spend
discount_sensitivity
return_frequency
avg_delivery_days
delivery_fee_sensitivity
free_return_importance
product_availability_online
impulse_buying_score
need_touch_feel_score
brand_loyalty_score
environmental_awareness
time_pressure_level
gender
city_tier
shopping_preference

If the query compares two categorical columns 
(e.g., gender and shopping_preference),
then use COUNT(*) and GROUP BY both columns.

Example:
SELECT gender, shopping_preference, COUNT(*) as total
FROM customers
GROUP BY gender, shopping_preference;

Return ONLY JSON like this:

{{
 "sql": "SQL_QUERY",
 "chart": "bar | line | pie | scatter | histogram"
}}

Examples:

Average comparison
{{
 "sql": "SELECT gender, AVG(avg_online_spend) FROM customers GROUP BY gender",
 "chart": "bar"
}}

Distribution
{{
 "sql": "SELECT shopping_preference, COUNT(*) FROM customers GROUP BY shopping_preference",
 "chart": "pie"
}}

Trend
{{
 "sql": "SELECT age, AVG(tech_savvy_score) FROM customers GROUP BY age ORDER BY age",
 "chart": "line"
}}

Scatter relationship
{{
 "sql": "SELECT monthly_income, avg_online_spend FROM customers LIMIT 500",
 "chart": "scatter"
}}

Histogram
{{
 "sql": "SELECT age FROM customers",
 "chart": "histogram"
}}

User question:
{user_query}
"""

    response = model.generate_content(prompt)

    text = response.text.strip()

    text = re.sub(r"```json", "", text)
    text = re.sub(r"```", "", text)

    data = json.loads(text)

    return data["sql"], data["chart"]
