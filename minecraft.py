from ursina import *
from player import player_entity
from ursina.shaders.lit_with_shadows_shader import lit_with_shadows_shader
import random
from item_bar import *
import numpy as np

create_new_world = 0


Text.default_font = 'assets/fonts/unifont.otf'

gametime = 3500


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
levelfile = sys.argv[2]

if lang == 'en_US':
    from assets.text.en_US import *
elif lang == 'zh_CN':
    from assets.text.zh_CN import *
elif lang == 'zh_TW':
    from assets.text.zh_TW import *
else:
    from assets.text.en_US import *


blocktexture = 'assets/textures/block/grass_top.png'

# If there are rendering issues, please press F5 to reload.


class Voxel(Button):
    def __init__(self, position=(0,0,0), texture=blocktexture, scale=1, use_deepcopy=True, highlight_color=color.light_gray, visible=True, psin='nether'):
        global destroy_block
        super().__init__(parent=scene,
            position=position,
            model='cube',
            scale=scale,
            color=color.white,
            origin_y=0,
            visible=visible,
            texture=texture,
            psin=psin,
            # shader=lit_with_shadows_shader,
            highlight_color=color.light_gray,
            on_click=self.destroy_block
        )
    def get_position(self):
        return self.position
    def destroy_block(self):
        if mouse.hovered_entity == self:
            # 获取当前方块的纹理和位置
            texture = self.texture
            position = self.get_position()
            
            # 查找 worldblock 中对应纹理的位置
            for i in range(0, len(worldblock), 2):  # 每两个元素迭代一次
                if worldblock[i] == texture:
                    # 检查位置是否匹配
                    if worldblock[i+1] == position:
                        worldblock.pop(i+1)  # 删除位置
                        worldblock.pop(i)    # 删除纹理
                        break  # 找到匹配的纹理和位置后退出循环

            # 删除方块实体
            destroy(self)

        




def input(key):
    global blocktexture
    global player_run
    global player_stealth
    global player_fly
    global game_bgm1
    global game_bgm2
    global game_bgm
    global gametime
    global worldblock
    if key == 'c':
        player_run = not player_run
        if player_run == True:
            player.speed = 10
        else:
            player.speed = 5
    if key == 'shift':
        player_stealth = not player_stealth
        if player_stealth == True:
            player.speed = 2.5
            player.height = 1.4
        else:
            player.speed = 5
            player.height = 1.6
    if key == 'v':
        with open(levelfile, 'w') as l:
            for i in range(0, len(worldblock), 2):  # 每两个元素迭代一次
                l.write(str(worldblock[i]) + '\n')  # 写入 texture
                l.write(str(worldblock[i+1]) + '\n')  # 写入 position
    if key == 'o':
        player.y = 10
    if key == 'n':
        player.y = 2050
    if key == 'f':
        player_fly = not player_fly
        if player_fly == True:
            player.gravity = 0
        else:
            player.gravity = 1
    '''if key == '.':
        for i in range(10):
            player.y = player.y + 1 * time.dt
    if key == ',':
        for i in range(10):
            player.y = player.y - 1 * time.dt'''
    if key == '1':
        blocktexture = 'assets/textures/block/grass_top.png'
    if key == '2':
        blocktexture = 'assets/textures/block/stone.png'
    if key == '3':
        blocktexture = 'assets/textures/block/planks_oak.png'
    if key == '4':
        blocktexture = 'assets/textures/block/glass.png'
    if key == '5':
        blocktexture = 'assets/textures/block/netherrack.png'    
    if key == 'z':
        sea.y += 1
    if key == 'x':
        sea.y -= 1
    if key == 'r':
        player.x = random.uniform(-511,511)
        player.y = 50
        player.z = random.uniform(-511,511)
    if key == 'j':
        player.position = (4090,2,4090)
    if key == 'k':
        new_block = Voxel(position=round(player.position,0),texture=blocktexture)
        worldblock.append(new_block.texture)
        worldblock.append(new_block.position)
        print(worldblock)
    if key == 'l':
        player.position = (0,10,0)
    if key == 'p':
        pause_menu()
    if key == 't':
        player.x = player.x + 10
    if key == 'b':
        game_bgm += 1
        if game_bgm > 2:
            game_bgm = 1
        if game_bgm == 1:
            game_bgm2.stop()
            game_bgm1.play()
        if game_bgm == 2:
            game_bgm1.stop()
            game_bgm2.play()
    if key == 'right mouse down':
        hit_info = raycast(camera.world_position, camera.forward, distance=10)
        if hit_info.hit:
            new_block = Voxel(position=hit_info.entity.position + hit_info.normal,texture=blocktexture)
            worldblock.append(new_block.texture)
            worldblock.append(new_block.position)
            print(worldblock)

