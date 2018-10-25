from zeep import Client
from dicttoxml import dicttoxml

wsdl = "https://testselect.herokuapp.com/server.php?wsdl"

soap_client = Client(wsdl)
a = {'room' : '05', 'time' : '12-09-2016 05:00', 'temp' : '22.5', 'humidity' : '10.12'}

test = soap_client.service.get_user("01")
# test = soap_client.service.set_data(a)

print(test)

# xml = dicttoxml(test, custom_root='air_data', attr_type=False)
