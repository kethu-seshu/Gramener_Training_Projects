import airQualityResource
a=airQualityResource.AirQualityEntryGETResource()
p=a.get(1)
# print(p)

def test_City():
    assert p['City'] == "Delhi"
    
def test_Date():
    assert p['Date'] =="2018-02-23"
    
def test_AQI():
    assert p['AQI'] == 331
    
def test_AQI_Bucket():
    assert p['AQI_Bucket'] == "Very Poor"
    
def test_co():
    assert p['CO'] == 1.81

