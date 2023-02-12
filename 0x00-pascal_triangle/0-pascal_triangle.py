#!usr/bin/python3
"""
Defines a list of integers if a Pascal's triangle
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's trianfle of n
    """
    if n <= 0:
        return []
        
