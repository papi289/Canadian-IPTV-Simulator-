#!/usr/bin/env python3
"""
Canadian IPTV Simulator - Main Application
Simulates a Canadian IPTV service with channels, EPG, and playback
"""

import sys
from player import IPTVPlayer
from config import Config

def main():
    """Main entry point for the IPTV simulator"""
    config = Config()
    player = IPTVPlayer(config)
    
    print("=" * 60)
    print("Welcome to Canadian IPTV Simulator")
    print("=" * 60)
    print()
    
    while True:
        print("\nMain Menu:")
        print("1. List Channels")
        print("2. View EPG (Electronic Program Guide)")
        print("3. Play Channel")
        print("4. Search Program")
        print("5. Exit")
        
        choice = input("\nSelect option (1-5): ").strip()
        
        if choice == "1":
            player.list_channels()
        elif choice == "2":
            player.view_epg()
        elif choice == "3":
            player.play_channel()
        elif choice == "4":
            player.search_program()
        elif choice == "5":
            print("Thank you for using Canadian IPTV Simulator!")
            sys.exit(0)
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()