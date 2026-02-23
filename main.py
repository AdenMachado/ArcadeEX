import arcade
import data
from menus import SubMenuForUpgr, SubMenuSUpgrd
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
CUBE = "sprites/cube.png"


class RotatingSprite(arcade.Sprite):
    def rotate_around_point(self, point: arcade.math.Point, degrees: float):
        self.angle += degrees
        self.position = arcade.math.rotate_point(

            self.center_x, self.center_y,

            point[0], point[1], degrees)


class MyGUIWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.cube = arcade.Sprite(CUBE)
        self.cube.position = SCREEN_MIDDLE
        self.cube_sprite_list = arcade.SpriteList()
        self.cube_sprite_list.append(self.cube)

        self.manager = UIManager()
        self.manager.enable()

        self.anchor_layout = UIAnchorLayout(y=-600)
        self.box_layout = UIBoxLayout(vertical=False, space_between=3)

        self.setup_widgets()
        self.anchor_layout.add(self.box_layout)
        self.manager.add(self.anchor_layout)

        self.text = None
        self.text2 = None
        self.text3 = None
        self.text4 = None

    def setup_widgets(self):
        button1 = UIFlatButton(text="1", width=100, height=50, color=arcade.color.GHOST_WHITE)
        self.box_layout.add(button1)
        button1.on_click = self.on_uprg_click

        button2 = UIFlatButton(text="2", width=100, height=50, color=arcade.color.GHOST_WHITE)
        self.box_layout.add(button2)
        button2.on_click = self.on_uprgs_click

        button3 = UIFlatButton(text="3", width=100, height=50, color=arcade.color.GHOST_WHITE)
        self.box_layout.add(button3)

        button4 = UIFlatButton(text="4", width=100, height=50, color=arcade.color.GHOST_WHITE)
        self.box_layout.add(button4)

    def on_update(self, delta_time: float):
        self.cube_sprite_list.update()
        self.cube_move(delta_time)
        self.textscore = arcade.Text(f"{data.score}", anchor_x="left", color=arcade.color.WHITE, font_size=17,
                                     x=50,
                                     y=1235)
        self.textupg1 = arcade.Text(f"{data.upgr11}", anchor_x="left", color=arcade.color.WHITE, font_size=17,
                                    x=50,
                                    y=1135)
        self.textupg2 = arcade.Text(f"{data.upgr12}", anchor_x="left", color=arcade.color.WHITE, font_size=17,
                                    x=50,
                                    y=1100)
        self.textupg3 = arcade.Text(f"{data.upgr13}", anchor_x="left", color=arcade.color.WHITE, font_size=17,
                                    x=50,
                                    y=1065)
        self.textupg4 = arcade.Text(f"{data.upgr14}", anchor_x="left", color=arcade.color.WHITE, font_size=17,
                                    x=50,
                                    y=1030)

    def setup(self):
        self.batch = Batch()

    def on_draw(self):
        self.clear()
        self.manager.draw()
        self.cube_sprite_list.draw()
        self.textscore.draw()
        self.textupg1.draw()
        self.textupg2.draw()
        self.textupg3.draw()
        self.textupg4.draw()
        arcade.draw_rect_outline(arcade.rect.XYWH(110, 1240, 200, 50), arcade.color.WHITE,
                                 2)

    def on_mouse_press(self, x, y, button, key_modifiers):
        clicked_sprites = arcade.get_sprites_at_point((x, y), self.cube_sprite_list)
        if clicked_sprites:
            data.score += 1

    def cube_move(self, delta_time):
        self.cube.angle += (1 + data.score) * delta_time / 100

    def on_uprg_click(self, event):
        menu = SubMenuForUpgr(0.5, 0.4)
        self.manager.add(menu, layer=1)

    def on_uprgs_click(self, event):
        menu2 = SubMenuSUpgrd(0.8, 0.4)
        self.manager.add(menu2, layer=1)


def setup_game(width=800, height=600, title="Tycoon"):
    game = MyGUIWindow(width, height, title)
    return game


def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
