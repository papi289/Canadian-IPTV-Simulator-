"""
Electronic Program Guide (EPG) for Canadian IPTV Simulator
"""

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Dict
from channels import Channel

@dataclass
class Program:
    """Program data class"""
    program_id: str
    title: str
    description: str
    start_time: datetime
    end_time: datetime
    channel: Channel
    genre: str
    rating: str  # G, PG, 14A, 18A, etc.
    image_url: str
    year: int = None  # Year the program aired/airs
    decade: str = None  # Decade (1980s, 1990s, 2000s, 2010s, 2020s)
    
    def is_live(self) -> bool:
        """Check if program is currently live"""
        now = datetime.now()
        return self.start_time <= now <= self.end_time
    
    def calculate_decade(self) -> str:
        """Calculate decade from year"""
        if self.year:
            decade_num = (self.year // 10) * 10
            return f"{decade_num}s"
        return None
    
    def __str__(self) -> str:
        time_str = self.start_time.strftime("%H:%M")
        status = "[LIVE]" if self.is_live() else ""
        year_str = f" ({self.year})" if self.year else ""
        decade_str = f" [{self.decade}]" if self.decade else ""
        return f"{time_str} {status} | {self.title:40s} | {self.rating:4s} | {self.genre}{year_str}{decade_str}"

class EPGManager:
    """Manages Electronic Program Guide"""
    
    def __init__(self):
        """Initialize EPG manager"""
        self.programs: List[Program] = []
        self._generate_sample_epg()
    
    def _generate_sample_epg(self) -> None:
        """Generate sample EPG data with years and decades"""
        sample_programs = [
            ("The National", "CBC News Network", "News program", "G", 2024),
            ("CTV News at 6", "CTV News", "Daily news broadcast", "G", 2024),
            ("Global News Hour", "Global News", "News and current affairs", "G", 2024),
            ("Jeopardy!", "CTV", "Game show", "G", 2023),
            ("The Bachelor", "CTV", "Reality dating show", "14A", 2024),
            ("Schitt's Creek", "CBC", "Comedy series", "14A", 2022),
            ("Workin' Moms", "CBC", "Comedy series", "14A", 2021),
            ("Blue Bloods", "Global", "Crime drama", "14A", 2023),
            ("Toronto Raptors Game", "Sportsnet", "NBA Basketball", "PG", 2024),
            ("Maple Leafs Game", "Sportsnet", "NHL Hockey", "PG", 2024),
            ("CFL Football", "TSN", "Canadian Football League", "PG", 2024),
            ("Monday Night Football", "Sportsnet", "NFL Football", "PG", 2023),
        ]
        
        # Generate EPG for next 7 days
        now = datetime.now()
        for day_offset in range(7):
            current_date = now + timedelta(days=day_offset)
            current_date = current_date.replace(hour=6, minute=0, second=0, microsecond=0)
            
            for idx, (title, channel_name, description, rating, year) in enumerate(sample_programs):
                start_time = current_date + timedelta(hours=idx*2)
                end_time = start_time + timedelta(hours=2)
                
                program = Program(
                    program_id=f"prog_{day_offset}_{idx}",
                    title=title,
                    description=description,
                    start_time=start_time,
                    end_time=end_time,
                    channel=Channel(idx, channel_name, channel_name[:3], None, "", "", True, "English"),
                    genre="Varies",
                    rating=rating,
                    image_url=f"http://images.iptv.ca/{title.replace(' ', '_')}.jpg",
                    year=year
                )
                # Calculate and set decade
                program.decade = program.calculate_decade()
                self.programs.append(program)
    
    def get_programs_by_channel(self, channel: Channel) -> List[Program]:
        """Get programs for a specific channel"""
        return [p for p in self.programs if p.channel.name == channel.name]
    
    def get_live_programs(self) -> List[Program]:
        """Get currently live programs"""
        return [p for p in self.programs if p.is_live()]
    
    def get_programs_by_time(self, start: datetime, end: datetime) -> List[Program]:
        """Get programs within a time range"""
        return [p for p in self.programs 
                if p.start_time >= start and p.end_time <= end]
    
    def get_programs_by_genre(self, genre: str) -> List[Program]:
        """Get programs by genre"""
        return [p for p in self.programs if p.genre.lower() == genre.lower()]
    
    def get_programs_by_year(self, year: int) -> List[Program]:
        """Get programs by year"""
        return [p for p in self.programs if p.year == year]
    
    def get_programs_by_decade(self, decade: str) -> List[Program]:
        """Get programs by decade (e.g., '1980s', '1990s', '2000s', '2010s', '2020s')"""
        return [p for p in self.programs if p.decade == decade]
    
    def get_available_years(self) -> List[int]:
        """Get list of available years in EPG"""
        years = set(p.year for p in self.programs if p.year is not None)
        return sorted(list(years), reverse=True)
    
    def get_available_decades(self) -> List[str]:
        """Get list of available decades in EPG"""
        decades = set(p.decade for p in self.programs if p.decade is not None)
        return sorted(list(decades), reverse=True)
    
    def search_programs(self, keyword: str) -> List[Program]:
        """Search programs by keyword"""
        keyword = keyword.lower()
        return [p for p in self.programs 
                if keyword in p.title.lower() or keyword in p.description.lower()]
    
    def search_programs_by_year(self, keyword: str, year: int) -> List[Program]:
        """Search programs by keyword and year"""
        keyword = keyword.lower()
        return [p for p in self.programs 
                if (keyword in p.title.lower() or keyword in p.description.lower()) and p.year == year]
    
    def search_programs_by_decade(self, keyword: str, decade: str) -> List[Program]:
        """Search programs by keyword and decade"""
        keyword = keyword.lower()
        return [p for p in self.programs 
                if (keyword in p.title.lower() or keyword in p.description.lower()) and p.decade == decade]
