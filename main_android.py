#!/usr/bin/env python3
"""
Canadian IPTV Simulator - Kivy GUI for Android APK
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.core.window import Window

from player import IPTVPlayer
from config import Config
from channels import ChannelCategory

# Set window size for mobile
Window.size = (720, 1280)

class IPTVSimulatorApp(App):
    """Kivy-based IPTV Simulator for Android"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.config_obj = Config()
        self.player = IPTVPlayer(self.config_obj)
        self.current_view = "menu"
    
    def build(self):
        """Build the main UI"""
        self.title = "Canadian IPTV Simulator"
        return self.show_main_menu()
    
    def show_main_menu(self):
        """Display main menu"""
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Title
        title = Label(text="Canadian IPTV Simulator", size_hint_y=0.15, bold=True, font_size='24sp')
        layout.add_widget(title)
        
        # Menu buttons
        button_layout = GridLayout(cols=1, spacing=10, size_hint_y=0.85)
        
        buttons_data = [
            ("📺 List Channels", self.show_channels),
            ("📅 View EPG", self.show_epg),
            ("▶ Play Channel", self.play_channel),
            ("🔍 Search Program", self.search_programs),
            ("⚙️ Settings", self.show_settings),
            ("❌ Exit", self.exit_app),
        ]
        
        for button_text, callback in buttons_data:
            btn = Button(text=button_text, size_hint_y=0.16, font_size='16sp')
            btn.bind(on_press=callback)
            button_layout.add_widget(btn)
        
        layout.add_widget(button_layout)
        return layout
    
    def show_channels(self, instance):
        """Display all channels"""
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Header
        header = Label(text="Available Channels", size_hint_y=0.1, bold=True, font_size='18sp')
        layout.add_widget(header)
        
        # Channel list
        scroll = ScrollView(size_hint=(1, 0.8))
        channel_layout = GridLayout(cols=1, spacing=5, size_hint_y=None)
        channel_layout.bind(minimum_height=channel_layout.setter('height'))
        
        for channel in self.player.channel_manager.get_all_channels():
            hd_label = "[HD]" if channel.hd else ""
            btn_text = f"{channel.channel_id:3d} | {channel.name:25s} {hd_label}\n{channel.call_sign} | {channel.category.value}"
            btn = Button(text=btn_text, size_hint_y=None, height=60, font_size='12sp')
            btn.channel_id = channel.channel_id
            btn.bind(on_press=self.on_channel_selected)
            channel_layout.add_widget(btn)
        
        scroll.add_widget(channel_layout)
        layout.add_widget(scroll)
        
        # Back button
        back_btn = Button(text="Back", size_hint_y=0.1, font_size='14sp')
        back_btn.bind(on_press=self.show_main_menu_popup)
        layout.add_widget(back_btn)
        
        self.root.clear_widgets()
        self.root.add_widget(layout)
    
    def show_epg(self, instance):
        """Display EPG"""
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Header
        header = Label(text="Electronic Program Guide", size_hint_y=0.1, bold=True, font_size='16sp')
        layout.add_widget(header)
        
        # EPG list
        scroll = ScrollView(size_hint=(1, 0.8))
        epg_layout = GridLayout(cols=1, spacing=5, size_hint_y=None)
        epg_layout.bind(minimum_height=epg_layout.setter('height'))
        
        live_programs = self.player.epg_manager.get_live_programs()
        
        if live_programs:
            live_label = Label(text="Currently Live:", size_hint_y=None, height=30, bold=True, font_size='13sp')
            epg_layout.add_widget(live_label)
            
            for program in live_programs[:10]:
                prog_text = f"{program.title}\n{program.start_time.strftime('%H:%M')} - {program.channel.name}"
                prog_btn = Button(text=prog_text, size_hint_y=None, height=70, font_size='11sp')
                epg_layout.add_widget(prog_btn)
        else:
            no_live = Label(text="No programs currently live", size_hint_y=None, height=40)
            epg_layout.add_widget(no_live)
        
        scroll.add_widget(epg_layout)
        layout.add_widget(scroll)
        
        # Back button
        back_btn = Button(text="Back", size_hint_y=0.1, font_size='14sp')
        back_btn.bind(on_press=self.show_main_menu_popup)
        layout.add_widget(back_btn)
        
        self.root.clear_widgets()
        self.root.add_widget(layout)
    
    def play_channel(self, instance):
        """Play a channel"""
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Header
        header = Label(text="Select Channel to Play", size_hint_y=0.1, bold=True, font_size='16sp')
        layout.add_widget(header)
        
        # Channel list
        scroll = ScrollView(size_hint=(1, 0.75))
        channel_layout = GridLayout(cols=1, spacing=5, size_hint_y=None)
        channel_layout.bind(minimum_height=channel_layout.setter('height'))
        
        for channel in self.player.channel_manager.get_all_channels():
            btn = Button(text=channel.name, size_hint_y=None, height=50, font_size='13sp')
            btn.channel = channel
            btn.bind(on_press=self.on_play_channel)
            channel_layout.add_widget(btn)
        
        scroll.add_widget(channel_layout)
        layout.add_widget(scroll)
        
        # Back button
        back_btn = Button(text="Back", size_hint_y=0.15, font_size='14sp')
        back_btn.bind(on_press=self.show_main_menu_popup)
        layout.add_widget(back_btn)
        
        self.root.clear_widgets()
        self.root.add_widget(layout)
    
    def on_play_channel(self, instance):
        """Handle channel selection for playback"""
        channel = instance.channel
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        info_text = f"Now Playing: {channel.name}\n\nProvider: {self.config_obj.provider}\nResolution: {self.config_obj.resolution}\nBitrate: {self.config_obj.bitrate} kbps"
        
        info_label = Label(text=info_text, size_hint_y=0.6, font_size='12sp')
        layout.add_widget(info_label)
        
        stop_btn = Button(text="Stop", size_hint_y=0.4, font_size='13sp')
        stop_btn.bind(on_press=self.show_main_menu_popup)
        layout.add_widget(stop_btn)
        
        self.root.clear_widgets()
        self.root.add_widget(layout)
    
    def search_programs(self, instance):
        """Search for programs"""
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Header
        header = Label(text="Search Programs", size_hint_y=0.1, bold=True, font_size='16sp')
        layout.add_widget(header)
        
        # Search input
        search_input = TextInput(multiline=False, size_hint_y=0.1, font_size='14sp')
        layout.add_widget(search_input)
        
        # Results area
        scroll = ScrollView(size_hint=(1, 0.7))
        results_layout = GridLayout(cols=1, spacing=5, size_hint_y=None)
        results_layout.bind(minimum_height=results_layout.setter('height'))
        scroll.add_widget(results_layout)
        layout.add_widget(scroll)
        
        def search_action(btn):
            """Perform search"""
            results_layout.clear_widgets()
            keyword = search_input.text
            
            if not keyword:
                results_layout.add_widget(Label(text="Enter a search term", size_hint_y=None, height=40))
                return
            
            results = self.player.epg_manager.search_programs(keyword)
            
            if results:
                for program in results[:20]:
                    prog_text = f"{program.title}\n{program.start_time.strftime('%H:%M')}"
                    prog_label = Label(text=prog_text, size_hint_y=None, height=70, font_size='11sp')
                    results_layout.add_widget(prog_label)
            else:
                results_layout.add_widget(Label(text="No programs found", size_hint_y=None, height=40))
        
        # Search button
        search_btn = Button(text="Search", size_hint_y=0.1, font_size='13sp')
        search_btn.bind(on_press=search_action)
        layout.add_widget(search_btn)
        
        # Back button
        back_btn = Button(text="Back", size_hint_y=0.1, font_size='13sp')
        back_btn.bind(on_press=self.show_main_menu_popup)
        layout.add_widget(back_btn)
        
        self.root.clear_widgets()
        self.root.add_widget(layout)
    
    def show_settings(self, instance):
        """Show settings menu"""
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Header
        header = Label(text="Settings", size_hint_y=0.1, bold=True, font_size='18sp')
        layout.add_widget(header)
        
        # Settings list
        settings_layout = GridLayout(cols=1, spacing=10, size_hint_y=0.7)
        
        # Provider selector
        provider_label = Label(text="Provider:", size_hint_y=None, height=30, bold=True)
        settings_layout.add_widget(provider_label)
        
        providers = list(self.config_obj.PROVIDERS.keys())
        provider_spinner = Spinner(
            text=self.config_obj.provider,
            values=providers,
            size_hint_y=None,
            height=40
        )
        provider_spinner.bind(text=self.on_provider_changed)
        settings_layout.add_widget(provider_spinner)
        
        # Resolution selector
        resolution_label = Label(text="Resolution:", size_hint_y=None, height=30, bold=True)
        settings_layout.add_widget(resolution_label)
        
        resolutions = ["480p", "720p", "1080p", "4K"]
        resolution_spinner = Spinner(
            text=self.config_obj.resolution,
            values=resolutions,
            size_hint_y=None,
            height=40
        )
        resolution_spinner.bind(text=self.on_resolution_changed)
        settings_layout.add_widget(resolution_spinner)
        
        layout.add_widget(settings_layout)
        
        # Back button
        back_btn = Button(text="Back", size_hint_y=0.2, font_size='14sp')
        back_btn.bind(on_press=self.show_main_menu_popup)
        layout.add_widget(back_btn)
        
        self.root.clear_widgets()
        self.root.add_widget(layout)
    
    def on_provider_changed(self, spinner, text):
        """Handle provider change"""
        self.config_obj.provider = text
    
    def on_resolution_changed(self, spinner, text):
        """Handle resolution change"""
        self.config_obj.resolution = text
    
    def on_channel_selected(self, instance):
        """Handle channel selection"""
        channel_id = instance.channel_id
        channel = self.player.channel_manager.get_channel_by_id(channel_id)
        
        popup = Popup(title=channel.name, size_hint=(0.9, 0.6))
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        info_text = f"Channel: {channel.name}\nCall Sign: {channel.call_sign}\nCategory: {channel.category.value}"
        
        info_label = Label(text=info_text, size_hint_y=0.7)
        content.add_widget(info_label)
        
        close_btn = Button(text="Close", size_hint_y=0.3)
        close_btn.bind(on_press=popup.dismiss)
        content.add_widget(close_btn)
        
        popup.content = content
        popup.open()
    
    def show_main_menu_popup(self, instance):
        """Return to main menu"""
        self.root.clear_widgets()
        self.root.add_widget(self.show_main_menu())
    
    def exit_app(self, instance):
        """Exit the application"""
        self.stop()

if __name__ == "__main__":
    IPTVSimulatorApp().run()
