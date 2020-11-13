from ColorManager import *

class Encrypt:

	def encrypt(self,string , key):
		string1 = self.level1(string,key)
		return self.level2(string1,key)

	def level1(self,string,key):
		len1 = len(string)
		len2 = len(key)
		xor_string = ""
		for i in range(len1):
			xor_string = xor_string+(chr)(ord(string[i])^ord(key[i%len2]))
		return xor_string

	def level2(self,string,key):
		C=ColorManager()
		color=C.getcolor(key)
		len1=len(string)

		encoded_string=""
		j=0
		for i in range(len1):
			r=self.gethighernibble(ord(string[i]))
			c=self.getlowernibble(ord(string[i]))
			encoded_string = encoded_string + (chr)((color[j] + r*16 + c)%256)
			j = (j+1)%(len(color))

		return encoded_string

	def gethighernibble(self,x):
		return (x&240)>>4

	def getlowernibble(self,x):
		return (x&15)

