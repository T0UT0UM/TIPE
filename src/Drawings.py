import numpy as np
from Model import *

class Drawings:
    def __init__(self, simul, canvas):
        self.canvas = canvas
        self.simul = simul

        self.start_point = None
        self.previous_point = None
        self.preview_line = None
        self.min_distance = 5  # Minimum distance to consider drawing as closed
    
    def draw_room(self, event):
        if self.start_point is None:
            # Set the starting point
            self.start_point = (event.x, event.y)
            self.previous_point = self.start_point
        else :
            current_point = self.room_CurrentPoint(event)

            # Draw the preview line
            self.simul.walls.append(Wall(np.array(self.previous_point)/self.simul.normalizer,
                                         np.array(current_point)/self.simul.normalizer))
            self.simul.update_canvas()
            self.preview_line = None

            # Update the previous point
            self.previous_point = current_point

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
        else:
            current_point = (self.previous_point[0], current_point[1])  # Force vertical line
        
        return current_point


    def distance(self, point1, point2):
        # Calculate the distance between two points
        x1, y1 = point1
        x2, y2 = point2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


    
    def random_place(self, event):
        # Complete the code
        pass

    def place_exit(self, event):
        # Complete the code
        print(2)

    
    def place_exit(self, event):
        # Implement the logic to place the exit here
        pass
