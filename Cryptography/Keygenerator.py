from ArmstrongManager import *

class Keygenerator:

	def getkeyvalue(self,sample):
		cnt=0
		for i in range(len(sample)):
			cnt = cnt + (ord)(sample[i])

		return cnt;

	def generatekey(self,sample):
		value = self.getkeyvalue(sample)
		A = ArmstrongManager()
		permutation=(int)(A.getpermutation(value))

		key = "" 
		while permutation > 0:
			key = (str)(A.ArmstrongNumbers[permutation%10 - 1])+key
			permutation = (int)(permutation/10)
		key = key + str(value)
		return key
