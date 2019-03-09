import pygame
import random
import time

#123

pygame.init()

screen = pygame.display.set_mode([800,720])
font = pygame.font.Font("font/CHILLER.TTF", 28)
font_for_numders = pygame.font.Font("font/CHILLER.TTF", 200)

keep_going = True
move_left = False
move_right = False
mouse_down = False
check_beer = False
game_over = False
check_game_over = False
game_start = 0
# doing_jump = False

# to = 1
counter = 1
timer = 3
T = time.time()
time_to_beer = time.time() - 5
time_picture = time.time() - 1

meat_and_beer = {}
chekanov = {}

pic_chekanov_left = pygame.image.load("image/chekanov left.png")
pic_chekanov_right = pygame.image.load("image/chekanov right.png")
pic_chekanov_front = pygame.image.load("image/chekanov front.png")
pic_game_over = pygame.image.load("image/game over2.png")
pic_main_menu = pygame.image.load("image/main menu.png")
pic_meat = [pygame.image.load("image/1_v2.png"),
			pygame.image.load("image/2_v2.png"),
			pygame.image.load("image/3_v2.png"),
			pygame.image.load("image/4_v2.png"),
			pygame.image.load("image/5_v2.png"),
			pygame.image.load("image/6_v2.png"),
			pygame.image.load("image/7_v2.png"),
			pygame.image.load("image/8_v2.png"),
			pygame.image.load("image/zero.png"),
			pygame.image.load("image/beer.png")]

text_numbers = [ "1", "2", "3", "4", "5" ]
text_about_food = [ "MMM DELICIOUS", 
					"IT'S TASTY",
					"I WANT TO HAVE CHILDREN FROM CHEKANOV",
					"IGNAT IS LOX",
					"I LIKE IT",
					"MATVEY IS KRYT" ]



class Meat_and_Beer:
	def __init__(self, x, y, speed, screen, k):
		self.x = x
		self.y = y
		self.speed = speed
		self.screen = screen
		self.k = k

	def move(self):
		self.y += self.speed

	def draw(self):
		self.screen.blit(pic_meat[self.k], (self.x, self.y))


class Chekanov:
	def __init__(self, x, y, points, screen):
		self.x = x
		self.y = y
		self.points = points
		self.screen = screen

	def move_left(self):
		self.x -= 0.75
		if (self.x < -80):
			self.x = 800

	def move_right(self):
		self.x += 0.75
		if (self.x > 800):
			self.x = -80

	# def jump(self, t):
	# 	self.y = 640 - 333*(time.time() - t) + 444*pow(time.time() - t, 2)

	def draw_left(self):
		self.screen.blit(pic_chekanov_left, (self.x, self.y))

	def draw_right(self):
		self.screen.blit(pic_chekanov_right, (self.x, self.y))

	def draw_front(self):
		self.screen.blit(pic_chekanov_front, (self.x, self.y))

	def update_points(self, drunk):
		for i in meat_and_beer:
			if (meat_and_beer[i].x > self.x - 15 and meat_and_beer[i].x < self.x + 80 and meat_and_beer[i].y > self.y - 80 and meat_and_beer[i].y < self.y + 80 and meat_and_beer[i].k < 8):
				if (drunk):	
					self.points += 1.5*(meat_and_beer[i].k + 1)
					print(self.points)
					return True
				else:
					self.points += 0.5*(meat_and_beer[i].k + 1)
					print(self.points)
					return True


	def draw_points(self):
		text = font.render(str(int(self.points)), True, (0,0,0))
		self.screen.blit(text,[0, 0])

	def check_beer(self):
		for i in meat_and_beer:
			if (meat_and_beer[i].x > self.x - 68 and meat_and_beer[i].x < self.x + 80 and meat_and_beer[i].y > self.y - 80 and meat_and_beer[i].y < self.y + 80 and meat_and_beer[i].k == 9):
				Game.delete(i)
				return True
			else: 
				return False


