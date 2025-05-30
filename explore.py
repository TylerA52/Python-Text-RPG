from character import *


class Explore:
    def __init__(self, world_map, start_location=(0, 0)):
        self.world_map = world_map
        self.player_location = start_location

    def show_map(self):
        x, y = self.player_location
        print(f"\nYou are at location ({x}, {y}):")
        print(self.world_map[y][x]) 

    def get_current_location(self):
        x, y = self.player_location
        return (x, y), self.world_map[y][x]

    def move(self, direction):
        x, y = self.player_location
        if direction == 'n' and y > 0:
            self.player_location = (x, y - 1)
        elif direction == 's' and y < len(self.world_map) - 1:
            self.player_location = (x, y + 1)
        elif direction == 'w' and x > 0:
            self.player_location = (x - 1, y)
        elif direction == 'e' and x < len(self.world_map[0]) - 1:
            self.player_location = (x + 1, y)
        else:
            print("You can't go that way!")

    def get_directions(self):
        directions = []
        x, y = self.player_location
        if y > 0:
            directions.append("north")
        if y < len(self.world_map) - 1:
            directions.append("south")
        if x > 0:
            directions.append("west")
        if x < len(self.world_map[0]) - 1:
            directions.append("east")
        return directions
