# coding: utf-8
#  காந்தள்இயக்கம் 

import math
import random
import pygame
from pygame.locals import *



# pygame
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode(( width, height))
#விசைகள்: டப்ளியு
keys = [False, False, False, False]
# பிளேயர் போஸ்
playerpos = [100, 100]
# காந்தள்இயக்கம் 
acc = [0, 0]
# காந்தள்இயக்கம் 
arrows = []
# தமிழி 
badtimer = 100
badtimer1 = 0
badguys = [[640, 100]]
healthvalue = 194
# தமிழி 
pygame.mixer.init()
# தமிழி 
rabbit_img = pygame.image.load("resources/images/dude.png")
# தமிழி 
grass_img = pygame.image.load("resources/images/grass.png")
castle_img = pygame.image.load("resources/images/castle.png")
# தமிழி 
arrow_img = pygame.image.load('resources/images/bullet.png')
# தமிழி 
badguy_img1 = pygame.image.load("resources/images/badguy.png")
badguy_img = badguy_img1
# தமிழி 
healthbar_img = pygame.image.load("resources/images/healthbar.png")
health_img = pygame.image.load("resources/images/health.png")
# தமிழி 
gameover_img = pygame.image.load("resources/images/gameover.png")
youwin_img = pygame.image.load("resources/images/youwin.png")
# தமிழி 
hit = pygame.mixer.Sound("resources/audio/explode.wav")
enemy = pygame.mixer.Sound("resources/audio/enemy.wav")
shoot = pygame.mixer.Sound("resources/audio/shoot.wav")
hit.set_volume(0.05)
enemy.set_volume(0.05)
shoot.set_volume(0.05)
# தமிழி 
pygame.mixer.music.load('resources/audio/moonlight.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)


'''பிரதான விளையாட்டு வளைய'''
# காந்தள்இயக்கம் 
# இயங்கும்，
# வெளியேறும் குறியீடு。
running = True
exitcode = False
while running:
	# தமிழி 
	screen.fill(0)
	# தமிழி 
	for x in range(width//grass_img.get_width()+1):
		for y in range(height//grass_img.get_height()+1):
			screen.blit(grass_img, (x*100, y*100))
	screen.blit(castle_img, (0, 30))
	screen.blit(castle_img, (0, 135))
	screen.blit(castle_img, (0, 240))
	screen.blit(castle_img, (0, 345))
	# தமிழி 。
	# தமிழி 。
	# தமிழி  。
	position = pygame.mouse.get_pos()
	angle = math.atan2(position[1]-(playerpos[1]+32), position[0]-(playerpos[0]+26))
	playerrot = pygame.transform.rotate(rabbit_img, 360-angle*57.29)
	playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
	screen.blit(playerrot, playerpos1)
	# காந்தள்இயக்கம் 
	# தமிழி 。
	# தமிழி 
	# தமிழி 
	#தமிழி  。
	for bullet in arrows:
		index = 0
		velx = math.cos(bullet[0])*10
		vely = math.sin(bullet[0])*10
		bullet[1] += velx
		bullet[2] += vely
		if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
			arrows.pop(index)
		index += 1
		for projectile in arrows:
			arrow1 = pygame.transform.rotate(arrow_img, 360-projectile[0]*57.29)
			screen.blit(arrow1, (projectile[1], projectile[2]))
	# தமிழி .
	# ஆய்வுbadtimerஅது0，அது இருந்தால்0，ஒரு ate ஐ உருவாக்கி மீட்டமைக்கவும்badtimer。
	# தமிழி  .
	# காந்தள்இயக்கம்  .
	if badtimer == 0:
		badguys.append([640, random.randint(50, 430)])
		badtimer = 100 -(badtimer1*2)
		if badtimer1 >= 35:
			badtimer1 = 35
		else:
			badtimer1 += 5
	index_badguy = 0
	for badguy in badguys:
		if badguy[0] < -64:
			badguys.pop(index_badguy)
		badguy[0] -= 7
		# கோட்டையை வெடிக்கச் செய்யலாம் .
		# இந்த குறியீடு மிகவும் எளிது. X இன் x ஒருங்கிணைப்பு இடமிருந்து 64 க்கும் குறைவாக இருந்தால்,
		# கெட்டவர்களை நீக்கி விளையாட்டின் ஆரோக்கியத்தை குறைக்கவும். குறைப்பு 5 முதல் 20 வரை ஒரு சீரற்ற எண்.
		# நிச்சயமாக நான் விரைந்து சென்று கோட்டையைத் தாக்கும் போது மறைந்துவிட்டேன்
		badrect = pygame.Rect(badguy_img.get_rect())
		badrect.top = badguy[1]
		badrect.left = badguy[0]
		if badrect.left < 64:
			hit.play()
			healthvalue -= random.randint(5, 20)
			badguys.pop(index_badguy)
		# மோதல்களைச் சரிபார்க்க அனைத்து பேட்ஸ்கள் மற்றும் அனைத்து அம்புகள் வழியாக சுழற்சி.
		# அது மோதினால், delete ஐ நீக்கு, அம்புக்குறியை நீக்கி, துல்லிய மாறிக்கு 1 ஐச் சேர்க்கவும்.
		# பயன்படுத்தவும்PyGameஇரண்டு செவ்வகங்கள் கடக்கிறதா என்று சோதிக்க உள்ளமைக்கப்பட்ட செயல்பாடு.
		index_arrow = 0
		for bullet in arrows:
			bulletrect = pygame.Rect(arrow_img.get_rect())
			bulletrect.left = bullet[1]
			bulletrect.top = bullet[2]
			if badrect.colliderect(bulletrect):
				enemy.play()
				acc[0] += 1
				badguys.pop(index_badguy)
				arrows.pop(index_arrow)
			index_arrow += 1
		index_badguy += 1
	for badguy in badguys:
		screen.blit(badguy_img, badguy)
	# ஒரு டைமரைச் சேர்க்கவும் .
	#பயன்படுத்தவும்PyGameநேரத் தகவலைக் காண்பிக்க இயல்புநிலை அளவு 24 எழுத்துருக்கள்.
	font = pygame.font.Font(None, 24)
	survivedtext = font.render(str((90000-pygame.time.get_ticks())//60000)+":"+
							   str((90000-pygame.time.get_ticks())//1000%60).zfill(2), True, (0,0,0))
	textRect = survivedtext.get_rect()
	textRect.topright=[635,5]
	screen.blit(survivedtext, textRect)
	# கோட்டை ஆரோக்கியத்தை வரையவும் .
	# முதலில் ஒரு முழு சிவப்பு சுகாதார பட்டியை வரையவும். பின்னர் கோட்டையின் ஆரோக்கியத்தின் அடிப்படையில் சுகாதாரப் பட்டியில் பச்சை சேர்க்கவும்.
	screen.blit(healthbar_img, (5, 5))
	for health1 in range(healthvalue):
		screen.blit(health_img, (health1+8, 8))
	# திரையைப் புதுப்பிக்கவும் .
	pygame.display.flip()
	# சில புதிய நிகழ்வுகளைச் சரிபார்த்து, வெளியேறும் கட்டளை இருந்தால் நிரலின் செயல்பாட்டை நிறுத்தவும் .
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		# விசையை அழுத்தியதன் அடிப்படையில் விசை பதிவு வரிசையைப் புதுப்பிக்கவும் .
		if event.type == pygame.KEYDOWN:
			if event.key == K_w:
				keys[0] = True
			elif event.key == K_a:
				keys[1] = True
			elif event.key == K_s:
				keys[2] = True
			elif event.key == K_d:
				keys[3] = True
		if event.type == pygame.KEYUP:
			if event.key == K_w:
				keys[0] = False
			elif event.key == K_a:
				keys[1] = False
			elif event.key == K_s:
				keys[2] = False
			elif event.key == K_d:
				keys[3] = False
		# வீரர் சுட்டியைக் கிளிக் செய்யும் போது, அவர் ஒரு அம்புக்குறியைச் சுடுவார்
		# இந்த குறியீடு சுட்டி சொடுக்கப்பட்டதா என்பதை சரிபார்க்கும். அதைக் கிளிக் செய்தால்,
		#காந்தள்இயக்கம் 
		# இது சுட்டி நிலையைப் பெற்று பிளேயர் மற்றும் கர்சர் நிலையின் அடிப்படையில் அம்பு சுழற்சி கோணத்தைக் கணக்கிடும்.
		# சுழற்சி கோணத்தின் மதிப்பு அம்புகளின் வரிசையில் சேமிக்கப்படுகிறது.
		if event.type == pygame.MOUSEBUTTONDOWN:
			shoot.play()
			position = pygame.mouse.get_pos()
			acc[1] += 1
			arrows.append([math.atan2(position[1]-(playerpos1[1]+32), position[0]-(playerpos1[0]+26)),
						   playerpos1[0]+32, playerpos1[1]+26])
	# மொபைல் பிளேயர்
	if keys[0]:
		playerpos[1] -= 5
	elif keys[2]:
		playerpos[1] += 5
	if keys[1]:
		playerpos[0] -= 5
	elif keys[3]:
		playerpos[0] += 5
	badtimer -= 1
	# வெற்றி / இழப்புக்கான சில அடிப்படை நிபந்தனைகள் இங்கே:
	# நேரம் முடிந்தால் (90 கள்): பின்னர், விளையாட்டை இயக்குவதை நிறுத்தி விளையாட்டின் வெளியீட்டை அமைக்கவும்;
	# கோட்டை அழிக்கப்பட்டால், பின்னர்: விளையாட்டை நிறுத்தி விளையாட்டின் வெளியீட்டை அமைக்கவும்.
	# துல்லியம் எப்போதும் கணக்கிடப்படுகிறது.
	# முதல் if வெளிப்பாடு நேரம் முடிந்ததா என்பதை சரிபார்க்க வேண்டும்.
	# இரண்டாவது கோட்டை அழிக்கப்பட்டுள்ளதா என்று சோதிக்க வேண்டும்.
	# மூன்றாவது உங்கள் துல்லியத்தை கணக்கிடுகிறது.
	#காந்தள்இயக்கம் 
	# அதன்பிறகு, ஒரு if வெளிப்பாடு நீங்கள் வென்றிருக்கிறீர்களா அல்லது இழந்தீர்களா என்பதைச் சரிபார்த்து, அதனுடன் தொடர்புடைய படத்தைக் காண்பிக்கும்。
	if pygame.time.get_ticks() >= 90000:
		running = False
		exitcode = True
	if healthvalue <= 0:
		running = False
		exitcode = False
	if acc[1] != 0:
		accuracy = acc[0]*1.0/acc[1]*100
		accuracy = ("%.2f" % accuracy)
	else:
		accuracy = 0
if exitcode == False:
	pygame.font.init()
	font = pygame.font.Font(None, 24)
	text = font.render("Accuracy: "+str(accuracy)+"%", True, (255,0,0))
	textRect = text.get_rect()
	textRect.centerx = screen.get_rect().centerx
	textRect.centery = screen.get_rect().centery+24
	screen.blit(gameover_img, (0, 0))
	screen.blit(text, textRect)
else:
	pygame.font.init()
	font = pygame.font.Font(None, 24)
	text = font.render("Accuracy: "+accuracy+"%", True, (0,255,0))
	textRect = text.get_rect()
	textRect.centerx = screen.get_rect().centerx
	textRect.centery = screen.get_rect().centery+24
	screen.blit(youwin_img, (0,0))
	screen.blit(text, textRect)
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
	pygame.display.flip()
