import psycopg

def run_demand_forecast_interface():
    db_url = input("Enter PostgreSQL connection string (e.g., postgresql://user:password@localhost:5432/dbname): ")
    
    try:
        num_rows = int(input("Enter number of rows (e.g., products/items): "))
        num_cols = int(input("Enter number of columns (e.g., forecast days/periods): "))
    except ValueError:
        print("Error: Rows and columns must be valid integers.")
        return

    if num_rows <= 0 or num_cols <= 0:
        print("Error: Rows and columns must be greater than zero.")
        return

    with psycopg.connect(db_url) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS dynamic_forecast_matrix (
                    forecast_id SERIAL PRIMARY KEY,
                    item_code VARCHAR(64),
                    period_index INT,
                    forecast_qty NUMERIC(10,4),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
            conn.commit()

            batch_data = []
            
            for r in range(1, num_rows + 1):
                item_code = f"SKU_PROD_{r:03d}"
                for c in range(1, num_cols + 1):
                    predicted_qty = round(100.0 + (r * 2.5) + (c * 1.2), 2)
                    batch_data.append((item_code, c, predicted_qty))

            cur.executemany(
                """
                INSERT INTO dynamic_forecast_matrix (item_code, period_index, forecast_qty)
                VALUES (%s, %s, %s)
                """,
                batch_data
            )
            conn.commit()

            cur.execute("""
                SELECT item_code, COUNT(period_index) AS total_periods, 
                       MIN(forecast_qty) AS min_forecast, 
                       MAX(forecast_qty) AS max_forecast, 
                       ROUND(AVG(forecast_qty), 2) AS avg_forecast
                FROM dynamic_forecast_matrix
                GROUP BY item_code
                LIMIT 5;
            """)
            
            print("\nSample Output Summary (First 5 Items):")
            print("-" * 65)
            for row in cur.fetchall():
                print(f"Item: {row[0]} | Periods: {row[1]} | Min: {row[2]} | Max: {row[3]} | Avg: {row[4]}")
            print("-" * 65)

if __name__ == "__main__":
    run_demand_forecast_interface()