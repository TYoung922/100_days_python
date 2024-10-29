# from time import sleep
# from turtle import Turtle
#
# # starting = [(0, 0), (-50, 0), (-100, 0)]
# # yellow_row_1 = [(0, 0), (59, 0)]
# start = -280
# end = 280
# increment = 35
# current = start
#
# coordinates = []
# while current <= end:
#     coordinates.append((current, 0))
#     current += increment
#
# print(coordinates)
#
#
# class BlockGrid:
#     def __init__(self):
#         self.blocks = []
#         # self.create_grid()
#         self.create_block((0,0), 'yellow')
#
#     def create_block(self, position, color):
#         block = Turtle()
#         block.shape("square")
#         block.color(color)
#         block.shapesize(stretch_wid=1, stretch_len=1.5)
#         block.penup()
#         block.goto(position)
#         self.blocks.append(block)
#
#     def create_grid(self):
#         for i in coordinates:
#             self.create_block(i, 'yellow')
#
#     def delete_block(self, index):
#         del coordinates[index]
#         self.clear_grid()
#         self.create_grid()
#
#     def clear_grid(self):
#         for block in self.blocks:
#             block.hideturtle()
#         self.blocks.clear()
#
#     def detect_collision(self, ball):
#         for i, (x, y) in enumerate(coordinates):
#             if ball.distance(x, y) < 20:
#                 self.delete_block(i)
#                 return True


from turtle import Turtle

# Parameters for the grid
start = -280
end = 280
increment = 35  # Space between blocks in a row
row_height = 35  # Vertical distance between rows


# Define colors for each pair of rows
row_colors = ['yellow', 'yellow', 'green', 'green', 'orange', 'orange', 'red', 'red']

# Generate coordinates with color for 8 rows
coordinates = []
# coordinates = [(-20, 0, 'yellow')]
for row_num, color in enumerate(row_colors):
    current_x = start
    y_position = (row_num + 1) * row_height  # Position each row at a different y level
    while current_x <= end:
        coordinates.append((current_x, y_position, color))
        current_x += increment

# print(coordinates)
blocks_remaining = len(coordinates)
print(blocks_remaining)

class BlockGrid:
    def __init__(self):
        self.blocks = []
        self.create_grid()

    def create_block(self, position, color):
        block = Turtle()
        block.shape("square")
        block.color(color)
        block.shapesize(stretch_wid=1, stretch_len=1.5)
        block.penup()
        block.goto(position)
        self.blocks.append(block)

    def create_grid(self):
        for (x, y, color) in coordinates:
            self.create_block((x, y), color)

    def delete_block(self, index):
        global blocks_remaining
        del coordinates[index]
        blocks_remaining = len(coordinates)
        print(blocks_remaining)
        self.clear_grid()
        self.create_grid()

    def clear_grid(self):
        for block in self.blocks:
            block.hideturtle()
        self.blocks.clear()

    def detect_collision(self, ball):
        for i, (x, y, color) in enumerate(coordinates):
            if ball.distance(x, y) < 20:
                self.delete_block(i)
                return i, color  # Return both index and color
        return None, None

    def out_of_blocks(self):
        if blocks_remaining == 0:
            return False
        else:
            return True
