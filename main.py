from fastapi import FastAPI


app = FastAPI()


@app.get("/portfolio")
async def root(tags: list[str] = []):
    return {"message": "Hello World"}

@app.get("/trade/{ticker}")
def trade(ticker: str):
    if not ticker:
        return {"error": "No ticker provided"}
    else:
        return {"tradeId": "123", "ticker": ticker}