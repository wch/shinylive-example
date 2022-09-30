from shiny import App, render, ui
import numpy as np
import matplotlib.pyplot as plt

app_ui = ui.page_fluid(
    ui.layout_sidebar(
        ui.panel_sidebar(
            ui.input_slider("period", "Period", 0.5, 4, 1, step=0.5),
            ui.input_slider("amplitude", "Amplitude", 0, 2, 1, step=0.25),
            ui.input_slider("shift", "Phase shift", 0, 2, 0, step=0.1),
        ),
        ui.panel_main(
            ui.output_plot("plot"),
        ),
    ),
)


def server(input, output, session):
    @output
    @render.plot(alt="Sine wave")
    def plot():
        t = np.arange(0.0, 4.0, 0.01)
        s = input.amplitude() * np.sin(
            2 * np.pi / input.period() * (t - input.shift() / 2)
        )
        fig, ax = plt.subplots()
        ax.set_ylim([-2, 2])
        ax.plot(t, s)
        ax.grid()


app = App(app_ui, server)
