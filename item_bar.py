from ursina import *

class item_bar:
    def __init__(self):
        item_bar = Entity(
            parent=camera.ui,
            model='cube',
            origin=(0,7),
            texture='assets/textures/gui/item_bar2.png',
            scale=(0.5,0.065,0.5)
        )