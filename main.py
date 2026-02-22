import arcade
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
SCREEN_HEIGHT = 1200
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
        self.anchor_layout = UIAnchorLayout(y=-550)
        self.box_layout = UIBoxLayout(vertical=False, space_between=3)

        self.setup_widgets()
        self.anchor_layout.add(self.box_layout)
        self.manager.add(self.anchor_layout)

    def setup_widgets(self):
        button1 = UIFlatButton(text="1", width=100, height=50, color=arcade.color.GHOST_WHITE)
        self.box_layout.add(button1)
        button2 = UIFlatButton(text="2", width=100, height=50, color=arcade.color.GHOST_WHITE)
        self.box_layout.add(button2)
        button3 = UIFlatButton(text="3", width=100, height=50, color=arcade.color.GHOST_WHITE)
        self.box_layout.add(button3)
        button4 = UIFlatButton(text="4", width=100, height=50, color=arcade.color.GHOST_WHITE)
        self.box_layout.add(button4)

    def on_update(self, delta_time: float):
        self.cube_sprite_list.update()
        self.cube_move(delta_time)

    def on_draw(self):
        self.clear()
        self.manager.draw()
        self.cube_sprite_list.draw()

    def cube_move(self, delta_time):
        self.cube.angle += 1 \
                           * 1 * delta_time


def setup_game(width=800, height=600, title="Tycoon"):
    game = MyGUIWindow(width, height, title)
    return game


def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()