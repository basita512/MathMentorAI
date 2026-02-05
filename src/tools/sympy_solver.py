"""SymPy mathematical solver."""
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
from src.utils.logger import get_logger

logger = get_logger()

class SymPySolver:
    @staticmethod
    def solve_equation(equation_str: str, variable: str = 'x'):
        """Solve algebraic equation."""
        try:
            # Parse equation
            if '=' in equation_str:
                lhs, rhs = equation_str.split('=')
                expr = parse_expr(lhs) - parse_expr(rhs)
            else:
                expr = parse_expr(equation_str)
            
            # Solve
            var = sp.Symbol(variable)
            solutions = sp.solve(expr, var)
            
            return [str(sol) for sol in solutions]
        except Exception as e:
            logger.error(f"SymPy solve failed: {e}")
            return []
    
    @staticmethod
    def differentiate(expr_str: str, variable: str = 'x'):
        """Compute derivative."""
        try:
            expr = parse_expr(expr_str)
            var = sp.Symbol(variable)
            derivative = sp.diff(expr, var)
            return str(derivative)
        except Exception as e:
            logger.error(f"Differentiation failed: {e}")
            return None
    
    @staticmethod
    def integrate(expr_str: str, variable: str = 'x'):
        """Compute integral."""
        try:
            expr = parse_expr(expr_str)
            var = sp.Symbol(variable)
            integral = sp.integrate(expr, var)
            return str(integral)
        except Exception as e:
            logger.error(f"Integration failed: {e}")
            return None
    
    @staticmethod
    def simplify(expr_str: str):
        """Simplify expression."""
        try:
            expr = parse_expr(expr_str)
            simplified = sp.simplify(expr)
            return str(simplified)
        except Exception as e:
            logger.error(f"Simplification failed: {e}")
            return expr_str
