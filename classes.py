class Pokemon:
    def __init__(self, name, sprite, oppSprite, type, moves, EVs, healthBar, health="================"):
        # save variables as attributes
        self.name = name
        self.sprite = sprite
        self.oppSprite = oppSprite
        self.type = type
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.healthBar = healthBar
        self.health = health
        # health bars
        self.bars = 20


# a move class, so combat can be calculated by move type/attributes
class Move:
    def __init__(self, name, type, dmg):
        self.name = name
        self.type = type
        self.dmg = dmg