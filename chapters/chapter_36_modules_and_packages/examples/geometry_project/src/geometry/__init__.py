"""Friendly public imports for the geometry example package."""

from .circle import area as circle_area
from .rectangle import area as rectangle_area
from .shapes_3d.cube import volume as cube_volume
from .shapes_3d.sphere import volume as sphere_volume

__all__ = ["circle_area", "rectangle_area", "sphere_volume", "cube_volume"]
