# Imports
from itertools import count
import random
import pygame
import os
from pygame import mixer

pygame.font.init()

# Constant Variables
WIDTH, HEIGHT = 900, 500
BGHEIGHT, BGWIDTH = 620*1.46, 360*1.39
SHOPHEIGHT,SHOPWIDTH = 128*3.5,60*3.5
NPCHEIGHT, NPCWIDTH = 32*4, 32*4
POTHEIGHT, POTWIDTH = 32*2, 32*2
PROMPT_FONT = pygame.font.SysFont('comicsans', 17)
BOOK_FONT = pygame.font.SysFont('times', 18)
BREW_FONT = pygame.font.SysFont('times', 13, bold = True)
HEADER_FONT = pygame.font.SysFont('times', 45, bold = True)
font = pygame.font.SysFont('Consolas', 30)

correctCounter = 2
wrongCounter = 5
defaultCountTime = 15

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRASS_FILL = (1,23,28)

# Setup
pygame.init()

#screen = pygame.display.set_mode((500,300))

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SBUHacks 2022")
FPS = 60

#timeleft = pygame.time.set_timer(pygame.USEREVENT,30000)

mixer.init()
mixer.music.load("medievalmusic.mp3")
mixer.music.play(-1)

# Images
ShopImage = pygame.image.load(os.path.join('Assets', 'shop.png'))
ShopImage = pygame.transform.scale(ShopImage,(SHOPHEIGHT,SHOPWIDTH))

BackgroundImage = pygame.image.load(os.path.join('Assets', 'background.png'))
BackgroundImage = pygame.transform.scale(BackgroundImage, (BGHEIGHT, BGWIDTH))

BackgroundImageBlur = pygame.image.load(os.path.join('Assets', 'blur.png'))
BackgroundImageBlur = pygame.transform.scale(BackgroundImageBlur, (BGHEIGHT, BGWIDTH))

ForegroundImage = pygame.image.load(os.path.join('Assets', 'foregrass.png'))
ForegroundImage = pygame.transform.scale(ForegroundImage, (920, 365))
GrassFillBox = pygame.Rect(0, 460, 900, 50)

SparkPot1 = pygame.image.load(os.path.join('Assets', 'sparklypot1.png'))
SparkPot1 = pygame.transform.scale(SparkPot1, (POTHEIGHT*2,POTWIDTH*2))

SparkPot2 = pygame.image.load(os.path.join('Assets', 'sparklypot2.png'))
SparkPot2 = pygame.transform.scale(SparkPot2, (POTHEIGHT*2,POTWIDTH*2))

TextPanelImage = pygame.image.load(os.path.join('Assets', 'panel.png'))
TextPanelImage = pygame.transform.scale(TextPanelImage, (450, 150))

AvatarPanelImage = pygame.image.load(os.path.join('Assets', 'panel.png'))
AvatarPanelImage = pygame.transform.scale(TextPanelImage, (120, 320))

PotionPanelUI = pygame.image.load(os.path.join('Assets', 'panel.png'))
PotionPanelUI = pygame.transform.scale(PotionPanelUI, (225,400))

Book = pygame.image.load(os.path.join('Assets', 'book.png'))
Book = pygame.transform.scale(Book, (70, 64))

OpenBookUI = pygame.image.load(os.path.join('Assets', 'openbook.png'))
OpenBookUI = pygame.transform.scale(OpenBookUI, (800,450))

Hourglass = pygame.image.load(os.path.join('Assets', 'hourglass.png'))
Hourglass = pygame.transform.scale(Hourglass, (32, 32))

TimeUI = pygame.image.load(os.path.join('Assets', 'panel.png'))
TimeUI = pygame.transform.scale(TimeUI, (75,85))

# NPCs
AdventurerNPC = pygame.image.load(os.path.join('Assets', 'adventurer_npc.png'))
AdventurerNPC = pygame.transform.scale(AdventurerNPC, (NPCHEIGHT, NPCWIDTH))

