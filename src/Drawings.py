import numpy as np
from Model import *

class Drawings:
    def __init__(self, simul, canvas):
        self.canvas = canvas
        self.simul = simul

        self.start_point = None
        self.previous_point = None
        self.preview_line = None

    def on_canvas_enter(self, event):
        # Cursor enters the canvas, show the preview line if it exists
        if self.preview_line:
            self.canvas.itemconfig(self.preview_line, state="normal")

    def on_canvas_leave(self, event):
        # Cursor leaves the canvas, hide the preview line if it exists
        if self.preview_line:
            self.canvas.itemconfig(self.preview_line, state="hidden")
    
    def draw_room(self, event):
        if self.start_point is None:
            # Set the starting point
            self.start_point = (event.x, event.y)
            self.previous_point = self.start_point
        else :
            current_point = self.room_CurrentPoint(event)

            # Add the wall in simulation data
            self.simul.walls.append(Wall(np.array(self.previous_point)/self.simul.normalizer,
                                         np.array(current_point)/self.simul.normalizer))
            self.simul.update_canvas()
            self.preview_line = None

            # Update the previous point
            self.previous_point = current_point

            if current_point == self.start_point:
                self.start_point = None
                self.previous_point = None
                self.preview_line = None
                

    def draw_room_move(self, event):
        if self.start_point is not None:
            current_point = self.room_CurrentPoint(event)

            if self.preview_line:
                self.canvas.delete(self.preview_line)

            self.preview_line = self.canvas.create_line(self.previous_point[0], self.previous_point[1], current_point[0], current_point[1], dash=(4, 2))

    def room_CurrentPoint(self, event):
        current_point = (event.x, event.y)

        # Calculate the absolute differences in x and y
        dx = abs(current_point[0] - self.previous_point[0])
        dy = abs(current_point[1] - self.previous_point[1])
        
        # Check if the drawing is closer to being horizontal or vertical
        if dx > dy:
            current_point = (current_point[0], self.previous_point[1])  # Force horizontal line
            for wall in self.simul.walls:
                if abs(current_point[0] - wall.ext1[0]*self.simul.normalizer) < 20:
                    current_point = (wall.ext1[0]*self.simul.normalizer, current_point[1])
        else:
            current_point = (self.previous_point[0], current_point[1])  # Force vertical line
            for wall in self.simul.walls:
                if abs(current_point[1] - (wall.ext1[1]*self.simul.normalizer)) < 20:
                    current_point = (current_point[0], wall.ext1[1]*self.simul.normalizer)
        return current_point

    
    def place_agent(self, event):
       self.simul.agents.append(Agent(np.array([event.x, event.y])/self.simul.normalizer,
                                     self.simul.exit,
                                     np.random.normal(1.5, 0.02, 1)[0],
                                     np.random.normal(0.4, 0.02, 1)[0],
                                     np.random.normal(80, 10, 1)[0],
                                     0.5))
       self.simul.update_canvas()

    def random_place(self):
        pass

    def place_exit(self, event):
        self.simul.exit = np.array([event.x/self.simul.normalizer, event.y/self.simul.normalizer])
        self.simul.update_canvas()
        self.simul.update_exit()