import os
import psycopg2
import json
from dotenv import load_dotenv
from datetime import datetime, date
from decimal import Decimal

# Load environment variables
load_dotenv()

# Function to connect to PostgreSQL database
def conectar_db():
    conn = psycopg2.connect(
        host=os.environ.get("DB_HOST"),
        database=os.environ.get("DB_NAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASS")
    )
    print(conn)
    return conn

# Function to load data from gold_vendas_por_vendedor
def carregar_dados_vendas():
    conn = conectar_db()
    query = "SELECT * FROM vendas;"
    with conn.cursor() as cursor:
        cursor.execute(query)
        dados = cursor.fetchall()
        colunas = [desc[0] for desc in cursor.description]
    dados_dict = [dict(zip(colunas, row)) for row in dados]
    conn.close()
    return dados_dict

# Custom serializer for non-serializable types
def custom_serializer(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    elif isinstance(obj, Decimal):
        return float(obj)
    raise TypeError(f"Tipo {type(obj)} não é serializável")

# Function to save data into a JSON file
def salvar_em_json(dados, file_path):
    with open(file_path, 'w') as file:
        json.dump(dados, file, indent=4, default=custom_serializer)

# Main execution: read data and save into JSON files
if __name__ == "__main__":
    dados_vendas = carregar_dados_vendas()
    salvar_em_json(dados_vendas, "vendas.json")
    
    print("Dados salvos em 'dados_vendas.json'.")