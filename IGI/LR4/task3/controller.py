"""
Provides user interface for series analysis tasks.
"""

import numpy as np
from typing import List
from task3.calculator import SeriesCalculator
from task3.plotter import SeriesPlotter

class SeriesAnalysisController:
    """Manages complete series analysis workflow."""

    def __init__(self):
        self.calculator = None
        self.plotter = None

    def run_analysis(self):
        """Execute full analysis pipeline."""
        x_values = self._get_input_values()
        precision = self._get_precision()

        self.calculator = SeriesCalculator(x_values, precision)
        self.plotter = SeriesPlotter(self.calculator)

        self._show_statistics()
        self.plotter.plot_comparison()
        self.plotter.save_plot()
        print("Plot saved to series_comparison.png")

    def _get_input_values(self) -> List[float]:
        """Get user input for x values."""
        while True:
            try:
                start = float(input("Enter start x value: "))
                end = float(input("Enter end x value: "))
                num_points = int(input("Number of points: "))
                
                if num_points < 2:
                    raise ValueError("Minimum 2 points required")
                    
                return np.linspace(start, end, num_points).tolist()
                
            except ValueError as e:
                print(f"Invalid input: {str(e)}. Try again.")
                
    def _get_precision(self) -> float:
        """Get calculation precision from user."""
        while True:
            try:
                prec = float(input("Enter calculation precision (default 1e-6): ") or 1e-6)
                if prec <= 0:
                    raise ValueError("Precision must be positive")
                return prec
            except ValueError:
                print("Invalid precision value. Try again.")
                
    def _show_statistics(self):
        """Display statistical parameters."""
        stats = self.calculator.get_statistics()
        print("\n=== Statistical Parameters ===")
        print(f"Mean iterations: {stats['mean']:.2f}")
        print(f"Median iterations: {stats['median']:.2f}")
        print(f"Mode iterations: {stats['mode']}")
        print(f"Variance: {stats['variance']:.2f}")
        print(f"Standard deviation: {stats['stdev']:.2f}")