import pygame

dis = pygame.display.set_mode((500, 400))
pygame.display.update()
pygame.display.set_caption('Змейка от Skillbox')

game_over = False

while not game_over:
for event in pygame.event.get():
if event.type == pygame.QUIT:
game_over = True
pygame.quit()

x1 = dis_width / 2
y1 = dis_height / 2
snake_block = 10
x1_change = 0
y1_change = 0

clock = pygame.time.Clock()
snake_speed = 15

font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
mesg = font_style.render(msg, True, color)
dis.blit(mesg, [dis_width / 2, dis_height / 2])

def gameLoop():
game_over = False
game_close = False
x1 = dis_width / 2
y1 = dis_height / 2
x1_change = 0
y1_change = 0

foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0

x1_change = snake_block
y1_change = 0

y1_change = -snake_block
x1_change = 0

y1_change = snake_block
x1_change = 0

game_close = True
x1 += x1_change
y1 += y1_change
dis.fill(white)
pygame.display.update()