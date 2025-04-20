"""
Handles graph creation and visualization using matplotlib.
"""

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from task3.calculator import SeriesCalculator

class SeriesPlotter:
    """Creates comparison plots for series expansion and math function."""

    def __init__(self, calculator: SeriesCalculator):
        self.calculator = calculator
        self.fig, self.ax = plt.subplots(figsize=(10, 6))

    def _configure_axes(self):
        """Configure plot axes and labels."""
        self.ax.set_title("e^x Series Expansion Comparison", fontsize=14)
        self.ax.set_xlabel("x values", fontsize=12)
        self.ax.set_ylabel("Function values", fontsize=12)
        self.ax.grid(True, linestyle='--', alpha=0.7)
        self.ax.legend()

    def plot_comparison(self):
        """Plot both series expansion and math function."""
        x_values = [res['x'] for res in self.calculator.results]

        # Plot series expansion
        self.ax.plot(
            x_values, 
            [res['F(x)'] for res in self.calculator.results],
            'bo-',
            label='Series Expansion'
        )
        
        # Plot math function
        self.ax.plot(
            x_values,
            [res['Math F(x)'] for res in self.calculator.results],
            'r--',
            label='math.exp(x)'
        )
        
        self._configure_axes()

    def save_plot(self, filename: str = "series_comparison.png"):
        """Save plot to file."""
        self.fig.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()


