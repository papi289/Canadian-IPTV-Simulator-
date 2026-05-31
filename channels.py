"""
Channel management for Canadian IPTV Simulator
"""

from dataclasses import dataclass
from typing import List, Dict
from enum import Enum

class ChannelCategory(Enum):
    """Channel categories"""
    NEWS = "News"
    SPORTS = "Sports"
    ENTERTAINMENT = "Entertainment"
    MOVIES = "Movies"
    KIDS = "Kids"
    INTERNATIONAL = "International"
    MUSIC = "Music"
    EDUCATIONAL = "Educational"

@dataclass
class Channel:
    """Channel data class"""
    channel_id: int
    name: str
    call_sign: str
    category: ChannelCategory
    url: str
    logo_url: str
    hd: bool
    language: str
    
    def __str__(self) -> str:
        hd_label = "[HD]" if self.hd else ""
        return f"{self.channel_id:3d} | {self.name:25s} {hd_label} | {self.call_sign:8s} | {self.category.value}"

class ChannelManager:
    """Manages IPTV channels"""
    
    def __init__(self):
        """Initialize channel manager with Canadian channels"""
        self.channels: List[Channel] = self._initialize_channels()
    
    def _initialize_channels(self) -> List[Channel]:
        """Initialize Canadian IPTV channels"""
        return [
            # News Channels
            Channel(1, "CBC News Network", "CBCNN", ChannelCategory.NEWS, 
                   "http://streams.cbc.ca/news", "http://logos.cbc.ca/cnn.png", True, "English"),
            Channel(2, "CTV News", "CTV", ChannelCategory.NEWS, 
                   "http://streams.ctv.ca/news", "http://logos.ctv.ca/news.png", True, "English"),
            Channel(3, "Global News", "GLOBAL", ChannelCategory.NEWS, 
                   "http://streams.globalnews.ca/news", "http://logos.globalnews.ca/news.png", True, "English"),
            Channel(4, "Noovo", "NOOVO", ChannelCategory.NEWS, 
                   "http://streams.noovo.ca/news", "http://logos.noovo.ca/news.png", True, "French"),
            
            # Sports Channels
            Channel(10, "TSN", "TSN", ChannelCategory.SPORTS, 
                   "http://streams.tsn.ca/main", "http://logos.tsn.ca/main.png", True, "English"),
            Channel(11, "Sportsnet", "SN", ChannelCategory.SPORTS, 
                   "http://streams.sportsnet.ca/main", "http://logos.sportsnet.ca/main.png", True, "English"),
            Channel(12, "RDS", "RDS", ChannelCategory.SPORTS, 
                   "http://streams.rds.ca/main", "http://logos.rds.ca/main.png", True, "French"),
            Channel(13, "Sportsnet 360", "SN360", ChannelCategory.SPORTS, 
                   "http://streams.sportsnet.ca/360", "http://logos.sportsnet.ca/360.png", True, "English"),
            
            # Entertainment Channels
            Channel(20, "CTV", "CTV", ChannelCategory.ENTERTAINMENT, 
                   "http://streams.ctv.ca/main", "http://logos.ctv.ca/main.png", True, "English"),
            Channel(21, "Global", "GLOBAL", ChannelCategory.ENTERTAINMENT, 
                   "http://streams.globalnews.ca/main", "http://logos.globalnews.ca/main.png", True, "English"),
            Channel(22, "City", "CITY", ChannelCategory.ENTERTAINMENT, 
                   "http://streams.citytv.ca/main", "http://logos.citytv.ca/main.png", True, "English"),
            Channel(23, "Crave", "CRAVE", ChannelCategory.ENTERTAINMENT, 
                   "http://streams.crave.ca/main", "http://logos.crave.ca/main.png", True, "English"),
            
            # Movie Channels
            Channel(30, "CineMax", "CMAX", ChannelCategory.MOVIES, 
                   "http://streams.cinemax.ca/main", "http://logos.cinemax.ca/main.png", True, "English"),
            Channel(31, "TMN", "TMN", ChannelCategory.MOVIES, 
                   "http://streams.tmn.ca/main", "http://logos.tmn.ca/main.png", True, "English"),
            Channel(32, "HBO", "HBO", ChannelCategory.MOVIES, 
                   "http://streams.hbo.ca/main", "http://logos.hbo.ca/main.png", True, "English"),
            
            # Kids Channels
            Channel(40, "Treehouse", "TREE", ChannelCategory.KIDS, 
                   "http://streams.treehouse.ca/main", "http://logos.treehouse.ca/main.png", True, "English"),
            Channel(41, "Disney Channel", "DISN", ChannelCategory.KIDS, 
                   "http://streams.disney.ca/channel", "http://logos.disney.ca/channel.png", True, "English"),
            
            # Music Channels
            Channel(50, "MuchMusic", "MUCH", ChannelCategory.MUSIC, 
                   "http://streams.muchmusic.ca/main", "http://logos.muchmusic.ca/main.png", True, "English"),
            Channel(51, "Space", "SPACE", ChannelCategory.MUSIC, 
                   "http://streams.space.ca/main", "http://logos.space.ca/main.png", True, "English"),
        ]
    
    def get_all_channels(self) -> List[Channel]:
        """Get all channels"""
        return self.channels
    
    def get_channel_by_id(self, channel_id: int) -> Channel:
        """Get channel by ID"""
        for channel in self.channels:
            if channel.channel_id == channel_id:
                return channel
        raise ValueError(f"Channel {channel_id} not found")
    
    def get_channels_by_category(self, category: ChannelCategory) -> List[Channel]:
        """Get channels by category"""
        return [ch for ch in self.channels if ch.category == category]
    
    def get_channels_by_language(self, language: str) -> List[Channel]:
        """Get channels by language"""
        return [ch for ch in self.channels if ch.language.lower() == language.lower()]
    
    def search_channels(self, keyword: str) -> List[Channel]:
        """Search channels by keyword"""
        keyword = keyword.lower()
        return [ch for ch in self.channels 
                if keyword in ch.name.lower() or keyword in ch.call_sign.lower()]