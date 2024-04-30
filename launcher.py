from ursina import *
import os
from ursina.shaders.lit_with_shadows_shader import lit_with_shadows_shader

app = Ursina(borderless=False,title='Minecraft CE Launcher')
camera.position = (0,2,0)
camera.fov = 500
#EditorCamera(position=(0,0.5,0))
Text.default_font = 'assets/fonts/unifont.otf'
menu_bgm1 = Audio('assets/sounds/bgm/menu1.mp3', loop=True, autoplay=True)
buttonclick = Audio('assets/sounds/gui/click.mp3', autoplay=False)

window.exit_button.visible = False

menu_bgm1.play()

def play_game():
    buttonclick.play()
    os.system('python minecraft.py')
'''
bg_buttom = Entity(
    parent=scene,
    model='cube',
    texture='assets/textures/gui/background/panorama_5.png',
    position=(0,0,0),
    rotation_y=90,
    scale=(1,0.01,1)
)

bg_up = Entity(
    parent=scene,
    model='cube',
    texture='assets/textures/gui/background/panorama_4.png',
    position=(0,1,0),
    rotation_y=90,
    rotation_x=-180,
    scale=(1,0.01,1)
)

bg_forward = Entity(
    parent=scene,
    model='cube',
    texture='assets/textures/gui/background/panorama_0.png',
    position=(0.5,0.5,0),
    rotation_x=-90,
    rotation_y=90,
    scale=(1,0.01,1)
)

bg_back = Entity(
    parent=scene,
    model='cube',
    texture='assets/textures/gui/background/panorama_2.png',
    position=(-0.5,0.5,0),
    rotation_x=-90,
    rotation_y=90,
    rotation_z=180,
    scale=(1,0.01,1)
)

bg_left = Entity(
    parent=scene,
    model='cube',
    texture='assets/textures/gui/background/panorama_3.png',
    position=(0,0.5,0.5),
    rotation_x=-90,
    rotation_y=0,
    rotation_z=0,
    scale=(1,0.01,1)
)

bg_right = Entity(
    parent=scene,
    model='cube',
    texture='assets/textures/gui/background/panorama_1.png',
    position=(0,0.5,-0.5),
    rotation_x=-90,
    rotation_y=180,
    rotation_z=0,
    scale=(1,0.01,1)
)
'''

background = Entity(
    parent=scene,
    model='cube',
    position=(0,0,0),
    scale=(1024,1,1024),
    shader=lit_with_shadows_shader,
    texture='assets/textures/block/grass_top.png',
    texture_scale=(1024,1024),
    collider='box',
    color=color.green
)

title = Entity(
    parent=camera.ui,
    model='cube',
    texture='assets/textures/gui/title.png',
    origin=(0,-1.5),
    scale=(0.9,0.2)
)

about1 = Text(
    parent=camera.ui,
    text='Minecraft by Mojang Studio',
    origin=(2.2,18),
    scale=(1,1)
)

about2 = Text(
    parent=camera.ui,
    text='Minecraft Community Edition by BedrockMCBBS',
    origin=(1.13,19),
    scale=(1,1)
)

about3 = Text(
    parent=camera.ui,
    text='Minecraft Cuommunity Edition Demo',
    origin=(-1.6,19),
    scale=(1,1)
)

play_button = Button(
    parent=camera.ui,
    model='cube',
    texture='assets/textures/gui/button1.png',
    text='Play',
    color='#dddddd',
    scale=(0.3,0.1),
    origin=(0,0),
    highlight_color=color.green,
    on_click=play_game
)

pivot = Entity()
DirectionalLight(parent=pivot,position=(0,128,0),shader=False)

sky = Sky(texture='assets/textures/shader/sky.png')

def update():
    camera.rotation_y += 5 * time.dt

app.run()