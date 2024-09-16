Web VPython 3.2

from vpython import *

def magnitude(vector):
    return math.sqrt(sum(pow(element, 2) for element in vector))

# User inputs for initial velocity and angle
initial_velocity = float(input("Enter the initial velocity (m/s): "))
initial_angle_deg = float(input("Enter the launch angle (degrees): "))
while True:
    initial_height = float(input("Enter the initial positive height above the ground (m): "))
    if initial_height >= 0:
        break

# Convert angle to radians
initial_angle = radians(initial_angle_deg)

# Constants
g = 9.81  # Gravity (m/s^2)
time_step = 0.01  # Time increment for the simulation

# Calculate initial velocity components
vx = initial_velocity * cos(initial_angle)
vy = initial_velocity * sin(initial_angle)

# Create the ground (green surface)
ground = box(pos=vector(0, -0.05, 0), size=vector(50, 0.1, 10), color=color.green)

# Create the projectile (red sphere)
projectile = sphere(pos=vector(0, 0, 0), radius=0.5, color=color.red, make_trail=True)

# Set background color to white
scene.background = color.white

# Position the camera
scene.camera.pos = vector(-10, 5, 20)
scene.camera.axis = vector(10, -5, -20)

# Set initial conditions
projectile_velocity = vector(vx, vy, 0)
projectile.pos = vector(0, initial_height, 0)
projectile.trail_color = color.blue

# Time variable
t = 0  # Initial time

# Create a 2D label for horizontal displacement in the upper left corner
displacement_label = wtext(text="Horizontal Displacement: 0.00 m \nFoo Bar")

# Adjust the position of the label using xoffset and yoffset in the window
scene.append_to_caption('\n\n')  # Line break to make sure label appears at the top

# adjust to allow for max y

max_x = projectile.pos.x
max_y = projectile.pos.y
min_x_velo = projectile_velocity.x
min_y_velo = projectile_velocity.y

# Run the simulation
while projectile.pos.y >= 0:
    rate(100)  # Set frame rate (100 frames per second)

    # Update position and velocity using basic kinematic equations
    projectile.pos += projectile_velocity * time_step
    projectile_velocity.y -= g * time_step

    # get max y
    if max_y < projectile.pos.y:
        max_y = projectile.pos.y
        max_x = projectile.pos.x
        min_x_velo = projectile_velocity.x
        min_y_velo = projectile_velocity.y



    # Update the label with the current horizontal displacement
    displacement_label.text = (f"Horizontal Displacement: {projectile.pos.x:.2f} m\n"+
                                "Maximum Height Coordinates: (" + round(max_x, 4) + ", " +
                                round(max_y, 4) + ")\n" +
                                "Min velocity: (" + round(min_x_velo, 4) + ", " +
                                round(min_y_velo, 4) + ")\n" +
                                "Min acceleration: " + g + " m/s^2")

    t += time_step
