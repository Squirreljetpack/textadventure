import sys
import random
import text
from changedict import *
from collections import OrderedDict


def it_t(arg):
	global it_it
	it_it=arg

def badinput1():
	print 'I don\'t understand that. Please check your spelling, phrase it differently or give a different command.'
def badinput2(name):
	print 'You can\'t do that with %s.' %(name)
def badinput3():
	print "There is nothing there."
def itemc():
	for item in list(OrderedDict.fromkeys(inventory)):
		print dictionary2.get(item,item), " x ", inventory.count(item)
inventory=['backpack','oil','compass','oil','berries','porridge']
nouns=nouns + inventory
comb=['combine','mix']
poot=['put','place','insert','install','position','set','stick']
nos=['don\'t','not','except']
plos=['into', 'in', 'on','onto','upon','near','by','within','inside','under','above',]
def save():
	pass
def north(arg):
	if border[0]!=0:
		print border[0]
	elif arg in v_go+v_run:
		print "You went north."
		energ(2.5)
		map_matrix[m_row-1][m_column][0]()
	elif arg in v_no:
		print "What the fuck?"
	else:
		badinput2("a direction")
def south(arg):
	if border[1]!=0:
		print border[1]
	elif arg in v_go+v_run:
		print "You went south."
		energ(2.5)
		map_matrix[m_row+1][m_column][0]()
	elif arg in v_no:
		print "What the fuck?"
	else:
		badinput2("a direction")
def east(arg):
	if border[2]!=0:
		print border[2]
	elif arg in v_go+v_run:
		print "You went east."
		energ(2.5)
		map_matrix[m_row][m_column+1][0]()
	elif arg in v_no:
		print "What the fuck?"
	else:
		badinput2("a direction")
def west(arg):
	if border[3]!=0:
		print border[3]
	elif arg in v_go+v_run:
		print "You went west."
		energ(2.5)
		map_matrix[m_row][m_column-1][0]()
	elif arg in v_no:
		print "What the fuck?"
	else:
		badinput2("a direction")
def northeast(arg):
	if arg in v_go+v_run:
		direction=randrange(0,2)
		if direction<1:
			north(arg)
		else:
			east(arg)
	elif arg in v_no:
		print "What the fuck?"
	else:
		badinput2("a direction")
def northwest(arg):
	if arg in v_go+v_run:
		direction=randrange(0,2)
		if direction<1:
			north(arg)
		else:
			west(arg)
	elif arg in v_no:
		print "What the fuck?"
	else:
		badinput2("a direction")
def southeast(arg):
	if arg in v_go+v_run:
		direction=randrange(0,2)
		if direction<1:
			south(arg)
		else:
			east(arg)
	elif arg in v_no:
		print "What the fuck?"
	else:
		badinput2("a direction")
def southwest(arg):
	if arg in v_go+v_run:
		direction=randrange(0,2)
		if direction<1:
			south(arg)
		else:
			west(arg)
	elif arg in v_no:
		print "What the fuck?"
	else:
		badinput2("a direction")
def cict(arg,func):
	global dictionary
	for string in arg:
		dictionary[string]=func

def remv(*args):
	global inventory
	list=[]
	for arg in args:
		list.append(arg)
	listi=list[::2]
	listn=list[1::2]
	i=0
	no=0
	s="You don't have enough items for that. You still need "
	for item in listi:
		if inventory.count(item)<listn[i]:
			t=listn[i]-inventory.count(item)
			s=s+str(t)+' '+dictionary2[item]+', '
			no=1
		i=i+1
	i=0
	if no==0:
		for item in listi:
			for num in range(listn[listi.index(item)]):
				inventory.remove(item)
				i=i+1
		return True
	else:
		s=s[:-2]+'.'
		print s[s.rindex(','):(s.rindex(',')+1)]
		try:
			s=s[:s.rindex(',')]+' and'+s[s.rindex(',')+1:]
		except:
			pass
		print s
		return False
