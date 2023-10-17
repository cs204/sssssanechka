import sm

class Turnstile1(sm.SM):
	startState = 'locked'
	def getNextValues(self, state, inp):
		if state == 'locked':
			if inp == 'coin':
				return ('unlocked', 'enter')
			else:
				return ('locked', 'pay')
		else:	# state == 'unlocked'
			if inp == 'turn':
				return ('locked', 'pay')
			else:
				return ('unlocked', 'enter')


t1 = Turnstile1()
print (t1.transduce(['turn', 'coin', 'turn', 'coin']))