class Game:
	def add_record():
		records_str = ''
		records = open("files/records.txt", 'r')
		records_list = records.read().split('\n')
		records.close()
		# records_list.append(str(int(chekanov[0].points)))
		sorted(records_list, reverse = True)
		for i in range(len(records_list)):
			records_str += str(records_list[i]) +'\n'
		records = open("files/records.txt", 'w')
		records.write(records_str)
		records.close()
	def check_delete():
		for i in meat_and_beer:
			if (meat_and_beer[i].x > chekanov[0].x - 15 and meat_and_beer[i].x < chekanov[0].x + 80 and meat_and_beer[i].y > chekanov[0].y - 80 and meat_and_beer[i].y < chekanov[0].y + 80 and meat_and_beer[i].k < 8):
				Game.delete(i)
				break
			if (meat_and_beer[i].x > chekanov[0].x - 68 and meat_and_beer[i].x < chekanov[0].x + 80 and meat_and_beer[i].y > chekanov[0].y - 80 and meat_and_beer[i].y < chekanov[0].y + 80 and meat_and_beer[i].k == 9):
				Game.delete(i)
				break
			if (meat_and_beer[i].y > 730):
				Game.delete(i)
				break

	def check_game_over(i):
		if (meat_and_beer[i].y >= 720 and meat_and_beer[i].k != 8 and meat_and_beer[i].k != 9):
			return True
		elif (meat_and_beer[i].x > chekanov[0].x - 15 and meat_and_beer[i].x < chekanov[0].x + 80 and meat_and_beer[i].y > chekanov[0].y - 80 and meat_and_beer[i].y < chekanov[0].y + 80 and meat_and_beer[i].k == 8):
			return True
		else: 
			return False

	def check_game_start(x, y):
		if (x<600 and x>200 and y<200 and y>0):
			return True
		if (x<600 and x>200 and y<700 and y>500):
			Game.add_record()
			pygame.quit()


	def game_over(x, y):
		if (200 < x and x < 600 and 215 < y and y < 415):
			return False
		elif (200 < x and x < 600 and 500 < y and y < 700):
			Game.add_record()
			pygame.quit()	
		else:
			return True

	def game_over_draw(screen):
		screen.blit(pic_game_over, (0, 0))

	def draw_main_menu(screen):
		screen.blit(pic_main_menu, (0, 0))

	def delete(i):
		del meat_and_beer[i]

	def draw_picture_about_food(screen, n):	
		text = font.render(str(text_about_food[n]), True, (0,0,0))
		screen.blit(text,(80, 0))

	def timer(screen, number):
		text = font_for_numders.render(str(text_numbers[number]), True, (128,0,0))
		screen.blit(text, (360, 240))

	def random():
		x = random.randint(0,720)
		y = random.randint(-280,-180)
		n = random.randint(1,55)
		if (0 < n and n < 9):
			k = 0
		elif (8 < n and n < 16):
			k = 1
		elif (15 < n and n < 22):
			k = 2
		elif (21 < n and n < 27):
			k = 3
		elif (26 < n and n < 31):
			k = 4
		elif (30 < n and n < 34):
			k = 5
		elif (33 < n and n < 36):
			k = 6
		elif (n == 36):
			k = 7
		elif (35 < n and n < 41):
			k = 8
		elif (40 < n and n < 56):
			k = 9
		if (counter < 21):
			speed = counter/40 + 0.25
		else:
			speed = 0.75
		if (k == 9):
			speed = speed/2
		x = Meat_and_Beer(x, y, speed, screen, k)
		return x