AdventurerNPC2 = pygame.image.load(os.path.join('Assets', 'adventurer_05_1.png'))
AdventurerNPC2 = pygame.transform.scale(AdventurerNPC2, (NPCHEIGHT, NPCWIDTH))

BlacksmithNPC = pygame.image.load(os.path.join('Assets', 'blacksmith_00.png'))
BlacksmithNPC = pygame.transform.scale(BlacksmithNPC, (NPCHEIGHT, NPCWIDTH))

CaptainNPC = pygame.image.load(os.path.join('Assets', 'captain_1.png'))
CaptainNPC = pygame.transform.scale(CaptainNPC, (NPCHEIGHT, NPCWIDTH))

DwarfNPC = pygame.image.load(os.path.join('Assets', 'dwarf_1.png'))
DwarfNPC = pygame.transform.scale(DwarfNPC, (NPCHEIGHT, NPCWIDTH))

ElderNPC = pygame.image.load(os.path.join('Assets', 'elder_npc.png'))
ElderNPC = pygame.transform.scale(ElderNPC, (NPCHEIGHT, NPCWIDTH))

JesterNPC = pygame.image.load(os.path.join('Assets', 'jester_00.png'))
JesterNPC = pygame.transform.scale(JesterNPC, (NPCHEIGHT, NPCWIDTH))

KingNPC = pygame.image.load(os.path.join('Assets', 'king_00.png'))
KingNPC = pygame.transform.scale(KingNPC, (NPCHEIGHT, NPCWIDTH))

ShadyNPC = pygame.image.load(os.path.join('Assets', 'shady_guy_00.png'))
ShadyNPC = pygame.transform.scale(ShadyNPC, (NPCHEIGHT, NPCWIDTH))

PaladinNPC = pygame.image.load(os.path.join('Assets', 'paladin_npc.png'))
PaladinNPC = pygame.transform.scale(PaladinNPC, (NPCHEIGHT, NPCWIDTH))

npcs = [AdventurerNPC, AdventurerNPC2, BlacksmithNPC, CaptainNPC, DwarfNPC, ElderNPC, JesterNPC, KingNPC, ShadyNPC, PaladinNPC]
npcs_bl = []
queue = []

def addNPC():
    rand = random.randrange(0, len(npcs));
    queue.append(npcs[rand])
    npcs_bl.append(npcs[rand])
    npcs.remove(npcs[rand])
    
def moveLine():
    npcs.append(queue[0])
    npcs_bl.remove(queue[0])
    del queue[0]
    

# Pots
pot1 = pygame.image.load(os.path.join('Assets', 'pot1.png'))
pot1 = pygame.transform.scale(pot1, (POTHEIGHT, POTWIDTH))

pot2 = pygame.image.load(os.path.join('Assets', 'pot2.png'))
pot2 = pygame.transform.scale(pot2, (POTHEIGHT, POTWIDTH))

pot3 = pygame.image.load(os.path.join('Assets', 'pot3.png'))
pot3 = pygame.transform.scale(pot3, (POTHEIGHT, POTWIDTH))

pot4 = pygame.image.load(os.path.join('Assets', 'pot4.png'))
pot4 = pygame.transform.scale(pot4, (POTHEIGHT, POTWIDTH))

pot5 = pygame.image.load(os.path.join('Assets', 'pot5.png'))
pot5 = pygame.transform.scale(pot5, (POTHEIGHT, POTWIDTH))

pots = [pot1, pot2, pot3, pot4, pot5]