def add(*args):
	global inventory
	list=[]
	for arg in args:
		list.append(arg)
	listi=list[::2]
	listn=list[1::2]
	i=0
	for item in listi:
		inventory=inventory+[item]*listn[i]
		i=i+1
def environment():
	pass
def backpack(arg):
	if arg in v_look+v_open:
		print "You picked it up. It's sturdy and large. It looks like it could store a lot of items. Press 'i' to see whats inside."
	elif arg in v_destroy+v_harm+v_kick+v_punch:
		print "It's sturdy and large. A little wear won't affect it. The material it's made of feels kinda good too."
	elif arg in v_no:
		print "You're sick."
	else:
		badinput2('a backpack')
	it_t('backpack')
def tree(arg):
	if arg in v_harm+v_punch+v_kick:
		print "You shook the tree. Wood+1"
def berries(arg):
	global inventory
	if arg=='get' or arg=='take' or arg=='pick':
		berrynum=random.randrange(2, 5)
		add('berries',berrynum)
		print "You picked some nice plump berries. Berry +"+str(berrynum)
		hurt(1)
	if arg=='kick':
		print "An apple fell down."

def grass(arg):
	if arg in v_harm+v_destroy+v_punch+v_kick+v_get+v_no:
		print "You imagine each blade of grass screaming in pain as you do that. You monster."
	elif arg in v_look+v_smell+v_touch:
		print "It's grass."
	else:
		badinput2('grass')
	it_t('grass')
def sky(arg):
	if arg in v_look:
		print terrain_sky
		if energy<10:
			if terrain_sky=="forest":
				print "You look up to see moonlight fall through the branches like notes of a piano. You then follow it down and watch the shifting foliage creates ethereal patterns on the speckled forest floor. What \x1B[3mis\x1B[23m this place?"
			if terrain_sky=="beach":
				print "Confronted with austere moon, you inadvertently shiver in its cold glow. Soft waves lap against your feet repeatedly, the frothy edges leaving bubbles on your toes. What \x1B[3mis\x1B[23m this place?"
			if terrain_sky=="clear":
				print "You stagger at the sight that beholds you. The sky is strewn with a river of stars, so densely packed their iridescence seemingly light up the night like day. What \x1B[3mis\x1B[23m this place?"
		else:
			if terrain_sky=="forest":
				print "You look up to see the blindingly strong sunlight flood through the gaps in the leaves. The ever-shifting shafts of light split and almagate in mesmerizing order, presenting an unreal lightshow in the midst of this strange forest. What \x1B[3mis\x1B[23m this place?"
			if terrain_sky=="beach":
				print "The sun, hampered by nothing on this easy day radiates gloriously as far as the eye can see in every direction; its brilliance illuminates the clouds, the waters, the sands. What \x1B[3mis\x1B[23m this place?"
			if terrain_sky=="clear":
				print "It's too bright to look at but you can feel the heat, a tender envelope around your skin. The sunlight radiates into evey corner, behind every rock, reaches every flower-filling the forest with life and vitality. What \x1B[3mis\x1B[23m this place?"
	else:
		badinput2('sky')
	it_t('sky')


class boots(object):
	def __init__(self, name, description,health):
		self.description=description
		self.health=health
		self.equipped=False
		self.name=name
	def func(self,arg):
		global inventory
		global maxhealth
		if arg in v_look:
				print self.description
		elif arg in v_get:
			if self.equipped==False:
				if 'boots' in inventory:
					remv('boots',1)
				dictionary2['boots']=self.name
				add('boots',1)
				print "%s equipped. +%s health"%(self.name,self.health)
				maxhealth=maxhealth+self.health
				self.equipped=True
			elif self.equipped==True:
				badinput3()
		elif arg in v_remove:
			if self.equipped==True:
				truth=remv('boots',1)
				if truth==True:
					print "You dropped the %s. -%s health"%(self.name,self.health)
					maxhealth=maxhealth+self.health
				else:
					print "You don't have any boots to remove."
		elif arg in v_no:
			print "You're sick."
		else:
			badinput2("boots")
		it_t('boots')
starterboots=boots("Starter boots", "A pair of sturdy boots.",1)


