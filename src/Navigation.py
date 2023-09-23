import tkinter as tk
from tkinter import ttk
from Drawings import *

class Navigation:
    def __init__(self, simul, window, canvas):
        self.simul = simul
        self.window = window
        self.canvas = canvas
        self.current_menu = None  # Store the current active menu
        self.drawing = Drawings(self.simul, self.canvas)

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

        menu_func()

    def start_simulation(self):
        self.simul.run_simulation()
 
    def reset_canvas(self):
        self.simul.agents = []
        self.simul.walls = []
        self.simul.update_canvas()
        self.drawing.start_point = None

    def configure_room(self):
        def room_binds():
            self.canvas.bind("<Button-1>", self.drawing.draw_room)
            self.canvas.bind("<Motion>", self.drawing.draw_room_move)
        
        # Dropdown menu for room types
        tk.Label(self.window, text="Room Type", anchor='w').pack(fill='x', padx=10, pady=5)
        room_type_var = tk.StringVar()
        room_type_combobox = ttk.Combobox(self.window, textvariable=room_type_var, values=["Room Type 1", "Room Type 2", "Room Type 3", "Room Type 4"])
        room_type_combobox.pack(fill='x', padx=10, pady=5)
        #room_type_combobox.set("Room Type 1")  # Set the default value

        # Label for Tools
        tk.Label(self.window, text="Tools", anchor='w').pack(fill='x', padx=10, pady=10)

        def set_tool(tool_name):
            self.canvas.current_tool = tool_name  # Set the current tool in the canvas

        # Wall button
        wall_button = tk.Button(self.window, text="Wall", command=room_binds)
        wall_button.pack(padx=10, anchor='w')

        # Exit button
        exit_button = tk.Button(self.window, text="Exit", command=lambda:self.canvas.bind("<Button-1>", self.drawing.place_exit))
        exit_button.pack(padx=10, anchor='w')

        # Reset button
        reset_button = tk.Button(self.window, text="Reset", command=self.reset_canvas)
        reset_button.pack(padx=10, pady=5, anchor='w')


    def configure_agents(self):
        # Random Placement
        tk.Button(self.window,
                  text="Place Randomly",
                  command=lambda:self.canvas.bind("<Button-1>", self.drawing.random_place),
                  anchor='w',
                  bg='#f0f0f0',
                  activebackground='#bdbdbd').pack(fill='x', ipady=10, pady=3)

        # Number of agents slider
        num_agents_scale = tk.Scale(self.window, from_=0, to=100, orient='horizontal')
        num_agents_scale.pack(fill='x', padx=10, pady=5)        
        tk.Label(self.window, text="Number of Agents", anchor='w').pack(fill='x', padx=10)


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
        self.canvas.unbind("<Enter>")
        self.canvas.unbind("<Motion>")
        self.canvas.unbind("<Button-1>")

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
                  command=lambda: self.show_menu(self.configure_room),
                  anchor='w',
                  bg='#f0f0f0',
                  activebackground='#bdbdbd').pack(fill='x', ipady=10, pady=3)

        # Configure agents button
        tk.Button(self.window,
                  text="Agents Configuration",
                  command=lambda: self.show_menu(self.configure_agents),
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