# Prompts
prompts = [
    "Help! I got into a tavern fight and broke my arm.",
    "I am losing hair at a rapid rate... is there a cure?",
    #"They say the winter is coming. What can I use to stay warm?",
    "My friends are saying I am starting to develop an odor. Can you help me?",
    "Mushrooms started appearing on my feet! Do you have something to get rid of it?",
    "Grub doesn't taste as good as it used to. Is there a way you can help?",
    #"My donkey riding exam is tomorrow but my vision is far too poor for me to pass! Help!",
    #"My farm animals seem to have grown used to my voice. Can you change it?",
    "My village needs guards at night but I'm too sleepy at night. How can I help?",
    "I have been unsuccessful in my recent hunting trips. What can I use to fix this?",
    #"There is a rat infestation in my house. I need a way to find the source.",
    "My town is going to war at nightfall. I need a fast combat boost!",
    "Some wizard made me extremely itchy! Help!",
    "I've got a meat pie eating competition tomorrow. Got anything?",
    "My donkey keeps floating! How do I stop it?",
    "My child turned invisible! How can I change them back?!",
    "I keep on sleepwalking! Got a fix?",
    "The river water I drink is making me feel funny...", 
    "I've got a few coins to spare. Got anything to make me luckier?",
    "The village is on fire but we lack water! How can we fix this?!",
    "I want to attend the medieval carnival but I lack the clothes for it. What can I do?",
    "My farm has spoiled from those pesky bugs! How can I recover it?"
]

# Brews 
brews = [
    "Calcius - Improves bone growth",
    "Jungle Juice - Improves hair growth",
    "B.O. Brew - Alters bodily odors",
    "Fung-o-clear - Clears fungus off skin",
    "Super-sense - Improves body senses",
    "Nightswake - Keeps user awake",
    "Carnoscent - Enhances smell of animals",
    "Bloodlust - Improves physical ability",
    "Tingle-Be-Gone - Removes body itches",
    "Pig's Belly - Enhances metabolism",
    "Boulder's Brew - Makes user heavier",
    "Invisibrew - Lets user toggle invisibility",
    "Locklimb - Makes user immovable when",
    "Stom-o-clear - Clears the stomach",
    "Clover's Charm - Gives the user good luck",
    "Aquabrew - Has water that can clear any heat",
    "Porta-clothes - Presents a change of outfits",
    "Miracle Matter - Revives any dead crops"
]

brew_titles = {
    "Calcius - Improves bone growth":"Calcius",
    "Jungle Juice - Improves hair growth":"Jungle Juice",
    "B.O. Brew - Alters bodily odors":"B.O. Brew",
    "Fung-o-clear - Clears fungus off skin":"Fung-o-clear",
    "Super-sense - Improves body senses":"Super-sense",
    "Nightswake - Keeps user awake":"Nightswake",
    "Carnoscent - Enhances smell of animals":"Carnoscent",
    "Bloodlust - Improves physical ability":"Bloodlust",
    "Tingle-Be-Gone - Removes body itches":"Tingle-Be-Gone",
    "Pig's Belly - Enhances metabolism":"Pig's Belly",
    "Boulder's Brew - Makes user heavier":"Boulder's Brew",
    "Invisibrew - Lets user toggle invisibility":"Invisibrew",
    "Locklimb - Makes user immovable when":"Locklimb",
    "Stom-o-clear - Clears the stomach":"Stom-o-clear",
    "Clover's Charm - Gives the user good luck":"Clover's Charm",
    "Aquabrew - Has water that can clear any heat":"Aquabrew",
    "Porta-clothes - Presents a change of outfits":"Porta-clothes",
    "Miracle Matter - Revives any dead crops":"Miracle Matter"
}

