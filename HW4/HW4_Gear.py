#---------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from ipywidgets import interact, FloatSlider
from IPython.display import display

radius_drive = 0.1  # Initial radius of the drive gear
radius_driven = 0.3  # Initial radius of the driven gear
speed_ratio = radius_driven/radius_drive  # Ratio of rotational speeds

t = np.linspace(0, 10, 100)

# Figure and axis setup
fig, ax = plt.subplots()
ax.set(xlim=(0, 1), ylim=(0, 1), aspect='equal')
ax.set_title("Gearbox Simulation")


drive_gear = plt.Circle((0.3, 0.5), radius_drive, color='grey', alpha=0.7, label="Drive Gear")
driven_gear = plt.Circle((0.7, 0.5), radius_driven, color='blue', alpha=0.7, label="Driven Gear")
ax.add_patch(drive_gear)
ax.add_patch(driven_gear)

drive_line, = ax.plot([], [], color='black', lw=2)
driven_line, = ax.plot([], [], color='green', lw=2)

ax.legend()

def update(frame, radius_drive, radius_driven):
    # Remove old gear circles
    drive_gear.set_radius(radius_drive)
    driven_gear.set_radius(radius_driven)
    #Main_Gear = plt.Circle((x, 0.5), diameter / 2, color='blue', fill=True, label='Driven Gear')

    angle_drive = frame * np.pi / 15  # Drive gear rotation
    angle_driven = -frame * np.pi / (15 * speed_ratio)  # Driven gear rotation (slower)
    
    drive_line.set_data(
        [0.3, 0.3 + radius_drive * np.cos(angle_drive)],
        [0.5, 0.5 + radius_drive * np.sin(angle_drive)]
    )
    

    driven_line.set_data(
        [0.7, 0.7 + radius_driven * np.cos(angle_driven)],
        [0.5, 0.5 + radius_driven * np.sin(angle_driven)]
    )
    
    return drive_line, driven_line


def run_animation(radius_drive, radius_driven):
    ani = animation.FuncAnimation(fig, update, frames=range(100), fargs=(radius_drive, radius_driven), interval=50, blit=True)
    plt.show()

# Interactive sliders
drive_slider = FloatSlider(value=0.1, min=0.05, max=0.2, step=0.01, description='Drive Gear Size:')
driven_slider = FloatSlider(value=0.3, min=0.1, max=0.5, step=0.01, description='Driven Gear Size:')
interact(run_animation, radius_drive=drive_slider, radius_driven=driven_slider)