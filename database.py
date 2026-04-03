import sqlite3
import pandas as pd

def create_database():

    df = pd.read_csv("dataset.csv")

    # remove empty rows
    df = df.dropna(how="all")

    # replace missing values
    df = df.fillna(0)

    numeric_columns = [
        "age","monthly_income","daily_internet_hours","smartphone_usage_years",
        "social_media_hours","online_payment_trust_score","tech_savvy_score",
        "monthly_online_orders","monthly_store_visits","avg_online_spend",
        "avg_store_spend","discount_sensitivity","return_frequency",
        "avg_delivery_days","delivery_fee_sensitivity","free_return_importance",
        "product_availability_online","impulse_buying_score","need_touch_feel_score",
        "brand_loyalty_score","environmental_awareness","time_pressure_level"
    ]

    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors="coerce")

    conn = sqlite3.connect("customer.db")

    df.to_sql("customers", conn, if_exists="replace", index=False)

    conn.commit()
    conn.close()


def run_query(sql_query):

    conn = sqlite3.connect("customer.db")

    df = pd.read_sql_query(sql_query, conn)

    conn.close()

    return df