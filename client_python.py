from zeep import Client
from dicttoxml import dicttoxml

wsdl = "https://testselect.herokuapp.com/server.php?wsdl"
# wsdl = "https://testselect-wolfbit.c9users.io/server.php?wsdl"
soap_client = Client(wsdl)
a = {'room' : '05', 'time' : '12-09-2016 05:00', 'temp' : '22.5', 'humidity' : '10.12'}
kerry1 = {'name' : 'fern', 'addr' : '123', 'weight' : '22.5'}
kerry2 = {'name' : 'pee', 'addr' : '345', 'weight' : '50'}

# test = soap_client.service.set_data(a)

# test = soap_client.service.get_user('01')

# test = soap_client.service.send_kerry(kerry)
# test = soap_client.service.update_kerry(kerry2)
test = soap_client.service.get_kerry('1')
print(test)

xml = dicttoxml(test, custom_root='user_data', attr_type=False)
print(xml)
