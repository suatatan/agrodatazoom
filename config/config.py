"""
Configuration settings for AgroDataZoom project.
"""

import os
from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).parent.parent

# Data directories
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXTERNAL_DATA_DIR = DATA_DIR / "external"

# Country-specific data directories
TURKEY_DATA_DIR = RAW_DATA_DIR / "turkey"
TUIK_DATA_DIR = TURKEY_DATA_DIR / "tuik"

# Output directories
REPORTS_DIR = PROJECT_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

# TÜİK specific settings
TUIK_CONFIG = {
    "base_url": "https://www.tuik.gov.tr",
    "encoding": "utf-8",
    "date_format": "%Y-%m-%d",
    "file_extensions": [".xlsx", ".xls", ".csv"]
}

# Visualization settings
VIZ_CONFIG = {
    "figure_size": (12, 8),
    "dpi": 300,
    "style": "seaborn-v0_8",
    "color_palette": "Set2",
    "font_size": 12
}

# Data processing settings
PROCESSING_CONFIG = {
    "missing_value_threshold": 0.1,
    "outlier_method": "iqr",
    "date_columns": ["year", "date", "period"],
    "numeric_precision": 2
}
