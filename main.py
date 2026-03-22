from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

BALANCE : dict = {}

class OperationRequest(BaseModel):
    wallet_name: str
    amount: float
    description: str | None = None

@app.get("/balance")
def get_balance(wallet_name: str | None = None):
    if wallet_name is None:
        return {"total_balance": sum(BALANCE.values())}
    if wallet_name not in BALANCE:
        raise HTTPException(
            status_code=404,
            detail=f"Wallet '{wallet_name}' not found"
            )
    return {"wallet": wallet_name, "balance": BALANCE[wallet_name]}

@app.post("/wallets/{name}")
def create_wallet(name: str, initial_balance: float | None = 0):
    if name in BALANCE:
        raise HTTPException(
            status_code=400,
            detail=f"Wallet '{name}' already exists"
            )
    BALANCE[name] = initial_balance
    return {"message": f"Wallet '{name}' created successfully"}