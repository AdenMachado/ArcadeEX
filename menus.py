import os
import arcade
import data
from arcade.gui import (
    UIAnchorLayout,
    UIBoxLayout,
    UITextWidget,
    UITextArea
)

font_path = os.path.join("Assets", "Fonts", "VMVSegaGenesis-Regular.otf")
font_name = "VMV Sega Genesis"
click_button_sound = arcade.load_sound("Assets/Sound/click_button.wav")


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

        self.text1 = arcade.gui.UITextWidget(text=f"Upgrade 1 - B(1bytes/sec)                          ")
        button1 = arcade.gui.UIFlatButton(text="Buy", width=50)
        box_layout.add(button1)
        button1.on_click = self.on_click_upg11
        self.text2 = arcade.gui.UITextWidget(text=f"Upgrade 2 - KB(6bytes/sec)                        ")
        button2 = arcade.gui.UIFlatButton(text="Buy", width=50)
        box_layout.add(button2)
        button2.on_click = self.on_click_upg12

        self.text3 = arcade.gui.UITextWidget(text=f"Upgrade 3 - MB(40bytes/sec)                    ")
        button3 = arcade.gui.UIFlatButton(text="Buy", width=50)
        box_layout.add(button3)
        button3.on_click = self.on_click_upg13

        self.text4 = arcade.gui.UITextWidget(text=f"Upgrade 4 - GB(300bytes/sec)                   ")
        button4 = arcade.gui.UIFlatButton(text="Buy", width=50)
        box_layout.add(button4)
        button4.on_click = self.on_click_upg14

        self.cost_text1 = arcade.gui.UITextWidget(text=f"Upgrade 1 costs - {convector(data.upgr11costs)} Bytes")
        self.cost_text2 = arcade.gui.UITextWidget(text=f"Upgrade 2 costs - {convector(data.upgr12costs)} Bytes")
        self.cost_text3 = arcade.gui.UITextWidget(text=f"Upgrade 3 costs - {convector(data.upgr13costs)} Bytes")
        self.cost_text4 = arcade.gui.UITextWidget(text=f"Upgrade 4 costs - {convector(data.upgr14costs)} Bytes")

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
        click_button_sound.play(volume=0.1)
        self.parent.remove(self)

    def on_draw(self):
        self.clear()
        self.manager.draw()

    def on_updater(self, dt):
        self.cost_text1.text = f"Upgrade 1 costs - {convector(data.upgr11costs)} Bytes"
        self.cost_text2.text = f"Upgrade 2 costs - {convector(data.upgr12costs)} Bytes"
        self.cost_text3.text = f"Upgrade 3 costs - {convector(data.upgr13costs)} Bytes"
        self.cost_text4.text = f"Upgrade 4 costs - {convector(data.upgr14costs)} Bytes"

    def on_click_upg11(self, event):
        click_button_sound.play(volume=0.1)
        if data.score >= data.upgr11costs:
            data.upgr11 += 1
            data.score -= data.upgr11costs
            data.upgr11costs = 20 * (1 + data.upgr11)
        self.on_updater(self)

    def on_click_upg12(self, event):
        click_button_sound.play(volume=0.1)
        if data.score >= data.upgr12costs:
            data.upgr12 += 1
            data.score -= data.upgr12costs
            data.upgr12costs = 150 * (1 + data.upgr12)
        self.on_updater(self)

    def on_click_upg13(self, event):
        click_button_sound.play(volume=0.1)
        if data.score >= data.upgr13costs:
            data.upgr13 += 1
            data.score -= data.upgr13costs
            data.upgr13costs = 1200 * (1 + data.upgr13)
        self.on_updater(self)

    def on_click_upg14(self, event):
        click_button_sound.play(volume=0.1)
        if data.score >= data.upgr14costs:
            data.upgr14 += 1
            data.score -= data.upgr14costs
            data.upgr14costs = 10_000 * (1 + data.upgr14)
        self.on_updater(self)


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
        arcade.load_font(font_path)

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

        self.text1 = arcade.gui.UITextWidget(text=f"Stone click(+2bytes/click)                      ")
        button1 = arcade.gui.UIFlatButton(text="Buy", width=50)
        box_layout.add(button1)
        button1.on_click = self.on_click_upg21
        self.text2 = arcade.gui.UITextWidget(text=f"Bronze click(+5bytes/click)                    ")
        button2 = arcade.gui.UIFlatButton(text="Buy", width=50)
        box_layout.add(button2)
        button2.on_click = self.on_click_upg22

        self.text3 = arcade.gui.UITextWidget(text=f"Silver click(+12bytes/click)                    ")
        button3 = arcade.gui.UIFlatButton(text="Buy", width=50)
        box_layout.add(button3)
        button3.on_click = self.on_click_upg23

        self.text4 = arcade.gui.UITextWidget(text=f"Gold click(+30bytes/click)                    ")
        button4 = arcade.gui.UIFlatButton(text="Buy", width=50)
        box_layout.add(button4)
        button4.on_click = self.on_click_upg24

        self.cost_text1 = arcade.gui.UITextWidget(text=f"Upgrade 1 costs - {convector(data.upgr21costs)} Bytes, 1 RED")
        self.cost_text2 = arcade.gui.UITextWidget(
            text=f"Upgrade 2 costs - {convector(data.upgr22costs)} Bytes, 1 GREEN")
        self.cost_text3 = arcade.gui.UITextWidget(text=f"Upgrade 3 costs - {convector(data.upgr23costs)} Bytes, 1 BLUE")
        self.cost_text4 = arcade.gui.UITextWidget(
            text=f"Upgrade 4 costs - {convector(data.upgr24costs)} Bytes, 1 WHITE")

        self.cost_text_layout.add(self.cost_text1)
        self.cost_text_layout.add(self.cost_text2)
        self.cost_text_layout.add(self.cost_text3)
        self.cost_text_layout.add(self.cost_text4)

        self.text_layout.add(self.text1)
        self.text_layout.add(self.text2)
        self.text_layout.add(self.text3)
        self.text_layout.add(self.text4)

        back_button = arcade.gui.UIFlatButton(text="⛌", width=50, )
        back_button.on_click = self.on_click_back_button

        widget_layout = arcade.gui.UIBoxLayout(align="left", space_between=10)
        widget_layout.add(back_button)

        frame.add(child=widget_layout, anchor_x="right", anchor_y="top")
        frame.add(child=box_layout, anchor_x="right", anchor_y="center")
        frame.add(child=self.text_layout, anchor_x="center", anchor_y="center")
        frame.add(child=self.cost_text_layout, anchor_x="center", anchor_y="bottom")

    def on_click_back_button(self, event):
        click_button_sound.play(volume=0.1)
        self.parent.remove(self)

    def on_draw(self):
        self.clear()
        self.manager.draw()

    def on_updater(self, dt):
        self.cost_text1.text = f"Upgrade 1 costs - {convector(data.upgr21costs)} Bytes, 1 RED"
        self.cost_text2.text = f"Upgrade 2 costs - {convector(data.upgr22costs)} Bytes, 1 BLUE"
        self.cost_text3.text = f"Upgrade 3 costs - {convector(data.upgr23costs)} Bytes, 1 GREEN"
        self.cost_text4.text = f"Upgrade 4 costs - {convector(data.upgr24costs)} Bytes, 1 WHITE"

    def on_click_upg21(self, event):
        click_button_sound.play(volume=0.1)
        if data.score >= data.upgr21costs and data.red >= 1:
            data.upgr21 += 1
            data.score -= data.upgr21costs
            data.red -= 1
            data.upgr21costs = 15 * (1 + data.upgr21 ** 2)
        self.on_updater(self)

    def on_click_upg22(self, event):
        click_button_sound.play(volume=0.1)
        if data.score >= data.upgr22costs and data.green >= 1:
            data.upgr22 += 1
            data.score -= data.upgr22costs
            data.green -= 1
            data.upgr22costs = 60 * (1 + data.upgr22 ** 2)
        self.on_updater(self)

    def on_click_upg23(self, event):
        click_button_sound.play(volume=0.1)
        if data.score >= data.upgr23costs and data.blue >= 1:
            data.upgr23 += 1
            data.score -= data.upgr23costs
            data.blue -= 1
            data.upgr23costs = 250 * (1 + data.upgr23 ** 2)
        self.on_updater(self)

    def on_click_upg24(self, event):
        click_button_sound.play(volume=0.1)
        if data.score >= data.upgr24costs and data.white >= 1:
            data.upgr24 += 1
            data.score -= data.upgr24costs
            data.white -= 1
            data.upgr24costs = 1000 * (1 + data.upgr24 ** 2)
        self.on_updater(self)


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

        self.text = UITextWidget(
            text=f"                                 You have clicks: {convector(data.currentclicks)}")
        self.text_layout.add(self.text)

        button1 = arcade.gui.UIFlatButton(text="Buy red color", width=250)
        box_layout.add(button1)
        button1.on_click = self.buy_red

        button2 = arcade.gui.UIFlatButton(text="Buy green color", width=250)
        box_layout.add(button2)
        button2.on_click = self.buy_green

        button3 = arcade.gui.UIFlatButton(text="Buy blue color", width=250)
        box_layout.add(button3)
        button3.on_click = self.buy_blue

        button4 = arcade.gui.UIFlatButton(text="Buy white color", width=250)
        box_layout.add(button4)
        button4.on_click = self.buy_white

        back_button = arcade.gui.UIFlatButton(text="⛌", width=50)
        back_button.on_click = self.on_click_back_button

        widget_layout = arcade.gui.UIBoxLayout(align="left", space_between=10)
        widget_layout.add(back_button)

        frame.add(child=widget_layout, anchor_x="right", anchor_y="top")
        frame.add(child=box_layout, anchor_x="right", anchor_y="center")
        frame.add(child=self.text_layout, anchor_x="left", anchor_y="top")
        frame.add(child=self.cost_text_layout, anchor_x="center", anchor_y="bottom")

    def on_click_back_button(self, event):
        click_button_sound.play(volume=0.1)
        self.parent.remove(self)

    def on_draw(self):
        self.clear()
        self.manager.draw()

    def on_updater(self, dt):
        self.text.text = f"                                 You have clicks: {convector(data.currentclicks)}"

    def buy_red(self, event):
        click_button_sound.play(volume=0.1)
        if data.currentclicks >= 100:
            data.red += 1
            data.currentclicks -= 100
            self.on_updater(self)

    def buy_green(self, event):
        click_button_sound.play(volume=0.1)
        if data.currentclicks >= 200:
            data.green += 1
            data.currentclicks -= 200
            self.on_updater(self)

    def buy_blue(self, event):
        click_button_sound.play(volume=0.1)
        if data.currentclicks >= 400:
            data.blue += 1
            data.currentclicks -= 400
            self.on_updater(self)

    def buy_white(self, event):
        click_button_sound.play(volume=0.1)
        if data.currentclicks >= 500:
            data.white += 1
            data.currentclicks -= 500
            self.on_updater(self)


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
        self.text_layout = UIBoxLayout(vertical=True, space_between=60)

        back_button = arcade.gui.UIFlatButton(text="⛌", width=50)
        back_button.on_click = self.on_click_back_button

        widget_layout = arcade.gui.UIBoxLayout(align="left", space_between=10)
        widget_layout.add(back_button)

        self.text1 = UITextWidget(text=f"Total clicks: {data.clicks}")
        self.text2 = UITextWidget(text=f"Total bytes spent: {data.spentmoney}")
        self.text3 = UITextWidget(text=f"Total upgrades purchased: {data.upgr21 + data.upgr22 + data.upgr23
                                                                    + data.upgr24}")
        self.text4 = UITextWidget(text=f"Total miners purchased: {data.upgr11 + data.upgr12 + data.upgr13
                                                                  + data.upgr14}")

        self.text_layout.add(self.text1)
        self.text_layout.add(self.text2)
        self.text_layout.add(self.text3)
        self.text_layout.add(self.text4)

        frame.add(child=widget_layout, anchor_x="right", anchor_y="top")
        frame.add(child=self.text_layout, anchor_x="center", anchor_y="center")

    def on_click_back_button(self, event):
        click_button_sound.play(volume=0.1)
        self.parent.remove(self)

    def on_draw(self):
        self.clear()
        self.manager.draw()


