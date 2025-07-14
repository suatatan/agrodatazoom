"""
Data processing utilities for AgroDataZoom project.
"""

import pandas as pd
import numpy as np
from pathlib import Path
import logging
from typing import Dict, List, Optional, Union

from ..config.config import PROCESSING_CONFIG

class DataProcessor:
    """Base class for data processing operations."""
    
    def __init__(self):
        self.config = PROCESSING_CONFIG
        self.logger = logging.getLogger(__name__)
    
    def clean_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Clean a dataframe by handling missing values and outliers.
        
        Args:
            df: Input dataframe
            
        Returns:
            Cleaned dataframe
        """
        # Handle missing values
        missing_threshold = self.config["missing_value_threshold"]
        df = df.dropna(thresh=int(len(df) * (1 - missing_threshold)))
        
        # Convert date columns
        for col in self.config["date_columns"]:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col], errors='coerce')
        
        return df
    
    def standardize_column_names(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Standardize column names to lowercase with underscores.
        
        Args:
            df: Input dataframe
            
        Returns:
            Dataframe with standardized column names
        """
        df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('-', '_')
        return df
    
    def detect_outliers(self, df: pd.DataFrame, column: str) -> pd.Series:
        """
        Detect outliers using IQR method.
        
        Args:
            df: Input dataframe
            column: Column name to check for outliers
            
        Returns:
            Boolean series indicating outliers
        """
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        return (df[column] < lower_bound) | (df[column] > upper_bound)

class TuikDataProcessor(DataProcessor):
    """Specialized processor for TÜİK data."""
    
    def __init__(self):
        super().__init__()
    
    def process_agricultural_data(self, file_path: Union[str, Path]) -> pd.DataFrame:
        """
        Process TÜİK agricultural data files.
        
        Args:
            file_path: Path to the data file
            
        Returns:
            Processed dataframe
        """
        try:
            # Read the file (usually Excel for TÜİK)
            if str(file_path).endswith('.xlsx') or str(file_path).endswith('.xls'):
                df = pd.read_excel(file_path)
            else:
                df = pd.read_csv(file_path, encoding='utf-8')
            
            # Basic cleaning
            df = self.clean_dataframe(df)
            df = self.standardize_column_names(df)
            
            self.logger.info(f"Successfully processed {file_path}")
            return df
            
        except Exception as e:
            self.logger.error(f"Error processing {file_path}: {str(e)}")
            raise
    
    def aggregate_regional_data(self, df: pd.DataFrame, 
                              value_col: str, 
                              region_col: str = 'province') -> pd.DataFrame:
        """
        Aggregate data by regions.
        
        Args:
            df: Input dataframe
            value_col: Column containing values to aggregate
            region_col: Column containing region information
            
        Returns:
            Aggregated dataframe
        """
        return df.groupby(region_col)[value_col].agg(['sum', 'mean', 'std']).reset_index()
