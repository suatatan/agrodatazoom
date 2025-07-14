# Data Directory

This directory contains all datasets used in the AgroDataZoom project.

## Structure

- `raw/`: Original, unprocessed data files as downloaded from sources
- `processed/`: Cleaned and processed datasets ready for analysis  
- `external/`: Third-party datasets and supplementary data sources

## Data Sources by Country

### Turkey (`raw/turkey/`)
- `tuik/`: TÜİK (Turkish Statistical Institute) datasets
  - Agricultural production statistics
  - Livestock data
  - Regional agricultural indicators
  - Trade statistics

### Global (`raw/global/`)
- FAO global food security indicators
- World Bank agricultural development data
- USDA international agricultural data

## Data Guidelines

1. **Raw Data**: Never modify files in the `raw/` directory
2. **Documentation**: Each dataset should have accompanying metadata
3. **Versioning**: Use date stamps for data file versions
4. **Format**: Prefer CSV format for processed data when possible

## Naming Convention

```
[country]_[source]_[indicator]_[year_range].csv
```

Example: `turkey_tuik_crop_production_2010_2023.csv`