app = Ursina(borderless=False,title=gamename)

window.exit_button.visible = False

player_run = False
player_fly = False
player_stealth = False

game_bgm = 1

game_bgm1 = Audio('assets/sounds/bgm/creative1.mp3', loop=True, autoplay=False)
game_bgm2 = Audio('assets/sounds/bgm/creative2.mp3', loop=True, autoplay=False)

# input_entity = Entity(input=input)

# noise = PerlinNoise(octaves=1,seed=1000)

scale_x = 16
scale_z = 16



        # block.y = floor(noise([x/16,z/16])*8)+10


def update():
    global gametime
    if held_keys['.']:
        player.y = player.y + 6 * time.dt
    elif held_keys[',']:
        player.y = player.y - 6 * time.dt
    #clouds.x = player.x
    #clouds.z = player.z
    gametime += 1
    if gametime == 8000:
        overworld_sky.color = color.light_gray
    elif gametime == 10000:
        dark.texture='assets/textures/shader/dark.png'
        overworld_sky.color = color.hex('#2e2e2e')
        gametime = 0
    elif gametime == 2500:
        overworld_sky.color = color.light_gray
    elif gametime == 3500:
        dark.texture='assets/textures/gui/none.png'
        overworld_sky.color = color.white
    if clouds.x > 256:
        clouds.x = 0
    else:
        clouds.x += 1 * time.dt
    # communism.x = player.x
    # communism.z = player.z
    overworld_sky.x = player.x
    overworld_sky.z = player.z
    nether_sky.x = player.x
    nether_sky.z = player.z
    seay = sea.y
    cameray = player.y + 1
    if cameray < seay:
        in_water.texture = 'assets/textures/shader/in_water.png'
    elif cameray > seay:
        in_water.texture = 'assets/textures/gui/none.png'
        

    

if game_bgm == 1:
    game_bgm1.play()
if game_bgm == 2:
    game_bgm2.play()


item_bar()

overworld_sky = Entity(
    parent=scene,
    model='cube',
    texture='assets/textures/shader/sky.png',
    position=(0,0,0),
    scale=(512,1024,512),
    double_sided=True
)

nether_sky = Entity(
    parent=scene,
    model='cube',
    color=color.hex('#8a0808'),
    position=(0,2048,0),
    scale=(512,256,512),
    double_sided=True
)

sea  = Entity(
    parent=scene,
    position=(0,0.3,0),
    scale=(8193,0.1,8193),
    model='cube',
    texture='assets/textures/block/water.png',
    texture_scale=(8192,8192),
    # shader=lit_with_shadows_shader
)



fakeplane = Entity(
    parent=scene,
    model='cube',
    position=(0,-4096.7,0),
    scale=(8193,8192.5,8193),
    # shader=lit_with_shadows_shader,
    texture='assets/textures/block/bedrock.png',
    texture_scale=(8192,8192),
    collider='box'
)

