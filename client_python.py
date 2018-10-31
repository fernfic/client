from zeep import Client, helpers

wsdl = "https://testselect.herokuapp.com/server.php?wsdl"
soap_client = Client(wsdl)

class Pretest():
	def get_air(self):
		test = soap_client.service.get_data('1')
		print(test)
	def set_air(self, room, time, temp, humidity):
		data = {'room' : room, 'time' : time, 'temp' : temp, 'humidity' : humidity}
		test = soap_client.service.set_data(data)
		print(test)

class Test1():
	def get_user(self):
		test = soap_client.service.get_user('1')
		print(test)

class Test2():
	def set_kerry(self, name, addr, weight):
		kerry = {'name' : name, 'addr' : addr, 'weight' : weight}
		test = soap_client.service.send_kerry(kerry)
		print(test)		
	def update_kerry(self, name, id):
		kerry = {'name' : name, 'id' : id}
		test = soap_client.service.update_kerry(kerry)
		print(test)	
	def get_kerry(self):
		test = soap_client.service.get_kerry('01')
		print(test)	

a = Pretest()
# a.get_air()
# a.set_air('08','12-09-2016 05:00','18','56')

b = Test1()
# b.get_user()

c = Test2()
# c.set_kerry('Pee', '111', '23')
# c.update_kerry('Nut', '1')
# c.get_kerry()