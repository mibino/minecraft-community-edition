from ursina import *
import os
import sys
from ursina.shaders.lit_with_shadows_shader import lit_with_shadows_shader

lang = sys.argv[1]

if lang == 'en_US':
    from assets.text.en_US import *
elif lang == 'zh_CN':
    from assets.text.zh_CN import *
elif lang == 'zh_TW':
    from assets.text.zh_TW import *
elif lang == 'en_UK':
    from assets.text.en_UK import *
elif lang == 'ru_RU':
    from assets.text.ru_RU import *
else:
    from assets.text.en_US import *

app = Ursina(borderless=False,title=launcher_title)
camera.position = (0,0.5,0)
camera.fov = 150
Text.default_font = 'assets/fonts/unifont.otf'
menu_bgm1 = Audio('assets/sounds/bgm/menu1.mp3', loop=True, autoplay=True)
buttonclick = Audio('assets/sounds/gui/click.mp3', autoplay=False)

window.exit_button.visible = False



menu_bgm1.play()

tln = ''

def input(key):
    global tln
    if key == '1':
        tln = '1.mclevel'
    if key == '2':
        tln = '2.mclevel'
    if key == '3':
        tln = '3.mclevel'
    if key == '4':
        tln = '4.mclevel'
    if key == '5':
        tln = '5.mclevel'

def play_game():
    global tln
    buttonclick.play()
    print(tln)
    os.system('python minecraft.py ' + lang + ' ' +  tln)
 
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


'''background = Entity(
    parent=scene,
    model='cube',
    position=(0,0,0),
    scale=(1024,1,1024),
    shader=lit_with_shadows_shader,
    texture='assets/textures/block/grass_top.png',
    texture_scale=(1024,1024),
    collider='box',
    color=color.green
)'''

title = Entity(
    parent=camera.ui,
    model='cube',
    texture='assets/textures/gui/title.png',
    origin=(0,-1.5),
    scale=(0.9,0.2)
)

splashes = Text(
    parent=camera.ui,
    text=splashes_text,
    origin=(-0.8,-3.5),
    color=color.yellow,
    scale=(1.5,1.5),
    rotation_z=-20
)

about1 = Text(
    parent=camera.ui,
    text='Minecraft by Mojang Studio',
    origin=(2.2,18),
    scale=(1,1)
)

about2 = Text(
    parent=camera.ui,
    text='Minecraft Community Edition by Ekuta Studio',
    origin=(1.13,19),
    scale=(1,1)
)

about3 = Text(
    parent=camera.ui,
    text='Alpha 0.3.0',
    origin=(-5.8,19),
    scale=(1,1)
)

play_button = Button(
    parent=camera.ui,
    model='cube',
    texture='assets/textures/gui/button1.png',
    text=play_button_text,
    color="#dddddd",
    scale=(0.3,0.1),
    origin=(0,0),
    highlight_color=color.green,
    on_click=play_game
)

play_multigame_button = Button(
    parent=camera.ui,
    model='cube',
    texture='assets/textures/gui/button1.png',
    text="MultiPlayer game",
    color=color.gray,
    scale=(0.3,0.1),
    origin=(0,1.2),
    highlight_color=color.gray,
    # on_click=play_game
)

# pivot = Entity()
# DirectionalLight(parent=pivot,position=(0,128,0),shader=False)

# sky = Sky(texture='assets/textures/shader/sky.png')



select_level_pstext = Text(
    parent=camera.ui,
    text=select_level_pstext_text,
    origin=(0,8.5)
)


def update():
    camera.rotation_y += 5 * time.dt

app.run()