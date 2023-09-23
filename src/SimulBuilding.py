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


# Normaliser
normalizer = 600 / 20

# Simulation Class
class Simulation:
    def __init__(self, dt):
        # Initialize simulation variables
        self.agents = []  # List of agents
        self.walls = []   # List of wall positions [(x1, y1, x2, y2), ...]
        self.exit = []   # List of exit positions [(x, y), ...]

        self.motion = Motion(dt)

    def update_position(self):
        self.motion.euler(self.agents, self.walls)





simul = Simulation(0.1)
navig = Navigation(window, canvas)

simul.agents = [Agent(np.array([10, 10]), np.array([0, 0]), 1.5, 0.5, 80, 0.5) , Agent(np.array([12, 12]), np.array([0, 0]), 1.5, 0.5, 80, 0.5)]
simul.walls = [Wall(np.array([3, 5]), np.array([7, 5]))]


# Placeholder function to draw walls
def draw_walls():
    # Add code here to draw walls on the canvas
    pass

# Placeholder function to draw agents
def draw_agents(agent_positions):
    # Add code here to draw agents on the canvas
    pass

# Placeholder function to draw exits
def draw_exits(exit_positions):
    # Add code here to draw exits on the canvas
    pass

# Create a function to update the canvas based on simulation data
def update_canvas(simul):
    canvas.delete("all")  # Clear the canvas

    # Draw walls
    for wall in simul.walls:
        x1 = wall.ext1[0] * normalizer
        y1 = wall.ext1[1] * normalizer
        x2 = wall.ext2[0] * normalizer
        y2 = wall.ext2[1] * normalizer
        canvas.create_line(x1, y1, x2, y2, fill="blue", width=2)

    # Draw exits
    for exit_pos in simul.exit:
        x, y = exit_pos * normalizer
        canvas.create_rectangle(x - 5, y - 5, x + 5, y + 5, fill="green")

    # Draw agents
    for agent in simul.agents:
        x, y = agent.position * normalizer
        canvas.create_circle(x, y, agent.radius * normalizer,fill="red")

update_canvas(simul)

# Start the simulation loop
def start_simulation():
    navig.menu()
    """
    simul.update_position()
    update_canvas(simul)
    window.after(100, start_simulation)  # Schedule the next update after 100 milliseconds
    """

# Add a button to start the simulation
start_button = tk.Button(window, text="Start !", command=start_simulation)
start_button.pack(fill='x', ipady=10, pady=3)


# Start the Tkinter main loop
window.geometry("800x600")
window.mainloop()
