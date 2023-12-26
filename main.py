from fastapi import FastAPI
import json


app = FastAPI()


@app.get("/portfolio")
async def root(tags: list[str] = []):
    #get mock data
    f_portfolio = open("./fixtures/portfolio.json")
    f_postions = open("./fixtures/positions.json")
    mock_portfolio = json.load(f_portfolio)
    mock_positions = json.load(f_postions)
    f_portfolio.close()
    f_postions.close()

    portfolio_id = "123" # get from db and user_id from auth
    positions = []
    for position in mock_positions:
        if position["portfolio_id"] == portfolio_id:
            positions.append(position)
    print(positions)

    return {**mock_portfolio, "positions": positions}

@app.get("/trade/{ticker}")
def trade(ticker: str):
    if not ticker:
        return {"error": "No ticker provided"}
    else:
        return {"tradeId": "123", "ticker": ticker}