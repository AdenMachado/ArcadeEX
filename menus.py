import arcade
import data
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
    UITextWidget,
)


class SubMenuForUpgr(arcade.gui.UIMouseFilterMixin, arcade.gui.UIAnchorLayout):

    def __init__(
            self,
            posx,
            posy,
    ):
        super().__init__(size_hint=(posx, posy))

        frame = self.add(arcade.gui.UIAnchorLayout(width=300, height=400, size_hint=None, ))
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
        box_layout = UIBoxLayout(vertical=True, space_between=10)
        text_layout = UIBoxLayout(vertical=True, space_between=60)

        self.text1 = arcade.gui.UITextWidget(text=f"Upgrade 1 - B(1bytes/sec)                             ")
        button1 = arcade.gui.UIFlatButton(text="Buy", width=50)
        box_layout.add(button1)
        button1.on_click = self.on_click_upg11

        self.text2 = arcade.gui.UITextWidget(text=f"Upgrade 2 - KB(10bytes/sec)                        ")
        button2 = arcade.gui.UIFlatButton(text="Buy", width=50)
        box_layout.add(button2)
        button2.on_click = self.on_click_upg12

        self.text3 = arcade.gui.UITextWidget(text=f"Upgrade 3 - MB(100bytes/sec)                    ")
        button3 = arcade.gui.UIFlatButton(text="Buy", width=50)
        box_layout.add(button3)
        button3.on_click = self.on_click_upg13

        self.text4 = arcade.gui.UITextWidget(text=f"Upgrade 4 - TB(1000bytes/sec)                   ")
        button4 = arcade.gui.UIFlatButton(text="Buy", width=50)
        box_layout.add(button4)
        button4.on_click = self.on_click_upg14

        text_layout.add(self.text1)
        text_layout.add(self.text2)
        text_layout.add(self.text3)
        text_layout.add(self.text4)

        back_button = arcade.gui.UIFlatButton(text="⛌", width=50)
        back_button.on_click = self.on_click_back_button

        widget_layout = arcade.gui.UIBoxLayout(align="left", space_between=10)
        widget_layout.add(back_button)

        frame.add(child=widget_layout, anchor_x="right", anchor_y="top")
        frame.add(child=box_layout, anchor_x="right", anchor_y="center")
        frame.add(child=text_layout, anchor_x="center", anchor_y="center")


    def on_click_back_button(self, event):
        self.parent.remove(self)

    def on_draw(self):
        self.clear()

    def on_click_upg11(self, event):
        data.upgr11 += 1

    def on_click_upg12(self, event):
        data.upgr12 += 1

    def on_click_upg13(self, event):
        data.upgr13 += 1

    def on_click_upg14(self, event):
        data.upgr14 += 1


class SubMenuSUpgrd(arcade.gui.UIMouseFilterMixin, arcade.gui.UIAnchorLayout):

    def __init__(
            self,
            posx,
            posy,
    ):
        super().__init__(size_hint=(posx, posy))

        frame = self.add(arcade.gui.UIAnchorLayout(width=300, height=400, size_hint=None, ))
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

        back_button = arcade.gui.UIFlatButton(text="⛌", width=50)
        back_button.on_click = self.on_click_back_button
        widget_layout = arcade.gui.UIBoxLayout(align="left", space_between=10)
        widget_layout.add(back_button)
        frame.add(child=widget_layout, anchor_x="right", anchor_y="top")

    def on_click_back_button(self, event):
        self.parent.remove(self)
