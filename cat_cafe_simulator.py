import pygame
import sys
import math
import random

pygame.init()

WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Whiskers & Paws Cafe")
clock = pygame.time.Clock()

# ── Colors ────────────────────────────────────────────────────────────────
CREAM       = (255, 248, 220)
WARM_BROWN  = (139, 90,  43)
LIGHT_BROWN = (205, 170, 125)
PINK        = (255, 182, 193)
DARK_PINK   = (220, 100, 120)
WHITE       = (255, 255, 255)
BLACK       = (20,  20,  20)
DARK_BROWN  = ( 80,  40,  10)
SOFT_GREEN  = (144, 200, 144)
SOFT_BLUE   = (173, 216, 230)
GOLD        = (255, 215,   0)
ORANGE      = (255, 140,   0)
GRAY        = (180, 180, 180)
LAVENDER    = (200, 180, 230)
CAFE_WALL   = (245, 222, 179)
CAFE_FLOOR  = (210, 180, 140)
TILE_LIGHT  = (220, 195, 155)
TILE_DARK   = (200, 170, 130)
RED         = (220,  60,  60)
TEAL        = ( 70, 180, 160)
DARK_TEAL   = ( 40, 130, 115)
ROSE_GOLD   = (255, 200, 170)
MINT        = (170, 230, 200)
SALMON      = (250, 150, 120)
DARK_GREEN  = (50, 100, 50)
BAG_BROWN   = (139, 69, 19)
BAG_LIGHT   = (160, 100, 40)

# ── Fonts ──────────────────────────────────────────────────────────────────
font_tiny  = pygame.font.SysFont("couriernew", 12, bold=True)
font_small = pygame.font.SysFont("couriernew", 16, bold=True)
font_med   = pygame.font.SysFont("couriernew", 20, bold=True)
font_large = pygame.font.SysFont("couriernew", 28, bold=True)
font_title = pygame.font.SysFont("couriernew", 40, bold=True)

# ── Game States ────────────────────────────────────────────────────────────
STATE_WELCOME   = "welcome"
STATE_CAFE      = "cafe"
STATE_FEED_CAT  = "feed_cat"
STATE_ORDER     = "order"
STATE_COLLECT   = "collect"
STATE_DONE      = "done"
STATE_POEM      = "poem"

# ── Cat Data ────────────────────────────────────────────────────────────────
CAT_DATA = [
    {"name": "Oreo",     "color": (30, 30, 30),    "spot": (WHITE),       "ear": (30, 30, 30),    "pos": (180, 360)},
    {"name": "Mochi",    "color": (255, 220, 180), "spot": (255, 200, 150),"ear": (230, 160, 120), "pos": (320, 390)},
    {"name": "Santa",    "color": (220, 80, 80),   "spot": (255, 150, 150),"ear": (200, 60, 60),   "pos": (470, 360)},
    {"name": "Willow",   "color": (180, 160, 200), "spot": (210, 195, 230),"ear": (160, 140, 180), "pos": (620, 390)},
    {"name": "Espresso", "color": (90, 55, 25),    "spot": (130, 90, 50),  "ear": (70, 40, 15),    "pos": (770, 360)},
]

# ── Food Items (8 options) ─────────────────────────────────────────────────
FOOD_ITEMS = [
    {"name": "Fish",      "color": SOFT_BLUE,   "shape": "fish"},
    {"name": "Tuna",      "color": ORANGE,      "shape": "oval"},
    {"name": "Kibble",    "color": WARM_BROWN,  "shape": "dots"},
    {"name": "Milk",      "color": WHITE,       "shape": "bowl"},
    {"name": "Chicken",   "color": GOLD,        "shape": "bone"},
    {"name": "Salmon",    "color": SALMON,      "shape": "fish"},
    {"name": "Shrimp",    "color": PINK,        "shape": "oval"},
    {"name": "Pumpkin",   "color": ORANGE,      "shape": "bowl"},
]

# ── Menu Items (9 options) ─────────────────────────────────────────────────
MENU_ITEMS = [
    {"name": "Latte",        "color": LIGHT_BROWN,  "price": 180, "shape": "cup"},
    {"name": "Matcha",       "color": SOFT_GREEN,   "price": 160, "shape": "cup"},
    {"name": "Cookie",       "color": WARM_BROWN,   "price": 80,  "shape": "cookie"},
    {"name": "Cheesecake",   "color": CREAM,        "price": 220, "shape": "cake"},
    {"name": "Cat Paw Bun",  "color": PINK,         "price": 120, "shape": "bun"},
    {"name": "Espresso",     "color": DARK_BROWN,   "price": 140, "shape": "cup"},
    {"name": "Mocha",        "color": DARK_TEAL,    "price": 190, "shape": "cup"},
    {"name": "Croissant",    "color": GOLD,         "price": 150, "shape": "cookie"},
    {"name": "Catpuccino",   "color": LAVENDER,     "price": 210, "shape": "cup"},
]

# ── Cat Poems Collection ───────────────────────────────────────────────────
POEMS = [
    {
        "title": "Macavity: The Mystery Cat",
        "author": "T.S. Eliot",
        "lines": [
            "Macavity's a Mystery Cat: he's called the Hidden Paw—",
            "For he's the master criminal who can defy the Law.",
            "He's the bafflement of Scotland Yard, the Flying Squad's despair:",
            "For when they reach the scene of crime—Macavity's not there!",
            "",
            "Macavity, Macavity, there's no one like Macavity,",
            "He's broken every human law, he breaks the law of gravity.",
            "His powers of levitation would make a fakir stare,",
            "And when you reach the scene of crime—Macavity's not there!",
            "",
            "You may seek him in the basement, you may look up in the air—",
            "But I tell you once and once again, Macavity's not there!"
        ]
    },
    {
        "title": "The Naming of Cats",
        "author": "T.S. Eliot",
        "lines": [
            "The Naming of Cats is a difficult matter,",
            "It isn't just one of your holiday games;",
            "You may think at first I'm as mad as a hatter",
            "When I tell you, a cat must have THREE DIFFERENT NAMES.",
            "",
            "First of all, there's the name that the family use daily,",
            "Such as Peter, Augustus, Alonzo or James,",
            "Such as Victor or Jonathan, George or Bill Bailey—",
            "All of them sensible everyday names.",
            "",
            "But I tell you, a cat needs a name that's particular,",
            "A name that's peculiar, and more dignified,",
            "Else how can he keep up his tail perpendicular,",
            "Or spread out his whiskers, or cherish his pride?"
        ]
    },
    {
        "title": "The Owl and the Pussycat",
        "author": "Edward Lear",
        "lines": [
            "The Owl and the Pussy-cat went to sea",
            "In a beautiful pea-green boat,",
            "They took some honey, and plenty of money,",
            "Wrapped up in a five-pound note.",
            "",
            "The Owl looked up to the stars above,",
            "And sang to a small guitar,",
            "'O lovely Pussy! O Pussy, my love,",
            "What a beautiful Pussy you are,'",
            "",
            "Pussy said to the Owl, 'You elegant fowl!'",
            "How charmingly sweet you sing!",
            "O let us be married! too long we have tarried:",
            "But what shall we do for a ring?'"
        ]
    },
    {
        "title": "The Kitten and the Falling Leaves",
        "author": "William Wordsworth",
        "lines": [
            "See the kitten on the wall,",
            "Sporting with the leaves that fall,",
            "Withered leaves—one—two—and three,",
            "Falling from the elder tree.",
            "",
            "Through the calm and frosty air",
            "Of this morning bright and fair,",
            "Eddying round and round they sink",
            "Softly, slowly: one might think,",
            "",
            "From the motions that are made,",
            "That they glittering scythes displayed;",
            "While the kitten, round about,",
            "Sported with them in and out."
        ]
    }
]

