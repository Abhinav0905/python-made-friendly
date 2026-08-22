"""Use geometry modules through full dotted imports."""

import geometry.circle
import geometry.rectangle


print(f"{geometry.circle.area(5):.4f}")
print(geometry.rectangle.area(3, 4))
