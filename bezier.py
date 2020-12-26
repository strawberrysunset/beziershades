import numpy as np

def createCubicBezier(p0, h0, h1, p1):
    return lambda t : (1 - t)**3 * np.array(p0) + 3*(1 - t)**2*t * np.array(h0) + 3*(1 - t)*t**2 * np.array(h1) + t**3 * np.array(p1)

p0 = [0, 0]
p1 = [1, 1]
h0 = [0.25, 0.75]
h1 = [0.75, 0.75]
curve = createCubicBezier(p0, h0, h1, p1)

print(curve(0.5))
    