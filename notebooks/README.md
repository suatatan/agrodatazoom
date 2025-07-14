# Notebooks Directory

This directory contains Jupyter notebooks for data analysis and exploration.

## Structure

### `/exploratory/`
Initial data exploration notebooks:
- Data quality assessment
- Basic statistical analysis
- Initial visualizations
- Data understanding and profiling

### `/analysis/`
Detailed analytical notebooks:
- In-depth trend analysis
- Comparative studies
- Statistical modeling
- Publication-ready analyses

## Notebook Naming Convention

```
[##]_[category]_[description]_[date].ipynb
```

Where:
- `##`: Sequential number (01, 02, 03...)
- `category`: Type of analysis (exploratory, analysis, modeling, etc.)
- `description`: Brief description of the notebook content
- `date`: Creation date in YYYYMMDD format

### Examples:
- `01_exploratory_turkey_crop_data_20250714.ipynb`
- `02_analysis_regional_yield_comparison_20250714.ipynb`
- `03_modeling_production_forecasting_20250714.ipynb`

## Best Practices

1. **Documentation**: Each notebook should have a clear markdown introduction
2. **Reproducibility**: Include all necessary imports and data loading steps
3. **Clean Code**: Remove unnecessary cells before committing
4. **Outputs**: Clear outputs before committing to reduce repository size
5. **Modularity**: Keep notebooks focused on specific analyses

## Getting Started

1. Install required packages: `pip install -r requirements.txt`
2. Launch Jupyter: `jupyter notebook`
3. Navigate to the appropriate subdirectory
4. Create a new notebook following the naming convention
