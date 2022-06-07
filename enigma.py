'''
This module can create three classes Engima, Rotor and Plugboard
It is designed to emulate the encryption used during WW2 that 
lead to the creation of the first turing machine
The rotor and plugboard classes are components of the Engima class
When run it will translate any message into an Enigma encoded message
'''
import random

#Global dict that is used as the core alphabet to letter conection for tranlsation in rotors
ALPHADIR = {'A': 1, 'B' : 2, 'C' : 3, 'D':4, 'E':5,
'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,
'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20
,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

#ADD LOGGING FUNCTIONS WITH ERROR CODES

class Rotor:
	'''
	Creates a rotor with the key matching to number pairs
	Has three variables key, notch, turnover
	'''
	def __init__(self, key, notch, turnover):
		self.turnover = turnover
		self.notch = notch
		self.keys = {}
		for k in key:
			self.keys[key.index(k)+1] = k

	def __str__(self):
		return f'Keys: {self.keys}, turnover {self.turnover}, notch {self.notch}'

	def turn(self):
		'''
		Moves the rotor dict one 'turn' which moves all values forward one position and takes the tail
		sets it as the head
		Takes no parameter and does an inplace change of self.keys
		'''
		temp = {}
		for i, _v in self.keys.items():
			temp[i] = self.keys.get(i+1)
		if temp[len(temp)] is None:
			temp[len(temp)] = self.keys.get(1)
		self.keys = temp

	def translate(self, letter):
		'''
		Translates the given letter to a new letter based off of rotor configuration
		Takes one parameter letter : string returns a string
		'''
		global ALPHADIR
		return self.keys.get(ALPHADIR.get(letter))

class Plugboard:
	'''
	A Plugboard object takes no parameter and has two attributes
	plugboard, an empty dict and aplhalist a list of the letters in the english alphabet
	'''
	def __init__(self):
		self.plugboard = {}
		self.aplhalist = ['A', 'B', 'C', 'D', 'E','F','G','H','I','J','K','L','M','N',
		'O','P','Q','R','S','T','U','V','W','X','Y','Z']

	def __str__(self):
		return f'{self.plugboard}'

	def get(self, char):
		'''
		Gets the matching character from a plugboard
		Takes one parameter char which is the key to search
		Returns a char the value of key char
		'''
		return self.plugboard.get(char)

	def create_board(self, num = 10):
		'''
		Creates a randomized plug board for an enimga
		Takes one parameter num : int default is 10
		'''
		if num > 26:
			print('Too many pair attempts only 26 letters in the alphabet')
			return
		for k in range(0,num+1):
			self.plugboard[random.choice(self.aplhalist)] = random.choice(self.aplhalist)

class Enigma:
	'''
	Enigma class is the whole encryption method and system
	Takes two parameters rotors : list[Rotors] , Plugboard : Dir
	'''
	def __init__(self, rotors, plugboard):
		self.rotors = rotors
		self.plugboard = plugboard

	def __str__(self):
		return f'Plugboard: {self.plugboard}'

	def reflector(self):
		'''
		Reverses the order of the rotor objects in the Enigma
		No paraemetrs, returns nothing. Inplace for self.rotors
		'''
		self.rotors = self.rotors[::-1]

	def teslate(self, msg):
		'''
		Passes a msg through a set of rotors that the Enigma class has
		and is half of the encryption process
		Takes one Parameter msg :String returns a string
		'''
		global ALPHADIR
		#Stripping the msg of spaces and sending it to upper case for matches
		msg = msg.upper()
		msg = msg.replace(" ", "")
		#Encrypt Message using plug board
		msg_plug = ''
		for char in msg:
			if self.plugboard.get(char) is not None:
				msg_plug += self.plugboard.get(char)
			else:
				msg_plug += char
		#For every character in the msg translate it per each rotor
		for _r in self.rotors:
			out = ''
			for char in msg_plug:
				if _r == self.rotors[0]:
					_r.turn()
				out += _r.translate(char)
			msg_plug = out
		return msg_plug

	def encrypt(self, msg):
		'''
		Combines the compents of the encryption and fully encrypts the message
		Takes one parameter message : String and returns a string encrypted
		'''
		first_pass = self.teslate(msg)
		#reverses the rotors
		self.reflector()
		return self.teslate(first_pass)

r1 = Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q', 'Y')
r2 = Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'M', 'E')
r3 = Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'D', 'V')
rs = [r1,r2,r3]
pb = Plugboard()
pb.create_board()
print(pb)
E1 = Enigma(rs,pb)
print(E1.encrypt('Hello'))
