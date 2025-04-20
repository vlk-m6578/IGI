"""
Implements mathematical series calculations and statistical analysis.
"""

import math
from typing import List
from statistics import mean, median, mode, variance, stdev

class SeriesCalculator:
    """Calculates e^x series expansion and statistical parameters."""

    DEFAULT_PROCISION =  1e-6
    MAX_ITERATIONS = 1000
    
    def __init__(self, x_values: List[float], precision: float = DEFAULT_PROCISION):
        self._x_values = x_values
        self._precision = precision
        self._results = []

    @property
    def results(self) -> List[dict]:
        """Get calculation results with n, F(x), Math F(x), eps."""
        if not self._results:
            self.calculate_series()
        return self._results
    
    def calculate_series(self):
        """Calculate series expansion for all x values."""
        for x in self._x_values:
            term = 1.0
            total = 1.0
            n = 1
            math_fx = math.exp(x)

            while abs(total - math_fx) > self._precision and n < self.MAX_ITERATIONS:
                term *= x / n
                total += term
                n += 1

            self._results.append({
                'x': x,
                'n': n,
                'F(x)': total,
                'Math F(x)': math_fx,
                'eps': abs(total - math_fx)
            })

    def get_statistics(self) -> dict:
        """Calculate statistical parameters for iterations count."""
        iterations = [res['n'] for res in self.results]
        return{
            'mean': mean(iterations),
            'median': median(iterations),
            'mode': mode(iterations),
            'variance': variance(iterations),
            'stdev': stdev(iterations)
        }