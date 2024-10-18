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

# Visualization parameters - Start near an interesting edge
xmin, xmax, ymin, ymax = -0.74877, -0.74872, 0.06505, 0.06510  # Close to an edge of the Mandelbrot set
width, height = 400, 400  # Keep resolution moderate
max_iter = 150  # Adjust for performance

# Create the figure
fig, ax = plt.subplots()
mandelbrot_image = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)
im = ax.imshow(mandelbrot_image.T, cmap='hot', extent=[xmin, xmax, ymin, ymax])

# Update function for animation
def update(frame):
    global xmin, xmax, ymin, ymax
    zoom_factor = 0.98 ** frame  # Slow zoom
    xmin_new, xmax_new = xmin * zoom_factor, xmax * zoom_factor
    ymin_new, ymax_new = ymin * zoom_factor, ymax * zoom_factor

    # Prevent singular transformations by limiting zoom depth
    if abs(xmax_new - xmin_new) < 0.0000001 or abs(ymax_new - ymin_new) < 0.0000001:
        return [im]
    
    xmin, xmax, ymin, ymax = xmin_new, xmax_new, ymin_new, ymax_new
    mandelbrot_image = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)
    im.set_array(mandelbrot_image.T)
    im.set_extent([xmin, xmax, ymin, ymax])
    return [im]

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=450, blit=True)  # More frames for longer animation

# Save the animation as an MP4 video
ani.save("scripts/mandelbrot_animation.mp4", writer="ffmpeg", fps=10)


plt.close()  # Close the plot to prevent it from displaying
