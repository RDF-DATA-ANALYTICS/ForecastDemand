import os
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def create_database():
    user = os.getenv("DB_USER", "postgres")
    password = os.getenv("DB_PASSWORD", "postgres")
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "5432")
    db_name = os.getenv("DB_NAME", "demand_forecasting")

    con = psycopg2.connect(
        dbname="postgres",
        user=admin,
        password=admin,
        host=localhost,
        port=5432
    )
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()

    try:
        cur.execute(
            sql.SQL("CREATE DATABASE {}").format(
                sql.Identifier(db_name)
            )
        )
        print(f"Database '{db_name}' created successfully!")
    except psycopg2.errors.DuplicateDatabase:
        print(f"Database '{db_name}' already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cur.close()
        con.close()

if __name__ == "__main__":
    create_database()
