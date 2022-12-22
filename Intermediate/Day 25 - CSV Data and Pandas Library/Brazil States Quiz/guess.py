from turtle import Turtle

import pandas

TRIES = 27
BRAZIL_STATES = pandas.read_csv("brazil_states.csv")
STATES_LIST = BRAZIL_STATES.state.tolist()  # Turn into a list to perform list operation "in" on it.
STATES_ACR = BRAZIL_STATES.acronym
X_LIST = BRAZIL_STATES.x
Y_LIST = BRAZIL_STATES.y


class Guess(Turtle):
    def __init__(self, window):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.correct_tries = 0
        self.screen = window
        self.correct_states_list = []

    def quiz_the_user(self):
        """Quiz the user until he runs out of tries"""
        for _ in range(TRIES):
            # Text input on the screen to insert answer.
            answer_state = self.screen.textinput(title=f"{self.correct_tries}/27 Correct tries",
                                                 prompt="State Name: ").title()
            # Checks if the answer is equal to any state.
            correct_state = self.check_state(answer_state)
            # If the answer is correct, add into the correct_stages_list and to correct_tries counter.
            if correct_state is not None:
                self.correct_tries += 1
                self.correct_states_list.append(correct_state)
                # Pass the index of the correct state in STATES_LIST
                self.write_state(STATES_LIST.index(correct_state))

    def check_state(self, answer):
        """Check if the answer is a valid state"""
        for _ in range(len(STATES_LIST)):
            # If the answer is correct and has not already been input, return the correct state/answer.
            if answer == STATES_LIST[_] and answer not in self.correct_states_list:
                return STATES_LIST[_]

    def write_state(self, state_id):
        """Write the state's acronym in it's position in the map"""
        self.goto(X_LIST[state_id], Y_LIST[state_id])
        self.write(STATES_ACR[state_id], align="center", font=("Courier", 10, "bold"))
