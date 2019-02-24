
from abc import ABCMeta, abstractmethod
from random import randint



class Acct(metaclass=ABCMeta):


	@abstractmethod
	def createAcct():
		return 0


	@abstractmethod
	def is_auth():
		return 0



	@abstractmethod
	def with_amt():
		return 0




	@abstractmethod
	def dep_amt():
		return 0



	@abstractmethod
	def get_balance():	
		return 0



class SaveAcct(Acct):


	def __init__(self):
		self.saveAcct = {} ## in this dictionary, [key][0]=name; [key][1]=balance




	def createAcct(self, name, ini_dep):
		self.acctnum = randint(10000, 99999)
		self.saveAcct[self.acctnum]=[name, ini_dep]
		print("Acct created. Acct num is {}".format(self.acctnum))







	def is_auth(self, name, acctnum):
		
		if acctnum in self.saveAcct.keys():
			if self.saveAcct[acctnum][0] == name:
				print("success")
				self.acctnum = acctnum
				return True
			else:
				print("failed")
				return False
		else:
			print("auth failed")
			return False








	def with_amt(self, amtwith):

		if amtwith > self.saveAcct[self.acctnum][1]:
			print("insufficient balance")

		else:
			self.saveAcct[self.acctnum]-=amtwith
			print("Withdraw successful") ## Avail balance is {}".format(self.saveAcct[self.acctnum][1]))
			self.get_balance()






	def dep_amt(self, amtdep):
		self.saveAcct[self.acctnum][1]+= amtdep
		print("Deposit done.") ## Avail balace is {}".format(self.saveAcct[self.acctnum][1]))
		self.get_balance() 




	def get_balance(self):	
		print("Avail balance is {}".format(self.saveAcct[self.acctnum][1]))




test_app = SaveAcct()

while True:
	print("Enter 1 to create new acct")
	print("Enter 2 to existing acct")
	print("Enter 3 to exit")

	userChoise = int(input())

	if userChoise is 1:
		print("Enter your name: ")
		name = input()

		print("Your deposit")
		deposit = int(input())

		test101 = test_app.createAcct(name, deposit)


	elif userChoise is 2:
		print("Enter your name: ")
		name = input()

		print("your acct num")
		acctnum = int(input())

		auth_stat = test_app.is_auth(name, acctnum)


		if auth_stat is True:
			while True:
				print("Enter 1 to withdraw")
				print("Enter 2 to dep")
				print("Enter 3 to display")
				print("Enter 4 to go back")

				userChoise = int(input())
				if userChoise is 1:
					print("Enter withdraw amount")
					withamt = int(input())
					test_app.with_amt(withamt)


				elif userChoise is 2:
					print("Enter deposit amount")
					depamt = int(input())
					test_app.dep_amt(depamt)



				elif userChoise is 3:
					test_app.get_balance()



				elif userChoise is 4:
					break


	elif userChoise is 3:
		quit()
	






