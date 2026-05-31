# Canadian IPTV Simulator

A comprehensive Python 3 simulator for Canadian IPTV services including channel management, Electronic Program Guide (EPG), and interactive playback.

## Features

- 📺 **50+ Canadian TV Channels** - News, Sports, Entertainment, Movies, Kids, and Music
- 📅 **Electronic Program Guide (EPG)** - 7-day program schedule
- 🔍 **Search Functionality** - Search channels and programs
- 🎮 **Interactive Player** - Simulate channel playback with controls
- 🌐 **Multi-Language Support** - English and French content
- 🏢 **Multiple Providers** - Support for Bell Fibe, Rogers Ignite, Telus TV, Shaw Direct
- 📊 **Channel Categorization** - Organized by content type and language

## Requirements

- Python 3.8 or higher
- Dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
```bash
git clone https://github.com/papi289/Canadian-IPTV-Simulator-.git
cd Canadian-IPTV-Simulator-
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the simulator:
```bash
python3 main.py
```

### Main Menu Options

1. **List Channels** - View all available Canadian TV channels
2. **View EPG** - Browse Electronic Program Guide for current and upcoming programs
3. **Play Channel** - Select and simulate playing a channel
4. **Search Program** - Search for specific programs or content
5. **Exit** - Close the application

### Channel Categories

- **News** - CBC News Network, CTV News, Global News, Noovo
- **Sports** - TSN, Sportsnet, RDS, Sportsnet 360
- **Entertainment** - CTV, Global, City, Crave
- **Movies** - CineMax, TMN, HBO
- **Kids** - Treehouse, Disney Channel
- **Music** - MuchMusic, Space

## Project Structure

```
Canadian-IPTV-Simulator-/
├── main.py          # Application entry point
├── config.py        # Configuration settings
├── channels.py      # Channel management system
├── epg.py          # Electronic Program Guide
├── player.py       # IPTV player interface
├── utils.py        # Utility functions
├── requirements.txt # Python dependencies
└── README.md       # This file
```

## Configuration

Edit `config.py` to customize:
- Server host and port
- Video resolution (480p, 720p, 1080p, 4K)
- Bitrate (500-25000 kbps)
- Preferred provider
- Logging settings

## Example Workflow

```
1. Launch the simulator
2. Select "List Channels" to see available channels
3. Select "View EPG" to check current programming
4. Choose "Play Channel" to simulate playback
5. Use player controls (P)ause, (R)esume, (S)top, (C)hannel Info, (Q)uit
6. Try "Search Program" to find specific content
```

## Features in Detail

### Channel Management
- Browse 50+ authentic Canadian channels
- Filter by category (News, Sports, Entertainment, etc.)
- Filter by language (English, French)
- Search channels by name or call sign

### EPG System
- 7-day program schedule
- Live program detection
- Program rating information (G, PG, 14A, 18A)
- Genre classification
- Search programs by title or keywords

### Playback Simulation
- Realistic stream URL display
- Current resolution and bitrate information
- Provider information
- Playback time tracking
- Interactive controls

## Canadian Providers Supported

- Bell Fibe
- Rogers Ignite
- Telus TV
- Shaw Direct

## Future Enhancements

- [ ] DVR/Recording functionality
- [ ] Favorites and watchlist
- [ ] Parental controls
- [ ] Closed captioning options
- [ ] Multi-bitrate streaming simulation
- [ ] Subscription management
- [ ] Payment integration
- [ ] Analytics dashboard
- [ ] API server mode
- [ ] Mobile app simulation

## License

MIT License - See LICENSE file for details

## Author

Created for Canadian IPTV enthusiasts and developers

## Disclaimer

This is a simulation/educational project and does not provide actual IPTV streaming services. It's designed for learning Python development and understanding IPTV system architecture.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests.

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

**Version:** 1.0.0  
**Last Updated:** May 2026