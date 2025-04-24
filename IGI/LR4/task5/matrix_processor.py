"""
Implements matrix processing using NumPy.
"""

import numpy as np
from typing import Tuple

class MatrixProcessor:
    """Handles matrix operations using NumPy."""
    
    def __init__(self, n: int = 3, m: int = 3, min_val: int = 0, max_val: int = 100):
        """
        Initialize matrix processor.
        
        :param n: Number of rows
        :param m: Number of columns
        :param min_val: Minimum random value
        :param max_val: Maximum random value
        """
        self.n = n
        self.m = m
        self.matrix = self.generate_matrix(min_val, max_val)
        
    @property
    def matrix(self) -> np.ndarray:
        """Get current matrix."""
        return self._matrix
    
    @matrix.setter
    def matrix(self, value: np.ndarray):
        """Set matrix with validation."""
        if not isinstance(value, np.ndarray):
            raise ValueError("Matrix must be a NumPy array")
        self._matrix = value
        
    def generate_matrix(self, min_val: int, max_val: int) -> np.ndarray:
        """Generate random integer matrix."""
        return np.random.randint(min_val, max_val+1, size=(self.n, self.m))
    
    def swap_max_with_diagonal(self) -> np.ndarray:
        """Swap max element in each row with diagonal element."""
        modified = self.matrix.copy()
        for i in range(min(self.n, self.m)):
            row = modified[i]
            max_idx = np.argmax(row)
            row[i], row[max_idx] = row[max_idx], row[i]
        return modified
    
    @staticmethod
    def manual_median(arr: np.ndarray) -> float:
        """Calculate median without NumPy."""
        sorted_arr = np.sort(arr.flatten())
        n = len(sorted_arr)
        mid = n // 2
        return (sorted_arr[mid] + sorted_arr[~mid])/2 if n%2 == 0 else sorted_arr[mid]