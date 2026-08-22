"""Three-dimensional shapes."""

from .cube import volume as cube_volume
from .sphere import volume as sphere_volume

__all__ = ["sphere_volume", "cube_volume"]
