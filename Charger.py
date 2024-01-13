import pygame

PATH_BLOCK = "assets/blocks/"
PATH_FOND = "assets/fond/"
PATH_ITEM = "assets/items/"

def load_button(
    name: str,
    size: tuple,
    pos: tuple = None,
    func = None
    ):
    button = pygame.image.load(f"{BUTTON_FOLDER}{name}.png").convert()
    button = pygame.transform.scale(button, size)
    button_rect = button.get_rect()
    button_pressed = pygame.image.load(f"{BUTTON_FOLDER}{name}_press.png").convert()
    button_pressed = pygame.transform.scale(button_pressed, size)

    if pos:
        button_rect.x = pos[0]
        button_rect.y = pos[1]

    if func:
        return button, button_pressed, button_rect, func
    return button, button_pressed, button_rect

def load_block(
    name: str = None,
    size: tuple = None
    ):
    if name == None:
        return None, None
    else:
        block = pygame.image.load(f"{PATH_BLOCK}{name}.png")
        block = pygame.transform.scale(block, (size)).convert_alpha()
        block_rect = block.get_rect()


        return block, block_rect

def load_background(
    name: str,
    size: tuple
    ):

    background = pygame.image.load(f"{PATH_FOND}{name}.png").convert_alpha()
    background = pygame.transform.scale(background, (size))

    return background

def load_item(
    name: str = None,
    size: tuple = None
    ):

    if name != None:
        item = pygame.image.load(f"{PATH_ITEM}{name}.png").convert_alpha()
        item_rect = item.get_rect()
        if size != None:
            item = pygame.transform.scale(item, (size))
    
        return item, item_rect

def load_icon():
    icon = pygame.image.load("assets/icon/icon.png")
    return icon


def load_credit():
    file = codecs.open("data/generique.txt", "r", 'utf-8')

    lines = file.readlines()

    poscredit = []
    listcredit = []
    file.close()
    pos = 500
    for line in lines:
        poscredit.append(pos)
        pos += 50
        listcredit.append(line.strip())

    return poscredit, listcredit