class SubMenuTutor(arcade.gui.UIMouseFilterMixin, arcade.gui.UIAnchorLayout):
    def __init__(
            self,
            posx,
            posy,
            texts,
            width,
            height
    ):
        super().__init__(size_hint=(posx, posy))

        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        frame = self.add(arcade.gui.UIAnchorLayout(width=width, height=height, size_hint=None))
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
        text = "\n".join(texts)
        text_area = UITextArea(text=text,
                               width=width - 90,
                               height=height - 100,
                               font_size=14)
        self.v_box = arcade.gui.UIBoxLayout()

        back_button = arcade.gui.UIFlatButton(text="⛌", width=100)
        back_button.on_click = self.on_click_back_button

        widget_layout = arcade.gui.UIBoxLayout(align="left", space_between=10)
        widget_layout.add(back_button)

        frame.add(child=widget_layout, anchor_x="center", anchor_y="bottom")
        frame.add(child=text_area, anchor_x="left", anchor_y="center")

    def on_click_back_button(self, event):
        click_button_sound.play(volume=0.1)
        self.parent.remove(self)

    def on_draw(self):
        self.clear()
        self.manager.draw()


def convector(num):
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'),
                         ['', 'K', 'M', 'B', 'T', "qd", "qt", "st", "sp", "oc", "nn", "dc", "un", "dd", "td"]
                         [magnitude])
