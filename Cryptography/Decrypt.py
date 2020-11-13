from ColorManager import *

class Decrypt:
	def decrypt(self,string,key):
		string1 = self.level2(string,key)
		return self.level1(string1,key)

	def level2(self,string,key):
		c=ColorManager()
		color=c.getcolor(key)
		len1 = len(string)

		j=0
		decode = ""
		for i in range(len1):
			temp = (int)((ord(string[i])-color[j]+256)%256)
			r=(int)(temp/16)
			c=(int)(temp%16)
			decode = decode + (chr)(self.merge(r,c))
			j=(j+1)%(len(color))

		return decode

	def level1(self,string, key):
		len1=len(string)
		len2=len(key)
		decode=""
		for i in range(len1):
			decode =decode + (chr)(ord(string[i])^ord(key[i%len2]))

		return decode

	def merge(self,nibble1,nibble2):
		return (nibble1<<4)|nibble2

