from ursina import *

class pause_menu:
    def __init__(self):
        buttonclick = Audio('assets/sounds/gui/click.mp3', autoplay=False)
        def backtogame():
            buttonclick.play()
            destroy(title)
            destroy(back_to_game_button)
            destroy(background)
            destroy(quit_button)
            destroy(menubg)
            destroy(logo)
            mouse.locked = True
        def quitgame():
            buttonclick.play()
            quit() 
        mouse.locked = False
        background = Entity(
            parent=camera.ui,
            model="cube",
            texture='assets/textures/gui/pause_bg.png',
            scale=(1000,1000,1000)
        )
        menubg = Entity(
            parent=camera.ui,
            model="cube",
            texture='assets/textures/gui/menu.png',
            scale=(0.4,0.6,0.4),
            origin=(0,-0.1)
        )
        title = Text(
            parent=camera.ui,
            text='Pause Menu',
            origin=(0,-10)
        )
        back_to_game_button = Button(
            parent=camera.ui,
            model='cube',
            texture='assets/textures/gui/button1.png',
            text='Back to game',
            color='#dddddd',
            scale=(0.3,0.1),
            origin=(0,-1),
            highlight_color=color.green,
            on_click=backtogame
        )
        quit_button = Button(
            parent=camera.ui,
            model='cube',
            texture='assets/textures/gui/button1.png',
            text='Quit game',
            color='#dddddd',
            scale=(0.3,0.1),
            origin=(0,0),
            highlight_color=color.green,
            on_click=quitgame
        )
        logo = Entity(
            parent=camera.ui,
            model="cube",
            texture='assets/textures/gui/title.png',
            scale=(0.2,0.05,0.2),
            origin=(3.5,-8)
        )