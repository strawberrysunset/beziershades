# User defines a colour.
This colour has 3 properties. Hue, saturation and lightness (HSL)

We will take lightness value.
Linearly interpolate lightness values between a lower and upper bound.
Put interpolated values through bezier curve to give non-linear 
distribution of lightness shades.

Plug those values back into original HSL triplet.

We may find that only changing the lightness values doesn't suffice. 
We may need to change both the hue and saturation to get visually pleasing 
shades.