brewToPrompt = {
    "Calcius - Improves bone growth":"Help! I got into a tavern fight and broke my arm.",
    "Jungle Juice - Improves hair growth":"I am losing hair at a rapid rate... is there a cure?",
    "B.O. Brew - Alters bodily odors":"My friends are saying I am starting to develop an odor. Can you help me?",
    "Fung-o-clear - Clears fungus off skin":"Mushrooms started appearing on my feet! Do you have something to get rid of it?",
    "Super-sense - Improves body senses":"Grub doesn't taste as good as it used to. Is there a way you can help?",
    "Nightswake - Keeps user awake":"My village needs guards at night but I'm too sleepy at night. How can I help?",
    "Carnoscent - Enhances smell of animals":"I have been unsuccessful in my recent hunting trips. What can I use to fix this?",
    "Bloodlust - Improves physical ability":"My town is going to war at nightfall. I need a fast combat boost!",
    "Tingle-Be-Gone - Removes body itches":"Some wizard made me extremely itchy! Help!",
    "Pig's Belly - Enhances metabolism":"I've got a meat pie eating competition tomorrow. Got anything?",
    "Boulder's Brew - Makes user heavier":"My donkey keeps floating! How do I stop it?",
    "Invisibrew - Lets user toggle invisibility":"My child turned invisible! How can I change them back?!",
    "Locklimb - Makes user immovable when":"I keep on sleepwalking! Got a fix?",
    "Stom-o-clear - Clears the stomach":"The river water I drink is making me feel funny...",
    "Clover's Charm - Gives the user good luck":"I've got a few coins to spare. Got anything to make me luckier?",
    "Aquabrew - Has water that can clear any heat":"The village is on fire but we lack water! How can we fix this?!",
    "Porta-clothes - Presents a change of outfits":"I want to attend the carnival but I lack the clothes. What can I do?",
    "Miracle Matter - Revives any dead crops": "My farm's spoiled from those pesky bugs! How do I recover it?",
    "Angelipitch - Grants user angelic vocals":"I want to act in a play, but I lack the voice for it. Can I improve it?"
}

# books 
book_text1 = BOOK_FONT.render("Calcius - Improves bone growth", 1, BLACK)
book_text2 = BOOK_FONT.render("Jungle Juice - Improves hair growth", 1, BLACK)
book_text3 = BOOK_FONT.render("B.O. Brew - Alters bodily odors", 1, BLACK)
book_text4 = BOOK_FONT.render("Fung-o-clear - Clears fungus off skin", 1, BLACK)
book_text5 = BOOK_FONT.render("Super-sense - Improves body senses", 1, BLACK)
book_text6 = BOOK_FONT.render("Nightswake - Keeps user awake", 1, BLACK)
book_text7 = BOOK_FONT.render("Carnoscent - Enhances smell of animals", 1, BLACK)
book_text8 = BOOK_FONT.render("Bloodlust - Improves physical ability", 1, BLACK)
book_text9 = BOOK_FONT.render("Tingle-Be-Gone - Removes body itches", 1, BLACK)
book_text10 = BOOK_FONT.render("Pig's Belly - Enhances metabolism", 1, BLACK)
book_text11 = BOOK_FONT.render("Boulder's Brew - Makes user heavier", 1, BLACK)
book_text12 = BOOK_FONT.render("Invisibrew - Lets user toggle invisibility", 1, BLACK)
book_text13 = BOOK_FONT.render("Locklimb - Makes user immovable when", 1, BLACK)
book_text14 = BOOK_FONT.render("Stom-o-clear - Clears the stomach", 1, BLACK)
book_text15 = BOOK_FONT.render("Clover's Charm - Gives the user good luck", 1, BLACK)
book_text16 = BOOK_FONT.render("Aquabrew - Has water that can clear", 1, BLACK)
book_text17 = BOOK_FONT.render("Porta-clothes - Presents a change of", 1, BLACK)
book_text18 = BOOK_FONT.render("Miracle Matter - Revives any dead crops", 1, BLACK)
book_text19 = BOOK_FONT.render("Angelipitch - Grants user angelic vocals", 1, BLACK)

currentPotSelection = []
currentPotSelection.append(brews[random.randrange(0, len(brews))])
currentPotSelection.append(brews[random.randrange(0, len(brews))])
currentPotSelection.append(brews[random.randrange(0, len(brews))])
currentPotSelection.append(brews[random.randrange(0, len(brews))])
currentPotSelection.append(brews[random.randrange(0, len(brews))])

rightAnswer = []
rightAnswer.append(currentPotSelection[random.randrange(0, len(currentPotSelection))])

current_prompt = []
current_prompt.append(brewToPrompt[rightAnswer[0]])

