from manimlib import *


class Introduction_Part1(Scene):
"""
在这个Introduction的部分中，主要介绍我们以及我们的视频内容，其中包括：
    介绍视频的合作者，提供思路的人员，为什么会想着做微积分系列
"""

    def construct(self):
        # 字幕
        caption_Chinese = [
            "",  # 0
        ]

        caption_English = [
            "This is a triangle",  # 0
        ]

        # 将字幕写成一个数组，方便调用与调试
        captainC = VGroup(*[TexText(cap, font='思源黑体 CN Bold', font_size=22).to_edge(DOWN * 1.5).add_background_rectangle(color=WHITE, buff=0.1, opacity=0.1)for cap in caption_Chinese])
        captainE = VGroup(*[TexText(caps, font_size=22).next_to(captainC, DOWN).add_background_rectangle(color=WHITE, buff=0.1, opacity=0.1)for caps in caption_English])
