import os
import multiprocessing
import matplotlib.pyplot as plt

def generate_plot(data):
    """Function to generate and display the plot."""
    x, y = data
    plt.plot(x, y)
    plt.title("Generated Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()

if __name__ == "__main__":
    # Set the multiprocessing start method
    multiprocessing.set_start_method("spawn")

    # Place Kivy imports here to ensure they're only in the main process
    from kivy.app import App
    from kivy.uix.button import Button
    from kivy.uix.boxlayout import BoxLayout

    class PlottingApp(App):
        def build(self):
            layout = BoxLayout(orientation="vertical")
            plot_button = Button(text="Generate Plot")
            plot_button.bind(on_press=self.generate_plot)
            layout.add_widget(plot_button)
            return layout

        def generate_plot(self, *args):
            x = [1, 2, 3, 4, 5]
            y = [i ** 2 for i in x]
            data = (x, y)
            plot_process = multiprocessing.Process(target=generate_plot, args=(data,))
            plot_process.start()
            self.plot_processes.append(plot_process)

        def on_stop(self):
            for process in self.plot_processes:
                if process.is_alive():
                    process.terminate()
            super().on_stop()

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.plot_processes = []

    PlottingApp().run()