# ── Drawing Helpers (scaled up for clarity) ────────────────────────────────
def px_rect(surf, color, x, y, w, h):
    pygame.draw.rect(surf, color, (x, y, w, h))

def px_rect_outline(surf, color, x, y, w, h, thick=2):
    pygame.draw.rect(surf, color, (x, y, w, h), thick)

def draw_pixel_cat(surf, x, y, cat, scale=1, happy=True, tail_wag=False, blink=False):
    s = scale
    body_color = cat["color"]
    ear_color  = cat["ear"]
    spot_color = cat["spot"]
    nose_color = DARK_PINK
    eye_color  = BLACK

    px_rect(surf, body_color, x + 4*s, y + 14*s, 18*s, 14*s)
    px_rect(surf, (min(255, body_color[0]+40), min(255, body_color[1]+40), min(255, body_color[2]+40)), 
            x + 6*s, y + 15*s, 4*s, 4*s)
    px_rect(surf, body_color, x + 5*s, y + 4*s,  16*s, 12*s)
    px_rect(surf, body_color, x + 5*s, y,        5*s, 5*s)
    px_rect(surf, body_color, x + 16*s,y,        5*s, 5*s)
    px_rect(surf, ear_color,  x + 6*s, y + 1*s,  3*s, 3*s)
    px_rect(surf, ear_color,  x + 17*s,y + 1*s,  3*s, 3*s)
    
    eye_w = 3*s
    eye_h = 3*s
    if blink:
        px_rect(surf, body_color, x + 8*s, y + 8*s, 6*s, 2*s)
        px_rect(surf, body_color, x + 15*s, y + 8*s, 6*s, 2*s)
    elif happy:
        for dx in range(eye_w):
            pygame.draw.rect(surf, eye_color, (x + 8*s + dx, y + 8*s, s, s))
            pygame.draw.rect(surf, eye_color, (x + 15*s + dx, y + 8*s, s, s))
        pygame.draw.rect(surf, eye_color, (x + 9*s, y + 7*s, s, s))
        pygame.draw.rect(surf, eye_color, (x + 16*s, y + 7*s, s, s))
    else:
        px_rect(surf, eye_color, x + 8*s,  y + 8*s, 4*s, 4*s)
        px_rect(surf, eye_color, x + 15*s, y + 8*s, 4*s, 4*s)
        px_rect(surf, SOFT_BLUE, x + 9*s,  y + 12*s, 2*s, 3*s)
        px_rect(surf, SOFT_BLUE, x + 16*s, y + 12*s, 2*s, 3*s)
    
    px_rect(surf, nose_color, x + 12*s, y + 10*s, 2*s, 2*s)
    px_rect(surf, GRAY, x + 2*s,  y + 11*s, 5*s, s)
    px_rect(surf, GRAY, x + 19*s, y + 11*s, 5*s, s)
    
    if happy:
        px_rect(surf, BLACK, x + 11*s, y + 12*s, s, s)
        px_rect(surf, BLACK, x + 14*s, y + 12*s, s, s)
        px_rect(surf, BLACK, x + 10*s, y + 13*s, s, s)
        px_rect(surf, BLACK, x + 15*s, y + 13*s, s, s)
    else:
        px_rect(surf, BLACK, x + 10*s, y + 13*s, 6*s, s)
    
    tail_offset = 0
    if tail_wag:
        tail_offset = int(3 * math.sin(pygame.time.get_ticks() * 0.008))
    px_rect(surf, body_color, x + 19*s + tail_offset, y + 20*s, 4*s, 10*s)
    px_rect(surf, body_color, x + 15*s + tail_offset//2, y + 27*s, 4*s, 4*s)
    px_rect(surf, spot_color, x + 8*s, y + 17*s, 8*s, 6*s)
    px_rect(surf, body_color, x + 5*s,  y + 26*s, 5*s, 3*s)
    px_rect(surf, body_color, x + 14*s, y + 26*s, 5*s, 3*s)

def draw_food(surf, x, y, shape, color, size=3):
    s = size
    shadow = (max(0, color[0]-40), max(0, color[1]-40), max(0, color[2]-40))
    if shape == "fish":
        px_rect(surf, shadow, x+3*s+2, y+2*s+2, 10*s, 6*s)
        px_rect(surf, color, x+3*s, y+2*s, 10*s, 6*s)
        px_rect(surf, color, x, y+3*s, 3*s, 4*s)
        px_rect(surf, color, x+13*s, y+1*s, 3*s, 3*s)
        px_rect(surf, color, x+13*s, y+6*s, 3*s, 3*s)
        px_rect(surf, WHITE, x+5*s, y+4*s, 2*s, 2*s)
    elif shape == "bowl":
        px_rect(surf, shadow, x+2*s+2, y+5*s+2, 12*s, 7*s)
        px_rect(surf, color, x+2*s, y+5*s, 12*s, 7*s)
        px_rect(surf, color, x+4*s, y+3*s, 8*s, 2*s)
        px_rect(surf, WHITE, x+4*s, y+5*s, 8*s, 3*s)
    elif shape == "dots":
        px_rect(surf, shadow, x+2*s+2, y+4*s+2, 12*s, 8*s)
        px_rect(surf, color, x+2*s, y+4*s, 12*s, 8*s)
        for dx in range(0, 10, 4):
            for dy in range(0, 6, 3):
                px_rect(surf, DARK_BROWN, x+3*s+dx*s, y+5*s+dy*s, 2*s, 2*s)
    elif shape == "bone":
        px_rect(surf, shadow, x+5*s+2, y+4*s+2, 6*s, 4*s)
        px_rect(surf, color, x+5*s, y+4*s, 6*s, 4*s)
        px_rect(surf, color, x+2*s, y+2*s, 4*s, 4*s)
        px_rect(surf, color, x+10*s, y+2*s, 4*s, 4*s)
    elif shape == "oval":
        px_rect(surf, shadow, x+3*s+2, y+3*s+2, 10*s, 6*s)
        px_rect(surf, color, x+3*s, y+3*s, 10*s, 6*s)
        px_rect(surf, color, x+4*s, y+2*s, 8*s, 1*s)
        px_rect(surf, color, x+4*s, y+9*s, 8*s, 1*s)
    elif shape == "cup":
        px_rect(surf, shadow, x+2*s+2, y+2*s+2, 12*s, 10*s)
        px_rect(surf, color, x+2*s, y+2*s, 12*s, 10*s)
        px_rect(surf, DARK_BROWN, x+2*s, y+2*s, 12*s, 3*s)
        px_rect(surf, WHITE, x+4*s, y+4*s, 3*s, 2*s)
        px_rect(surf, LIGHT_BROWN, x+14*s, y+5*s, 3*s, 5*s)
        px_rect(surf, CAFE_WALL, x+3*s, y+12*s, 10*s, 2*s)
        steam_offset = int(3 * math.sin(pygame.time.get_ticks() * 0.005))
        px_rect(surf, GRAY, x+6*s, y-2*s+steam_offset, 2*s, 2*s)
        px_rect(surf, GRAY, x+9*s, y-1*s+steam_offset, 2*s, 2*s)
    elif shape == "cookie":
        px_rect(surf, shadow, x+2*s+2, y+2*s+2, 12*s, 10*s)
        px_rect(surf, color, x+2*s, y+2*s, 12*s, 10*s)
        for cx, cy in [(4,4),(8,4),(6,7),(10,7)]:
            px_rect(surf, DARK_BROWN, x+cx*s, y+cy*s, 2*s, 2*s)
    elif shape == "cake":
        px_rect(surf, shadow, x+2*s+2, y+4*s+2, 12*s, 8*s)
        px_rect(surf, color, x+2*s, y+4*s, 12*s, 8*s)
        px_rect(surf, WHITE, x+2*s, y+3*s, 12*s, 2*s)
        px_rect(surf, PINK, x+2*s, y+2*s, 12*s, 2*s)
        px_rect(surf, GOLD, x+7*s, y, 2*s, 3*s)
    elif shape == "bun":
        px_rect(surf, shadow, x+2*s+2, y+3*s+2, 12*s, 9*s)
        px_rect(surf, color, x+2*s, y+3*s, 12*s, 9*s)
        px_rect(surf, color, x+4*s, y+1*s, 8*s, 4*s)
        px_rect(surf, DARK_PINK, x+6*s, y+5*s, 2*s, 2*s)
        px_rect(surf, DARK_PINK, x+8*s, y+7*s, 2*s, 2*s)

def draw_pixel_bag(surf, x, y, size=4):
    s = size
    px_rect(surf, BAG_BROWN, x, y, 20*s, 15*s)
    px_rect(surf, BAG_LIGHT, x+2*s, y+2*s, 16*s, 11*s)
    px_rect(surf, DARK_BROWN, x+5*s, y-4*s, 10*s, 5*s)
    px_rect(surf, BAG_BROWN, x+6*s, y-3*s, 8*s, 4*s)
    px_rect(surf, DARK_PINK, x+8*s, y+2*s, 4*s, 4*s)
    px_rect(surf, DARK_PINK, x+5*s, y+4*s, 3*s, 6*s)
    px_rect(surf, DARK_PINK, x+12*s, y+4*s, 3*s, 6*s)
    px_rect(surf, BLACK, x+7*s, y+7*s, 3*s, 3*s)
    px_rect(surf, BLACK, x+12*s, y+7*s, 3*s, 3*s)
    px_rect(surf, DARK_PINK, x+9*s, y+11*s, 2*s, 2*s)
    px_rect(surf, ROSE_GOLD, x+15*s, y+3*s, 2*s, 2*s)

def draw_text_centered(surf, text, font, color, cx, y):
    s = font.render(text, True, color)
    surf.blit(s, (cx - s.get_width()//2, y))

def draw_panel(surf, x, y, w, h, bg=CREAM, border=WARM_BROWN, thick=3, gradient=False):
    if gradient:
        for i in range(h):
            ratio = i / h
            grad_color = (int(bg[0]*(1-ratio) + border[0]*ratio),
                         int(bg[1]*(1-ratio) + border[1]*ratio),
                         int(bg[2]*(1-ratio) + border[2]*ratio))
            pygame.draw.line(surf, grad_color, (x, y+i), (x+w, y+i))
    else:
        pygame.draw.rect(surf, bg, (x, y, w, h))
    pygame.draw.rect(surf, border, (x, y, w, h), thick)
    pygame.draw.rect(surf, DARK_BROWN, (x+4, y+h, w, 4))
    pygame.draw.rect(surf, DARK_BROWN, (x+w, y+4, 4, h))

def draw_button(surf, text, x, y, w, h, bg=TEAL, fg=WHITE, hover=False):
    color = DARK_TEAL if hover else bg
    draw_panel(surf, x, y, w, h, bg=color, border=DARK_BROWN, thick=2)
    draw_text_centered(surf, text, font_small, fg, x + w//2, y + h//2 - 7)

def button_hit(mx, my, x, y, w, h):
    return x <= mx <= x+w and y <= my <= y+h

# ── Particle effects ────────────────────────────────────────────────────────
particles = []
def spawn_particles(x, y, count, color=GOLD):
    for _ in range(count):
        particles.append([x + random.randint(-30, 30),
                         y + random.randint(-30, 30),
                         random.uniform(-1.5, 1.5),
                         random.uniform(-3, -0.8),
                         random.randint(30, 50),
                         color])

def update_particles():
    for p in particles[:]:
        p[0] += p[2]
        p[1] += p[3]
        p[4] -= 1
        if p[4] <= 0:
            particles.remove(p)

def draw_particles(surf):
    for p in particles:
        px_rect(surf, p[5], int(p[0]), int(p[1]), 3, 3)

def draw_sparkles(surf, cx, cy, t):
    for i in range(10):
        angle = t * 3 + i * math.pi / 5
        r = 30 + 6 * math.sin(t * 5 + i)
        sx = int(cx + r * math.cos(angle))
        sy = int(cy + r * math.sin(angle))
        px_rect(surf, GOLD, sx, sy, 5, 5)
        px_rect(surf, WHITE, sx+1, sy+1, 3, 3)

def draw_floating_hearts(surf, x, y):
    t = pygame.time.get_ticks() * 0.005
    for i in range(4):
        offset_x = int(15 * math.sin(t + i))
        offset_y = int(20 * math.sin(t * 2 + i))
        px_rect(surf, DARK_PINK, x + offset_x - 6, y + offset_y - 12, 5, 5)
        px_rect(surf, DARK_PINK, x + offset_x + 1, y + offset_y - 12, 5, 5)
        px_rect(surf, DARK_PINK, x + offset_x - 8, y + offset_y - 8, 16, 6)
        px_rect(surf, DARK_PINK, x + offset_x - 4, y + offset_y - 2, 10, 6)

# ── Cafe Background ─────────────────────────────────────────────────────────
def draw_cafe_bg(surf, time_of_day=0):
    for y in range(HEIGHT):
        if y < 420:
            intensity = 1 - (y / 420)
            wall_color = (int(CAFE_WALL[0] * (0.8 + intensity*0.2)),
                         int(CAFE_WALL[1] * (0.8 + intensity*0.2)),
                         int(CAFE_WALL[2] * (0.8 + intensity*0.2)))
            pygame.draw.line(surf, wall_color, (0, y), (WIDTH, y))
    for row in range(8):
        for col in range(12):
            c = TILE_LIGHT if (row + col) % 2 == 0 else TILE_DARK
            pygame.draw.rect(surf, c, (col*75, 420 + row*45, 75, 45))
            highlight = (min(255, c[0]+30), min(255, c[1]+30), min(255, c[2]+30))
            pygame.draw.rect(surf, highlight, (col*75, 420 + row*45, 75, 4))
    pygame.draw.rect(surf, WARM_BROWN, (0, 400, WIDTH, 30))
    for i in range(25):
        grain_x = i * 40
        pygame.draw.line(surf, DARK_BROWN, (grain_x, 405), (grain_x+25, 415), 2)
    pygame.draw.rect(surf, LIGHT_BROWN, (0, 395, WIDTH, 15))
    pygame.draw.rect(surf, SOFT_BLUE, (650, 70, 180, 130))
    pygame.draw.rect(surf, WHITE, (650, 70, 180, 130), 5)
    pygame.draw.rect(surf, WHITE, (740, 70, 5, 130))
    pygame.draw.rect(surf, WHITE, (650, 130, 180, 5))
    pygame.draw.ellipse(surf, WHITE, (665, 85, 40, 25))
    pygame.draw.ellipse(surf, WHITE, (690, 80, 45, 30))
    pygame.draw.ellipse(surf, WHITE, (790, 105, 30, 20))
    pygame.draw.rect(surf, DARK_BROWN, (40, 150, 230, 15))
    for i, c in enumerate([TEAL, DARK_PINK, SOFT_GREEN, GOLD, LAVENDER]):
        mx = 50 + i * 50
        pygame.draw.rect(surf, c, (mx, 120, 28, 30))
        pygame.draw.rect(surf, DARK_BROWN, (mx, 120, 28, 30), 2)
        pygame.draw.rect(surf, c, (mx+25, 130, 7, 12))
    pygame.draw.rect(surf, DARK_BROWN, (350, 70, 260, 120))
    pygame.draw.rect(surf, (40, 20, 5), (355, 75, 250, 110))
    t = font_med.render("WHISKERS & PAWS", True, GOLD)
    surf.blit(t, (360, 85))
    t2 = font_small.render("Cats  Coffee  Comfort", True, CREAM)
    surf.blit(t2, (390, 120))
    t3 = font_small.render("Est. 2024  ~  Purr-fect Brews", True, GRAY)
    surf.blit(t3, (380, 150))
    pygame.draw.rect(surf, WARM_BROWN, (800, 350, 40, 25))
    for leaf in [(815, 310), (830, 290), (805, 295), (840, 300), (820, 280)]:
        pygame.draw.circle(surf, SOFT_GREEN, leaf, 18)
        pygame.draw.circle(surf, DARK_GREEN, leaf, 9)
    for i in range(6):
        light_x = 120 + i * 140
        pygame.draw.line(surf, BLACK, (light_x, 25), (light_x+25, 50), 3)
        pygame.draw.circle(surf, GOLD, (light_x+12, 48), 8)
        pygame.draw.circle(surf, ORANGE, (light_x+12, 48), 4)

# ── Main Game Class ────────────────────────────────────────────────────────
class CatCafeGame:
    def __init__(self):
        self.reset()
        self.poem_index = 0
        self.poem_scroll = 0

    def reset(self):
        self.state         = STATE_WELCOME
        self.selected_cat  = None
        self.fed_items     = []
        self.cart_items    = []
        self.collected     = False
        self.t             = 0.0
        self.hover         = None
        self.message       = ""
        self.msg_timer     = 0
        self.blink_timer   = 0
        particles.clear()

    def show_message(self, msg):
        self.message = msg
        self.msg_timer = 90

    # ── Welcome Screen ──────────────────────────────────────────────────────
    def draw_welcome(self):
        screen.fill((30, 15, 5))
        for i in range(80):
            sx = (i * 197 + self.t * 10) % WIDTH
            sy = (i * 113 + self.t * 5) % 300
            c = WHITE if i % 3 == 0 else GOLD
            px_rect(screen, c, int(sx), int(sy), 3+(i%2), 3+(i%2))
        draw_panel(screen, 180, 140, 540, 240, bg=(50, 25, 8), border=GOLD, thick=5, gradient=True)
        for i in range(15):
            bx = 195 + i * 42
            px_rect(screen, GOLD if i%2==0 else ORANGE, bx, 145, 12, 12)
            px_rect(screen, GOLD if i%2==0 else ORANGE, bx, 360, 12, 12)
        t1 = font_title.render("WHISKERS & PAWS", True, GOLD)
        screen.blit(t1, (450 - t1.get_width()//2, 180))
        t2 = font_large.render("C  A  F  E", True, ORANGE)
        screen.blit(t2, (450 - t2.get_width()//2, 230))
        t3 = font_med.render("where every cup comes with purrs", True, CREAM)
        screen.blit(t3, (450 - t3.get_width()//2, 270))
        t4 = font_small.render("deluxe pixel edition ✨", True, ROSE_GOLD)
        screen.blit(t4, (450 - t4.get_width()//2, 305))
        cat_x = 430
        cat_y = 390 + int(6 * math.sin(self.t * 2))
        draw_pixel_cat(screen, cat_x, cat_y, CAT_DATA[1], scale=4, happy=True, tail_wag=True)
        draw_sparkles(screen, cat_x + 60, cat_y + 20, self.t)
        mx, my = pygame.mouse.get_pos()
        hov = button_hit(mx, my, 340, 520, 220, 60)
        draw_button(screen, "🐾 ENTER CAFE 🐾", 340, 520, 220, 60, bg=TEAL, hover=hov)
        for i in range(5):
            px = 200 + i * 60
            py = 565 + (i % 2) * 12
            pygame.draw.circle(screen, DARK_BROWN, (px, py), 6)
            pygame.draw.circle(screen, DARK_BROWN, (px+10, py-6), 4)
            pygame.draw.circle(screen, DARK_BROWN, (px+18, py-2), 4)

    # ── Cafe Screen ─────────────────────────────────────────────────────────
    def draw_cafe(self):
        draw_cafe_bg(screen, self.t)
        draw_panel(screen, 0, 0, WIDTH, 60, bg=DARK_BROWN, border=GOLD, thick=3, gradient=True)
        draw_text_centered(screen, "✨ Choose your furry companion ✨", font_large, GOLD, WIDTH//2, 15)
        mx, my = pygame.mouse.get_pos()
        self.blink_timer += 1
        for i, cat in enumerate(CAT_DATA):
            cx, cy = cat["pos"]
            bob = int(5 * math.sin(self.t * 2 + i))
            cat_draw_x = cx - 55
            cat_draw_y = cy - 55 + bob
            hit_box = (cx-60, cy-70, 130, 110)
            hov = button_hit(mx, my, *hit_box)
            if hov:
                pygame.draw.rect(screen, GOLD, hit_box, 0)
                pygame.draw.rect(screen, DARK_BROWN, hit_box, 3)
                draw_floating_hearts(screen, cx, cy)
            blink = (self.blink_timer // 40) % 20 == 0
            draw_pixel_cat(screen, cat_draw_x, cat_draw_y, cat, scale=3,
                           happy=True, tail_wag=True, blink=blink)
            draw_panel(screen, cx-45, cy+55, 90, 28, bg=CREAM, border=WARM_BROWN, thick=2)
            draw_text_centered(screen, cat["name"], font_med, DARK_BROWN, cx, cy+66)
        
        # Poem button
        poem_btn_hov = button_hit(mx, my, WIDTH-140, HEIGHT-60, 120, 40)
        draw_button(screen, "📖 POEMS", WIDTH-140, HEIGHT-60, 120, 40, bg=LAVENDER, hover=poem_btn_hov)
        
        draw_panel(screen, 20, 620, 260, 70, bg=CREAM, border=WARM_BROWN, thick=3)
        screen.blit(font_small.render("😻 Click a cat to start!", True, RED), (30, 630))
        screen.blit(font_small.render("Feed them yummy treats", True, DARK_BROWN), (30, 650))
        screen.blit(font_small.render("🐟 🥛 🍗", True, WARM_BROWN), (30, 670))
        update_particles()
        draw_particles(screen)
        
        # Handle poem button click
        if poem_btn_hov and pygame.mouse.get_pressed()[0]:
            self.state = STATE_POEM
            self.poem_scroll = 0

    # ── Feed Cat Screen (fixed overlapping) ────────────────────────────────
    def draw_feed_cat(self):
        draw_cafe_bg(screen)
        cat = self.selected_cat
        draw_panel(screen, 0, 0, WIDTH, 60, bg=DARK_BROWN, border=GOLD, thick=3, gradient=True)
        draw_text_centered(screen, f"🍽️ Feed {cat['name']} (Fed: {len(self.fed_items)} items) 🍽️", 
                          font_med, GOLD, WIDTH//2, 15)
        
        # Cat positioned at left side to avoid overlap
        cx, cy = 180, 220
        bob = int(5 * math.sin(self.t * 2))
        draw_pixel_cat(screen, cx-90, cy-70+bob, cat, scale=5,
                       happy=len(self.fed_items)>0, tail_wag=True)
        # Show fed food icons next to cat
        for idx, food in enumerate(self.fed_items[-6:]):
            draw_food(screen, cx+50 + idx*40, cy+50, food["shape"], food["color"], size=2)
        if len(self.fed_items) > 0:
            draw_sparkles(screen, cx+40, cy-30, self.t)
            draw_floating_hearts(screen, cx, cy)
        
        # Food grid placed clearly below and to the right of cat
        grid_x_start = 60
        grid_y_start = 400
        cols = 4
        item_w = 110
        item_h = 110
        mx, my = pygame.mouse.get_pos()
        draw_panel(screen, 30, 370, 840, 260, bg=CREAM, border=WARM_BROWN, thick=4)
        draw_text_centered(screen, "~~ TREATS MENU ~~", font_large, WARM_BROWN, WIDTH//2, 385)
        for i, food in enumerate(FOOD_ITEMS):
            row = i // cols
            col = i % cols
            fx = grid_x_start + col * (item_w + 15)
            fy = grid_y_start + row * (item_h + 15)
            if fy + item_h > 620: continue
            hov = button_hit(mx, my, fx-5, fy-5, item_w, item_h)
            if hov:
                pygame.draw.rect(screen, GOLD, (fx-10, fy-10, item_w+10, item_h+10), 0)
            draw_panel(screen, fx-5, fy-5, item_w, item_h,
                       bg=WHITE if not hov else (255, 255, 200),
                       border=WARM_BROWN, thick=3)
            draw_food(screen, fx+15, fy+15, food["shape"], food["color"], size=3)
            draw_text_centered(screen, food["name"], font_med, DARK_BROWN, fx+50, fy+85)
        
        btn_done_hov = button_hit(mx, my, 620, 650, 180, 50)
        btn_clear_hov = button_hit(mx, my, 100, 650, 180, 50)
        if len(self.fed_items) > 0:
            draw_button(screen, "✅ DONE FEEDING", 620, 650, 180, 50, bg=TEAL, hover=btn_done_hov)
        else:
            pygame.draw.rect(screen, GRAY, (620, 650, 180, 50))
            draw_text_centered(screen, "Feed at least one!", font_med, DARK_BROWN, 710, 670)
        draw_button(screen, "🗑️ CLEAR ALL", 100, 650, 180, 50, bg=DARK_PINK, hover=btn_clear_hov)
        if self.msg_timer > 0:
            self.msg_timer -= 1
            draw_text_centered(screen, self.message, font_med, RED, WIDTH//2, 660)

    # ── Order Screen (Cart) ─────────────────────────────────────────────────
    def draw_order(self):
        draw_cafe_bg(screen)
        cat = self.selected_cat
        draw_panel(screen, 0, 0, WIDTH, 60, bg=DARK_BROWN, border=GOLD, thick=3, gradient=True)
        draw_text_centered(screen, f"📋 {cat['name']} asks: What would you like? 📋", font_med, GOLD, WIDTH//2, 15)
        bob = int(4 * math.sin(self.t * 2))
        draw_pixel_cat(screen, 30, 70+bob, cat, scale=3, happy=True, tail_wag=True)
        pygame.draw.rect(screen, WHITE, (120, 65, 280, 60))
        pygame.draw.rect(screen, DARK_BROWN, (120, 65, 280, 60), 3)
        pygame.draw.polygon(screen, WHITE, [(120,95),(100,105),(120,110)])
        pygame.draw.polygon(screen, DARK_BROWN, [(120,95),(100,105),(120,110)], 2)
        screen.blit(font_small.render("Meow! Here's our full menu:", True, DARK_BROWN), (130, 80))
        screen.blit(font_small.render("Add items to your order!", True, WARM_BROWN), (130, 105))
        menu_x_start = 40
        menu_y_start = 150
        cols = 3
        item_w = 200
        item_h = 150
        mx, my = pygame.mouse.get_pos()
        draw_panel(screen, 20, 130, 640, 480, bg=CREAM, border=WARM_BROWN, thick=4)
        draw_text_centered(screen, "🐾 TODAY'S SPECIALS 🐾", font_large, WARM_BROWN, 340, 145)
        for i, item in enumerate(MENU_ITEMS):
            row = i // cols
            col = i % cols
            ix = menu_x_start + col * (item_w + 15)
            iy = menu_y_start + row * (item_h + 15)
            if iy + item_h > 590: continue
            hov = button_hit(mx, my, ix, iy, item_w, item_h)
            border_color = TEAL if hov else WARM_BROWN
            draw_panel(screen, ix, iy, item_w, item_h, bg=WHITE if not hov else (255, 255, 220),
                      border=border_color, thick=3)
            draw_food(screen, ix+25, iy+15, item["shape"], item["color"], size=3)
            draw_text_centered(screen, item["name"], font_med, DARK_BROWN, ix+100, iy+95)
            draw_text_centered(screen, f"₹{item['price']}", font_small, TEAL, ix+100, iy+120)
            add_hov = button_hit(mx, my, ix+140, iy+110, 50, 30)
            draw_button(screen, "+", ix+140, iy+110, 50, 30, bg=SOFT_GREEN, hover=add_hov)
        draw_panel(screen, 680, 130, 200, 480, bg=CREAM, border=DARK_BROWN, thick=4)
        draw_text_centered(screen, "🛒 YOUR ORDER", font_med, DARK_BROWN, 780, 145)
        pygame.draw.line(screen, DARK_BROWN, (690, 165), (870, 165), 3)
        y_offset = 175
        total = 0
        for idx, (item_name, qty) in enumerate(self.cart_items):
            item_data = next((i for i in MENU_ITEMS if i["name"] == item_name), None)
            if item_data:
                price = item_data["price"]
                total += price * qty
                text = font_tiny.render(f"{item_name} x{qty}", True, DARK_BROWN)
                screen.blit(text, (690, y_offset))
                price_text = font_tiny.render(f"₹{price*qty}", True, TEAL)
                screen.blit(price_text, (690, y_offset+15))
                rem_hov = button_hit(mx, my, 840, y_offset, 35, 25)
                pygame.draw.rect(screen, RED if rem_hov else DARK_PINK, (840, y_offset, 35, 25))
                draw_text_centered(screen, "X", font_tiny, WHITE, 857, y_offset+5)
                y_offset += 45
                if y_offset > 550: break
        draw_text_centered(screen, f"Total: ₹{total}", font_med, TEAL, 780, y_offset+15)
        checkout_hov = button_hit(mx, my, 700, y_offset+50, 160, 45)
        draw_button(screen, "🐱 CHECKOUT", 700, y_offset+50, 160, 45, bg=TEAL, hover=checkout_hov)
        clear_hov = button_hit(mx, my, 700, y_offset+105, 160, 35)
        draw_button(screen, "Clear Cart", 700, y_offset+105, 160, 35, bg=DARK_PINK, hover=clear_hov)

    # ── Collect Screen ─────────────────────────────────────────────────────
    def draw_collect(self):
        draw_cafe_bg(screen)
        cat = self.selected_cat
        draw_panel(screen, 0, 0, WIDTH, 60, bg=DARK_BROWN, border=GOLD, thick=3, gradient=True)
        draw_text_centered(screen, "🎉 Your order is ready! 🎉", font_large, GOLD, WIDTH//2, 15)
        bob = int(4 * math.sin(self.t * 2))
        draw_pixel_cat(screen, 100, 160+bob, cat, scale=5, happy=True, tail_wag=True)
        draw_sparkles(screen, 240, 200, self.t)
        mx, my = pygame.mouse.get_pos()
        if not self.collected:
            draw_panel(screen, 420, 100, 440, 420, bg=WHITE, border=DARK_BROWN, thick=4)
            draw_text_centered(screen, "🧾 RECEIPT 🧾", font_large, DARK_BROWN, 640, 120)
            pygame.draw.line(screen, DARK_BROWN, (430, 150), (850, 150), 3)
            y_offset = 165
            total = 0
            for item_name, qty in self.cart_items:
                item_data = next((i for i in MENU_ITEMS if i["name"] == item_name), None)
                if item_data:
                    price = item_data["price"]
                    subtotal = price * qty
                    total += subtotal
                    text = font_med.render(f"{item_name} x{qty} = ₹{subtotal}", True, DARK_BROWN)
                    screen.blit(text, (440, y_offset))
                    y_offset += 35
            draw_text_centered(screen, f"Grand Total: ₹{total}", font_large, TEAL, 640, y_offset+20)
            draw_text_centered(screen, f"Treats fed: {len(self.fed_items)}", font_med, DARK_PINK, 640, y_offset+60)
            hov = button_hit(mx, my, 540, y_offset+110, 200, 50)
            draw_button(screen, "🐾 COLLECT & PAY", 540, y_offset+110, 200, 50, bg=TEAL, hover=hov)
        else:
            draw_panel(screen, 420, 100, 440, 420, bg=WHITE, border=DARK_BROWN, thick=4)
            draw_text_centered(screen, "🎁 YOUR ORDER IS PACKED 🎁", font_large, DARK_BROWN, 640, 120)
            pygame.draw.line(screen, DARK_BROWN, (430, 150), (850, 150), 3)
            draw_pixel_bag(screen, 530, 170, size=4)
            msg = f"Served by {cat['name']}  ^._.^"
            draw_text_centered(screen, msg, font_large, TEAL, 640, 320)
            draw_text_centered(screen, "Thank you for your purchase!", font_med, DARK_PINK, 640, 370)
            hov = button_hit(mx, my, 540, 430, 200, 50)
            draw_button(screen, "🐱 CONTINUE", 540, 430, 200, 50, bg=DARK_PINK, hover=hov)
        update_particles()
        draw_particles(screen)

    # ── Poem Screen (new) ──────────────────────────────────────────────────
    def draw_poem(self):
        draw_cafe_bg(screen)
        poem = POEMS[self.poem_index]
        # Panel
        panel_w, panel_h = 700, 500
        panel_x = (WIDTH - panel_w) // 2
        panel_y = (HEIGHT - panel_h) // 2
        draw_panel(screen, panel_x, panel_y, panel_w, panel_h, bg=CREAM, border=WARM_BROWN, thick=5)
        # Title and author
        draw_text_centered(screen, poem["title"], font_large, DARK_BROWN, WIDTH//2, panel_y+30)
        draw_text_centered(screen, f"by {poem['author']}", font_med, TEAL, WIDTH//2, panel_y+65)
        pygame.draw.line(screen, DARK_BROWN, (panel_x+30, panel_y+85), (panel_x+panel_w-30, panel_y+85), 2)
        # Scrollable poem text
        line_height = 28
        max_lines_visible = (panel_h - 150) // line_height
        start_line = max(0, self.poem_scroll)
        end_line = min(len(poem["lines"]), start_line + max_lines_visible)
        y_text = panel_y + 110
        for i in range(start_line, end_line):
            line = poem["lines"][i]
            text_surf = font_small.render(line, True, DARK_BROWN)
            screen.blit(text_surf, (panel_x+40, y_text))
            y_text += line_height
        # Navigation buttons
        mx, my = pygame.mouse.get_pos()
        prev_hov = button_hit(mx, my, panel_x+50, panel_y+panel_h-60, 120, 40)
        next_hov = button_hit(mx, my, panel_x+panel_w-170, panel_y+panel_h-60, 120, 40)
        close_hov = button_hit(mx, my, panel_x+panel_w-80, panel_y+10, 60, 30)
        draw_button(screen, "◀ PREV", panel_x+50, panel_y+panel_h-60, 120, 40, bg=SOFT_BLUE, hover=prev_hov)
        draw_button(screen, "NEXT ▶", panel_x+panel_w-170, panel_y+panel_h-60, 120, 40, bg=SOFT_BLUE, hover=next_hov)
        # Scroll up/down indicators
        if self.poem_scroll > 0:
            draw_text_centered(screen, "▲", font_med, GRAY, WIDTH//2, panel_y+95)
        if end_line < len(poem["lines"]):
            draw_text_centered(screen, "▼", font_med, GRAY, WIDTH//2, panel_y+panel_h-80)
        # Close button (X)
        pygame.draw.rect(screen, RED, (panel_x+panel_w-80, panel_y+10, 60, 30))
        draw_text_centered(screen, "X", font_med, WHITE, panel_x+panel_w-50, panel_y+15)
        
        # Handle clicks (must be handled in click handler)
        if close_hov and pygame.mouse.get_pressed()[0]:
            self.state = STATE_CAFE
        if prev_hov and pygame.mouse.get_pressed()[0]:
            self.poem_index = (self.poem_index - 1) % len(POEMS)
            self.poem_scroll = 0
            pygame.time.wait(200)
        if next_hov and pygame.mouse.get_pressed()[0]:
            self.poem_index = (self.poem_index + 1) % len(POEMS)
            self.poem_scroll = 0
            pygame.time.wait(200)
        # Scroll with mouse wheel
        # (handled in event loop)

    # ── Done Screen ─────────────────────────────────────────────────────────
    def draw_done(self):
        screen.fill((25, 12, 5))
        for i in range(90):
            sx = (i * 163 + int(self.t * 20)) % WIDTH
            sy = (i * 97 + int(self.t * 10)) % HEIGHT
            px_rect(screen, GOLD if i%4==0 else WHITE, sx, sy, 3, 3)
        draw_panel(screen, 150, 80, 600, 480, bg=(50, 25, 8), border=GOLD, thick=5, gradient=True)
        for i, cat in enumerate(CAT_DATA):
            cx = 185 + i * 110
            draw_pixel_cat(screen, cx, 120, cat, scale=3, happy=True, tail_wag=True)
        draw_text_centered(screen, "✨ Thank you for visiting! ✨", font_title, GOLD, 450, 280)
        draw_text_centered(screen, "Whiskers & Paws Cafe", font_large, ORANGE, 450, 330)
        draw_text_centered(screen, "The cats were happy to serve you~", font_med, CREAM, 450, 370)
        total = sum([next((i["price"] for i in MENU_ITEMS if i["name"]==name), 0)*qty for name,qty in self.cart_items])
        draw_text_centered(screen, f"Total paid: ₹{total} + lots of purrs", font_med, TEAL, 450, 410)
        draw_text_centered(screen, f"Treats given: {len(self.fed_items)}", font_med, DARK_PINK, 450, 445)
        update_particles()
        draw_particles(screen)
        mx, my = pygame.mouse.get_pos()
        hov = button_hit(mx, my, 340, 490, 220, 55)
        draw_button(screen, "🐱 PLAY AGAIN", 340, 490, 220, 55, bg=DARK_PINK, hover=hov)

    # ── Click Handling ──────────────────────────────────────────────────────
    def handle_click(self, mx, my):
        if self.state == STATE_WELCOME:
            if button_hit(mx, my, 340, 520, 220, 60):
                self.state = STATE_CAFE
                spawn_particles(450, 450, 40, GOLD)
        elif self.state == STATE_CAFE:
            # Check poem button first
            if button_hit(mx, my, WIDTH-140, HEIGHT-60, 120, 40):
                self.state = STATE_POEM
                self.poem_scroll = 0
                return
            for i, cat in enumerate(CAT_DATA):
                cx, cy = cat["pos"]
                if button_hit(mx, my, cx-60, cy-70, 130, 110):
                    self.selected_cat = cat
                    self.fed_items = []
                    self.cart_items = []
                    self.collected = False
                    self.state = STATE_FEED_CAT
                    spawn_particles(cx, cy, 30, GOLD)
                    break
        elif self.state == STATE_FEED_CAT:
            self.handle_feed_click(mx, my)
        elif self.state == STATE_ORDER:
            self.handle_order_click(mx, my)
        elif self.state == STATE_COLLECT:
            if not self.collected:
                total_lines = len(self.cart_items)
                y_offset = 165 + total_lines * 35
                collect_btn_rect = (540, y_offset+110, 200, 50)
                if button_hit(mx, my, *collect_btn_rect):
                    self.collected = True
                    spawn_particles(640, 400, 40, GOLD)
            else:
                if button_hit(mx, my, 540, 430, 200, 50):
                    self.state = STATE_DONE
                    spawn_particles(450, 400, 50, GOLD)
        elif self.state == STATE_DONE:
            if button_hit(mx, my, 340, 490, 220, 55):
                self.reset()
                spawn_particles(450, 450, 40, GOLD)
        elif self.state == STATE_POEM:
            # Handle poem screen clicks (close, prev, next)
            panel_w, panel_h = 700, 500
            panel_x = (WIDTH - panel_w) // 2
            panel_y = (HEIGHT - panel_h) // 2
            if button_hit(mx, my, panel_x+panel_w-80, panel_y+10, 60, 30):
                self.state = STATE_CAFE
            elif button_hit(mx, my, panel_x+50, panel_y+panel_h-60, 120, 40):
                self.poem_index = (self.poem_index - 1) % len(POEMS)
                self.poem_scroll = 0
            elif button_hit(mx, my, panel_x+panel_w-170, panel_y+panel_h-60, 120, 40):
                self.poem_index = (self.poem_index + 1) % len(POEMS)
                self.poem_scroll = 0

    def handle_feed_click(self, mx, my):
        grid_x_start = 60
        grid_y_start = 400
        cols = 4
        item_w = 110
        item_h = 110
        for i, food in enumerate(FOOD_ITEMS):
            row = i // cols
            col = i % cols
            fx = grid_x_start + col * (item_w + 15)
            fy = grid_y_start + row * (item_h + 15)
            if button_hit(mx, my, fx-5, fy-5, item_w, item_h):
                self.fed_items.append(food)
                spawn_particles(mx, my, 15, food["color"])
                self.show_message(f"Fed {food['name']}! 🐱")
                return
        if button_hit(mx, my, 100, 650, 180, 50):
            self.fed_items.clear()
            self.show_message("Cleared all fed items.")
        if len(self.fed_items) > 0 and button_hit(mx, my, 620, 650, 180, 50):
            self.state = STATE_ORDER
            spawn_particles(450, 350, 30, GOLD)

    def handle_order_click(self, mx, my):
        menu_x_start = 40
        menu_y_start = 150
        cols = 3
        item_w = 200
        item_h = 150
        for i, item in enumerate(MENU_ITEMS):
            row = i // cols
            col = i % cols
            ix = menu_x_start + col * (item_w + 15)
            iy = menu_y_start + row * (item_h + 15)
            if button_hit(mx, my, ix+140, iy+110, 50, 30):
                found = False
                for idx, (name, qty) in enumerate(self.cart_items):
                    if name == item["name"]:
                        self.cart_items[idx] = (name, qty+1)
                        found = True
                        break
                if not found:
                    self.cart_items.append((item["name"], 1))
                spawn_particles(mx, my, 10, item["color"])
                return
        y_offset = 175
        for idx, (item_name, qty) in enumerate(self.cart_items):
            if button_hit(mx, my, 840, y_offset, 35, 25):
                if qty > 1:
                    self.cart_items[idx] = (item_name, qty-1)
                else:
                    self.cart_items.pop(idx)
                return
            y_offset += 45
        total = sum([next((i["price"] for i in MENU_ITEMS if i["name"]==name), 0)*qty for name,qty in self.cart_items])
        y_offset = 175 + len(self.cart_items) * 45
        if button_hit(mx, my, 700, y_offset+50, 160, 45) and len(self.cart_items) > 0:
            self.state = STATE_COLLECT
            self.collected = False
            spawn_particles(450, 400, 35, GOLD)
        if button_hit(mx, my, 700, y_offset+105, 160, 35):
            self.cart_items.clear()

    # ── Main Draw Dispatcher ────────────────────────────────────────────────
    def draw(self):
        if self.state == STATE_WELCOME:
            self.draw_welcome()
        elif self.state == STATE_CAFE:
            self.draw_cafe()
        elif self.state == STATE_FEED_CAT:
            self.draw_feed_cat()
        elif self.state == STATE_ORDER:
            self.draw_order()
        elif self.state == STATE_COLLECT:
            self.draw_collect()
        elif self.state == STATE_DONE:
            self.draw_done()
        elif self.state == STATE_POEM:
            self.draw_poem()
        if self.msg_timer > 0 and self.state in [STATE_FEED_CAT, STATE_ORDER]:
            draw_text_centered(screen, self.message, font_med, RED, WIDTH//2, 50)

# ── Main Loop ────────────────────────────────────────────────────────────────
def main():
    game = CatCafeGame()
    running = True
    while running:
        dt = clock.tick(60) / 1000.0
        game.t += dt
        update_particles()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                game.handle_click(*event.pos)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:  # scroll up
                if game.state == STATE_POEM:
                    game.poem_scroll = max(0, game.poem_scroll - 1)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:  # scroll down
                if game.state == STATE_POEM:
                    poem = POEMS[game.poem_index]
                    max_scroll = max(0, len(poem["lines"]) - ((500-150)//28))
                    game.poem_scroll = min(max_scroll, game.poem_scroll + 1)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
        game.draw()
        pygame.display.flip()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