def put(liste,listl):
	for element in liste:
		for location in listl:
			if element=='boots':
				if location=='girl':
					print 'why did you do that'
	if not liste:
		for location in listl:
			if location=='boots':
				print 'you aren\'t naked no more.'
			if location=='hat':
				print 'you aren\'t naked no more2.'

def apple(arg):
	if arg=='pick':
		print "You picked an apple. Apple+1"
def girl(arg):
	if arg=='punch' or 'kick':
		print "Oof. Nice one. You knocked her out cold!"
		energ(9)
def combi(list):
	global inventory
	if set(list)==set(['oil','berries','porridge']):
		truth=remv('oil',1,'berries',6,'porridge',1)
		if truth==True:
			print "Delicious!"
	else:
		print "This set of items cannot be used together."

def error(*arg):
	pass

dictionary={'apple':apple,'tree':tree,'girl':girl,'grass':grass,'berries':berries,'environment':environment}
dictionary2={'oil':'bottles of oil','porridge':'bowls of porridge','boots':'pairs of boots'}
cict(n_north,north)
cict(n_south,south)
cict(n_east,east)
cict(n_west,west)
cict(n_northeast,northeast)
cict(n_northwest,northwest)
cict(n_southeast,southeast)
cict(n_southwest,southwest)
cict(n_backpack,backpack)
cict(n_sky,sky)
def nl(*args):
	for arg in args:
		nouns.append(arg)
		print arg
	words=[]
	input=raw_input('>')
	input=input.lower().split()
	if input==['h']:
		print text.help
	elif input==['p']:
		menu()
	elif input==['i']:
		itemc()
	elif input==['m']:
		map_show()
	elif input==['s']:
		stats()
		save()
	else:
		for choice in input:
			if not choice[0].isalnum():
				choice=choice[1:]
			if not choice[-1].isalnum():
				choice=choice[:-1]
			if multiple_setting==-1:
				if choice in verbs or choice in nouns or choice in comb or choice in poot or choice in plos:
			 		words.append(choice)
			if multiple_setting==1:
				if choice in verbs or choice in nouns or choice in comb or choice in poot or choice in plos or choice.isdigit():
			 		words.append(choice)
			else:
			 	pass
		words.append('specialverb')
		words=['specialnoun']+words
		s=0
		A=[]
		m=0
		while s<len(words):
			if words[s] not in nouns and words[s] not in nos and words[s] not in plos:
				L=words[m:s]
				A.append(L)
				m=s
			s=s+1
		A=A[1:]
		if not A:
			badinput1()
		for action in A:
#			nub=1
	#		for number in action:
		#		if number.isdigit():
			#		nub=number*nub
			if action[0]=='use':
				if len(action)>2:
			#		for times in range(nub):
					combi(action[1:])
				else:
			#		for times in range(nub):
					try:
						dictionary.get(action)('use')
					except:
						badinput1()
			if action[0] in verbs:
				verb=action.pop(0)
				for noun in action:
#					for times in range(nub):
	#					lastnoun=0
		#				if noun==lastnoun:
			#				pass
				#		else:
					if noun=='it':
						dictionary.get(it_it)(verb)
					else:
						dictionary.get(noun)(verb)
		#				lastnoun=noun
			elif action[0] in comb:
	#			for times in range(nub):
				combi(action[1:])
			elif action[0] in poot:
				action.append('specialverb')
				t=1
				y=1
				k=0
				while k<2 and t<=len(action):
					if action[t] in plos or action[t]=='specialverb':
						listl=action[y:t]
						y=t+1
						k=k+1
						if k==2:
							break
						liste=listl
					t=t+1
					if t>=len(action):
							break
				put(liste,listl)
	nl()




health=3
hunger=0
energy=30
multiple_setting=1

maxenergy=30
maxhealth=3
maxhunger=10
days=0
stage=0
maxstages='?'


