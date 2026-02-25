
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

        self.manager = arcade.gui.UIManager()
        self.manager.enable()
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
        self.v_box = arcade.gui.UIBoxLayout()
        box_layout = UIBoxLayout(vertical=True, space_between=10)
        self.text_layout = UIBoxLayout(vertical=True, space_between=60)
        self.cost_text_layout = UIBoxLayout(vertical=True, space_between=13)

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

        self.text4 = arcade.gui.UITextWidget(text=f"Upgrade 4 - GB(1000bytes/sec)                   ")
        button4 = arcade.gui.UIFlatButton(text="Buy", width=50)
        box_layout.add(button4)
        button4.on_click = self.on_click_upg14

        self.cost_text1 = arcade.gui.UITextWidget(text=f"Upgrade 1 costs - {data.upgr11costs} Bytes")
        self.cost_text2 = arcade.gui.UITextWidget(text=f"Upgrade 2 costs - {data.upgr12costs} Bytes")
        self.cost_text3 = arcade.gui.UITextWidget(text=f"Upgrade 3 costs - {data.upgr13costs} Bytes")
        self.cost_text4 = arcade.gui.UITextWidget(text=f"Upgrade 4 costs - {data.upgr14costs} Bytes")

        self.cost_text_layout.add(self.cost_text1)
        self.cost_text_layout.add(self.cost_text2)
        self.cost_text_layout.add(self.cost_text3)
        self.cost_text_layout.add(self.cost_text4)

        self.text_layout.add(self.text1)
        self.text_layout.add(self.text2)
        self.text_layout.add(self.text3)
        self.text_layout.add(self.text4)

        back_button = arcade.gui.UIFlatButton(text="⛌", width=50)
        back_button.on_click = self.on_click_back_button

        widget_layout = arcade.gui.UIBoxLayout(align="left", space_between=10)
        widget_layout.add(back_button)

        frame.add(child=widget_layout, anchor_x="right", anchor_y="top")
        frame.add(child=box_layout, anchor_x="right", anchor_y="center")
        frame.add(child=self.text_layout, anchor_x="center", anchor_y="center")
        frame.add(child=self.cost_text_layout, anchor_x="center", anchor_y="bottom")

    def on_click_back_button(self, event):
        self.parent.remove(self)

    def on_draw(self):
        self.clear()
        self.manager.draw()

    def on_updater(self, dt):
        self.cost_text1.text = f"Upgrade 1 costs - {data.upgr11costs} Bytes"
        self.cost_text2.text = f"Upgrade 2 costs - {data.upgr12costs} Bytes"
        self.cost_text3.text = f"Upgrade 3 costs - {data.upgr13costs} Bytes"
        self.cost_text4.text = f"Upgrade 4 costs - {data.upgr14costs} Bytes"

    def on_click_upg11(self, event):
        self.on_updater(self)
        if data.score >= data.upgr11costs:
            data.upgr11 += 1
            data.score -= data.upgr11costs
            data.upgr11costs += 1 * 60 * data.upgr11

    def on_click_upg12(self, event):
        self.on_updater(self)
        if data.score >= data.upgr12costs:
            data.upgr12 += 1
            data.score -= data.upgr12costs
            data.upgr12costs += 10 * 60 * data.upgr12

    def on_click_upg13(self, event):
        self.on_updater(self)
        if data.score >= data.upgr13costs:
            data.upgr13 += 1
            data.score -= data.upgr13costs
            data.upgr13costs += 100 * 60 * data.upgr13

    def on_click_upg14(self, event):
        self.on_updater(self)
        if data.score >= data.upgr14costs:
            data.upgr14 += 1
            data.score -= data.upgr14costs
            data.upgr14costs += 1 * 60 * data.upgr14


