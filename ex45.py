from sys import exit
from random import randint

class scene(object):
	def going_a_direction(self):
		direction=raw_input("go left, right, straight, or back")
		return direction
	def fighting(self):
		number_of_monsters=randint(0,3)
		while True:
			if number_of_monsters==0:
				return 'nothing'
				
			number_of_monsters_str= str(number_of_monsters)
			hit=raw_input("there are " + number_of_monsters_str + " monsters, what do you do?\n fight or run \n >")
			if hit == 'fight':
				outcome = randint(0,10)
				if 5 < outcome < 10:
					print "you kill 1 monster"
					number_of_monsters= number_of_monsters-1
				elif outcome == 10:
					print "you critical hit you kill all monsters"
					number_of_monsters=0
				elif outcome == 0:
					print "you die"
					return 'death'
				else:
					print "you miss"
			elif hit == 'run':
				return 'room1'
			else:
				print "I didn't understand"
class room1(scene):
	def what_happens(self):
		print 'you are in an empty room somehow you know this is room 1'
		while True:
			direction = self.going_a_direction()
			if direction == 'right':
				return 'room2'
			elif direction == 'left':
				return 'room3'
			elif direction == 'straight':
				return 'room4'
			elif direction == 'back':
				return 'room5'
			else:
				print "I don't understand"
class room2(scene):
	def what_happens(self):
		print 'you are in an empty room somehow you know this is room 2'
		outcome = self.fighting()
		if outcome == 'nothing':
			while True:
				direction= self.going_a_direction()
				if direction == 'right':
					return 'room3'
				elif direction == 'left':
					return 'room4'
				elif direction == 'straight':
					return 'room5'
				elif direction == 'back':
					return 'room6'
				else:
					print "I don't understand"
		else:
			return outcome
class room3(scene):
	def what_happens(self):
		print 'you are in an empty room somehow you know this is room 3'
		while True:
			direction = self.going_a_direction()
			if direction == 'right':
				return 'room4'
			elif direction == 'left':
				return 'room5'
			elif direction == 'straight':
				return 'room6'
			elif direction == 'back':
				return 'room1'
			else:
				print "I don't understand"
class room4(scene):
	def what_happens(self):
		print 'you are in an empty room somehow you know this is room 4'
		outcome = self.fighting()
		if outcome == 'nothing':
			while True:
				direction = self.going_a_direction()
				if direction == 'right':
					return 'room5'
				elif direction == 'left':
					return 'room6'
				elif direction == 'straight':
					return 'room1'
				elif direction == 'back':
					return 'room2'
				else: 
					print 'you notince something weird about a lamp you wake up'
					return 'win'
		else:
			return outcome
class room5(scene):
	def what_happens(self):
		print 'you are in an empty room somehow you know this is room 5'
		while True:
			direction = self.going_a_direction()
			if direction == 'right':
				return 'room6'
			elif direction == 'left':
				return 'room1'
			elif direction == 'straight':
				return 'room2'
			elif direction == 'back':
				return 'room3'
			else:
				print "I don't understand"	
class room6(scene):
	def what_happens(self):
		print 'you are in an empty room somehow you know this is room 6'
		outcome = self.fighting()
		if outcome == 'nothing':
			while True:
				direction = self.going_a_direction()
				if direction == 'right':
					return 'room1'
				elif direction == 'left':
					return 'room2'
				elif direction == 'straight':
					return 'room3'
				elif direction == 'back':
					return 'room4'
				else:
					print "I don't understand"
		else:
			return outcome	
class death(scene):
	def what_happens(self):
		print 'you lose'
		exit(1)
class win(scene):
	def what_happens(self):
		print 'you win'
		exit(1)
		
class engine(object):
	def __init__(self, scene_map):
		self.scene_map = scene_map
	def play(self):
		current_scene=self.scene_map.where_you_are()
		while True:
			next_scene_name = current_scene.what_happens()
			current_scene = self.scene_map.where_you_go(next_scene_name)
		
class map(object):
	scene = {
		'room1': room1(),
		'room2': room2(),
		'room3': room3(),
		'room4': room4(),
		'room5': room5(),
		'room6': room6(),
		'death': death(),
		'win'  : win()
		}
	
	def __init__(self,start):
		self.start=start
	def where_you_go(self,scene_name):
		return self.scene.get(scene_name)
	def where_you_are(self):
		return self.where_you_go(self.start)
a_map=map('room1')
a_game=engine(a_map)
a_game.play() 