import arcade
import data
import random
import os
from menus import SubMenuForUpgr, SubMenuSUpgrd, SubMenuMiners, SubMenuStatic, SubMenuTutor
from pyglet.graphics import Batch
from arcade.particles import FadeParticle, Emitter, EmitBurst, EmitInterval, EmitMaintainCount, Particle
from arcade.gui import (
    UIAnchorLayout,
    UIFlatButton,
    UIGridLayout,
    UIImage,
    UIOnChangeEvent,
    UITextureButton,
    UITextureToggle,
    UIView,
    UIManager,
    UIBoxLayout,
)

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 1300
SCREEN_MIDDLE = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
SCREEN_TITLE = "Tycoon"
font_path = os.path.join("Assets", "Fonts", "VMVSegaGenesis-Regular.otf")
font_name = "VMV Sega Genesis"
click_cube_sound = arcade.load_sound("Assets/Sound/click_cube.wav")
click_button_sound = arcade.load_sound("Assets/Sound/click_button.wav")
victory = arcade.load_sound("Assets/Sound/victory.mp3")



class RotatingSprite(arcade.Sprite):
    def rotate_around_point(self, point: arcade.math.Point, degrees: float):
        self.angle += degrees
        self.position = arcade.math.rotate_point(

            self.center_x, self.center_y,

            point[0], point[1], degrees)


class MyGUIWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.cube = arcade.Sprite("sprites/cube.png")
        self.cube.position = SCREEN_MIDDLE

        self.score_menu = arcade.Sprite("sprites/menu_score.png")
        self.score_menu.position = (110, 1240)

        self.upgrades_menu = arcade.Sprite("sprites/menu_upgrades.png")
        self.upgrades_menu.position = (380, 1215)

        self.colors_menu = arcade.Sprite("sprites/menu_colors.png")
        self.colors_menu.position = (650, 1134)

        self.clicks_menu = arcade.Sprite("sprites/menu_clicks.png")
        self.clicks_menu.position = (80, 1050)

        self.goal_menu = arcade.Sprite("sprites/menu_goals.png")
        self.goal_menu.position = (80, 960)

        self.cube_sprite_list = arcade.SpriteList()
        self.sprite_list = arcade.SpriteList()

        self.sprite_list.append(self.score_menu)
        self.sprite_list.append(self.upgrades_menu)
        self.sprite_list.append(self.colors_menu)
        self.sprite_list.append(self.clicks_menu)
        self.sprite_list.append(self.goal_menu)
        self.cube_sprite_list.append(self.cube)

        self.manager = UIManager()
        self.manager.enable()

        self.anchor_layout = UIAnchorLayout(y=-600)
        self.box_layout = UIBoxLayout(vertical=False, space_between=6)

        self.setup_widgets()
        self.anchor_layout.add(self.box_layout)
        self.manager.add(self.anchor_layout)

        arcade.schedule(self.score_updater, 1.0)
        self.emitters = []
        self.flag = False
        self.count = 0
        arcade.load_font(font_path)
        self.batch = Batch()

        tutor_menu1 = SubMenuTutor(0.36, 1, ["Добро пожаловать в кликер!", "Правила игры просты:",
                                             "Кликать на куб и получать байты,",
                                             "за них покупать майнеры, улучшения на клик и цвета"],
                                   250,
                                   400)
        tutor_menu2 = SubMenuTutor(1.1, 1.5,
                                   ["Наверху показаны все валюты, майнеры, цвета, которые понадобятся для прохождения игры."],
                                   300,
                                   250)
        tutor_menu3 = SubMenuTutor(1, 0.4, ["Внизу есть 4 вкладки:",
                                             "1: Miners - здесь можно купить майнеры - пасивный доход, указанный рядом с названием майнера",
                                             "2: Clicks - улучшения на клик, чтобы клик стал сильнее. Также улучшения требуют особую валюту, "
                                             "которую можно получить в 3 вкладке за обычные клики",
                                             "3: Color - покупка особой валюты - цвета. Чтобы купить надо просто кликать.",
                                             "4: Statistics - статистика всей игры "],
                                   500,
                                   400)
        tutor_menu4 = SubMenuTutor(1.1, 1.5, ["Цель прохождения указана слево, удачи!"],
                                   250,
                                   250)
        self.manager.add(tutor_menu4)
        self.manager.add(tutor_menu3)
        self.manager.add(tutor_menu2)
        self.manager.add(tutor_menu1)


    def setup_widgets(self):
        button1 = UIFlatButton(text="Miners", width=150, height=80, color=arcade.color.GHOST_WHITE)
        self.box_layout.add(button1)
        button1.on_click = self.on_uprg_click

        button2 = UIFlatButton(text="Clicks", width=150, height=80, color=arcade.color.GHOST_WHITE)
        self.box_layout.add(button2)
        button2.on_click = self.on_uprgs_click

        button3 = UIFlatButton(text="Colors", width=150, height=80, color=arcade.color.GHOST_WHITE)
        self.box_layout.add(button3)
        button3.on_click = self.on_miners

        button4 = UIFlatButton(text="Statistics", width=150, height=80, color=arcade.color.GHOST_WHITE)
        self.box_layout.add(button4)
        button4.on_click = self.on_statistics

    def on_update(self, delta_time: float):
        self.cube_sprite_list.update()
        self.cube_move(delta_time)
        self.text_score = arcade.Text(f"{convector(data.score)}", anchor_x="left", color=arcade.color.WHITE,
                                     font_size=16,
                                     font_name=font_name,
                                     x=30,
                                     y=1235,
                                     batch=self.batch)
        self.text_upg1 = arcade.Text(f"B:{convector(data.upgr11)}", anchor_x="left", color=arcade.color.WHITE,
                                    font_size=16,
                                    font_name=font_name,
                                    x=240,
                                    y=1230,
                                    batch=self.batch)
        self.text_upg2 = arcade.Text(f"KB:{convector(data.upgr12)}", anchor_x="left", color=arcade.color.WHITE,
                                    font_size=16,
                                    font_name=font_name,
                                    x=240,
                                    y=1167,
                                    batch=self.batch)
        self.text_upg3 = arcade.Text(f"MB:{convector(data.upgr13)}", anchor_x="left", color=arcade.color.WHITE,
                                    font_size=16,
                                    font_name=font_name,
                                    x=405,
                                    y=1230,
                                    batch=self.batch)
        self.text_upg4 = arcade.Text(f"GB:{convector(data.upgr14)}", anchor_x="left", color=arcade.color.WHITE,
                                    font_size=16,
                                    font_name=font_name,
                                    x=405,
                                    y=1167,
                                    batch=self.batch)
        self.text_click = arcade.Text(
            f"{convector(1 + (2 * data.upgr21) + (5 * data.upgr22) + (12 * data.upgr23) +
                         (30 * data.upgr24))}/tap",
            anchor_x="left", color=arcade.color.WHITE,
            font_size=16,
            font_name=font_name,
            x=20,
            y=1150,
            batch=self.batch)
        self.text_red = arcade.Text(f"R:{data.red}", anchor_x="left", color=arcade.color.WHITE,
                                   font_size=16,
                                   font_name=font_name,
                                   x=595,
                                   y=1233,
                                   batch=self.batch
                                   )
        self.text_green = arcade.Text(f"G:{data.green}", anchor_x="left", color=arcade.color.WHITE,
                                     font_size=16,
                                     font_name=font_name,
                                     x=595,
                                     y=1173,
                                     batch=self.batch
                                     )
        self.text_blue = arcade.Text(f"B:{data.blue}", anchor_x="left", color=arcade.color.WHITE,
                                    font_size=16,
                                    font_name=font_name,
                                    x=595,
                                    y=1113,
                                    batch=self.batch
                                    )
        self.text_white = arcade.Text(f"W:{data.white}", anchor_x="left", color=arcade.color.WHITE,
                                     font_size=16,
                                     font_name=font_name,
                                     x=595,
                                     y=1053,
                                     batch=self.batch
                                     )
        self.text_goal = arcade.Text("1M Bytes", anchor_x="left", color=arcade.color.WHITE,
                                     font_size=16,
                                     font_name=font_name,
                                     x=25,
                                     y=1055,
                                     batch=self.batch)
        emitters_copy = self.emitters.copy()  # Защищаемся от мутаций списка
        for e in emitters_copy:
            e.update(delta_time)
        for e in emitters_copy:
            if e.can_reap():  # Готов к уборке?
                self.emitters.remove(e)

    def setup(self):
        self.batch = Batch()

    def on_draw(self):
        self.clear()
        self.manager.draw()
        self.cube_sprite_list.draw()
        self.sprite_list.draw()
        self.batch.draw()
        for e in self.emitters:
            e.draw()

    def on_mouse_press(self, x, y, button, key_modifiers):
        clicked_sprites = arcade.get_sprites_at_point((x, y), self.cube_sprite_list)
        if clicked_sprites:
            click_cube_sound.play(volume=0.1)
            self.emitters.append(make_ring(x, y))
            data.score += 1 + (2 * data.upgr21) + (5 * data.upgr22) + (12 * data.upgr23) + (30 * data.upgr24)
            data.clicks += 1
            data.currentclicks += 1

    def cube_move(self, delta_time):
        self.cube.angle += (1 + data.score) * delta_time / 400

    def on_uprg_click(self, event):
        click_button_sound.play(volume=0.1)
        menu = SubMenuForUpgr(0.5, 0.4)
        self.manager.add(menu, layer=1)

    def on_uprgs_click(self, event):
        click_button_sound.play(volume=0.1)
        menu2 = SubMenuSUpgrd(0.8, 0.4)
        self.manager.add(menu2, layer=1)

    def on_miners(self, event):
        click_button_sound.play(volume=0.1)
        menu3 = SubMenuMiners(1.2, 0.4)
        self.manager.add(menu3, layer=1)

    def on_statistics(self, event):
        click_button_sound.play(volume=0.1)
        menu4 = SubMenuStatic(1.5, 0.4)
        self.manager.add(menu4, layer=1)

    def score_updater(self, delta_time):
        data.score += 1 * data.upgr11
        data.score += 6 * data.upgr12
        data.score += 40 * data.upgr13
        data.score += 300 * data.upgr14
        if data.score >= 1_000_000:
            text_win = SubMenuTutor(1.1, 1.5,
                                   ["Поздравляю ты достиг цели!"],
                                   300,
                                   250)
            data.score = 0
            self.flag = True
            self.manager.add(text_win)
        if self.flag:
            self.count += 1
            if self.count == 1:
                victory.play(volume=0.05)
            if self.count == 3:
                arcade.close_window()



