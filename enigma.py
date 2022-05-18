
import random


#This pyhton file will be used to create a enigma encyrption of any input text using the Engima 1 schema

aplhadir = {1 :'A', 2 : 'B', 3 : 'C', 4 :'D', 5:'E',
6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',
12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q',18:'R',19:'S',20:'T'
,21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z'}

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

	def translate(self, letter, alphabet):
		print(self.keys.get(letter))

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

r1 = Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q', 'Y')
r2 = Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'M', 'E')
r3 = Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'D', 'V')
rs = [r1,r2,r3]
pb = Plugboard()
r1.translate('A', aplhadir)
pb.create_board()
E1 = Enigma(rs,pb)
