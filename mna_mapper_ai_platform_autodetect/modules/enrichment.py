import pandas as pd
import random

def enrich_data(companies):
    data = []
    for c in companies:
        employees = random.randint(5, 50)
        traffic = random.randint(1000, 10000)
        revenue = employees * 150000
        data.append({
            "name": c["name"],
            "url": c["url"],
            "employees_est": employees,
            "web_traffic_est": traffic,
            "revenue_est_eur": revenue,
            "linkedin_url": f"https://linkedin.com/company/{c['name'].lower().replace(' ', '')}"
        })
    return pd.DataFrame(data)
