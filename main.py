# Imports
import random
import pygame
import os

pygame.font.init()

# Constant Variables
WIDTH, HEIGHT = 900, 500
BGHEIGHT, BGWIDTH = 620*1.46, 360*1.39
SHOPHEIGHT,SHOPWIDTH = 128*3.5,60*3.5
NPCHEIGHT, NPCWIDTH = 32*4, 32*4
POTHEIGHT, POTWIDTH = 32*2, 32*2
PROMPT_FONT = pygame.font.SysFont('comicsans', 17)
BOOK_FONT = pygame.font.SysFont('times', 20)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRASS_FILL = (1,23,28)

# Pygame Setup
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SBUHacks 2022")
FPS = 60

# Images
ShopImage = pygame.image.load(os.path.join('Assets', 'shop.png'))
ShopImage = pygame.transform.scale(ShopImage,(SHOPHEIGHT,SHOPWIDTH))

BackgroundImage = pygame.image.load(os.path.join('Assets', 'background.png'))
BackgroundImage = pygame.transform.scale(BackgroundImage, (BGHEIGHT, BGWIDTH))

ForegroundImage = pygame.image.load(os.path.join('Assets', 'foregrass.png'))
ForegroundImage = pygame.transform.scale(ForegroundImage, (920, 365))
GrassFillBox = pygame.Rect(0, 460, 900, 50)

TextPanelImage = pygame.image.load(os.path.join('Assets', 'panel.png'))
TextPanelImage = pygame.transform.scale(TextPanelImage, (450, 150))

AvatarPanelImage = pygame.image.load(os.path.join('Assets', 'panel.png'))
AvatarPanelImage = pygame.transform.scale(TextPanelImage, (120, 320))

PotionPanelUI = pygame.image.load(os.path.join('Assets', 'panel.png'))
PotionPanelUI = pygame.transform.scale(PotionPanelUI, (225,400))

Book = pygame.image.load(os.path.join('Assets', 'book.png'))
Book = pygame.transform.scale(Book, (64, 64))

OpenBookUI = pygame.image.load(os.path.join('Assets', 'openbook.png'))
OpenBookUI = pygame.transform.scale(OpenBookUI, (800,450))

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
    npc = queue.pop()
    npcs.append(npc)
    npcs_bl.remove(npc)
    

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
    "They say the winter is coming. What can I use to stay warm?",
    "My friends are saying I am starting to develop an odor. Can you help me?",
    "Mushrooms started appearing on my feet! Do you have something to get rid of it?",
    "Grub doesn't taste as good as it used to. Is there a way you can help?",
    "There is a rat infestation in my house. I need a way to find the source.",
    "My donkey riding exam is tomorrow but my vision is far too poor for me to pass! Help!",
    "My farm animals seem to have grown used to my voice. Is there any way to make my voice boom?",
    "My village is in dire need of watchguards at night but I'm too sleepy at night. How can I help?",
    "I have been unsuccessful in my recent hunting trips. What can I use to fix this?",
    "My town is going to war at nightfall. I need a fast combat boost!",
    "Some wizard made me extremely itchy! Help!",
    "I've got a meat pie eating competition tomorrow and I need a... slight upper hand. Got anything?",
    "My donkey keeps floating! How do I stop it?",
    "My child turned invisible! How can I change them back?!",
    "I keep on sleepwalking! Got a fix?",
    "The river water I drink is making me feel funny...", 
    "I've got a few coins to spare. Got anything to make me luckier "
]

# books 
book_text1 = BOOK_FONT.render("Calcius - Improves bone growth", 1, BLACK)
book_text2 = BOOK_FONT.render("Jungle Juice - Improves hair growth", 1, BLACK)
book_text3 = BOOK_FONT.render("B.O Brew - Alters body growth", 1, BLACK)
book_text4 = BOOK_FONT.render("Fung-o-clear - Clears fungus off skin", 1, BLACK)
book_text5 = BOOK_FONT.render("Super-sense - Improves body senses", 1, BLACK)
book_text6 = BOOK_FONT.render("Nightswake - Keeps user awake", 1, BLACK)
book_text7 = BOOK_FONT.render("Carnoscent - Allows smell of animals", 1, BLACK)
book_text8 = BOOK_FONT.render("Bloodlust - Improves physical ability", 1, BLACK)
book_text9 = BOOK_FONT.render("Tingle-Be-Gone - Removes body itches", 1, BLACK)
book_text10 = BOOK_FONT.render("Pig's Belly - Enhances metabolism", 1, BLACK)
book_text11 = BOOK_FONT.render("Boulder's Brew - Makes user heavier", 1, BLACK)
book_text12 = BOOK_FONT.render("Invisibrew - Lets user toggle invisibility", 1, BLACK)
book_text13 = BOOK_FONT.render("Locklimb - Makes user immovable when", 1, BLACK)
book_text14 = BOOK_FONT.render("Stom-o-clear - Clears the stomach", 1, BLACK)
book_text15 = BOOK_FONT.render("Clover's Charm - Bestows the user with", 1, BLACK)

current_prompt = prompts[random.randrange(0, len(prompts))]

# Draw 
def draw_window(bookOpened):
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

    # Tiny Book
    WIN.blit(Book, (5, 410))

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
        WIN.blit(book_text9, (460,65))
        WIN.blit(book_text10, (460,95))
        WIN.blit(book_text11, (460,125))
        WIN.blit(book_text12, (460,155))
        WIN.blit(book_text13, (460,185))
        WIN.blit(BOOK_FONT.render("asleep", 1, BLACK), (460,205))
        WIN.blit(book_text14, (460,235))
        WIN.blit(book_text15, (460,265))

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
    #prompt_text = PROMPT_FONT.render("NPC: " + current_prompt, 1, BLACK)
    #WIN.blit(prompt_text, (400, 50))

    rect = pygame.Rect(410, 50, 350, 70)
    drawText(WIN, current_prompt, BLACK, rect, PROMPT_FONT)

def change_prompt():
    current_prompt = prompts[random.randrange(0, len(prompts))]

def main():

    addNPC()
    addNPC()
    addNPC()

    clock = pygame.time.Clock()
    run = True
    bookOpened = False
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
                print(x, y)
                
                if(x > 10 and x < 65 and y > 410 and y < 470):
                    bookOpened = not bookOpened

        draw_window(bookOpened)

    pygame.quit()

    

if __name__ == "__main__":
    main()