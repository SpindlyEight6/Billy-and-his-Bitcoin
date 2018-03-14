# --- Import The Stuff ---
import pygame

# --- Start Pygame ---
pygame.init()

# --- Game Screen Stuff ---
display_width = 800
display_height = 800
display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Billy and his Bitcoin')

# --- Game Clock ---
clock = pygame.time.Clock()

# --- Vars ---
crashed = False

# --- Colors ---
GRAY = (100,100,100)

# --- Bitcoin Img Stuff ---
bitcoinImg = pygame.image.load('bitcoin.png')

# --- Set Icon For Game ---
pygame.display.set_icon(bitcoinImg)

# --- Draw The Bitcoin ---
def bitcoinDraw(x,y):
	display.blit(bitcoinImg,(x,y))

x = (588)
y = (212)

# --- Main Loop ---
while not crashed:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			print (pos)
	# --- Setting The Backgrond Color ---
	display.fill(GRAY)	

	# --- Darw Bitcoin On Screen ---
	bitcoinDraw(x,y)
	
	
	# --- Update The Screen ---
	pygame.display.update()
	clock.tick(60)
		
# --- Ends The Game ---
pygame.quit()
quit()	
