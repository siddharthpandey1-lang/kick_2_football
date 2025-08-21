
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
GOAL_WIDTH = 120
GOAL_HEIGHT = 60
BALL_RADIUS = 15
KICK_POWER = 20

class FootballGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Kick 2 Football")
        self.canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="green")
        self.canvas.pack()
        self.score = 0

        # Draw goal
        self.goal_x1 = (WINDOW_WIDTH - GOAL_WIDTH) // 2
        self.goal_y1 = 10
        self.goal_x2 = self.goal_x1 + GOAL_WIDTH
        self.goal_y2 = self.goal_y1 + GOAL_HEIGHT
        self.canvas.create_rectangle(self.goal_x1, self.goal_y1, self.goal_x2, self.goal_y2, fill="yellow", outline="black", width=3)
        self.canvas.create_text((WINDOW_WIDTH//2, self.goal_y1 + GOAL_HEIGHT//2), text="GOAL", font=("Arial", 20, "bold"))

        # Draw ball
        self.ball_x = WINDOW_WIDTH // 2
        self.ball_y = WINDOW_HEIGHT - 50
        self.ball = self.canvas.create_oval(self.ball_x - BALL_RADIUS, self.ball_y - BALL_RADIUS,
                                            self.ball_x + BALL_RADIUS, self.ball_y + BALL_RADIUS, fill="white", outline="black")

        # Score display
        self.score_text = self.canvas.create_text(60, 20, text=f"Score: {self.score}", font=("Arial", 16), fill="white")

        # Bindings
        self.canvas.bind("<Button-1>", self.kick_ball)
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)

    def move_left(self, event):
        if self.ball_x - BALL_RADIUS > 0:
            self.ball_x -= 20
            self.update_ball()

    def move_right(self, event):
        if self.ball_x + BALL_RADIUS < WINDOW_WIDTH:
            self.ball_x += 20
            self.update_ball()

    def update_ball(self):
        self.canvas.coords(self.ball, self.ball_x - BALL_RADIUS, self.ball_y - BALL_RADIUS,
                           self.ball_x + BALL_RADIUS, self.ball_y + BALL_RADIUS)

    def kick_ball(self, event):
        angle = random.uniform(-0.3, 0.3)  # Slight randomness
        dx = KICK_POWER * angle
        dy = -KICK_POWER
        self.animate_kick(dx, dy, 0)

    def animate_kick(self, dx, dy, step):
        steps = 20
        if step >= steps:
            self.reset_ball()
            return

        self.ball_x += dx
        self.ball_y += dy
        self.update_ball()
        dy += 1  # Gravity

        # Check for goal
        if (self.goal_x1 < self.ball_x < self.goal_x2 and
            self.goal_y1 < self.ball_y - BALL_RADIUS < self.goal_y2):
            self.score += 1
            self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
            self.reset_ball()
            return

        # Out of bounds
        if self.ball_y < 0 or self.ball_x < 0 or self.ball_x > WINDOW_WIDTH:
            self.reset_ball()
            return

        self.root.after(20, lambda: self.animate_kick(dx, dy, step + 1))

    def reset_ball(self):
        self.ball_x = WINDOW_WIDTH // 2
        self.ball_y = WINDOW_HEIGHT - 50 
         if: self.ball_y < 0:
            self.ball_y = WINDOW_HEIGHT - 50
        elif: self.ball_x < 0:
            self.ball_x = 4
        elif: self.ball_x > WINDOW_WIDTH:
        else:
            self.ball_x = WINDOW_WIDTH - 4