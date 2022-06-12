import sys, pygame, random, math

pygame.init()

screen = pygame.display.set_mode((1920,1080))

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green=(0,255,0)
titleFont = pygame.font.SysFont('Comic Sans MS', 120)
midFont = pygame.font.SysFont('Comic Sans MS', 90)
subTitleFont = pygame.font.SysFont('Comic Sans MS', 60)
smallFont = pygame.font.SysFont('Comic Sans MS', 30)
    
def main():
    prevStats = ("easy",0,0)
    
    
    titleScreen()
    
    while True:
        difficulty = settingsScreen(prevStats)
        prevStats = gameScreen(difficulty)
        
        
        
        

def titleScreen():
    
    titleCard = titleFont.render("Novaaks 3.0",True,white)
    titleRect = titleCard.get_rect()
    titleRect.center = (960,540)
    
    subCard = smallFont.render("[Click to Continue]",True,white)
    subRect = subCard.get_rect()
    subRect.center = (960,900)
    
    pygame.event.get() 
    while pygame.mouse.get_pressed(3) [0] == False:
        screen.fill(black)
        
        pygame.draw.rect(screen,green,titleRect)
        pygame.draw.rect(screen,green,subRect)
        
        screen.blit(titleCard, titleRect)
        screen.blit(subCard, subRect)
        
        pygame.display.flip()
        pygame.event.get() 


def settingsScreen(prevStats):
    
    texts = []
    textsRect = []
    
    difficulty = prevStats[0]
    
    
    texts.append(titleFont.render("Novaaks 3.0",True,white))
    textsRect.append(texts[0].get_rect())
    textsRect[0].center = (960,100)

    texts.append(midFont.render("Difficulty",True,white))
    textsRect.append(texts[1].get_rect())
    textsRect[1].center = (480,220)    
    
    texts.append(midFont.render("Statistics",True,white))
    textsRect.append(texts[2].get_rect())
    textsRect[2].center = (1440,220)    
    
    texts.append(midFont.render("Start",True,white))
    textsRect.append(texts[3].get_rect())
    textsRect[3].center = (960,950)    
    
    texts.append(subTitleFont.render("Easy",True,white))
    textsRect.append(texts[4].get_rect())
    textsRect[4].center = (540,350)
    
    texts.append(subTitleFont.render("Medium",True,white))
    textsRect.append(texts[5].get_rect())
    textsRect[5].center = (540,450)
    
    texts.append(subTitleFont.render("Hard",True,white))
    textsRect.append(texts[6].get_rect())
    textsRect[6].center = (540,550)   
    
    texts.append(subTitleFont.render("Quit",True,white))
    textsRect.append(texts[7].get_rect())
    textsRect[7].center = (1700,950)
    
    texts.append(subTitleFont.render(prevStats[0],True,white))
    textsRect.append(texts[8].get_rect())
    textsRect[8].center = (1440,350)

    if prevStats [1] != 0:
        
        texts.append(subTitleFont.render("Hits: " + str(prevStats[1]),True,white))
        textsRect.append(texts[9].get_rect())
        textsRect[9].center = (1440,500)
        
        
    pygame.event.wait(1000)
    pygame.event.get() 
    

    easyRect = pygame.Rect(290,320,600,60)
    
    midRect = pygame.Rect(290,420,600,60)
    
    hardRect = pygame.Rect(290,520,600,60)
    
    
    while True:
       
        screen.fill(black)
                
        for i in range(len(texts)):
            
            if i == 3:
                pygame.draw.rect(screen,(0,200,0),textsRect[i])
            if i == 7:
                pygame.draw.rect(screen,red,textsRect[7])
            else:
                pygame.draw.rect(screen,green,textsRect[i])
            
            screen.blit(texts[i],textsRect[i])
            
        pygame.draw.circle(screen,white,(325,350),30)
        pygame.draw.circle(screen,white,(325,450),30)
        pygame.draw.circle(screen,white,(325,550),30)
        
        if difficulty == "easy":
            pygame.draw.circle(screen,red,(325,350),30)
        elif difficulty == "medium":
            pygame.draw.circle(screen,red,(325,450),30)
        elif difficulty == "hard":
            pygame.draw.circle(screen,red,(325,550),30)

        pygame.display.flip()
        
        pygame.event.get()

        if pygame.mouse.get_pressed(3) [0] == True:
            clickLoc = pygame.mouse.get_pos()
        
        
            if easyRect.collidepoint(clickLoc) == True:
                difficulty = "easy"
            elif midRect.collidepoint(clickLoc) == True:
                difficulty = "medium"
            elif hardRect.collidepoint(clickLoc) == True:
                difficulty = "hard"
            elif textsRect[3].collidepoint(clickLoc) == True:
                break
            elif textsRect[7].collidepoint(clickLoc) == True:
                pygame.quit()
                sys.exit()

    return difficulty

def gameScreen(difficulty):
    clicks = 0
    hits = 0
    
    
    if difficulty == "easy":
        size = 50
        time = 3000
    elif difficulty == "medium":
        size = 40
        time = 750
    elif difficulty == "hard":
        size = 10
        time = 300

    i = 10*3000
    
    clock = pygame.time.Clock()
    
    while i > 0:
        randX = random.randrange(size,1921-size)
        randY = random.randrange(size,1081-size)       
       
        msPassed = 0
        while msPassed < time:
            screen.fill(black)

            pygame.draw.circle(screen,red,(randX,randY),size)
            pygame.display.flip()
            
            pygame.event.get()
            if pygame.mouse.get_pressed(3) [0] == True:
                clickLoc = pygame.mouse.get_pos()
            
                if pygame.Rect(randX - size,randY - size,2*size,2*size).collidepoint(clickLoc) == True:
                    hits += 1

                    break
            
            pygame.event.clear()
            pygame.event.wait(100)
            clock.tick()
            msPassed += clock.get_time()
        
        i -= msPassed
        
    return difficulty, hits, clicks



main()

    