while keep_going:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			keep_going = False

		if (event.type == pygame.KEYDOWN):
			if (event.key == pygame.K_ESCAPE):
				keep_going = False

		# if (event.type == pygame.KEYDOWN):
		# 	if (event.key == pygame.K_SPACE):
		# 		doing_jump = True

		if (event.type == pygame.KEYDOWN):
			if (event.key == pygame.K_a):
				move_left = True
		elif (event.type == pygame.KEYUP):
			if (event.key == pygame.K_a):
				move_left = False

		if (event.type == pygame.KEYDOWN):
			if (event.key == pygame.K_d):
				move_right = True
		elif (event.type == pygame.KEYUP):
			if (event.key == pygame.K_d):
				move_right = False


		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_down = True
		if event.type == pygame.MOUSEBUTTONUP:
			mouse_down = False

	screen.fill((255,255,255))	

	if (mouse_down and game_start == 0):
		(mx, my) = pygame.mouse.get_pos()
		if (Game.check_game_start(mx,my)):
			game_start = 1

	if (game_start == 0):
		Game.draw_main_menu(screen)

	if (game_over == False and check_game_over == False and game_start == 1):
		if (counter == 1):								#start ( when counter == 1 )
			meat_and_beer[counter] = Game.random()
			chekanov[0] = Chekanov(360, 640, 0, screen)
			T = time.time()
			counter += 1


		if (time.time() > (T + timer)):				#add new meat or beer
			meat_and_beer[counter] = Game.random()
			T = time.time()
			if (counter < 21):
				timer = -0.1*counter + 3
			else:
				timer = 1
			counter += 1


		for i in meat_and_beer:			#moving of meat or beer
			meat_and_beer[i].move()
			meat_and_beer[i].draw()


		if (time.time() < time_to_beer + 5):							#moving of Chekanov
			Game.timer(screen, (4 - int(time.time() - time_to_beer)))
			if (move_left and move_right == False):
				chekanov[0].move_right()
				chekanov[0].draw_right()
			elif (move_right == False):
				chekanov[0].draw_front()

			if (move_right and move_left == False):
				chekanov[0].move_left()
				chekanov[0].draw_left()
			elif (move_left == False):
				chekanov[0].draw_front()

			if(move_left and move_right):
				chekanov[0].draw_front()

			chekanov[0].update_points(True)
			check_beer = chekanov[0].check_beer()

		elif (check_beer == False):
			if (move_left and move_right == False):
				chekanov[0].move_left()
				chekanov[0].draw_left()
			elif (move_right == False):
				chekanov[0].draw_front()

			if (move_right and move_left == False):
				chekanov[0].move_right()
				chekanov[0].draw_right()
			elif (move_left == False):
				chekanov[0].draw_front()

			if(move_left and move_right):
				chekanov[0].draw_front()

			chekanov[0].update_points(False)
			check_beer = chekanov[0].check_beer()

		if (check_beer == True):
			time_to_beer = time.time()
			check_beer = False


		# if (doing_jump):
		# 	if (to == 1):
		# 		t = time.time() - 0.001
		# 		to = 0
		# 	chekanov[0].jump(t)
		# 	if (chekanov[0].y < 640):
		# 		doing_jump = True
		# 	else:
		# 		doing_jump = False
		# 		to = 1


		if (Chekanov.update_points(chekanov[0], False)):	#update points
			n = random.randint(0, 5)
			time_picture = time.time()
		if (time.time() < time_picture + 1):				
			Game.draw_picture_about_food(screen, n)

		for i in meat_and_beer:								#check game over
			if (Game.check_game_over(i)):
				check_game_over = Game.check_game_over(i)
				Game.delete(i)
				break

		chekanov[0].draw_points()							
		Game.check_delete()


	if (check_game_over == True or game_over == True):				#when game ended ( resume menu )
		Game.game_over_draw(screen)
		if (mouse_down):
			(mx, my) = pygame.mouse.get_pos()
			if (Game.game_over(mx, my) == False):
				counter = 1
				timer = 3 
				T = time.time()
				time_to_beer = time.time() - 5
				meat_and_beer = {}
				chekanov = {}
			check_game_over = game_over = Game.game_over(mx, my)
		else:
			check_game_over = game_over = Game.game_over(0, 0)


	pygame.display.update()
pygame.quit()