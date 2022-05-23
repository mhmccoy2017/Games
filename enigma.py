
import random


#This pyhton file will be used to create a enigma encyrption of any input text using the Engima 1 schema

#Global dict that is used as the core alphabet to letter conection for tranlsation in rotors
aplhadir = {'A': 1, 'B' : 2, 'C' : 3, 'D':4, 'E':5,
'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,
'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20
,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

class Rotor:
	'''
	Creates a rotor with the key matching to number pairs
	Has three varies key, notch, turnover
	'''
	def __init__(self, key, notch, turnover):
		self.turnover = turnover
		self.notch = notch
		self.keys = {}
		for k in key:
			self.keys[key.index(k)+1] = k

	def __str__(self):
		return f'Keys: {self.keys}, turnover {self.turnover}, notch {self.notch}'

	#Define a turn method when the ring hits it's notch it turns the key

	def turn(self):
		pass

	def translate(self, letter):
		global aplhadir
		return self.keys.get(aplhadir.get(letter))
		

#A randomized plugboard that built for the engima to match letters
class Plugboard:

	def __init__(self):
		self.plugboard = {}
		self.aplhalist = ['A', 'B', 'C', 'D', 'E','F','G','H','I','J','K','L','M','N',
		'O','P','Q','R','S','T','U','V','W','X','Y','Z']

	def __str__(self):
		return f'{self.plugboard}'

	#Creates a randomized pair of letters and saves them to plugboard dict, default input is 10 pairs 
	def create_board(self, num = 10):
		if num > 26:
			print(f'Too many pair attempts only 26 letters in the alphabet')
			return 
		for k in range(0,num+1): 
			self.plugboard[random.choice(self.aplhalist)] = random.choice(self.aplhalist)



#The Entire Enigma machine that will take each compnent and produce the scrambled output
class Enigma:

	def __init__(self, rotors, plugboard):
		self.rotors = rotors
		self.plugboard = plugboard

	#Define str method to print both the rotors in and the plugboard
	def __str__(self):
		return f'Plugboard: {self.plugboard}'

	#Define a reflector value that will take in one character and then pass it through the rotors in reverse order

	#Define an input method that will take any string and step through each letter of that string
	def encrypt(self, msg):
		global aplhadir
		#Stripping the msg of spaces and sending it to upper case for matches
		msg = msg.upper()
		msg = msg.replace(" ", "")
		#Init the out string
		#For every character in the msg translate it per each rotor
		temp = msg
		for r in self.rotors:
			out = ''
			for char in temp:
				out += r.translate(char)
			temp = out
		return temp

r1 = Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q', 'Y')
r2 = Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'M', 'E')
r3 = Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'D', 'V')
rs = [r1,r2,r3]
pb = Plugboard()
pb.create_board()
E1 = Enigma(rs,pb)
print(E1.encrypt('Hello my name is mark'))