def changePotSelection():
    currentPotSelection.pop()
    currentPotSelection.pop()
    currentPotSelection.pop()
    currentPotSelection.pop()
    currentPotSelection.pop()

    currentPotSelection.append(brews[random.randrange(0, len(brews))])
    currentPotSelection.append(brews[random.randrange(0, len(brews))])
    currentPotSelection.append(brews[random.randrange(0, len(brews))])
    currentPotSelection.append(brews[random.randrange(0, len(brews))])
    currentPotSelection.append(brews[random.randrange(0, len(brews))])

    rightAnswer.pop()
    rightAnswer.append(currentPotSelection[random.randrange(0, len(currentPotSelection))])

    current_prompt.pop()
    current_prompt.append(brewToPrompt[rightAnswer[0]])


# Draw 
def draw_window(bookOpened, playingGame, loadingScreen, text, highscore):
    # Always in the back
    WIN.blit(BackgroundImage, (0, 0))
    WIN.blit(ShopImage,(450-(SHOPHEIGHT/2),250))

    

    # Middle ground
    WIN.blit(queue[0], (525, 340)) # 125 pixels apart
    WIN.blit(queue[1], (650, 340))
    WIN.blit(queue[2], (775, 340))
    
    # Always in the front
    WIN.blit(ForegroundImage, (0, 105))
    pygame.draw.rect(WIN, GRASS_FILL, GrassFillBox)

    # Avatar text and photo
    WIN.blit(TextPanelImage, (360, 10))
    WIN.blit(AvatarPanelImage, (780, -100))
    WIN.blit(queue[0], (780, 10))

    # Potions menu
    WIN.blit(PotionPanelUI,(0,20))
    WIN.blit(pot1, (25,130))
    WIN.blit(pot2, (25,200))
    WIN.blit(pot3, (75,250))
    WIN.blit(pot4, (125,130))
    WIN.blit(pot5, (125,200))

    WIN.blit(BREW_FONT.render(brew_titles[currentPotSelection[0]], 1, BLACK), (25,120))
    WIN.blit(BREW_FONT.render(brew_titles[currentPotSelection[1]], 1, BLACK), (125,120))
    WIN.blit(BREW_FONT.render(brew_titles[currentPotSelection[2]], 1, BLACK), (25,190))
    WIN.blit(BREW_FONT.render(brew_titles[currentPotSelection[3]], 1, BLACK), (125,190))
    WIN.blit(BREW_FONT.render(brew_titles[currentPotSelection[4]], 1, BLACK), (75,310))

    # Tiny Book
    WIN.blit(Book, (5, 410))

    # Time
    WIN.blit(TimeUI, (-10,-20))
    WIN.blit(Hourglass, (-5,7))
    #WIN.blit(BREW_FONT.render(timeleft, 1, BLACK),(25,25))
    
    display_prompt()
 
    if bookOpened:
        WIN.blit(OpenBookUI, (50,25))
        WIN.blit(book_text1, (150,65))
        WIN.blit(book_text2, (150,95))
        WIN.blit(book_text3, (150,125))
        WIN.blit(book_text4, (150,155))
        WIN.blit(book_text5, (150,185))
        WIN.blit(book_text6, (150,215))
        WIN.blit(book_text7, (150,245))
        WIN.blit(book_text8, (150,275))
        WIN.blit(book_text16, (150,305))
        WIN.blit(BOOK_FONT.render("any heat", 1, BLACK), (150,325))
        WIN.blit(book_text17, (150,355))
        WIN.blit(BOOK_FONT.render("outfits", 1, BLACK), (150,375))
        WIN.blit(book_text9, (460,65))
        WIN.blit(book_text10, (460,95))
        WIN.blit(book_text11, (460,125))
        WIN.blit(book_text12, (460,155))
        WIN.blit(book_text13, (460,185))
        WIN.blit(BOOK_FONT.render("asleep", 1, BLACK), (460,205))
        WIN.blit(book_text14, (460,235))
        WIN.blit(book_text15, (460,265))
        WIN.blit(book_text18, (460,295))
        WIN.blit(book_text19, (460,325))

    # End Screen
    if not playingGame:
        WIN.fill(BLACK)
        WIN.blit(HEADER_FONT.render("Game Over", 1, WHITE), (345,230))
        WIN.blit(BOOK_FONT.render("Press any button to replay.",1,WHITE),(360,300))

    # Begin Screen 
    if loadingScreen:
        WIN.fill(WHITE)
        WIN.blit(BackgroundImageBlur, (0, 0))
        WIN.blit(pygame.font.SysFont('times', 65, bold = True).render("POTION", 1, WHITE), (325,75))
        WIN.blit(pygame.font.SysFont('times', 55, bold = True).render("MASTER", 1, WHITE), (330,150))
        WIN.blit(HEADER_FONT.render("Press any button to begin.",1,WHITE),(220,300))

        WIN.blit(SparkPot1, (590,90))
        WIN.blit(SparkPot2, (180,90))

    if not loadingScreen:
            WIN.blit(font.render(text, True, (0, 0, 0)), (4, 9))
    else:
        WIN.blit(font.render("HIGHSCORE: " + str(highscore), True, WHITE), (348, 450))

    if not playingGame:
        WIN.blit(font.render("HIGHSCORE: " + str(highscore), True, WHITE), (348, 450))

    pygame.display.update()

