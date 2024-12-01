import pygame,math,random

pygame.display.init()
pygame.font.init()

size = (512,512)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("OPENS THE DOOR")

font = pygame.font.SysFont("Times New Roman", 64, True)


def get_polygon_points(theta,n,length):
    points = []
    slice_interval = (360/n)*0.01745
    theta_offset = theta*0.01745
    for i in range(n):
        i = i+1
        x = math.cos(slice_interval*i+theta_offset)*length
        y = math.sin(slice_interval*i+theta_offset)*length
        points.append((x,y))
    return points

angle = 0
sides = 9
line_thickness = 10
t_switch = False
length = 150
l_switch = False
max_length = 300
pnts = get_polygon_points(angle,sides,length)
while True:
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.fill((0,0,0))

    for p in pnts:
        x = p[0]+size[0]//2
        y = p[1]+size[1]//2
        #pygame.draw.circle(screen, (255,0,0), (x,y), 5)
        for q in pnts:
            x2 = q[0]+size[0]//2
            y2 = q[1]+size[1]//2
            pygame.draw.line(screen, (255,0,0), (x,y), (x2,y2), line_thickness//5)

    if line_thickness <= 5 or line_thickness >= 25: 
        t_switch = not t_switch
    if t_switch:
        line_thickness += 1
    else:
        line_thickness -= 1

    angle = (angle+1)%360

    pnts = get_polygon_points(angle,sides,length)
    

    layers = 30
    for i in range(layers):
        c = ((255/layers)*i,0,0)
        if i%2==0:
            c = (0,0,0)
        top_title = font.render("NONAGON",True,c)
        top_rect = top_title.get_rect(center=(size[0]/2, 100-i*2))
        top_rect.y = max(top_rect.y,0)

        bottom_title = font.render("INFINITY",True,c)
        bottom_rect = bottom_title.get_rect(center=(size[0]/2, size[1]-50-i*2))
        bottom_rect.y = min(bottom_rect.y,size[1])


        screen.blit(top_title,top_rect)
        screen.blit(bottom_title,bottom_rect)

    pygame.display.flip()
