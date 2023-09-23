import tkinter as tk
from Drawings import *

class Navigation:
    def __init__(self, window, canvas):
        self.window = window
        self.canvas = canvas
        self.current_menu = None  # Store the current active menu

    def clear_tool_frame(self):
        # Remove all widgets from the tool frame
        for widget in self.window.winfo_children():
            if not isinstance(widget, tk.Canvas):
                widget.destroy()

    def show_menu(self, menu_func):
        # Clear the tool frame and show the specified menu
        self.clear_tool_frame()

        # Back button
        tk.Button(self.window, text="Back", command=self.menu, width=30, anchor='w', bg='#f0f0f0', activebackground='#bdbdbd').pack(fill='x', ipady=10, pady=3)

        menu_func(self, self.canvas)

    def start_simulation(self):
        # Add code to start the simulation here
        pass

    def configure_room(self):
        # Add code to configure the room here
        pass

    def configure_agents(self):
        # Add code to configure agents here
        pass

    def toggle_panic(self):
        # Add code to toggle panic mode here
        pass

    def toggle_external_phenomena(self):
        # Add code to toggle external phenomena here
        pass

    def exit_program(self):
        self.window.destroy()

    def menu(self):
        self.clear_tool_frame()

        # Start simulation button
        tk.Button(self.window,
                  text="Start Simulation",
                  command=self.start_simulation,
                  anchor='w',
                  bg='#ff6666',
                  activebackground='#bdbdbd').pack(fill='x', ipady=10, pady=3)

        # Configure room button
        tk.Button(self.window,
                  text="Room Configuration",
                  command=lambda: self.show_menu(Drawings.configure_room),
                  anchor='w',
                  bg='#f0f0f0',
                  activebackground='#bdbdbd').pack(fill='x', ipady=10, pady=3)

        # Configure agents button
        tk.Button(self.window,
                  text="Agents Configuration",
                  command=lambda: self.show_menu(Drawings.configure_agents),
                  anchor='w',
                  bg='#f0f0f0',
                  activebackground='#bdbdbd').pack(fill='x', ipady=10, pady=3)

        # Panic button
        tk.Button(self.window,
                  text="Panic \n (On/Off)",
                  command=self.toggle_panic,
                  anchor='w',
                  bg='#f0f0f0',
                  activebackground='#bdbdbd').pack(fill='x', ipady=10, pady=3)

        # External phenomena button
        tk.Button(self.window,
                  text="External Phenomena \n (On/Off)",
                  command=self.toggle_external_phenomena,
                  anchor='w',
                  bg='#f0f0f0',
                  activebackground='#bdbdbd').pack(fill='x', ipady=10, pady=3)

        # Exit button
        tk.Button(self.window,
                  text="Exit",
                  command=self.exit_program,
                  anchor='w',
                  bg='#f0f0f0',
                  activebackground='#bdbdbd').pack(fill='x', ipady=10, pady=3)