# Wrap method
def drawText(surface, text, color, rect, font, aa=False, bkg=None):
    rect = pygame.Rect(rect)
    y = rect.top
    lineSpacing = 3

    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word      
        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text
 

# Display the current prompt
def display_prompt():
    rect = pygame.Rect(410, 50, 350, 70)
    drawText(WIN, current_prompt[0], BLACK, rect, PROMPT_FONT)

def setNewConditions():
    moveLine()
    addNPC()
    changePotSelection()
    

def checkAnswer(potNum):
    if (currentPotSelection[potNum] == rightAnswer[0]):
        print("correct, ", currentPotSelection[potNum])
        setNewConditions()
        return True
    else:
        print("WRONGG", currentPotSelection[potNum])
        setNewConditions()
        return False

def main():

    addNPC()
    addNPC()
    addNPC()

    clock = pygame.time.Clock()
    counter, text = defaultCountTime, str(defaultCountTime).rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    run = True
    playingGame = True
    loadingScreen = True
    bookOpened = False
    score = 0
    highscore = 0
    while run:
        #clock.tick(FPS)

        pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.USEREVENT and (not loadingScreen): 
                counter -= 1
                if counter >= 0:
                    text = str(counter).rjust(3)
                else:
                    playingGame = False
                    if score > highscore:
                        highscore = score

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and loadingScreen:
                loadingScreen = False
            if event.type == pygame.KEYDOWN and (not playingGame):
                playingGame = True
                counter = defaultCountTime + 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
                print(x, y)
                
                if(x > 10 and x < 65 and y > 410 and y < 470):
                    bookOpened = not bookOpened

                if (x>25 and x<90 and y>130 and y<190):
                    outcome = checkAnswer(0)
                    if (outcome):
                        counter += correctCounter
                        score += 1
                    else:
                        counter -= wrongCounter

                if (x>127 and x<187 and y>129 and y<188):
                    outcome = checkAnswer(1)
                    if (outcome):
                        counter += correctCounter
                        score += 1
                    else:
                        counter -= wrongCounter

                if (x>29 and x<80 and y>199 and y<250):
                    outcome = checkAnswer(2)
                    if (outcome):
                        counter += correctCounter
                        score += 1
                    else:
                        counter -= wrongCounter

                if (x>126 and x<182 and y>201 and y<258):
                    outcome = checkAnswer(3)
                    if (outcome):
                        counter += correctCounter
                        score += 1
                    else:
                        counter -= wrongCounter

                if (x>78 and x<133 and y>254 and y<310):
                    outcome = checkAnswer(4)
                    if (outcome):
                        counter += correctCounter
                        score += 1
                    else:
                        counter -= wrongCounter

            # create hover text

        draw_window(bookOpened, playingGame, loadingScreen, text, highscore)

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()