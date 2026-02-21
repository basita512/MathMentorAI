"""Safe calculator tool for numerical computation."""
import ast
import operator
import math
from typing import Dict, Any, Union
import re

from src.utils.logger import get_logger

logger = get_logger()

# Safe operators allowed in expressions
SAFE_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}

# Safe functions allowed in expressions
SAFE_FUNCTIONS = {
    'abs': abs,
    'round': round,
    'min': min,
    'max': max,
    # Math functions
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'asin': math.asin,
    'acos': math.acos,
    'atan': math.atan,
    'sinh': math.sinh,
    'cosh': math.cosh,
    'tanh': math.tanh,
    'exp': math.exp,
    'log': math.log,
    'log10': math.log10,
    'sqrt': math.sqrt,
    'ceil': math.ceil,
    'floor': math.floor,
    'factorial': math.factorial,
    'radians': math.radians,
    'degrees': math.degrees,
}

# Safe constants
SAFE_CONSTANTS = {
    'pi': math.pi,
    'e': math.e,
    'tau': math.tau,
}

class Calculator:
    """
    Safe numerical calculator with support for scientific functions.
    
    Uses AST (Abstract Syntax Tree) parsing to safely evaluate mathematical expressions
    without executing arbitrary code.
    """
    
    def __init__(self):
        """Initialize calculator."""
        self.functions = SAFE_FUNCTIONS.copy()
        self.constants = SAFE_CONSTANTS.copy()
        self.operators = SAFE_OPERATORS.copy()
    
    def evaluate(self, expression: str, variables: Dict[str, float] = None) -> Dict[str, Any]:
        """
        Safely evaluate a mathematical expression.
        
        Args:
            expression: Math expression string (e.g., "2 * sin(pi/2)")
            variables: Optional dict of variable values (e.g., {"x": 5})
            
        Returns:
            Dict with keys: result, success, error (if failed)
            
        Examples:
            >>> calc = Calculator()
            >>> calc.evaluate("2 + 3 * 4")
            {"result": 14, "success": True}
            >>> calc.evaluate("sin(pi/2)")
            {"result": 1.0, "success": True}
            >>> calc.evaluate("sqrt(x**2 + y**2)", {"x": 3, "y": 4})
            {"result": 5.0, "success": True}
        """
        try:
            # Preprocessing: replace common math notations
            expression = self._preprocess_expression(expression)
            
            # Add variables to namespace
            namespace = self.constants.copy()
            if variables:
                namespace.update(variables)
            
            # Parse expression to AST
            tree = ast.parse(expression, mode='eval')
            
            # Evaluate safely
            result = self._eval_node(tree.body, namespace)
            
            logger.info(f"Evaluated: {expression} = {result}")
            
            return {
                "result": result,
                "success": True,
                "expression": expression
            }
            
        except Exception as e:
            logger.error(f"Calculation error: {e}")
            return {
                "result": None,
                "success": False,
                "error": str(e),
                "expression": expression
            }
    
    def _preprocess_expression(self, expr: str) -> str:
        """Preprocess expression to handle common notations."""
        # Replace ^ with ** for exponentiation
        expr = expr.replace('^', '**')
        
        # Replace implicit multiplication: 2(x+1) -> 2*(x+1)
        expr = re.sub(r'(\d)(\()', r'\1*\2', expr)
        
        # Replace implicit multiplication: 2pi -> 2*pi
        expr = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expr)
        
        return expr
    
    def _eval_node(self, node, namespace):
        """
        Recursively evaluate AST node.
        
        Only allows whitelisted operations to prevent code injection.
        """
        if isinstance(node, ast.Constant):  # Python 3.8+
            return node.value
        
        elif isinstance(node, ast.Num):  # Python <3.8
            return node.n
        
        elif isinstance(node, ast.Name):
            # Variable or constant lookup
            if node.id in namespace:
                return namespace[node.id]
            else:
                raise NameError(f"Variable '{node.id}' not defined")
        
        elif isinstance(node, ast.BinOp):
            # Binary operation (e.g., +, -, *, /)
            if type(node.op) not in self.operators:
                raise TypeError(f"Operator {type(node.op).__name__} not allowed")
            
            left = self._eval_node(node.left, namespace)
            right = self._eval_node(node.right, namespace)
            return self.operators[type(node.op)](left, right)
        
        elif isinstance(node, ast.UnaryOp):
            # Unary operation (e.g., -x, +x)
            if type(node.op) not in self.operators:
                raise TypeError(f"Operator {type(node.op).__name__} not allowed")
            
            operand = self._eval_node(node.operand, namespace)
            return self.operators[type(node.op)](operand)
        
        elif isinstance(node, ast.Call):
            # Function call
            if not isinstance(node.func, ast.Name):
                raise TypeError("Only simple function calls allowed")
            
            func_name = node.func.id
            if func_name not in self.functions:
                raise NameError(f"Function '{func_name}' not allowed")
            
            # Evaluate arguments
            args = [self._eval_node(arg, namespace) for arg in node.args]
            
            # Call function
            return self.functions[func_name](*args)
        
        else:
            raise TypeError(f"Node type {type(node).__name__} not allowed")
    
    def calculate_derivative_numerically(self, expression: str, var: str, point: float, h: float = 1e-7) -> float:
        """
        Calculate numerical derivative using central difference.
        
        Args:
            expression: Expression as string (e.g., "x**2 + 2*x")
            var: Variable to differentiate with respect to
            point: Point at which to evaluate derivative
            h: Step size
            
        Returns:
            Approximate derivative value
        """
        # f'(x) ≈ [f(x+h) - f(x-h)] / (2h)
        f_plus = self.evaluate(expression, {var: point + h})
        f_minus = self.evaluate(expression, {var: point - h})
        
        if not (f_plus["success"] and f_minus["success"]):
            raise ValueError("Failed to evaluate function")
        
        derivative = (f_plus["result"] - f_minus["result"]) / (2 * h)
        return derivative
    
    def calculate_integral_numerically(self, expression: str, var: str, a: float, b: float, n: int = 1000) -> float:
        """
        Calculate definite integral using trapezoidal rule.
        
        Args:
            expression: Expression as string
            var: Variable to integrate over
            a: Lower bound
            b: Upper bound
            n: Number of trapezoids
            
        Returns:
            Approximate integral value
        """
        h = (b - a) / n
        total = 0.0
        
        # Evaluate at endpoints
        f_a = self.evaluate(expression, {var: a})["result"]
        f_b = self.evaluate(expression, {var: b})["result"]
        
        total += (f_a + f_b) / 2
        
        # Evaluate at interior points
        for i in range(1, n):
            x = a + i * h
            f_x = self.evaluate(expression, {var: x})["result"]
            total += f_x
        
        return total * h

# Global instance
calculator = Calculator()
