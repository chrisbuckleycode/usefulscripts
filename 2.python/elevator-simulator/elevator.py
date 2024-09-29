class Elevator:
    def __init__(self, id):
        self.id = id
        self.current_floor = 1
        self.requests = []  # List of tuples (floor, direction)
        self.direction = 'idle'  # 'idle', 'up', or 'down'

    def get_state(self):
        return {
            'id': self.id,
            'current_floor': self.current_floor,
            'requests': [r[0] for r in self.requests],  # Only return floor numbers
            'direction': self.direction
        }

    def update_direction(self):
        if self.requests:
            if self.current_floor < self.requests[0][0]:
                self.direction = 'up'
            elif self.current_floor > self.requests[0][0]:
                self.direction = 'down'
            else:
                self.direction = 'idle'
        else:
            self.direction = 'idle'