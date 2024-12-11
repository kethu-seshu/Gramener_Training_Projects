import airQualityResource
a=airQualityResource.InvestmentGETResource()
p=a.get(2)
# print(p)
def test_type():
    assert p[0]['type'] == "Stock"
    
def test_Buyer():
    assert p[0]['Buyer'] == 'Keerthan'
    
def test_Company():
    assert p[0]['Company'] == 'GOOGL'
    
def test_amount():
    assert p[0]['amount'] == 50
    
def test_value():
    assert p[0]['investment_value'] == 140000
    