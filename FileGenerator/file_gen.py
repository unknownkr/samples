import msvcrt
import os
import shutil
import time
import tkinter as tk
import tkinter.messagebox as messagebox


class App:
    def __init__(self):
        self.waiting = False
        self.window = tk.Tk()

        # Create a new frame to hold the button
        self.button_frame = tk.Frame(self.window)
        self.button_frame.pack(fill=tk.X, expand=True)

        self.button_create = tk.Button(self.button_frame, text="Create files", command=self.on_button_create)
        self.button_create.pack(padx=120, pady=30)

        self.message_frame = tk.Frame(self.window)
        self.message_frame.pack(padx=30, pady=30)

        # Create a scrollbar
        self.scrollbar = tk.Scrollbar(self.message_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.message_text = tk.Text(self.message_frame, bd=1, relief='solid', width=80, height=15, yscrollcommand=self.scrollbar.set)
        self.message_text.pack(fill=tk.X, expand=True)

        # Connect the scrollbar to the Text widget
        self.scrollbar.config(command=self.message_text.yview)

        # Register the close_window method to be called when the window is closed
        self.window.protocol("WM_DELETE_WINDOW", self.close_window)

    def on_button_create(self):
        # This method is called when the button is clicked
        print("Button clicked!")
        path = os.getcwd() + "/Exclusive_lock_test"
        self.delete_directory(path)

        self.waiting = True

        try:
            if not os.path.exists(path):
                os.makedirs(path)
                print("Directory created successfully!")
            else:
                print("Directory already exists!")

            files = []
            # Create 20 files and hold the file objects in a list and possess the file exclusively
            for i in range(20):
                file_path = os.path.join(path, f"file_{i}.txt")
                file = open(file_path, "x")
                msvcrt.locking(file.fileno(), msvcrt.LK_LOCK, os.path.getsize(file_path))
                file.write(f"This is file {i}")
                files.append(file)
            print("Files created successfully!")
            self.message_text.insert(tk.END, f"{len(files)} Files created successfully!\n")
            self.window.update_idletasks()

            # Close file one by one every 3 seconds
            for f in files:
                time.sleep(3)
                f.close()
                print(f"File {f.name} closed successfully!")
                self.message_text.insert(tk.END, f"File {f.name} closed successfully!\n")
                self.window.update_idletasks()
        except Exception as e:
            print(f"An error occurred: {e}")

    def delete_directory(self, dir_path):
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)
            print(f"'{dir_path}' directory deleted.")

    def close_window(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            # Release all resources and close the window safely
            self.window.destroy()

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
