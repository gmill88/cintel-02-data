import plotly.express as px
from shiny.express import ui, render
from shinywidgets import render_plotly
import palmerpenguins

penguins_df = palmerpenguins.load_penguins()

ui.page_opts(title="Miller Penguin Data")
with ui.layout_columns():

    @render_plotly
    def plot1():
        return px.histogram(px.data.tips(), y="tip")

    @render_plotly
    def plot2():
        return px.histogram(px.data.tips(), y="total_bill")
