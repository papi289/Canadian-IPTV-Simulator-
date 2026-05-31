"""
Utility functions for Canadian IPTV Simulator
"""

import logging
import json
from datetime import datetime
from typing import Any, Dict

def setup_logging(log_file: str, log_level: str) -> logging.Logger:
    """Setup logging configuration"""
    logger = logging.getLogger("IPTV_Simulator")
    logger.setLevel(getattr(logging, log_level))
    
    # File handler
    fh = logging.FileHandler(log_file)
    fh.setLevel(getattr(logging, log_level))
    
    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(getattr(logging, log_level))
    
    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    
    logger.addHandler(fh)
    logger.addHandler(ch)
    
    return logger

def validate_resolution(resolution: str) -> bool:
    """Validate video resolution"""
    valid_resolutions = ["480p", "720p", "1080p", "4K"]
    return resolution in valid_resolutions

def validate_bitrate(bitrate: int) -> bool:
    """Validate bitrate"""
    return 500 <= bitrate <= 25000  # 500 kbps to 25 Mbps

def format_channel_info(channel_data: Dict[str, Any]) -> str:
    """Format channel information"""
    return json.dumps(channel_data, indent=2)

def get_canadian_time() -> str:
    """Get current Canadian time"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def check_geolocation() -> bool:
    """Check if access is from Canada (simulated)"""
    # In a real implementation, this would check IP geolocation
    return True