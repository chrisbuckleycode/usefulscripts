from elevator import Elevator
import time

class Simulator:
    def __init__(self):
        self.elevators = [Elevator(1), Elevator(2)]
        self.calls = {}  # floor: {'up': bool, 'down': bool}
        self.assigned_calls = set()  # Set to keep track of assigned calls
        self.last_update_time = time.time()
        self.elevator_movement_times = {1: 0, 2: 0}  # Tracks when each elevator last moved
        self.elevator_stop_times = {1: 0, 2: 0}  # Tracks when each elevator stopped at a floor
        self.elevator_next_move_times = {1: 0, 2: 0}  # Tracks when each elevator should next move

    def call_elevator(self, floor, direction):
        if floor not in self.calls:
            self.calls[floor] = {'up': False, 'down': False}
        self.calls[floor][direction] = True
        self._assign_elevator(floor, direction)

    def _assign_elevator(self, floor, direction):
        if (floor, direction) in self.assigned_calls:
            return  # This call has already been assigned

        idle_elevators = [e for e in self.elevators if e.direction == 'idle']
        same_direction_elevators = [e for e in self.elevators if e.direction == direction]
        opposite_direction_elevators = [e for e in self.elevators if e.direction != direction and e.direction != 'idle']
        
        def calculate_score(elevator):
            if elevator.direction == 'idle':
                return abs(elevator.current_floor - floor)
            elif elevator.direction == direction:
                if (direction == 'up' and elevator.current_floor <= floor) or \
                   (direction == 'down' and elevator.current_floor >= floor):
                    return abs(elevator.current_floor - floor)
                else:
                    return float('inf')
            else:
                return float('inf')

        all_elevators = idle_elevators + same_direction_elevators + opposite_direction_elevators
        chosen = min(all_elevators, key=calculate_score)

        if calculate_score(chosen) < float('inf'):
            if (floor, direction) not in chosen.requests:
                chosen.requests.append((floor, direction))
                self.assigned_calls.add((floor, direction))
                if chosen.direction == 'idle':
                    self.elevator_next_move_times[chosen.id] = time.time() + 2  # Set next move time for idle elevator

    def select_floor(self, elevator_id, floor):
        elevator = self.elevators[elevator_id - 1]
        if (floor, 'up') not in elevator.requests and (floor, 'down') not in elevator.requests:
            elevator.requests.append((floor, elevator.direction))
            if elevator.direction == 'idle':
                self.elevator_next_move_times[elevator.id] = time.time() + 2  # Set next move time for idle elevator

    def update(self):
        current_time = time.time()

        for elevator in self.elevators:
            # Check if the elevator is stopped at a floor
            if current_time - self.elevator_stop_times[elevator.id] < 5:
                continue  # Skip this elevator's update if it's still stopped

            # Check if it's time for the elevator to move
            if current_time < self.elevator_next_move_times[elevator.id]:
                continue  # Skip this elevator's update if it's not time to move yet

            elevator.update_direction()
            if elevator.requests:
                current_request = elevator.requests[0]
                if elevator.current_floor < current_request[0]:
                    elevator.current_floor += 1
                elif elevator.current_floor > current_request[0]:
                    elevator.current_floor -= 1
                
                # Set the next move time
                self.elevator_next_move_times[elevator.id] = current_time + 2

                # Check if the elevator has reached the requested floor
                if elevator.current_floor == current_request[0]:
                    completed_floor, completed_direction = elevator.requests.pop(0)
                    if completed_floor in self.calls:
                        self.calls[completed_floor][completed_direction] = False
                        if not any(self.calls[completed_floor].values()):
                            del self.calls[completed_floor]
                    if (completed_floor, completed_direction) in self.assigned_calls:
                        self.assigned_calls.remove((completed_floor, completed_direction))
                    
                    # Set the stop time for this elevator
                    self.elevator_stop_times[elevator.id] = current_time

                # Check if we can fulfill any requests on the way
                for floor, direction in list(elevator.requests):
                    if (floor == elevator.current_floor and
                        ((elevator.direction == 'up' and direction == 'up') or
                         (elevator.direction == 'down' and direction == 'down'))):
                        elevator.requests.remove((floor, direction))
                        if floor in self.calls:
                            self.calls[floor][direction] = False
                            if not any(self.calls[floor].values()):
                                del self.calls[floor]
                        if (floor, direction) in self.assigned_calls:
                            self.assigned_calls.remove((floor, direction))
                        
                        # Set the stop time for this elevator
                        self.elevator_stop_times[elevator.id] = current_time

            elevator.update_direction()

        # Assign any unassigned calls
        for floor, directions in self.calls.items():
            for direction in ['up', 'down']:
                if directions[direction] and (floor, direction) not in self.assigned_calls:
                    self._assign_elevator(floor, direction)

    def get_state(self):
        return {
            'elevators': [e.get_state() for e in self.elevators],
            'calls': self.calls
        }