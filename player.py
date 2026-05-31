"""
IPTV Player - Main playback interface
"""

import time
from typing import Optional
from channels import ChannelManager, ChannelCategory, Channel
from epg import EPGManager, Program
from config import Config

class IPTVPlayer:
    """IPTV Player application"""
    
    def __init__(self, config: Config):
        """Initialize IPTV Player"""
        self.config = config
        self.channel_manager = ChannelManager()
        self.epg_manager = EPGManager()
        self.current_channel: Optional[Channel] = None
        self.is_playing = False
    
    def list_channels(self) -> None:
        """Display list of all channels"""
        print("\n" + "=" * 80)
        print("CHANNEL LIST")
        print("=" * 80)
        
        # Group by category
        categories = {}
        for channel in self.channel_manager.get_all_channels():
            cat = channel.category.value
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(channel)
        
        for category, channels in sorted(categories.items()):
            print(f"\n{category}:")
            print("-" * 80)
            for channel in channels:
                print(channel)
    
    def view_epg(self) -> None:
        """View Electronic Program Guide"""
        print("\n" + "=" * 80)
        print("ELECTRONIC PROGRAM GUIDE (EPG)")
        print("=" * 80)
        
        channel_num = input("\nEnter channel number (or press Enter for all): ").strip()
        
        if channel_num:
            try:
                channel = self.channel_manager.get_channel_by_id(int(channel_num))
                programs = self.epg_manager.get_programs_by_channel(channel)
                
                if programs:
                    print(f"\n{channel.name} - {channel.call_sign}")
                    print("-" * 80)
                    for program in programs[:10]:  # Show next 10 programs
                        print(program)
                else:
                    print(f"No programs found for channel {channel_num}")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            # Show live programs
            live = self.epg_manager.get_live_programs()
            if live:
                print("\nCurrently Live:")
                print("-" * 80)
                for program in live[:10]:
                    print(program)
            else:
                print("No programs currently live")
    
    def play_channel(self) -> None:
        """Play a channel"""
        self.list_channels()
        
        channel_num = input("\nEnter channel number to play: ").strip()
        
        try:
            channel = self.channel_manager.get_channel_by_id(int(channel_num))
            self._play(channel)
        except ValueError as e:
            print(f"Error: {e}")
    
    def _play(self, channel: Channel) -> None:
        """Start playing a channel"""
        self.current_channel = channel
        self.is_playing = True
        
        print("\n" + "=" * 80)
        print(f"Now Playing: {channel.name} ({channel.call_sign})")
        print("=" * 80)
        print(f"Resolution: {self.config.resolution}")
        print(f"Bitrate: {self.config.bitrate} kbps")
        print(f"Stream URL: {channel.url}")
        print(f"Provider: {self.config.provider}")
        print("\nPlayback Controls:")
        print("  [P] Pause  [R] Resume  [S] Stop  [C] Channel Info  [Q] Quit")
        print("=" * 80)
        
        # Simulate playback
        self._simulate_playback()
    
    def _simulate_playback(self) -> None:
        """Simulate channel playback"""
        elapsed = 0
        while self.is_playing:
            try:
                command = input(f"\nPlayback Time: {self._format_time(elapsed)} > ").strip().upper()
                
                if command == "Q":
                    self.is_playing = False
                    print("Stopping playback...")
                elif command == "P":
                    print("Paused")
                elif command == "R":
                    print("Resumed")
                elif command == "S":
                    self.is_playing = False
                    print("Stopped")
                elif command == "C":
                    self._show_channel_info()
                else:
                    elapsed += 5
            except KeyboardInterrupt:
                self.is_playing = False
                print("\nPlayback stopped")
    
    def _show_channel_info(self) -> None:
        """Show current channel information"""
        if self.current_channel:
            programs = self.epg_manager.get_programs_by_channel(self.current_channel)
            if programs:
                print(f"\nChannel: {self.current_channel.name}")
                print(f"Call Sign: {self.current_channel.call_sign}")
                print(f"Category: {self.current_channel.category.value}")
                print(f"Language: {self.current_channel.language}")
                print(f"HD: {'Yes' if self.current_channel.hd else 'No'}")
                print(f"\nNext Programs:")
                for program in programs[:3]:
                    print(f"  {program}")
    
    def search_program(self) -> None:
        """Search for programs"""
        print("\n" + "=" * 80)
        print("SEARCH PROGRAMS")
        print("=" * 80)
        
        keyword = input("Enter program name or keyword: ").strip()
        
        if not keyword:
            print("No search term entered")
            return
        
        results = self.epg_manager.search_programs(keyword)
        
        if results:
            print(f"\nFound {len(results)} programs:")
            print("-" * 80)
            for program in results[:20]:  # Show top 20 results
                print(program)
        else:
            print(f"No programs found matching '{keyword}'")
    
    @staticmethod
    def _format_time(seconds: int) -> str:
        """Format seconds to HH:MM:SS"""
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        secs = seconds % 60
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"