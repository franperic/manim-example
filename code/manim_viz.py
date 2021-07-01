import numpy as np
import pandas as pd

from manim import *

data = pd.read_csv("data/illustration.csv")

# Config
CUSTOM_BLUE = "#013848"
CUSTOM_GREY = "#696969"
CUSTOM_ORANGE = "#ff8000"
config.background_color = WHITE
config.axes_color = CUSTOM_GREY

# Visualizations
# Single Time Series
class TimeSeriesPlot(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 182],
            y_range=[50, 550],
            x_length=10,
            axis_config={"color": CUSTOM_GREY, "include_ticks": False},
            tips=True,
        )

        axes_labels = axes.get_axis_labels(x_label="Time", y_label="Sales")
        ts1 = axes.get_graph(
            lambda x: data.loc[x, "var1"], x_range=[0, 168, 1], color=CUSTOM_BLUE
        )
        pred1 = axes.get_graph(
            lambda x: data.loc[x, "var1"], x_range=[169, 181, 1], color=CUSTOM_ORANGE
        )

        self.add(axes, axes_labels, ts1, pred1)


# Animation
class TimeSeriesAnimation(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 182],
            y_range=[50, 550],
            x_length=10,
            axis_config={"color": CUSTOM_GREY, "include_ticks": False},
            tips=True,
        )

        axes_labels = axes.get_axis_labels(x_label="Time", y_label="Sales")
        ts1 = axes.get_graph(
            lambda x: data.loc[x, "var1"], x_range=[0, 181, 1], color=CUSTOM_BLUE
        )

        ts2 = axes.get_graph(
            lambda x: data.loc[x, "var2"], x_range=[0, 181, 1], color=CUSTOM_BLUE
        )

        self.add(axes, axes_labels)
        self.play(FadeIn(ts1))
        self.wait(4)
        self.play(FadeOut(ts1))
        self.play(FadeIn(ts2))
        self.wait(4)
