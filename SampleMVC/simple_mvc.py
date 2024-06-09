import tkinter as tk


class Model:
    def __init__(self):
        self.data = None

    def load_data(self, path):
        # Load data from the given path
        pass

    def process_data(self):
        # Process the data
        pass


class View:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.pack()

        self.run_button = tk.Button(self.frame, text="Run")
        self.run_button.pack(side=tk.LEFT)

    def set_run_button_command(self, command):
        self.run_button.config(command=command)


class Controller:
    def __init__(self):
        self.root = tk.Tk()
        self.model = Model()
        self.view = View(self.root)
        self.view.set_run_button_command(self.run_command)

    def run_command(self):
        # Load and process the data when the Run button is clicked
        self.model.load_data("path/to/data")
        self.model.process_data()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = Controller()
    app.run()
