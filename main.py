import arcade
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

class SubMenu(arcade.gui.UIMouseFilterMixin, arcade.gui.UIAnchorLayout):

    def __init__(
        self,
    ):
        super().__init__(size_hint=(0.5, 0.4))

        frame = self.add(arcade.gui.UIAnchorLayout(width=300, height=400, size_hint=None,))
        frame.with_padding(all=20)

        frame.with_background(
            texture=arcade.gui.NinePatchTexture(
                left=7,
                right=7,
                bottom=7,
                top=7,
                texture=arcade.load_texture(
                    "sprites/menu.png"
                ),
            )
        )

        back_button = arcade.gui.UIFlatButton(text="Back", width=250)
        # The type of event listener we used earlier for the button will not work here.
        back_button.on_click = self.on_click_back_button

        # Internal widget layout to handle widgets in this class.
        widget_layout = arcade.gui.UIBoxLayout(align="left", space_between=10)

        widget_layout.add(back_button)

        frame.add(child=widget_layout, anchor_x="center_x", anchor_y="top")

    def on_click_back_button(self, event):
        self.parent.remove(self)


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
        self.buttons_list = []
        self.score = 0

        self.setup_widgets()
        self.anchor_layout.add(self.box_layout)
        self.manager.add(self.anchor_layout)

    def setup_widgets(self):
        button1 = UIFlatButton(text="1", width=100, height=50, color=arcade.color.GHOST_WHITE)
        self.box_layout.add(button1)
        button1.on_click = self.on_menu_click
        button2 = UIFlatButton(text="2", width=100, height=50, color=arcade.color.GHOST_WHITE)
        self.box_layout.add(button2)
        button3 = UIFlatButton(text="3", width=100, height=50, color=arcade.color.GHOST_WHITE)
        self.box_layout.add(button3)
        button4 = UIFlatButton(text="4", width=100, height=50, color=arcade.color.GHOST_WHITE)
        self.box_layout.add(button4)


    def on_update(self, delta_time: float):
        self.cube_sprite_list.update()
        self.cube_move(delta_time)
        self.text = arcade.Text(f"{self.score}", anchor_x="left", color=arcade.color.WHITE, font_size=17, x=50, y=1235)

    def setup(self):
        self.batch = Batch()

    def on_draw(self):
        self.clear()
        self.manager.draw()
        self.cube_sprite_list.draw()
        self.text.draw()
        arcade.draw_rect_outline(arcade.rect.XYWH(110, 1240, 200, 50), arcade.color.WHITE, 2)

    def on_mouse_press(self, x, y, button, key_modifiers):
        clicked_sprites = arcade.get_sprites_at_point((x, y), self.cube_sprite_list)
        if clicked_sprites:
            self.score += 1

    def cube_move(self, delta_time):
        self.cube.angle += (1 + self.score) * delta_time / 100

    def on_menu_click(self, event):
        menu = SubMenu()
        self.manager.add(menu, layer=1000000000)






def setup_game(width=800, height=600, title="Tycoon"):
    game = MyGUIWindow(width, height, title)
    return game


def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
