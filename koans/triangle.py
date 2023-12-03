#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def is_sum_of_two_sides_greater(a, b, c):
    """
    Check if the sum of any two sides is greater than the third side.

    Args:
        a (float): Length of side a.
        b (float): Length of side b.
        c (float): Length of side c.

    Returns:
        bool: True if the sum of any two sides is greater than the third side, False otherwise.
    """
    return all((a + b > c, a + c > b, b + c > a))

def triangle(a, b, c):
    unique_sides = {a, b, c}
    filtered_greater_than_zero = [x for x in unique_sides if x < 1]

    if len(filtered_greater_than_zero) > 0:
       raise TriangleError('All sides must be greater than zero')

    if not is_sum_of_two_sides_greater(a, b, c):
       raise TriangleError('Triangle must have valid sides')

    if len(unique_sides) == 3:
      return 'scalene'

    elif len(unique_sides) == 2:
      return 'isosceles'

    else:
      return 'equilateral'

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
