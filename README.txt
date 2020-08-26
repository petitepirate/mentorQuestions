Repository for random questions

boggle.py was given to us, but line 26 is returning an unused-variable y error with pylint.
However everything is actually running from what I can see.  Is there something that I'm missing?

    def make_board(self):
        """Make and return a random boggle board."""

        board = []

        for y in range(5):
            row = [choice(string.ascii_uppercase) for i in range(5)]
            board.append(row)

        return board



