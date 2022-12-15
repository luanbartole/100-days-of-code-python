from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_tail = []
        for _ in range(0, 3):
            self.add_tail()
        self.head = self.snake_tail[0]
        self.head.color("purple")

    def add_tail(self):
        """Add a segment/block to snake's tail."""
        tail_segment = Turtle(shape="circle")
        tail_segment.color("yellow")
        tail_segment.penup()
        new_position = len(self.snake_tail)

        # If the snake_tail has more than 2 segments, create the next one in the end of the previous segment.
        if len(self.snake_tail) > 2:
            new_x = self.snake_tail[len(self.snake_tail) - 1].xcor()
            new_y = self.snake_tail[len(self.snake_tail) - 1].ycor()
            tail_segment.goto(new_x, new_y)
        else:
            tail_segment.goto(x=-20 * new_position, y=0)
        self.snake_tail.append(tail_segment)

    def move(self):
        """Moves every tail's segment to the position the previous one was and move the head [0]."""
        for seg_index in range(len(self.snake_tail) - 1, 0, -1):
            new_x = self.snake_tail[seg_index - 1].xcor()
            new_y = self.snake_tail[seg_index - 1].ycor()
            self.snake_tail[seg_index].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Movement methods, it can't act if the opposite is pressed
    # Example: Snake can't go up if it's going down.
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