class SubMenuSUpgrd(arcade.gui.UIMouseFilterMixin, arcade.gui.UIAnchorLayout):

    def __init__(
            self,
            posx,
            posy,
    ):
        super().__init__(size_hint=(posx, posy))

        self.manager = arcade.gui.UIManager()
        self.manager.enable()
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
        self.v_box = arcade.gui.UIBoxLayout()
        box_layout = UIBoxLayout(vertical=True, space_between=10)
        self.text_layout = UIBoxLayout(vertical=True, space_between=60)
        self.cost_text_layout = UIBoxLayout(vertical=True, space_between=13)

        self.text1 = arcade.gui.UITextWidget(text=f"Click upgr - Stone(+1bytes/click)                      ")
        button1 = arcade.gui.UIFlatButton(text="Buy", width=50)
        box_layout.add(button1)
        button1.on_click = self.on_click_upg21
        self.text2 = arcade.gui.UITextWidget(text=f"Click upgr - Bronze(+5bytes/click)                    ")
        button2 = arcade.gui.UIFlatButton(text="Buy", width=50)
        box_layout.add(button2)
        button2.on_click = self.on_click_upg22

        self.text3 = arcade.gui.UITextWidget(text=f"Click upgr - Silver(+10bytes/click)                    ")
        button3 = arcade.gui.UIFlatButton(text="Buy", width=50)
        box_layout.add(button3)
        button3.on_click = self.on_click_upg23

        self.text4 = arcade.gui.UITextWidget(text=f"Click upgr - Gold(+100bytes/click)                   ")
        button4 = arcade.gui.UIFlatButton(text="Buy", width=50)
        box_layout.add(button4)
        button4.on_click = self.on_click_upg24

        self.cost_text1 = arcade.gui.UITextWidget(text=f"Upgrade 1 costs - {data.upgr21costs} Bytes")
        self.cost_text2 = arcade.gui.UITextWidget(text=f"Upgrade 2 costs - {data.upgr22costs} Bytes")
        self.cost_text3 = arcade.gui.UITextWidget(text=f"Upgrade 3 costs - {data.upgr23costs} Bytes")
        self.cost_text4 = arcade.gui.UITextWidget(text=f"Upgrade 4 costs - {data.upgr24costs} Bytes")

        self.cost_text_layout.add(self.cost_text1)
        self.cost_text_layout.add(self.cost_text2)
        self.cost_text_layout.add(self.cost_text3)
        self.cost_text_layout.add(self.cost_text4)

        self.text_layout.add(self.text1)
        self.text_layout.add(self.text2)
        self.text_layout.add(self.text3)
        self.text_layout.add(self.text4)

        back_button = arcade.gui.UIFlatButton(text="⛌", width=50)
        back_button.on_click = self.on_click_back_button

        widget_layout = arcade.gui.UIBoxLayout(align="left", space_between=10)
        widget_layout.add(back_button)

        frame.add(child=widget_layout, anchor_x="right", anchor_y="top")
        frame.add(child=box_layout, anchor_x="right", anchor_y="center")
        frame.add(child=self.text_layout, anchor_x="center", anchor_y="center")
        frame.add(child=self.cost_text_layout, anchor_x="center", anchor_y="bottom")

    def on_click_back_button(self, event):
        self.parent.remove(self)

    def on_draw(self):
        self.clear()
        self.manager.draw()

    def on_updater(self, dt):
        self.cost_text1.text = f"Upgrade 1 costs - {data.upgr21costs} Bytes"
        self.cost_text2.text = f"Upgrade 2 costs - {data.upgr22costs} Bytes"
        self.cost_text3.text = f"Upgrade 3 costs - {data.upgr23costs} Bytes"
        self.cost_text4.text = f"Upgrade 4 costs - {data.upgr24costs} Bytes"

    def on_click_upg21(self, event):
        self.on_updater(self)
        if data.score >= data.upgr21costs:
            data.upgr21 += 1
            data.score -= data.upgr21costs
            print("Succesful")

    def on_click_upg22(self, event):
        self.on_updater(self)
        if data.score >= data.upgr22costs:
            data.upgr22 += 1
            data.score -= data.upgr22costs
            print("Succesful")

    def on_click_upg23(self, event):
        self.on_updater(self)
        if data.score >= data.upgr23costs:
            data.upgr23 += 1
            data.score -= data.upgr23costs
            print("Succesful")

    def on_click_upg24(self, event):
        self.on_updater(self)
        if data.score >= data.upgr24costs:
            data.upgr24 += 1
            data.score -= data.upgr24costs
            print("Succesful")


