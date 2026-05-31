"""
Configuration settings for Canadian IPTV Simulator
"""

class Config:
    """Configuration class for IPTV simulator"""
    
    # Server settings
    SERVER_HOST = "localhost"
    SERVER_PORT = 8080
    
    # IPTV settings
    BUFFER_SIZE = 1024 * 1024  # 1MB
    STREAM_TIMEOUT = 30
    
    # Canadian providers
    PROVIDERS = {
        "Bell Fibe": "bell_fibe",
        "Rogers Ignite": "rogers_ignite",
        "Telus TV": "telus_tv",
        "Shaw Direct": "shaw_direct"
    }
    
    # Logging
    LOG_LEVEL = "INFO"
    LOG_FILE = "iptv_simulator.log"
    
    def __init__(self):
        """Initialize configuration"""
        self.provider = "Bell Fibe"
        self.resolution = "1080p"
        self.bitrate = 5000  # kbps