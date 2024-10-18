import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to compute the Mandelbrot set
def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

# Generate the Mandelbrot set
def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    mandelbrot_image = np.empty((width, height))
    
    for i in range(width):
        for j in range(height):
            mandelbrot_image[i, j] = mandelbrot(r1[i] + 1j * r2[j], max_iter)
    
    return mandelbrot_image

# Visualization parameters
xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
width, height = 800, 800
max_iter = 256

# Create the figure
fig, ax = plt.subplots()
mandelbrot_image = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)
im = ax.imshow(mandelbrot_image.T, cmap='hot', extent=[xmin, xmax, ymin, ymax])

# Update function for animation
def update(frame):
    global xmin, xmax, ymin, ymax
    # Zoom in by shrinking the bounds
    zoom_factor = 0.95 ** frame
    xmin, xmax = xmin * zoom_factor, xmax * zoom_factor
    ymin, ymax = ymin * zoom_factor, ymax * zoom_factor
    
    mandelbrot_image = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)
    im.set_array(mandelbrot_image.T)
    im.set_extent([xmin, xmax, ymin, ymax])
    return [im]

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=300, blit=True)

# Save the animation as an MP4 video
ani.save("mandelbrot_animation.mp4", writer="ffmpeg", fps=10)

plt.close()  # Close the plot to prevent it from displaying
