import tkinter as tk

from Model import *
from Navigation import *

# Create a Tkinter window
window = tk.Tk()
window.title("Building Simulation")


# Define the tool section and the canvas to draw on
canvas = tk.Canvas(window,width = 600, height = 600, bg = 'white')
canvas.pack(side = 'right')


# Create a circle in Tkinter
def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle


# Simulation Class
class Simulation:
    def __init__(self, dt, window, canvas):
        # Normaliser
        self.normalizer = 600 / 20

        # Initialize simulation variables
        self.agents = []  # List of agents
        self.walls = []   # List of wall positions [(x1, y1, x2, y2), ...]
        self.exit = np.array([1, 1])   # List of exit positions [(x, y), ...]

        self.dt = dt
        self.window = window
        self.canvas = canvas

        self.navig = Navigation(self, self.window, self.canvas)
        self.motion = Motion()

    def update_exit(self):
        for agent in self.agents:
            agent.exit = self.exit
            agent.speed = agent.f_DesiredSpeed()
    
    # Create a function to update the canvas based on simulation data
    def update_canvas(self):
        self.canvas.delete("all")  # Clear the canvas

        # Draw walls
        for wall in self.walls:
            x1 = wall.ext1[0] * self.normalizer
            y1 = wall.ext1[1] * self.normalizer
            x2 = wall.ext2[0] * self.normalizer
            y2 = wall.ext2[1] * self.normalizer
            self.canvas.create_line(x1, y1, x2, y2, fill="blue", width=2)

        # Draw exits
        x, y = self.exit * self.normalizer
        self.canvas.create_line(x - 5, y, x + 5, y, fill="green")
        self.canvas.create_line(x, y - 5, x, y + 5, fill="green")

        # Draw agents
        for agent in self.agents:
            x, y = agent.position * self.normalizer
            self.canvas.create_circle(x, y, agent.radius * self.normalizer,fill="red")
    
    def run_simulation(self):
        self.motion.euler(self.agents, self.walls, self.dt)
        self.update_canvas()
        window.after(100, self.run_simulation)


simul = Simulation(0.1, window, canvas)

simul.agents = [Agent(np.array([10, 10]), simul.exit, 1.5, 0.5, 80, 0.5) , Agent(np.array([12, 12]), np.array([0, 0]), 1.5, 0.5, 80, 0.5)]
simul.walls = [Wall(np.array([3, 5]), np.array([7, 5]))]


simul.update_canvas()

# Start the simulation loop
def start():
    simul.navig.menu()

# Add a button to start the simulation
start_button = tk.Button(window, text="Start !", command=start)
start_button.pack(fill='x', ipady=10, pady=3)


# Start the Tkinter main loop
window.geometry("800x600")
window.mainloop()
