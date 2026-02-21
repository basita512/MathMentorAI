"""Unit tests for calculator and plotter tools."""
import pytest
import numpy as np
from pathlib import Path

from src.tools.calculator import Calculator
from src.tools.plotter import Plotter

class TestCalculator:
    """Test calculator tool."""
    
    def test_basic_arithmetic(self):
        """Test basic arithmetic operations."""
        calc = Calculator()
        
        assert calc.evaluate("2 + 3")["result"] == 5
        assert calc.evaluate("10 - 4")["result"] == 6
        assert calc.evaluate("3 * 4")["result"] == 12
        assert calc.evaluate("15 / 3")["result"] == 5
    
    def test_order_of_operations(self):
        """Test order of operations."""
        calc = Calculator()
        
        result = calc.evaluate("2 + 3 * 4")
        assert result["result"] == 14  # Not 20
    
    def test_exponentiation(self):
        """Test power operations."""
        calc = Calculator()
        
        assert calc.evaluate("2 ** 3")["result"] == 8
        assert calc.evaluate("2^3")["result"] == 8  # Preprocessed to **
    
    def test_scientific_functions(self):
        """Test math functions."""
        calc = Calculator()
        
        # Test sin, cos
        result = calc.evaluate("sin(0)")
        assert abs(result["result"] - 0) < 1e-10
        
        result = calc.evaluate("cos(0)")
        assert abs(result["result"] - 1) < 1e-10
        
        # Test sqrt
        result = calc.evaluate("sqrt(16)")
        assert result["result"] == 4
        
        # Test log
        result = calc.evaluate("log(e)")
        assert abs(result["result"] - 1) < 1e-10
    
    def test_constants(self):
        """Test mathematical constants."""
        calc = Calculator()
        
        result = calc.evaluate("pi")
        assert abs(result["result"] - 3.14159265) < 1e-7
        
        result = calc.evaluate("e")
        assert abs(result["result"] - 2.71828182) < 1e-7
    
    def test_variables(self):
        """Test with variables."""
        calc = Calculator()
        
        result = calc.evaluate("x + 5", {"x": 10})
        assert result["result"] == 15
        
        result = calc.evaluate("sqrt(x**2 + y**2)", {"x": 3, "y": 4})
        assert result["result"] == 5
    
    def test_implicit_multiplication(self):
        """Test preprocessing of implicit multiplication."""
        calc = Calculator()
        
        # 2(x+1) should become 2*(x+1)
        result = calc.evaluate("2(3+1)")
        assert result["result"] == 8
        
        # 2pi should become 2*pi
        result = calc.evaluate("2pi")
        assert abs(result["result"] - 2*3.14159265) < 1e-7
    
    def test_error_handling(self):
        """Test error cases."""
        calc = Calculator()
        
        # Undefined variable
        result = calc.evaluate("x + 5")
        assert not result["success"]
        assert "error" in result
        
        # Division by zero
        result = calc.evaluate("1 / 0")
        assert not result["success"]
    
    def test_numerical_derivative(self):
        """Test numerical differentiation."""
        calc = Calculator()
        
        # d/dx(x^2) at x=3 should be 2*3 = 6
        deriv = calc.calculate_derivative_numerically("x**2", "x", 3.0)
        assert abs(deriv - 6) < 1e-5
        
        # d/dx(sin(x)) at x=0 should be cos(0) = 1
        deriv = calc.calculate_derivative_numerically("sin(x)", "x", 0)
        assert abs(deriv - 1) < 1e-5
    
    def test_numerical_integral(self):
        """Test numerical integration."""
        calc = Calculator()
        
        # ∫₀¹ x dx = 0.5
        integral = calc.calculate_integral_numerically("x", "x", 0, 1)
        assert abs(integral - 0.5) < 1e-3
        
        # ∫₀^π sin(x) dx = 2
        integral = calc.calculate_integral_numerically("sin(x)", "x", 0, 3.14159265)
        assert abs(integral - 2) < 1e-2

class TestPlotter:
    """Test plotter tool."""
    
    def test_plot_function(self, tmp_path):
        """Test plotting a simple function."""
        plotter = Plotter(output_dir=str(tmp_path))
        
        result = plotter.plot_function(
            expression="x**2",
            x_range=(-5, 5),
            use_interactive=False
        )
        
        assert result["success"]
        assert "plot_path" in result
        assert Path(result["plot_path"]).exists()
    
    def test_plot_interactive(self, tmp_path):
        """Test interactive plotting."""
        plotter = Plotter(output_dir=str(tmp_path))
        
        result = plotter.plot_function(
            expression="sin(x)",
            x_range=(0, 6.28),
            use_interactive=True
        )
        
        assert result["success"]
        assert result["plot_type"] == "plotly"
        assert result["plot_path"].endswith(".html")
    
    def test_plot_multiple_functions(self, tmp_path):
        """Test plotting multiple functions."""
        plotter = Plotter(output_dir=str(tmp_path))
        
        result = plotter.plot_multiple_functions(
            expressions=["x**2", "x**3"],
            x_range=(-2, 2),
            labels=["Quadratic", "Cubic"],
            use_interactive=False
        )
        
        assert result["success"]
        assert Path(result["plot_path"]).exists()
    
    def test_plot_parametric(self, tmp_path):
        """Test parametric plotting."""
        plotter = Plotter(output_dir=str(tmp_path))
        
        # Circle: x = cos(t), y = sin(t)
        result = plotter.plot_parametric(
            x_expr="cos(t)",
            y_expr="sin(t)",
            t_range=(0, 6.28)
        )
        
        assert result["success"]
        assert "fig" in result
    
    def test_plot_with_title(self, tmp_path):
        """Test plotting with custom title."""
        plotter = Plotter(output_dir=str(tmp_path))
        
        result = plotter.plot_function(
            expression="exp(x)",
            x_range=(-2, 2),
            title="Exponential Function",
            use_interactive=False
        )
        
        assert result["success"]
    
    def test_plot_error_handling(self, tmp_path):
        """Test error cases."""
        plotter = Plotter(output_dir=str(tmp_path))
        
        # Invalid expression
        result = plotter.plot_function(
            expression="invalid_func(x)",
            x_range=(0, 1),
            use_interactive=False
        )
        
        assert not result["success"]
        assert "error" in result
