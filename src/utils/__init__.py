"""
Utility functions for AgroDataZoom project.
"""

import os
import json
import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional, Union
import pandas as pd

def setup_logging(log_level: str = "INFO") -> logging.Logger:
    """
    Setup logging configuration.
    
    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR)
        
    Returns:
        Configured logger object
    """
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    return logging.getLogger(__name__)

def create_metadata(file_path: Union[str, Path],
                   source: str,
                   description: str,
                   additional_info: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Create metadata for a dataset.
    
    Args:
        file_path: Path to the data file
        source: Data source information
        description: Description of the dataset
        additional_info: Additional metadata information
        
    Returns:
        Metadata dictionary
    """
    metadata = {
        "file_path": str(file_path),
        "source": source,
        "description": description,
        "created_date": datetime.now().isoformat(),
        "file_size_mb": round(Path(file_path).stat().st_size / (1024 * 1024), 2)
    }
    
    if additional_info:
        metadata.update(additional_info)
    
    return metadata

def save_metadata(metadata: Dict[str, Any], output_path: Union[str, Path]) -> None:
    """
    Save metadata to a JSON file.
    
    Args:
        metadata: Metadata dictionary
        output_path: Path where to save the metadata file
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)

def get_data_summary(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Generate a summary of a dataframe.
    
    Args:
        df: Input dataframe
        
    Returns:
        Summary statistics dictionary
    """
    summary = {
        "shape": df.shape,
        "columns": list(df.columns),
        "data_types": df.dtypes.to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
        "numeric_summary": df.describe().to_dict() if len(df.select_dtypes(include='number').columns) > 0 else {}
    }
    
    return summary

def ensure_directory(path: Union[str, Path]) -> Path:
    """
    Ensure a directory exists, create if it doesn't.
    
    Args:
        path: Directory path
        
    Returns:
        Path object
    """
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return path

def validate_file_exists(file_path: Union[str, Path]) -> bool:
    """
    Check if a file exists.
    
    Args:
        file_path: Path to check
        
    Returns:
        True if file exists, False otherwise
    """
    return Path(file_path).exists()

def get_file_extension(file_path: Union[str, Path]) -> str:
    """
    Get file extension.
    
    Args:
        file_path: Path to the file
        
    Returns:
        File extension (e.g., '.csv', '.xlsx')
    """
    return Path(file_path).suffix.lower()

# Turkish province mappings for data standardization
TURKEY_PROVINCES = {
    'adana': 'Adana',
    'adiyaman': 'Adıyaman', 
    'afyonkarahisar': 'Afyonkarahisar',
    'agri': 'Ağrı',
    'amasya': 'Amasya',
    'ankara': 'Ankara',
    'antalya': 'Antalya',
    'artvin': 'Artvin',
    'aydin': 'Aydın',
    'balikesir': 'Balıkesir',
    'bilecik': 'Bilecik',
    'bingol': 'Bingöl',
    'bitlis': 'Bitlis',
    'bolu': 'Bolu',
    'burdur': 'Burdur',
    'bursa': 'Bursa',
    'canakkale': 'Çanakkale',
    'cankiri': 'Çankırı',
    'corum': 'Çorum',
    'denizli': 'Denizli',
    'diyarbakir': 'Diyarbakır',
    'edirne': 'Edirne',
    'elazig': 'Elazığ',
    'erzincan': 'Erzincan',
    'erzurum': 'Erzurum',
    'eskisehir': 'Eskişehir',
    'gaziantep': 'Gaziantep',
    'giresun': 'Giresun',
    'gumushane': 'Gümüşhane',
    'hakkari': 'Hakkâri',
    'hatay': 'Hatay',
    'isparta': 'Isparta',
    'mersin': 'Mersin',
    'istanbul': 'İstanbul',
    'izmir': 'İzmir',
    'kars': 'Kars',
    'kastamonu': 'Kastamonu',
    'kayseri': 'Kayseri',
    'kirklareli': 'Kırklareli',
    'kirsehir': 'Kırşehir',
    'kocaeli': 'Kocaeli',
    'konya': 'Konya',
    'kutahya': 'Kütahya',
    'malatya': 'Malatya',
    'manisa': 'Manisa',
    'kahramanmaras': 'Kahramanmaraş',
    'mardin': 'Mardin',
    'mugla': 'Muğla',
    'mus': 'Muş',
    'nevsehir': 'Nevşehir',
    'nigde': 'Niğde',
    'ordu': 'Ordu',
    'rize': 'Rize',
    'sakarya': 'Sakarya',
    'samsun': 'Samsun',
    'siirt': 'Siirt',
    'sinop': 'Sinop',
    'sivas': 'Sivas',
    'tekirdag': 'Tekirdağ',
    'tokat': 'Tokat',
    'trabzon': 'Trabzon',
    'tunceli': 'Tunceli',
    'sanliurfa': 'Şanlıurfa',
    'usak': 'Uşak',
    'van': 'Van',
    'yozgat': 'Yozgat',
    'zonguldak': 'Zonguldak',
    'aksaray': 'Aksaray',
    'bayburt': 'Bayburt',
    'karaman': 'Karaman',
    'kirikkale': 'Kırıkkale',
    'batman': 'Batman',
    'sirnak': 'Şırnak',
    'bartin': 'Bartın',
    'ardahan': 'Ardahan',
    'igdir': 'Iğdır',
    'yalova': 'Yalova',
    'karabuk': 'Karabük',
    'kilis': 'Kilis',
    'osmaniye': 'Osmaniye',
    'duzce': 'Düzce'
}
