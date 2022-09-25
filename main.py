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
POTHEIGHT, POTWIDTH = 32, 32
PROMPT_FONT = pygame.font.SysFont('comicsans', 20)

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
TextPanelImage = pygame.transform.scale(TextPanelImage, (150, 150))

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

current_prompt = prompts[random.randrange(0, len(prompts))]

# Brews 
brews = [
    "Calcius - Stimulates bone growth",
    "Jungle Juice - Severely enhances hair growth",
    "B.O. Brew - Alters the smell of bacteria released by the skin",
    "Fung-o-clear - Completely clears the skin for a 24 hour period",
    "Super-sense - Temporarily enhances all five senses",
    "Nightswake - Makes the drinker nocturnal for a day",
    "Carnoscent - Allows the drinker to smell the scent of animals",
    "Bloodlust - Temporarily causes hyper-aggression and enhances physical strength and resilience",
    "Tingle-Be-Gone - Suppresses body irritations",
    "Pig's Belly - Extremely enhances metabolisms",
    "Boulder's Brew - Makes the drinker permanenetly heavier",
    "Invisibrew - Causes the user to switch between invisibility and visibility",
    "Locklimb - When unconcious, the user becomes immovable",
    "Stom-o-clear - Clears the stomach",
    "Clover's Charm - Bestows the user with "
]

# Draw 
def draw_window():
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
    WIN.blit(TextPanelImage, (600, 10))

    display_prompt()

    pygame.display.update()

# Display the current prompt
def display_prompt():
    prompt_text = PROMPT_FONT.render("NPC: " + current_prompt, 1, WHITE)
    WIN.blit(prompt_text, (100, 100))

def change_prompt():
    current_prompt = prompts[random.randrange(0, len(prompts))]

def main():

    addNPC()
    addNPC()
    addNPC()

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    print(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()