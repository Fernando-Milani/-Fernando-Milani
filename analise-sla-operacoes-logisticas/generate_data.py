import pandas as pd
import numpy as np
from datetime import timedelta

import os
#------------------------------------------------------------
np.random.seed(42)

def generate_logistics_data(n_orders=5000):
    # Customers -----
    customers = pd.DataFrame({
        "customer_id": range(1, 1001),
        "region": np.random.choice(
            ["Sudeste", "Sul", "Nordeste", "Centro-Oeste", "Norte"],
            size=1000, p=[0.45, 0.2, 0.18, 0.1, 0.07]
        )
    })

    # Carriers -----
    carriers = pd.DataFrame({
        "carrier_id": range(1, 6),
        "carrier_name": [
            "TransLog", "RápidoX", "EntregaJá", "BrasilExpress", "SulCargo"
        ],
        "delay_risk": [0.10, 0.25, 0.18, 0.12, 0.30]
    })

    # Orders -----
    orders = pd.DataFrame({
        "order_id": range(1, n_orders + 1),
        "customer_id": np.random.choice(customers["customer_id"], n_orders),
        "order_date": pd.to_datetime("2024-01-01") +
                      pd.to_timedelta(np.random.randint(0, 365, n_orders), unit="D"),
        "sla_days": np.random.choice([3, 5, 7], n_orders, p=[0.4, 0.4, 0.2])
    })
    orders["promised_date"] = orders["order_date"] + \
                              pd.to_timedelta(orders["sla_days"], unit="D")

    # Deliveries -----
    deliveries = orders[["order_id", "order_date", "promised_date"]].copy()
    deliveries["carrier_id"] = np.random.choice(carriers["carrier_id"], n_orders)

    deliveries = deliveries.merge(
        carriers[["carrier_id", "delay_risk"]],
        on="carrier_id",
        how="left"
    )

    delays = np.random.rand(n_orders) < deliveries["delay_risk"]
    extra_days = np.where(delays, np.random.randint(1, 5, n_orders), 0)

    deliveries["delivery_date"] = deliveries["promised_date"] + \
    pd.to_timedelta(extra_days, unit="D")

    deliveries["delivered_late"] = deliveries["delivery_date"] > deliveries["promised_date"]

    deliveries = deliveries.drop(columns=["delay_risk"])

    return customers, carriers, orders, deliveries

#------------------------------------------------------------
if __name__ == "__main__":
    customers, carriers, orders, deliveries = generate_logistics_data()

    output_dir = os.path.join("data", "raw")
    os.makedirs(output_dir, exist_ok=True)

    customers.to_csv(os.path.join(output_dir, "customers.csv"), index=False)
    carriers.to_csv(os.path.join(output_dir, "carriers.csv"), index=False)
    orders.to_csv(os.path.join(output_dir, "orders.csv"), index=False)
    deliveries.to_csv(os.path.join(output_dir, "deliveries.csv"), index=False)

    print("Arquivos gerados")