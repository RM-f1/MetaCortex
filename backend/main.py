# FastAPI ko import kar rahe hain
# FastAPI ek framework hai jo backend APIs banane ke kaam aata hai
from fastapi import FastAPI

# FastAPI ka object bana rahe hain
# Ye object poori app ko represent karega
app = FastAPI(title="MetaCortex")

# Ye route "/" ke liye hai
# Jab koi browser ya client root URL hit karega, ye function chalega
@app.get("/")
def root():
    # Ye response JSON format me return hoga
    # Bas batane ke liye ki app zinda hai
    return {"status": "MetaCortex is alive"}

# Ye route "/health" ke liye hai
# Iska use system health check ke liye hota hai
@app.get("/health")
def health():
    # Agar ye "ok" return kare, matlab backend theek chal raha hai
    return {"health": "ok"}
