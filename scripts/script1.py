import numpy as np
import matplotlib.pyplot as plt

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

# Generate and save the fractal image
mandelbrot_image = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)

plt.imshow(mandelbrot_image.T, cmap='hot', extent=[xmin, xmax, ymin, ymax])
plt.colorbar()
plt.title("Mandelbrot Fractal")

# Save the image to a file instead of displaying it
plt.savefig("mandelbrot_fractal.png")