class SubMenuMiners(arcade.gui.UIMouseFilterMixin, arcade.gui.UIAnchorLayout):
    def __init__(
            self,
            posx,
            posy,
    ):
        super().__init__(size_hint=(posx, posy))

        self.manager = arcade.gui.UIManager()
        self.manager.enable()
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
        self.v_box = arcade.gui.UIBoxLayout()
        box_layout = UIBoxLayout(vertical=True, space_between=15)
        self.text_layout = UIBoxLayout(vertical=True, space_between=60)
        self.cost_text_layout = UIBoxLayout(vertical=True, space_between=13)

        button1 = arcade.gui.UIFlatButton(text="Buy", width=250)
        box_layout.add(button1)
        button1.on_click = self.on_click_upg21

        button2 = arcade.gui.UIFlatButton(text="Buy", width=250)
        box_layout.add(button2)
        button2.on_click = self.on_click_upg22

        button3 = arcade.gui.UIFlatButton(text="Buy", width=250)
        box_layout.add(button3)
        button3.on_click = self.on_click_upg23

        button4 = arcade.gui.UIFlatButton(text="Buy", width=250)
        box_layout.add(button4)
        button4.on_click = self.on_click_upg24

        back_button = arcade.gui.UIFlatButton(text="⛌", width=50)
        back_button.on_click = self.on_click_back_button

        widget_layout = arcade.gui.UIBoxLayout(align="left", space_between=10)
        widget_layout.add(back_button)

        frame.add(child=widget_layout, anchor_x="right", anchor_y="top")
        frame.add(child=box_layout, anchor_x="right", anchor_y="center")
        frame.add(child=self.text_layout, anchor_x="center", anchor_y="center")
        frame.add(child=self.cost_text_layout, anchor_x="center", anchor_y="bottom")

    def on_click_back_button(self, event):
        self.parent.remove(self)

    def on_draw(self):
        self.clear()
        self.manager.draw()

    def on_updater(self, dt):
        pass

    def on_click_upg21(self, event):
        pass

    def on_click_upg22(self, event):
        pass

    def on_click_upg23(self, event):
        pass

    def on_click_upg24(self, event):
        pass


class SubMenuStatic(arcade.gui.UIMouseFilterMixin, arcade.gui.UIAnchorLayout):
    def __init__(
            self,
            posx,
            posy,
    ):
        super().__init__(size_hint=(posx, posy))

        self.manager = arcade.gui.UIManager()
        self.manager.enable()
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
        self.v_box = arcade.gui.UIBoxLayout()
        box_layout = UIBoxLayout(vertical=True, space_between=15)
        self.text_layout = UIBoxLayout(vertical=True, space_between=60)
        self.cost_text_layout = UIBoxLayout(vertical=True, space_between=13)

        button1 = arcade.gui.UIFlatButton(text="Buy", width=250)
        box_layout.add(button1)
        button1.on_click = self.on_click_upg21

        button2 = arcade.gui.UIFlatButton(text="Buy", width=250)
        box_layout.add(button2)
        button2.on_click = self.on_click_upg22

        button3 = arcade.gui.UIFlatButton(text="Buy", width=250)
        box_layout.add(button3)
        button3.on_click = self.on_click_upg23

        button4 = arcade.gui.UIFlatButton(text="Buy", width=250)
        box_layout.add(button4)
        button4.on_click = self.on_click_upg24

        back_button = arcade.gui.UIFlatButton(text="⛌", width=50)
        back_button.on_click = self.on_click_back_button

        widget_layout = arcade.gui.UIBoxLayout(align="left", space_between=10)
        widget_layout.add(back_button)

        frame.add(child=widget_layout, anchor_x="right", anchor_y="top")
        frame.add(child=box_layout, anchor_x="right", anchor_y="center")
        frame.add(child=self.text_layout, anchor_x="center", anchor_y="center")
        frame.add(child=self.cost_text_layout, anchor_x="center", anchor_y="bottom")

    def on_click_back_button(self, event):
        self.parent.remove(self)

    def on_draw(self):
        self.clear()
        self.manager.draw()

    def on_updater(self, dt):
        pass

    def on_click_upg21(self, event):
        pass

    def on_click_upg22(self, event):
        pass

    def on_click_upg23(self, event):
        pass

    def on_click_upg24(self, event):
        pass