def energ(arg):
	global health
	global energy
	global hunger
	global days
	if arg=='sleep':
		energy=0
	else:
		energy=energy-arg
	if energy<=0:
		energy=maxenergy
		s="Good night  +%s energy"%(maxenergy)
		if hunger>maxhunger:
			health=health-1
			s=s+"  -1 health"
		hunger+4
		days=days+1
		print s
		print "...\nGood morning!"
		environment()
		return
def hurt(arg):
	global health
	global energy
	global hunger
	health1=health
	health=health+arg
	if health>=maxhealth:
		health=maxhealth
	hur=health-health1
	if hur>=0:
		s="You gained"
	else:
		s="You lost"
	print s,hur,"health"
	if health<=0:
		print "dead"

def stats():
	h=e=u="    "
	if health*3<=maxhealth:
		h="[!] "
	if energy<5:
		e="[!] "
	if hunger>maxhunger:
		u="[!] "
	print "	%sHealth:		%s/%s\n	%sEnergy:		%s/%s\n	%sHunger:		%s/%s" %(h,health,maxhealth,e,energy,maxenergy,u,hunger,maxhunger)
	print "	    Days:		%s\n	    Stage:		%s/%s\n	    [Saved]" %(days,stage,maxstages)
def settings():
	print "\n"+"-"*90
	global multiple_setting
	if multiple_setting==-1:
		sone="Off"
	if multiple_setting==1:
		sone="On"
	print "Enter the number by the option to adjust it. Press return to return to menu."
	print "1. [%s] Carry out numbers multiple times using numbers. (E.g. Shake the tree 3 times or Pick 3 berries.)" %sone
	result=raw_input('>')
	if result=='1':
		multiple_setting=multiple_setting*-1
		print "Setting Changed. Setting 1 is now %s." %sone
		settings()
	if result=='':
		menu()
	else:
		result=raw_input('>')

def menu():
	print "\n"*2+"-"*90+"""
	What do you want to do?
	[Y] Continue [N] Exit [S] Save [O] Options [V] View Credits [E] Select Scenario"""
	menv=raw_input('?')
	if menv.lower()=='y':
		current.input()
	if menv.lower()=='n':
		save()
		sys.exit(0)
	if menv.lower()=='s':
		save()
		stats()
	if menv.lower()=='o':
		settings()
	if menv.lower()=='v':
		print credits
	if menv.lower()=='e':
		print "1. ", scen1
		print "2. ", scen2
		print "3. ", scen3
		print "4. ", scen4
		print "5. ", scen5
		print "6. ", scen6
		print "7. ", scen7
		print "8. ", scen8
	else:
		menu()
border=[0,0,0,0]
m_row=7
m_column=6

def m_locate(row,column,sign):
	global m_row
	global m_column
	global map_matrix
	m_row=row
	m_column=column
	map_matrix[m_row][m_column][1]="[%s]"%sign
	map_matrix[m_row][m_column][2]+=1

#start
terrain_sky="forest"
def r7c6():
	m_locate(7,6," S ")
	a_boots="Your boots are on the ground. You better pick them up."
	a_trees="There are no trees in your clearing but outside, the wood is dense."
	def environment(arg):
		if arg in v_look:
			if starterboots.equipped==False:
				print a_boots
			print a_trees
		else:
			badinput2('the environment')
		it_t('environment')
	cict(n_boots,starterboots.func)
	cict(n_environment,environment)
	if map_matrix[7][6][2]==1:
		print text.r7c6_1
		halp=raw_input('>')
		print text.help
		nl('grass','boots','backpack')
	else:
		if energy<10:
			print text.r7c6_n
			nl('grass')
		else:
			print text.r7c6_d
			nl('grass')

def r6c6():
	m_locate(6,6,"   ")
	print text.r6c6
	nl('grass','trees')
