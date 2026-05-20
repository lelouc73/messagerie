from fastapi import FastAPI
import psycopg2

app = FastAPI()

DB_URL = "postgresql://postgres.tcwgywxgpzsdwcsofuvj:##Ne730380##@db.tcwgywxgpzsdwcsofuvj.supabase.co:6543/postgres?sslmode=require"

@app.get("/")
def test_connexion():
    try:
        # On essaie de se connecter à Supabase
        conn = psycopg2.connect(DB_URL)
        conn.close()
        return {"status": "Succès", "message": "Connexion à Supabase réussie !"}
    except Exception as e:
        return {"status": "Erreur", "details": str(e)}