nether_fakeplane = Entity(
    parent=scene,
    model='cube',
    position=(0,2047,0),
    scale=(8193,1,8193),
    # shader=lit_with_shadows_shader,
    texture='assets/textures/block/netherrack.png',
    texture_scale=(8192,8192),
    collider='box'
)

worldborder = Entity(
    parent=scene,
    model='cube',
    position=(0,0,0),
    scale=(8193,8192.5,8193),
    # shader=lit_with_shadows_shader,
    texture='assets/textures/block/stone.png',
    texture_scale=(8192,8192),
    collider='box',
    double_sided=True
)

clouds = Entity(
    parent=scene,
    model='plane',
    position=(0,256,0),
    scale=(2048,1,2048),
    # shader=lit_with_shadows_shader,
    texture='assets/textures/shader/clouds.png',
    texture_scale=(1,1),
    double_sided=True
)

'''fakeplane_under = Entity(
    parent=scene,
    model='cube',
    position=(0,-1024,0),
    scale=(8193,1,8193),
    # shader=lit_with_shadows_shader,
    texture='assets/textures/gui/frame.png',
    texture_scale=(8191,8191),
    collider='box',
    origin_y=0.5
)'''

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


in_water = Entity(
    parent=camera.ui,
    origin=(0,0),
    scale=window.size,
    model='cube',
    texture='assets/textures/gui/none.png'
    # shader=lit_with_shadows_shader
)

dark = Entity(
    parent=camera.ui,
    origin=(0,0),
    scale=window.size,
    model='cube',
    texture='assets/textures/gui/none.png'
    # shader=lit_with_shadows_shader
)

# pivot = Entity()
# DirectionalLight(parent=pivot,position=(0,128,0),shader=True)


try:
    with open(levelfile, 'r') as k:
        worldblock = []
        lines = k.readlines()  # 读取所有行
        # 假设每一对行包含一个 texture 和一个 Vec3 位置信息
        for i in range(0, len(lines), 2):  # 每两行迭代一次
            texture = lines[i].strip()
            vec3_str = lines[i+1].strip()
            # 尝试解析 Vec3 字符串
            try:
                # 假设 Vec3 字符串格式为 "Vec3(x, y, z)"
                _, position_str = vec3_str.split('(')
                position_str = position_str.rstrip(')')
                x, y, z = map(float, position_str.split(','))  # 将 texture 和元组形式的位置存储在 worldblock 列表中
                # 创建 Voxel 对象并添加到场景
                level_new_block = Voxel(
                position=(x, y, z),
                texture=texture
                )
                worldblock.append(level_new_block.texture)
                worldblock.append(level_new_block.position)
            except Exception as e:
                print(f"Error parsing Vec3 string: {vec3_str}")
                print(e)
        print(worldblock)
except FileNotFoundError:
    print("World not found...")
    worldblock = []
    for bx in range(-scale_x,scale_x,1):
        for bz in range(-scale_z,scale_z,1):
            block = Voxel(position=(bx,0,bz),texture='assets/textures/block/grass_top.png')
            worldblock.append(block.texture)
            worldblock.append(block.position)
    for bx in range(-6,6,1):
        for bz in range(-6,6,1):
            block = Voxel(position=(bx,2048,bz),texture='assets/textures/block/netherrack.png')
            worldblock.append(block.texture)
            worldblock.append(block.position)



# def create_voxels_from_list(voxel_list):
'''for texture, position in worldblock:
    # 从元组中提取 x, y, z 值
    x, y, z = position
   # 创建 Voxel 对象并添加到场景
    level_new_block = Voxel(
        position=(x, y, z),
        texture=texture
    )
    worldblock.append(level_new_block.texture)
    worldblock.append(level_new_block.position)'''

# 在 Ursina 应用设置之后和 app.run() 之前调用函数
# create_voxels_from_list(worldblock)

# player = EditorCamera()
player = player_entity()
player.position = (0,12,0)
player.position = (0,12,0)



app.run()