class br(object):
	def __init__(self,row,column,*args):
		self.row=row
		self.column=column
		self.indx=[]
		for ind in args:
			self.indx.append(ind)
	def g(self):
		m_locate(self.row,self.column,"^^^")
		print text.rcmountains
		border[:]=(br_mountains,)*4
		for ind in self.indx:
			border[ind]=0
		def environment(arg):
			print br_mountains
		cict(n_environment,environment)
		nl('ground','grass','mountains')
	def f(self):
		m_locate(self.row,self.column,"~~~")
		print text.rcseas
		border[:]=(br_seas,)*4
		for ind in self.indx:
			border[ind]=0
		def environment(arg):
			print br_seas
		cict(n_environment,environment)
		nl('ground','grass','mountains')
br_mountains="The mountains surround you for miles. There's no point going any further."
r0c0=br(0,0).g
r0c1=br(0,1,1).g
r0c2=br(0,2,1).g
r0c3=br(0,3,1).g
r0c4=br(0,4,1).g
r1c0=br(1,0,2).g
r2c0=br(2,0,2).g
r3c0=br(3,0,2).g
r4c0=br(4,0).g
r4c1=br(4,1,0,1,2).g
r5c0=br(5,0,2).g
br_seas="Eternal waves wash against the soft shoreline. The sea's patient majesty fills you with awe. There's no point going any further."
r6c0=br(6,0).f
r6c1=br(6,1,0,1,2).f
r7c0=br(7,0,2).f
r8c0=br(8,0,2).f
r9c0=br(9,0,2).f
r10c0=br(10,0,2).f
r11c0=br(11,0,2).f
r12c0=br(12,0).f
r12c1=br(12,1,0,2).f
r13c0=br(13,0).f
r13c1=br(13,1).f
r13c2=br(13,2).f
r13c3=br(13,3,0).f
r13c4=br(13,4,0).f
r13c5=br(13,5).f
r13c6=br(13,6,0).f
r13c7=br(13,7).f
r13c8=br(13,8,0).f
r13c9=br(13,9).f
r13c10=br(13,10).f
r13c11=br(13,11).f
r13c12=br(13,12).f
r13c13=br(13,13).f
r13c14=br(13,14).f
r13c15=br(13,15).f
r12c4=br(12,4,0,2,3).f
r12c6=br(12,6,0,2,3).f
r12c9=br(12,9,0).f
r12c8=br(12,8,0,3).f
r12c10=br(12,10,0).f
r12c11=br(12,11,0).f
r12c12=br(12,12,0).f
r12c13=br(12,13,0).f
r12c14=br(12,14).f
r12c15=br(12,15).f
r11c15=br(11,15).f
r10c15=br(10,15).g
r9c15=br(9,15).g
r8c15=br(8,15).g
r7c15=br(7,15).g
r6c15=br(6,15).g
r5c15=br(5,15).g
r4c15=br(4,15).g
r3c15=br(3,15).g
r2c15=br(2,15).g
r1c15=br(1,15).g
r0c15=br(0,15).g
r3c14=br(3,14,0).g
r2c14=br(2,14,3).g
r1c14=br(1,14,1).g
r0c14=br(0,14).g
r5c14=br(5,14).f
r6c14=br(6,14).f
r7c14=br(7,14).f
r8c14=br(8,14).f
r9c14=br(9,14).f
r10c14=br(10,13).f
r11c14=br(11,13,3).f
r3c13=br(3,13,1,3).g
r1c13=br(1,13).g
r0c13=br(0,13).f
r5c13=br(5,13,0,3).f
r6c13=br(6,13,3).f
r7c13=br(7,13).f
r8c13=br(8,13).f
r9c13=br(9,13).f
r10c13=br(10,13,3,1).f
r0c12=br(0,12).f
r0c11=br(0,11).f
r0c10=br(0,10).f
r0c9=br(0,9).f
r0c8=br(0,8,1).f
r0c7=br(0,7,1).f
r0c6=br(0,6,1).f
r0c5=br(0,5,1).f
r1c5=br(1,5,1,2,3).f
r1c9=br(1,9,1,3).f
r1c10=br(1,10,1).f
r1c11=br(1,11).f
r1c12=br(1,12,1).f
r2c11=br(2,11,2,3).f
r3c11=br(3,11,1,2).f
r3c10=br(3,10,1,2).f
r3c9=br(3,9,1,2).f
r7c10=br(7,10,0,1,3).f
r9c10=br(9,10,0,1,3).f
r7c11=br(7,11,0).f
r8c11=br(8,11,3).f
r9c11=br(9,11,0,1).f
r7c12=br(7,12,0).f
r8c12=br(8,12).f
r9c12=br(9,12,1).f

