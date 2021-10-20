import pygame,sys, pymunk




def create_apple(space ,pos):
    body = pymunk.Body(1,100,body_type = pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body,50)
    space.add(body,shape)
    return shape


def draw_apples(apples):
    for apple in apples:
        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)
        apple_rect =apple_surface.get_rect(center = (pos_x,pos_y))
        screen.blit(apple_surface,apple_rect)

def static_ball(space,pos):
    body = pymunk.Body(body_type = pymunk.Body.STATIC) #static body therefore don't need mass and inertia in consideration
    body.position = pos
    shape = pymunk.Circle(body,50)
    space.add(body,shape)
    return shape


def draw_static_ball(balls):
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        pygame.draw.circle(screen,(0,0,0),(pos_x , pos_y),50)









pygame.init() # initialising pygame

screen = pygame.display.set_mode((800,800)) # creating the display window
clock = pygame.time.Clock()  # creating game clock
space = pymunk.Space()
space.gravity = (0,100)
apple_surface = pygame.image.load('apple.png')
apples =[]


balls = []
balls.append(static_ball(space,(500,500)))
balls.append(static_ball(space,(250,600)))


while True: #Game loop so that it stays for infinite time
    for event in pygame.event.get(): #checking for input
        if event.type == pygame.QUIT: # input to close the game
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            apples.append(create_apple(space,event.pos))


    screen.fill((217,217,217)) #background colour, RGB
    draw_apples(apples)
    draw_static_ball(balls)
    space.step(1/50)



    pygame.display.update() #rendering the frame
    clock.tick(120)  #limiting the frames per second to 120
    
    #Gravity space simulation done














