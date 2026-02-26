import arcade
import data
from numerize import numerize
from pyglet.graphics import Batch
import time
from menus import SubMenuForUpgr, SubMenuSUpgrd, SubMenuMiners, SubMenuStatic
from pyglet.graphics import Batch
import math
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
        self.upgrades_menu.position = (350, 1215)
        self.cube_sprite_list = arcade.SpriteList()
        self.sprite_list = arcade.SpriteList()
        self.sprite_list.append(self.score_menu)
        self.sprite_list.append(self.upgrades_menu)
        self.cube_sprite_list.append(self.cube)


        self.manager = UIManager()
        self.manager.enable()

        self.anchor_layout = UIAnchorLayout(y=-600)
        self.box_layout = UIBoxLayout(vertical=False, space_between=6)

        self.setup_widgets()
        self.anchor_layout.add(self.box_layout)
        self.manager.add(self.anchor_layout)

        self.text = None
        self.text2 = None
        self.text3 = None
        self.text4 = None
        self.total_time = 0.0
        self.timer = 0
        arcade.schedule(self.score_updater, 1.0)
        self.batch = Batch()

    def setup_widgets(self):
        button1 = UIFlatButton(text="Upgrades", width=150, height=80, color=arcade.color.GHOST_WHITE)
        self.box_layout.add(button1)
        button1.on_click = self.on_uprg_click

        button2 = UIFlatButton(text="Click upg.", width=150, height=80, color=arcade.color.GHOST_WHITE)
        self.box_layout.add(button2)
        button2.on_click = self.on_uprgs_click

        button3 = UIFlatButton(text="Miners", width=150, height=80, color=arcade.color.GHOST_WHITE)
        self.box_layout.add(button3)
        button3.on_click = self.on_miners

        button4 = UIFlatButton(text="Statistic", width=150, height=80, color=arcade.color.GHOST_WHITE)
        self.box_layout.add(button4)
        button4.on_click = self.on_statistics

    def on_update(self, delta_time: float):
        self.cube_sprite_list.update()
        self.cube_move(delta_time)
        self.textscore = arcade.Text(f"{convector(data.score)}", anchor_x="left", color=arcade.color.WHITE, font_size=18,
                                     x=50,
                                     y=1235,
                                     batch=self.batch)
        self.textupg1 = arcade.Text(f"B: {data.upgr11}", anchor_x="left", color=arcade.color.WHITE, font_size=18,
                                    x=260,
                                    y=1230,
                                    batch=self.batch)
        self.textupg2 = arcade.Text(f"KB: {data.upgr12}", anchor_x="left", color=arcade.color.WHITE, font_size=18,
                                    x=260,
                                    y=1167,
                                    batch=self.batch)
        self.textupg3 = arcade.Text(f"MB: {data.upgr13}", anchor_x="left", color=arcade.color.WHITE, font_size=18,
                                    x=370,
                                    y=1230,
                                    batch=self.batch)
        self.textupg4 = arcade.Text(f"GB: {data.upgr14}", anchor_x="left", color=arcade.color.WHITE, font_size=18,
                                    x=370,
                                    y=1167,
                                    batch=self.batch)


    def setup(self):
        self.batch = Batch()

    def on_draw(self):
        self.clear()
        self.manager.draw()
        self.cube_sprite_list.draw()
        self.sprite_list.draw()
        self.batch.draw()

    def on_mouse_press(self, x, y, button, key_modifiers):
        clicked_sprites = arcade.get_sprites_at_point((x, y), self.cube_sprite_list)
        if clicked_sprites:
            data.score += 1 + (1 * data.upgr21) + (1 * data.upgr22) + (1 * data.upgr23) + (1 * data.upgr24)
            data.clicks += 1
            data.currentclicks += 1

    def cube_move(self, delta_time):
        if data.score < 220000000:
            self.cube.angle += (1 + data.score) * delta_time / 100000
        else:
            self.cube.angle += 2200 * delta_time

    def on_uprg_click(self, event):
        menu = SubMenuForUpgr(0.5, 0.4)
        self.manager.add(menu, layer=1)

    def on_uprgs_click(self, event):
        menu2 = SubMenuSUpgrd(0.8, 0.4)
        self.manager.add(menu2, layer=1)

    def on_miners(self, event):
        menu3 = SubMenuMiners(1.2, 0.4)
        self.manager.add(menu3, layer=1)

    def on_statistics(self, event):
        menu4 = SubMenuStatic(1.5, 0.4)
        self.manager.add(menu4, layer=1)

    def score_updater(self, delta_time):
        data.score += 1 * data.upgr11
        data.score += 6 * data.upgr12
        data.score += 40 * data.upgr13
        data.score += 300 * data.upgr14

def convector(num):
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'),
                         ['', 'K', 'M', 'B', 'T', "qd", "qt", "st", "sp", "oc", "nn", "dc", "un", "dd", "td"]
                         [magnitude])

def setup_game(width=800, height=600, title="Tycoon"):
    game = MyGUIWindow(width, height, title)
    return game


def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
