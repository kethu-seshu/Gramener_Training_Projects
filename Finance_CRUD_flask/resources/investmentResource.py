from flask_restful import Resource
from flask import request
import json

investments = [
    {"id": 1, "type": "Stock", "Company": "AAPL","Buyer":"Sarath", "amount": 100, "price_per_unit": 150.00, "investment_value": 15000.00,"Date":"10-05-24"},
    {"id": 2, "type": "Stock", "Company": "GOOGL","Buyer":"Keerthan", "amount": 50, "price_per_unit": 2800.00, "investment_value": 140000.00,"Date":"1-12-24"}
]

class InvestmentsGETResource(Resource):
    def get(self):
        # statement = ""+ ""
        # return investments
        return  [{"id": investment['id'],"type": investment["type"],"Buyer":investment["Buyer"], "Company": investment["Company"], "amount": investment["amount"], "investment_value": investment["investment_value"],"Date":investment["Date"],"statement": investment["Buyer"]+ " bought " + str(investment["amount"]) + " shares of "+ investment['Company']+ " on "+ investment['Date'] +"."} for investment in investments]
    
# GET endpoint for a specific investment by ID
class InvestmentGETResource(Resource):
    def get(self, id):
        for investment in investments:
            if investment["id"] == id:
                statement = investment["Buyer"]+ " bought " + str(investment["amount"]) + " shares of "+ investment['Company']+ " on "+ investment['Date'] +"."
                return [{"id": investment['id'],"type": investment["type"],"Buyer":investment["Buyer"], "Company": investment["Company"], "amount": investment["amount"], "investment_value": investment["investment_value"],"Date":investment["Date"],"Statement":statement}]
        return {"message": "Investment not found"}, 404


# POST endpoint to create a new investment
class InvestmentPOSTResource(Resource):
    def post(self):
        investment = json.loads(request.data)
        new_id = max(investment["id"] for investment in investments) + 1 
        investment["id"] = new_id
        investment["investment_value"] = investment["amount"] * investment["price_per_unit"]  # Calculate the total investment value
        investments.append(investment)
        return investment, 201


# PUT endpoint to update an existing investment by ID
class InvestmentPUTResource(Resource):
    def put(self, id):
        investment_data = json.loads(request.data)
        for investment in investments:
            if investment["id"] == id:
                investment.update(investment_data)
                investment["investment_value"] = investment["amount"] * investment["price_per_unit"]  # Recalculate the investment value
                return investment
        return {"message": "Investment not found"}, 404


# DELETE endpoint to delete an investment by ID
class InvestmentDELETEResource(Resource):
    def delete(self, id):
        global investments
        investments = [investment for investment in investments if investment["id"] != id]
        return "", 204