def convector(num):
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'),
                         ['', 'K', 'M', 'B', 'T', "qd", "qt", "st", "sp", "oc", "nn", "dc", "un", "dd", "td"]
                         [magnitude])


SPARK_TEX = [
    arcade.make_soft_circle_texture(8, arcade.color.PASTEL_YELLOW),
    arcade.make_soft_circle_texture(8, arcade.color.PEACH),
    arcade.make_soft_circle_texture(8, arcade.color.BABY_BLUE),
    arcade.make_soft_circle_texture(8, arcade.color.ELECTRIC_CRIMSON),
]


def gravity_drag(p):  # Для искр: чуть вниз и затухание скорости
    p.change_y += -0.03
    p.change_x *= 0.92
    p.change_y *= 0.92


def make_ring(x, y, count=20, radius=5.0):
    return Emitter(
        center_xy=(x, y),
        emit_controller=EmitBurst(count),
        particle_factory=lambda e: FadeParticle(
            filename_or_texture="sprites/particle.png",
            change_xy=arcade.math.rand_on_circle((0.0, 0.0), radius),
            lifetime=random.uniform(0.8, 1.4),
            start_alpha=255, end_alpha=0,
            scale=random.uniform(1, 1),
            mutation_callback=gravity_drag,
        ),
    )


def setup_game(width=800, height=600, title="Tycoon"):
    game = MyGUIWindow(width, height, title)
    return game


def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
