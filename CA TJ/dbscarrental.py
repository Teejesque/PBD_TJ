
# Import different classes from car.py

from car import Car, ElectricCar, PetrolCar, DieselCar, HybridCar 

# Set Class Dealership

class Dealership(object):

	def __init__(self):
		self.electric_cars_jeep = []
		self.electric_cars_sedan = []
		self.petrol_cars_jeep = []
		self.petrol_cars_sedan = []
		self.diesel_cars_jeep = []
		self.diesel_cars_sedan = []
		self.hybrid_cars_jeep = []
		self.hybrid_cars_sedan = []

	
	#  create function setting stock of dealership
	def create_current_stock(self):
		for i in range(2):
			self.electric_cars_jeep.append(ElectricCar())
		for i in range(2):
			self.electric_cars_sedan.append(ElectricCar())
		for i in range(10):
			self.petrol_cars_jeep.append(PetrolCar())
		for i in range(10):
			self.petrol_cars_sedan.append(PetrolCar())
		for i in range(4):
			self.diesel_cars_jeep.append(DieselCar())
		for i in range(4):
			self.diesel_cars_sedan.append(DieselCar())
		for i in range(4):
			self.hybrid_cars_jeep.append(HybridCar())
		for i in range(4):
			self.hybrid_cars_sedan.append(HybridCar())


	
	# create function showing user stock of dealership
	def stock_count(self):
		print "Petrol Jeeps in stock : " + str(len(self.petrol_cars_jeep))
		print "Petrol Sedans in stock : " + str(len(self.petrol_cars_sedan))
		print "Electric Jeeps in stock : " + str(len(self.electric_cars_jeep))
		print "Electric Sedans in stock : " + str(len(self.electric_cars_sedan))
		print "Diesel Jeeps in stock : " + str(len(self.diesel_cars_jeep))
		print "Diesel Sedans in stock : " + str(len(self.diesel_cars_sedan))
		print "Hybrid Jeeps in stock : " + str(len(self.hybrid_cars_jeep))
		print "Hybrid Jeeps in stock : " + str(len(self.hybrid_cars_sedan))
		
		
	# create function for an insufficient amount of chosen vehicle	
	def rent(self, car_list, amount):
		if len(car_list) < amount:
			print 'Not enough cars in stock'
			return
		total = 0
		while total < amount:
			car_list.pop()
			total = total + 1
			
	def returning(self, car_list, amount):
		total = 0
		while total < amount:
			car_list.append(Car())
			total = total + 1
	
	# Create function for the rental process
	def process_rental(self):
	
		# Ask whether user would like to rent. Ensure answer is case sensitive
		answer = raw_input("Would you like to rent a car? Y/N : ")
		answer = answer.upper()
		
		# Once renting, offer the selection dealership has to offer, i.e. cars in stock. Ensure answer is case sensitive
		if answer == "Y":
			answer = raw_input("What type would you like? Enter 'P' for petrol, 'D' for diesel, 'E' for electric or 'H' for Hybrid : ")
			answer = answer.upper()
			
			# Offer customer choice of Jeep or Sedan. Ensure answer is case sensitive
			make = raw_input("Would you like to rent a Jeep or Sedan? Please enter 'J' for Jeep or 'S' for Sedan : ")
			make = make.upper()
			
			# Prompt customer for the amount of vehicles they wish to rent
			amount = int(raw_input("How many would you like? "))
			
			# Change stock numbers based on customer's selections
			if answer == "P" and make == "J":
				self.rent(self.petrol_cars_jeep, amount)
			elif answer == "P" and make == "S":
				self.rent(self.petrol_cars_sedan, amount)
			elif answer == "D" and make == "J":
				self.rent(self.diesel_cars_jeep, amount)
			elif answer =="D" and make == "S":
				self.rent(self.diesel_cars_sedan, amount)
			elif answer == "H" and make == "J":
				self.rent(self.hybrid_cars_jeep, amount)
			elif answer == "H" and make == "S":
				self.rent(self.hybrid_cars_sedan, amount)
			elif answer == "E" and make == "J":
				self.rent(self.electric_cars_jeep, amount)
			else:
				self.rent(self.electric_cars_jeep, amount)
				
		self.stock_count()
		
		# If customer is not renting, they may  be returning
		if answer == "N":
			returns = raw_input("Are you returning a car? : Y/N ")
			returns = returns.upper()
			if returns == "Y":
				
				# what car are they returning?
				back = raw_input("What type would you like to return? Enter 'P' for petrol, 'D' for diesel, 'E' for electric or 'H' for Hybrid : ")
				back = back.upper()
						
				rmake = raw_input("Would you like to return a Jeep or Sedan? Please enter 'J' for Jeep or 'S' for Sedan : ")
				rmake = rmake.upper()
			
				ramount = int(raw_input("How many would you like to return? "))
				
				# add chosen car back to lot
				if back == "P" and rmake == "J":
					self.returning(self.petrol_cars_jeep, ramount)
				elif back == "P" and rmake == "S":
					self.returning(self.petrol_cars_sedan, ramount)
				elif back == "D" and rmake == "J":
					self.returning(self.diesel_cars_jeep, ramount)
				elif back =="D" and rmake == "S":
					self.returning(self.diesel_cars_sedan, ramount)
				elif back == "H" and rmake == "J":
					self.returning(self.hybrid_cars_jeep, ramount)
				elif back == "H" and rmake == "S":
					self.returning(self.hybrid_cars_sedan, ramount)
				elif back == "E" and rmake == "J":
					self.returning(self.electric_cars_jeep, ramount)
				else:
					self.returning(self.electric_cars_jeep, ramount)
			
			self.stock_count()		

dealership = Dealership()
dealership.create_current_stock()
dealership.stock_count()



# Offer customer chance to continue or quit
proceed = "Y"
while proceed == "Y":
	dealership.process_rental()
	proceed = raw_input("Would you like to continue? Y/N : ")
	proceed = proceed.upper()
	
print "Thank you for your custom. Have a nice day. "