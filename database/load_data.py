import pandas as pd
import psycopg2

db_config = {
    "dbname":"cache_db",
    "host":"localhost",
    "port":5432,
    "password":"user_password",
    "user":"db_user"
}

def database_connection():
    return psycopg2.connect(**db_config)

def create_table(conn, name, columns):
    with conn.cursor() as cur:
        cur.execute(f"create table if not exists {name} ({','.join(columns)})")

def insert_data(conn, name, data):
    with conn.cursor() as cur:
        columns = ','.join(data.columns)
        for row in data.itertuples(index=False):
            cur.execute(f"insert into {name} ({columns}) values ({','.join(['%s'] * len(row))})",row)
    conn.commit()

def populate_database_table():
    table_name = "inventory"
    columns = ["product","price","category","subcategory"]
    excel_file = "./database/Products.xlsx"
    df = pd.read_excel(excel_file)
    df.columns = ["product","price","category","subcategory"]

    db_conn = database_connection()
    create_table(db_conn,table_name,columns)
    insert_data(db_conn,table_name,df)
    db_conn.close()

if __name__ == "__main__":
    populate_database_table()
