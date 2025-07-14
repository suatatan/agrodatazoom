"""
Visualization utilities for AgroDataZoom project.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from typing import Optional, List, Dict, Tuple

from ..config.config import VIZ_CONFIG

class AgroVisualizer:
    """Main visualization class for agricultural data."""
    
    def __init__(self):
        self.config = VIZ_CONFIG
        self.setup_style()
    
    def setup_style(self):
        """Setup default visualization style."""
        plt.style.use(self.config["style"])
        sns.set_palette(self.config["color_palette"])
        plt.rcParams['figure.figsize'] = self.config["figure_size"]
        plt.rcParams['figure.dpi'] = self.config["dpi"]
        plt.rcParams['font.size'] = self.config["font_size"]
    
    def plot_time_series(self, df: pd.DataFrame, 
                        x_col: str, 
                        y_col: str, 
                        title: str = "Time Series Analysis",
                        save_path: Optional[str] = None) -> plt.Figure:
        """
        Create a time series plot.
        
        Args:
            df: Input dataframe
            x_col: Column name for x-axis (time)
            y_col: Column name for y-axis (values)
            title: Plot title
            save_path: Optional path to save the figure
            
        Returns:
            Matplotlib figure object
        """
        fig, ax = plt.subplots(figsize=self.config["figure_size"])
        
        ax.plot(df[x_col], df[y_col], linewidth=2, marker='o', markersize=4)
        ax.set_title(title, fontsize=16, fontweight='bold')
        ax.set_xlabel(x_col.replace('_', ' ').title(), fontsize=12)
        ax.set_ylabel(y_col.replace('_', ' ').title(), fontsize=12)
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=self.config["dpi"], bbox_inches='tight')
        
        return fig
    
    def plot_regional_comparison(self, df: pd.DataFrame,
                               region_col: str,
                               value_col: str,
                               title: str = "Regional Comparison") -> go.Figure:
        """
        Create an interactive regional comparison chart.
        
        Args:
            df: Input dataframe
            region_col: Column containing region names
            value_col: Column containing values to compare
            title: Plot title
            
        Returns:
            Plotly figure object
        """
        fig = px.bar(df, x=region_col, y=value_col, 
                    title=title,
                    labels={region_col: region_col.replace('_', ' ').title(),
                           value_col: value_col.replace('_', ' ').title()})
        
        fig.update_layout(
            xaxis_tickangle=-45,
            height=600,
            showlegend=False
        )
        
        return fig
    
    def plot_correlation_matrix(self, df: pd.DataFrame,
                              columns: Optional[List[str]] = None,
                              title: str = "Correlation Matrix") -> plt.Figure:
        """
        Create a correlation matrix heatmap.
        
        Args:
            df: Input dataframe
            columns: Specific columns to include (if None, use all numeric columns)
            title: Plot title
            
        Returns:
            Matplotlib figure object
        """
        if columns:
            corr_data = df[columns].corr()
        else:
            corr_data = df.select_dtypes(include=[np.number]).corr()
        
        fig, ax = plt.subplots(figsize=(10, 8))
        
        sns.heatmap(corr_data, annot=True, cmap='coolwarm', center=0,
                   square=True, ax=ax, cbar_kws={'shrink': 0.8})
        
        ax.set_title(title, fontsize=16, fontweight='bold')
        plt.tight_layout()
        
        return fig

class TurkeyVisualizer(AgroVisualizer):
    """Specialized visualizer for Turkey agricultural data."""
    
    def plot_province_map(self, df: pd.DataFrame,
                         value_col: str,
                         title: str = "Turkey Province Data") -> go.Figure:
        """
        Create a choropleth map of Turkey provinces.
        Note: This requires geojson data for Turkey provinces.
        
        Args:
            df: Dataframe with province data
            value_col: Column containing values to map
            title: Map title
            
        Returns:
            Plotly figure object
        """
        # This is a placeholder - actual implementation would require
        # Turkey province geojson data
        fig = go.Figure(data=go.Scatter(
            x=[], y=[],
            text="Turkey province map placeholder",
            mode="text"
        ))
        
        fig.update_layout(
            title=title,
            annotations=[
                dict(
                    text="Province map requires geojson data",
                    showarrow=False,
                    xref="paper", yref="paper",
                    x=0.5, y=0.5, xanchor='center', yanchor='middle'
                )
            ]
        )
        
        return fig
