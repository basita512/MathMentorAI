"""Mathematical plotting tool for visualizations."""
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for Streamlit
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from pathlib import Path
from typing import List, Tuple, Optional, Dict, Any
import io
import base64

from src.utils.logger import get_logger
from src.tools.calculator import Calculator

logger = get_logger()

class Plotter:
    """
    Mathematical plotting tool supporting 2D curves, parametric plots,
    and interactive visualizations.
    """
    
    def __init__(self, output_dir: str = "data/plots"):
        """Initialize plotter."""
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.calculator = Calculator()
    
    def plot_function(
        self,
        expression: str,
        x_range: Tuple[float, float],
        variable: str = "x",
        title: Optional[str] = None,
        save_path: Optional[str] = None,
        use_interactive: bool = True
    ) -> Dict[str, Any]:
        """
        Plot a mathematical function.
        
        Args:
            expression: Function expression (e.g., "x**2 + 2*x + 1")
            x_range: (min, max) for x values
            variable: Variable name (default "x")
            title: Plot title
            save_path: Path to save plot (optional)
            use_interactive: Use Plotly (True) or Matplotlib (False)
            
        Returns:
            Dict with plot_path and success status
        """
        try:
            # Generate x values
            x_min, x_max = x_range
            x_values = np.linspace(x_min, x_max, 500)
            
            # Calculate y values
            y_values = []
            for x in x_values:
                result = self.calculator.evaluate(expression, {variable: float(x)})
                if result["success"]:
                    y_values.append(result["result"])
                else:
                    y_values.append(np.nan)
            
            y_values = np.array(y_values)
            
            if use_interactive:
                return self._plot_plotly(x_values, y_values, expression, title, save_path)
            else:
                return self._plot_matplotlib(x_values, y_values, expression, title, save_path)
                
        except Exception as e:
            logger.error(f"Plotting error: {e}")
            return {"success": False, "error": str(e)}
    
    def _plot_matplotlib(
        self,
        x_values: np.ndarray,
        y_values: np.ndarray,
        expression: str,
        title: Optional[str],
        save_path: Optional[str]
    ) -> Dict[str, Any]:
        """Create static plot using Matplotlib."""
        plt.figure(figsize=(10, 6))
        plt.plot(x_values, y_values, 'b-', linewidth=2)
        plt.grid(True, alpha=0.3)
        plt.xlabel('x', fontsize=12)
        plt.ylabel('f(x)', fontsize=12)
        plt.title(title or f'y = {expression}', fontsize=14)
        
        # Add zero lines
        plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5, alpha=0.3)
        plt.axvline(x=0, color='k', linestyle='-', linewidth=0.5, alpha=0.3)
        
        # Save plot
        if save_path is None:
            save_path = self.output_dir / f"plot_{hash(expression) % 1000000}.png"
        
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        plt.close()
        
        logger.info(f"Saved plot to {save_path}")
        
        return {
            "success": True,
            "plot_path": str(save_path),
            "plot_type": "matplotlib"
        }
    
    def _plot_plotly(
        self,
        x_values: np.ndarray,
        y_values: np.ndarray,
        expression: str,
        title: Optional[str],
        save_path: Optional[str]
    ) -> Dict[str, Any]:
        """Create interactive plot using Plotly."""
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=x_values,
            y=y_values,
            mode='lines',
            name=expression,
            line=dict(color='blue', width=2)
        ))
        
        fig.update_layout(
            title=title or f'y = {expression}',
            xaxis_title='x',
            yaxis_title='f(x)',
            hovermode='closest',
            template='plotly_white',
            showlegend=True
        )
        
        # Add grid and zero lines
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray', zeroline=True)
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray', zeroline=True)
        
        # Save as HTML
        if save_path is None:
            save_path = self.output_dir / f"plot_{hash(expression) % 1000000}.html"
        
        fig.write_html(save_path)
        
        logger.info(f"Saved interactive plot to {save_path}")
        
        return {
            "success": True,
            "plot_path": str(save_path),
            "plot_type": "plotly",
            "fig": fig  # Return figure for Streamlit display
        }
    
    def plot_multiple_functions(
        self,
        expressions: List[str],
        x_range: Tuple[float, float],
        labels: Optional[List[str]] = None,
        title: Optional[str] = None,
        save_path: Optional[str] = None,
        use_interactive: bool = True
    ) -> Dict[str, Any]:
        """
        Plot multiple functions on the same axes.
        
        Args:
            expressions: List of function expressions
            x_range: (min, max) for x values
            labels: Optional labels for each function
            title: Plot title
            save_path: Path to save plot
            use_interactive: Use Plotly or Matplotlib
            
        Returns:
            Dict with plot info
        """
        try:
            x_min, x_max = x_range
            x_values = np.linspace(x_min, x_max, 500)
            
            if use_interactive:
                fig = go.Figure()
                
                colors = ['blue', 'red', 'green', 'orange', 'purple', 'brown']
                
                for i, expr in enumerate(expressions):
                    y_values = []
                    for x in x_values:
                        result = self.calculator.evaluate(expr, {"x": float(x)})
                        y_values.append(result["result"] if result["success"] else np.nan)
                    
                    label = labels[i] if labels and i < len(labels) else expr
                    color = colors[i % len(colors)]
                    
                    fig.add_trace(go.Scatter(
                        x=x_values,
                        y=y_values,
                        mode='lines',
                        name=label,
                        line=dict(color=color, width=2)
                    ))
                
                fig.update_layout(
                    title=title or "Multiple Functions",
                    xaxis_title='x',
                    yaxis_title='f(x)',
                    template='plotly_white',
                    showlegend=True
                )
                
                fig.update_xaxes(showgrid=True, zeroline=True)
                fig.update_yaxes(showgrid=True, zeroline=True)
                
                if save_path is None:
                    save_path = self.output_dir / f"multi_plot_{len(expressions)}.html"
                
                fig.write_html(save_path)
                
                return {
                    "success": True,
                    "plot_path": str(save_path),
                    "plot_type": "plotly",
                    "fig": fig
                }
            else:
                # Matplotlib version
                plt.figure(figsize=(10, 6))
                
                colors = ['b', 'r', 'g', 'orange', 'purple', 'brown']
                
                for i, expr in enumerate(expressions):
                    y_values = []
                    for x in x_values:
                        result = self.calculator.evaluate(expr, {"x": float(x)})
                        y_values.append(result["result"] if result["success"] else np.nan)
                    
                    label = labels[i] if labels and i < len(labels) else expr
                    color = colors[i % len(colors)]
                    
                    plt.plot(x_values, y_values, color=color, linewidth=2, label=label)
                
                plt.grid(True, alpha=0.3)
                plt.xlabel('x')
                plt.ylabel('f(x)')
                plt.title(title or "Multiple Functions")
                plt.legend()
                plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5, alpha=0.3)
                plt.axvline(x=0, color='k', linestyle='-', linewidth=0.5, alpha=0.3)
                
                if save_path is None:
                    save_path = self.output_dir / f"multi_plot_{len(expressions)}.png"
                
                plt.savefig(save_path, dpi=150, bbox_inches='tight')
                plt.close()
                
                return {
                    "success": True,
                    "plot_path": str(save_path),
                    "plot_type": "matplotlib"
                }
                
        except Exception as e:
            logger.error(f"Multiple plot error: {e}")
            return {"success": False, "error": str(e)}
    
    def plot_parametric(
        self,
        x_expr: str,
        y_expr: str,
        t_range: Tuple[float, float],
        title: Optional[str] = None,
        save_path: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Plot parametric curve.
        
        Args:
            x_expr: Expression for x(t)
            y_expr: Expression for y(t)
            t_range: (min, max) for parameter t
            title: Plot title
            save_path: Save path
            
        Returns:
            Plot info dict
        """
        try:
            t_min, t_max = t_range
            t_values = np.linspace(t_min, t_max, 1000)
            
            x_values = []
            y_values = []
            
            for t in t_values:
                x_result = self.calculator.evaluate(x_expr, {"t": float(t)})
                y_result = self.calculator.evaluate(y_expr, {"t": float(t)})
                
                if x_result["success"] and y_result["success"]:
                    x_values.append(x_result["result"])
                    y_values.append(y_result["result"])
                else:
                    x_values.append(np.nan)
                    y_values.append(np.nan)
            
            fig = go.Figure()
            
            fig.add_trace(go.Scatter(
                x=x_values,
                y=y_values,
                mode='lines',
                name=f'x={x_expr}, y={y_expr}',
                line=dict(color='blue', width=2)
            ))
            
            fig.update_layout(
                title=title or f'Parametric: x(t)={x_expr}, y(t)={y_expr}',
                xaxis_title='x',
                yaxis_title='y',
                template='plotly_white',
                yaxis=dict(scaleanchor="x", scaleratio=1)  # Equal aspect ratio
            )
            
            if save_path is None:
                save_path = self.output_dir / f"parametric_{hash(x_expr + y_expr) % 1000000}.html"
            
            fig.write_html(save_path)
            
            return {
                "success": True,
                "plot_path": str(save_path),
                "plot_type": "plotly",
                "fig": fig
            }
            
        except Exception as e:
            logger.error(f"Parametric plot error: {e}")
            return {"success": False, "error": str(e)}

# Global instance
plotter = Plotter()
