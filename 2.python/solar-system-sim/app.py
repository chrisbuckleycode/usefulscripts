import math
import time
import tkinter as tk

# Constants
G = 6.67430e-11  # Gravitational constant
scaling_factor = 100  # Scaling factor for distances to fit within screen dimensions
speed_factor = 1.0  # Initial speed factor
zoom_factor = 1.0  # Initial zoom factor

# Create the main window
root = tk.Tk()
root.title("Solar System Simulation")
canvas = tk.Canvas(root, width=1600, height=1200, bg='black')
canvas.pack()

# Function to calculate the gravitational force
def calculate_gravitational_force(m1, m2, r):
    return G * m1 * m2 / (r ** 2)

# Define the properties of the sun and real planets of the solar system
sun = {'mass': 2e30, 'radius': 30, 'color': 'yellow', 'x': 800, 'y': 600}
planets = [
    {'name': 'Mercury', 'mass': 3.285e23, 'radius': 5, 'color': 'gray', 'distance': 0.39 * scaling_factor, 'angle': 0, 'velocity': 3.87,
     'moons': [{'name': 'Moon', 'radius': 2, 'color': 'white', 'distance': 0.1 * scaling_factor, 'angle': 0, 'velocity': 13.0}]},
    {'name': 'Venus', 'mass': 4.867e24, 'radius': 10, 'color': 'orange', 'distance': 0.72 * scaling_factor, 'angle': 0, 'velocity': 7.39,
     'moons': []},
    {'name': 'Earth', 'mass': 5.972e24, 'radius': 10, 'color': 'blue', 'distance': 1.0 * scaling_factor, 'angle': 0, 'velocity': 7.5,
     'moons': [{'name': 'Moon', 'radius': 3, 'color': 'white', 'distance': 0.2 * scaling_factor, 'angle': 0, 'velocity': 13.0}]},
    {'name': 'Mars', 'mass': 6.39e23, 'radius': 8, 'color': 'red', 'distance': 1.52 * scaling_factor, 'angle': 0, 'velocity': 5.0,
     'moons': [{'name': 'Phobos', 'radius': 1, 'color': 'gray', 'distance': 0.04 * scaling_factor, 'angle': 0, 'velocity': 14.0},
               {'name': 'Deimos', 'radius': 1, 'color': 'white', 'distance': 0.06 * scaling_factor, 'angle': 0, 'velocity': 9.0}]},
    {'name': 'Jupiter', 'mass': 1.898e27, 'radius': 20, 'color': 'brown', 'distance': 5.2 * scaling_factor, 'angle': 0, 'velocity': 2.75,
     'moons': [{'name': 'Io', 'radius': 2, 'color': 'orange', 'distance': 0.7 * scaling_factor, 'angle': 0, 'velocity': 9.0},
               {'name': 'Europa', 'radius': 2, 'color': 'white', 'distance': 0.9 * scaling_factor, 'angle': 0, 'velocity': 7.0}]},
    {'name': 'Saturn', 'mass': 5.683e26, 'radius': 18, 'color': 'yellow', 'distance': 9.58 * scaling_factor, 'angle': 0, 'velocity': 2.0,
     'moons': [{'name': 'Titan', 'radius': 2, 'color': 'orange', 'distance': 0.8 * scaling_factor, 'angle': 0, 'velocity': 5.0}]},
    {'name': 'Uranus', 'mass': 8.681e25, 'radius': 15, 'color': 'lightblue', 'distance': 19.22 * scaling_factor, 'angle': 0, 'velocity': 1.43,
     'moons': []},
    {'name': 'Neptune', 'mass': 1.024e26, 'radius': 15, 'color': 'blue', 'distance': 30.05 * scaling_factor, 'angle': 0, 'velocity': 1.13,
     'moons': []}
]

# Draw the sun
canvas.create_oval(sun['x'] - sun['radius'], sun['y'] - sun['radius'],
                    sun['x'] + sun['radius'], sun['y'] + sun['radius'], fill=sun['color'])

# Draw the real planets and their moons of the solar system
planet_shapes = []
moon_shapes = []
for planet_data in planets:
    planet_x = sun['x'] + planet_data['distance'] * zoom_factor
    planet_y = sun['y']
    planet_shape = canvas.create_oval(planet_x, planet_y, planet_x, planet_y, fill=planet_data['color'])
    planet_shapes.append(planet_shape)

    for moon_data in planet_data['moons']:
        moon_x = planet_x + moon_data['distance'] * zoom_factor
        moon_y = planet_y
        moon_shape = canvas.create_oval(moon_x, moon_y, moon_x, moon_y, fill=moon_data['color'])
        moon_shapes.append(moon_shape)

# Speed and Zoom Controls
def increase_speed():
    global speed_factor
    speed_factor += 0.1

def decrease_speed():
    global speed_factor
    if speed_factor > 0.1:
        speed_factor -= 0.1

def zoom_in():
    global zoom_factor
    zoom_factor *= 1.1
    update_positions()

def zoom_out():
    global zoom_factor
    zoom_factor *= 0.9
    update_positions()

# Update positions based on the zoom factor
def update_positions():
    for idx, planet_data in enumerate(planets):
        planet_x = sun['x'] + planet_data['distance'] * zoom_factor
        planet_y = sun['y']
        canvas.coords(planet_shapes[idx], planet_x - planet_data['radius'], planet_y - planet_data['radius'],
                      planet_x + planet_data['radius'], planet_y + planet_data['radius'])

        for moon_data in planet_data['moons']:
            moon_x = planet_x + moon_data['distance'] * zoom_factor
            moon_y = planet_y
            canvas.coords(moon_shapes[idx], moon_x - moon_data['radius'], moon_y - moon_data['radius'],
                          moon_x + moon_data['radius'], moon_y + moon_data['radius'])

# Bind controls to keys
root.bind("<Up>", lambda event: increase_speed())
root.bind("<Down>", lambda event: decrease_speed())
root.bind("<Right>", lambda event: zoom_in())
root.bind("<Left>", lambda event: zoom_out())

# Simulation loop
while True:
    for idx, planet_data in enumerate(planets):
        planet_data['angle'] += planet_data['velocity'] * speed_factor

        planet_x = sun['x'] + planet_data['distance'] * zoom_factor * math.cos(math.radians(planet_data['angle']))
        planet_y = sun['y'] + planet_data['distance'] * zoom_factor * math.sin(math.radians(planet_data['angle']))
        canvas.coords(planet_shapes[idx], planet_x - planet_data['radius'], planet_y - planet_data['radius'],
                      planet_x + planet_data['radius'], planet_y + planet_data['radius'])

        for moon_data in planet_data['moons']:
            moon_data['angle'] += moon_data['velocity'] * speed_factor
            moon_x = planet_x + moon_data['distance'] * zoom_factor * math.cos(math.radians(moon_data['angle']))
            moon_y = planet_y + moon_data['distance'] * zoom_factor * math.sin(math.radians(moon_data['angle']))
            canvas.coords(moon_shapes[idx], moon_x - moon_data['radius'], moon_y - moon_data['radius'],
                          moon_x + moon_data['radius'], moon_y + moon_data['radius'])

    root.update()
    time.sleep(0.01)

root.mainloop()