map_matrix=[
[[    r0c0,"     ",0],[    r0c1,"     ",0],[    r0c2,"     ",0],[    r0c3,"     ",0],[    r0c4,"     ",0],[    r0c5,"     ",0],[    r0c6,"     ",0],[    r0c7,"     ",0],[    r0c8,"     ",0],[    r0c9,"     ",0],[   r0c10,"     ",0],[   r0c11,"     ",0],[   r0c12,"     ",0],[   r0c13,"     ",0],[   r0c14,"     ",0],[   r0c15,"     ",0]],
[[    r1c0,"     ",0],[  "r1c1","     ",0],[  "r1c2","     ",0],[  "r1c3","     ",0],[  "r1c4","     ",0],[    r1c5,"     ",0],[  "r1c6","     ",0],[  "r1c7","     ",0],[  "r1c8","     ",0],[    r1c9,"     ",0],[   r1c10,"     ",0],[   r1c11,"     ",0],[ "r1c12","     ",0],[   r1c13,"     ",0],[   r1c14,"     ",0],[   r1c15,"     ",0]],
[[    r2c0,"     ",0],[  "r2c1","     ",0],[  "r2c2","     ",0],[  "r2c3","     ",0],[  "r2c4","     ",0],[  "r2c5","     ",0],[  "r2c6","     ",0],[  "r2c7","     ",0],[  "r2c8","     ",0],[  "r2c9","     ",0],[ "r2c10","     ",0],[   r2c11,"     ",0],[ "r2c12","     ",0],[ "r2c13","     ",0],[   r2c14,"     ",0],[   r2c15,"     ",0]],
[[    r3c0,"     ",0],[  "r3c1","     ",0],[  "r3c2","     ",0],[  "r3c3","     ",0],[  "r3c4","     ",0],[  "r3c5","     ",0],[  "r3c6","     ",0],[  "r3c7","     ",0],[  "r3c8","     ",0],[    r3c9,"     ",0],[   r3c10,"     ",0],[   r3c11,"     ",0],[ "r3c12","     ",0],[   r3c13,"     ",0],[   r3c14,"     ",0],[   r3c15,"     ",0]],
[[    r4c0,"     ",0],[    r4c1,"     ",0],[  "r4c2","     ",0],[  "r4c3","     ",0],[  "r4c4","     ",0],[  "r4c5","     ",0],[  "r4c6","     ",0],[  "r4c7","     ",0],[  "r4c8","     ",0],[  "r4c9","     ",0],[ "r4c10","     ",0],[ "r4c11","     ",0],[ "r4c12","     ",0],[ "r4c13","     ",0],[ "r4c14","     ",0],[   r4c15,"     ",0]],
[[    r5c0,"     ",0],[  "r5c1","     ",0],[  "r5c2","     ",0],[  "r5c3","     ",0],[  "r5c4","     ",0],[  "r5c5","     ",0],[  "r5c6","     ",0],[  "r5c7","     ",0],[  "r5c8","     ",0],[  "r5c9","     ",0],[ "r5c10","     ",0],[ "r5c11","     ",0],[ "r5c12","     ",0],[   r5c13,"     ",0],[   r5c14,"     ",0],[   r5c15,"     ",0]],
[[    r6c0,"     ",0],[    r6c1,"     ",0],[  "r6c2","     ",0],[  "r6c3","     ",0],[  "r6c4","     ",0],[  "r6c5","     ",0],[    r6c6,"     ",0],[  "r6c7","     ",0],[  "r6c8","     ",0],[  "r6c9","     ",0],[ "r6c10","     ",0],[ "r6c11","     ",0],[ "r6c12","     ",0],[   r6c13,"     ",0],[   r6c14,"     ",0],[   r6c15,"     ",0]],
[[    r7c0,"     ",0],[  "r7c1","     ",0],[  "r7c2","     ",0],[  "r7c3","     ",0],[  "r7c4","     ",0],[  "r7c5","     ",0],[    r7c6,"[ S ]",0],[  "r7c7","     ",0],[  "r7c8","     ",0],[  "r7c9","     ",0],[   r7c10,"     ",0],[   r7c11,"     ",0],[   r7c12,"     ",0],[   r7c13,"     ",0],[   r7c14,"     ",0],[   r7c15,"     ",0]],
[[    r8c0,"     ",0],[  "r8c1","     ",0],[  "r8c2","     ",0],[  "r8c3","     ",0],[  "r8c4","     ",0],[  "r8c5","     ",0],[  "r8c6","     ",0],[  "r8c7","     ",0],[  "r8c8","     ",0],[  "r8c9","     ",0],[ "r8c10","     ",0],[   r8c11,"     ",0],[   r8c12,"     ",0],[   r8c13,"     ",0],[   r8c14,"     ",0],[   r8c15,"     ",0]],
[[    r9c0,"     ",0],[  "r9c1","     ",0],[  "r9c2","     ",0],[  "r9c3","     ",0],[  "r9c4","     ",0],[  "r9c5","     ",0],[  "r9c6","     ",0],[  "r9c7","     ",0],[  "r9c8","     ",0],[  "r9c9","     ",0],[   r9c10,"     ",0],[   r9c11,"     ",0],[   r9c12,"     ",0],[   r9c13,"     ",0],[   r9c14,"     ",0],[   r9c15,"     ",0]],
[[   r10c0,"     ",0],[ "r10c1","     ",0],[ "r10c2","     ",0],[ "r10c3","     ",0],[ "r10c4","     ",0],[ "r10c5","     ",0],[ "r10c6","     ",0],[ "r10c7","     ",0],[ "r10c8","     ",0],[ "r10c9","     ",0],["r10c10","     ",0],["r10c11","     ",0],["r10c12","     ",0],[  r10c13,"     ",0],[  r10c14,"     ",0],[  r10c15,"     ",0]],
[[   r11c0,"     ",0],[ "r11c1","     ",0],[ "r11c2","     ",0],[ "r11c3","     ",0],[ "r11c4","     ",0],[ "r11c5","     ",0],[ "r11c6","     ",0],[ "r11c7","     ",0],[ "r11c8","     ",0],[ "r11c9","     ",0],["r11c10","     ",0],["r11c11","     ",0],["r11c12","     ",0],["r11c13","     ",0],[  r11c14,"     ",0],[  r11c15,"     ",0]],
[[   r12c0,"     ",0],[   r12c1,"     ",0],[ "r12c2","     ",0],[ "r12c3","     ",0],[   r12c4,"     ",0],[ "r12c5","     ",0],[   r12c6,"     ",0],[ "r12c7","     ",0],[   r12c8,"     ",0],[   r12c9,"     ",0],[  r12c10,"     ",0],[  r12c11,"     ",0],[  r12c12,"     ",0],[  r12c13,"     ",0],[  r12c14,"     ",0],[  r12c15,"     ",0]],
[[   r13c0,"     ",0],[   r13c1,"     ",0],[   r13c2,"     ",0],[   r13c3,"     ",0],[   r13c4,"     ",0],[   r13c5,"     ",0],[   r13c6,"     ",0],[   r13c7,"     ",0],[   r13c8,"     ",0],[   r13c9,"     ",0],[  r13c10,"     ",0],[  r13c11,"     ",0],[  r13c12,"     ",0],[  r13c13,"     ",0],[  r13c14,"     ",0],[  r13c15,"     ",0]],
]

def map_show():
	y=map_matrix[m_row][m_column][1]
	map_matrix[m_row][m_column][1]="[ X ]"
	for row in map_matrix:
		s=""
		for column in row:
			s=s+column[1]
		print s
	map_matrix[m_row][m_column][1]=y

r7c6()
