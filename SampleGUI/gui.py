import tkinter as tk
from tkinter import filedialog, messagebox


class GUI:
    def __init__(self):
        self.upload_var = None
        self.chart_var = None
        self.window = tk.Tk()
        self.window.protocol("WM_DELETE_WINDOW", self.close_window)

        # Source Block
        # Tkinter에서 위젯을 가로로 확장 하려면 fill=tk.X 옵션을 사용 하면 됩니다. 그러나 이 옵션은 위젯의 너비를 부모 위젯의 너비에
        # 맞추는 것이지, 내용을 가운데 정렬 하거나 오른쪽 정렬하는 것은 아닙니다. 위젯의 내용을 정렬 하려면 anchor 옵션을 사용 해야 합니다
        # 그러나 Entry 위젯과 Button 위젯에서는 anchor 옵션을 사용할 수 없습니다. 이 경우, Entry 위젯과 Button 위젯을 감싸는 Frame
        # 위젯을 만들고, 이 Frame 위젯을 가로로 확장하여 Entry 위젯과 Button 위젯을 가운데에 배치할 수 있습니다.
        self.source_frame = tk.Frame(self.window)
        self.source_frame.pack(fill=tk.X, padx=25, pady=10)  # Fill the window horizontally

        # Create a new frame to hold the folder label, entry, and button
        self.folder_frame = tk.Frame(self.source_frame)
        self.folder_frame.pack(fill=tk.X)

        self.folder_label = tk.Label(self.folder_frame, text="Source")
        self.folder_label.pack(side=tk.LEFT)  # Align the label to the left
        self.folder_entry = tk.Entry(self.folder_frame, width=50)
        self.folder_entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=10)  # Fill the parent widget horizontally
        self.folder_button = tk.Button(self.folder_frame, text="Select Folder", command=self.select_folder)
        self.folder_button.pack(side=tk.LEFT)

        # Select Block
        self.add_separator('Select')
        self.select_frame = tk.Frame(self.window)
        self.select_frame.pack(fill=tk.X, padx=25, pady=10)
        self.chart_check = tk.Checkbutton(self.select_frame, text="Chart", variable=self.chart_var)
        self.chart_check.pack(anchor='w')
        self.upload_check = tk.Checkbutton(self.select_frame, text="Upload", variable=self.upload_var)
        self.upload_check.pack(anchor='w')

        # Run Button Block
        # Tkinter에서 위젯을 가운데 정렬하려면 pack 메서드의 anchor 옵션을 사용할 수 있습니다. 그러나 이 옵션은 위젯의 위치를
        # 조정하는 것이지, 위젯의 너비를 조정하는 것은 아닙니다. 따라서, Run 버튼을 가운데에 배치하려면 Run 버튼을 감싸는
        # Frame 위젯을 만들고, 이 Frame 위젯을 가로로 확장하여 Run 버튼을 가운데에 배치할 수 있습니다.
        self.run_button_frame = tk.Frame(self.window)
        self.run_button_frame.pack(fill=tk.X, padx=25, pady=10)  # Adjust padding as needed
        # Create a new frame to hold the Run button
        self.run_button_inner_frame = tk.Frame(self.run_button_frame)
        self.run_button_inner_frame.pack(expand=True)

        self.run_button = tk.Button(self.run_button_inner_frame, text="Run", command=self.run_command, padx=80)
        self.run_button.pack(side=tk.LEFT)

        # Status Block
        self.add_separator('Status')
        self.status_frame = tk.Frame(self.window)
        self.status_frame.pack(fill=tk.X, padx=25, pady=10)
        self.status_label = tk.Label(self.status_frame, text="Status: ")
        self.status_label.pack(anchor='w')

        # Add a label to display status messages
        self.status_message = tk.StringVar()
        self.status_message.set("Waiting for input...")
        self.status_message_label = tk.Label(self.status_frame, textvariable=self.status_message,
                                             bg='lightgrey', bd=1, relief='solid', anchor='nw', width=80, height=15,
                                             padx=10, pady=10)
        self.status_message_label.pack(fill=tk.X, expand=True)

        # Chart Block
        self.add_separator('Chart')
        self.chart_frame = tk.Frame(self.window)
        self.chart_frame.pack(fill=tk.X, padx=10, pady=10)
        # Chart drawing will be implemented here

    def add_separator(self, block_name):
        separator_frame = tk.Frame(self.window)
        separator_frame.pack(fill=tk.X, padx=30, pady=5)

        # tk.Label(separator_frame, text=block_name).pack(side=tk.LEFT, anchor='w')  # Align the label to the left
        separator = tk.Frame(separator_frame, height=1, bg="black")
        separator.pack(side=tk.RIGHT, fill=tk.X, expand=True)

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        self.folder_entry.delete(0, tk.END)
        self.folder_entry.insert(0, folder_path)

    def run_command(self):
        self.status_message.set("Running command...")
        self.window.update_idletasks()
        # Run the command here
        self.status_message.set("Command completed.")
        self.window.update_idletasks()

    def close_window(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            # Release all resources and close the window safely
            self.window.destroy()

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    gui = GUI()
    gui.run()
