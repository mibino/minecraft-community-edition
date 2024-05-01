from ursina import *
from player import player_entity
from ursina.shaders.lit_with_shadows_shader import lit_with_shadows_shader
import random

Text.default_font = 'assets/fonts/unifont.otf'



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
            text=pause_menu_title,
            origin=(0,-10)
        )
        back_to_game_button = Button(
            parent=camera.ui,
            model='cube',
            texture='assets/textures/gui/button1.png',
            text=back_to_game_button_text,
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
            text=quit_game_button_text,
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



lang = sys.argv[1]

if lang == 'en_US':
    from assets.text.en_US import *
elif lang == 'zh_CN':
    from assets.text.zh_CN import *
else:
    from assets.text.en_US import *

def phfk():
    destroy(mouse.hovered_entity)

blocktexture = 'assets/textures/block/grass_top.png'
theblockcolor = color.green
# If there are rendering issues, please press F5 to reload.


class Voxel(Button):
    def __init__(self, position=(0,0,0), texture=blocktexture, scale=1, blockcolor=color.white):
        super().__init__(parent=scene,
            position=position,
            model='cube',
            scale=scale,
            origin_y=0,
            texture=texture,
            color=blockcolor,
            shader=lit_with_shadows_shader,
            highlight_color=color.light_gray,
            on_click=phfk
        )




def input(key):
    global blocktexture
    global theblockcolor
    if key == '1':
        blocktexture = 'assets/textures/block/grass_top.png'
        theblockcolor = color.green
    if key == '2':
        blocktexture = 'assets/textures/block/stone.png'
        theblockcolor = color.white
    if key == '3':
        blocktexture = 'assets/textures/block/planks_oak.png'
        theblockcolor = color.white
    if key == 'r':
        player.x = random.uniform(-511,511)
        player.y = 50
        player.z = random.uniform(-511,511)
    if key == 'l':
        player.position = (0,1,0)
    if key == 'm':
        sea.visible = not sea.visible
    if key == 'p':
        pause_menu()
    if key == 't':
        player.x = player.x + 10
    if key == 'right mouse down':
        hit_info = raycast(camera.world_position, camera.forward, distance=10)
        if hit_info.hit:
            Voxel(position=hit_info.entity.position + hit_info.normal,texture=blocktexture,blockcolor=theblockcolor)


app = Ursina(borderless=False,title=gamename)

window.exit_button.visible = False


game_bgm1 = Audio('assets/sounds/bgm/creative1.mp3', loop=True, autoplay=True)
game_bgm1.play()

# input_entity = Entity(input=input)

for x in range(-12,12,1):
    for z in range(-12,12,1):
        Voxel(position=(x,0,z),texture=blocktexture,blockcolor=color.green)



fakeplane = Entity(
    parent=scene,
    model='cube',
    position=(0,-1,0),
    scale=(1024,1,1024),
    shader=lit_with_shadows_shader,
    texture='assets/textures/block/grass_top.png',
    texture_scale=(1024,1024),
    collider='box',
    color=color.green
)

sea  = Entity(
    parent=scene,
    position=(0,0.3,0),
    scale=(1024,0.1,1024),
    model='cube',
    texture='assets/textures/block/water.png',
    texture_scale=(1024,1024),
    shader=lit_with_shadows_shader
)

sea.visible = False

gametitle = Text(
    parent=camera.ui,
    text=gamename,
    origin=(2.13,-19)
)

ps = Text(
    parent=camera.ui,
    text=gameps,
    origin=(0.75,-18)
)


pivot = Entity()
DirectionalLight(parent=pivot,position=(0,128,0),shader=True)

sky = Sky(texture='assets/textures/shader/sky.png')

player = player_entity()


app.run()