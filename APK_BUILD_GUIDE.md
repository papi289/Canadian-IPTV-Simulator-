# Canadian IPTV Simulator - APK Build Instructions

## Building APK from Python

To convert the Canadian IPTV Simulator into an Android APK, follow these steps:

### **Prerequisites**

1. **Python 3.8+** installed on your system
2. **Linux environment** (WSL on Windows is recommended, or use a Linux VM)
3. **Java Development Kit (JDK)** installed
4. **Android SDK** installed
5. **Buildozer** package

### **Step 1: Install Required Tools**

```bash
# Install Buildozer
pip install buildozer

# Install Kivy
pip install kivy

# On Linux, you may need additional dependencies:
sudo apt-get update
sudo apt-get install -y build-essential git python3-dev ffmpeg libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev openjdk-11-jdk-headless
```

### **Step 2: Initialize Buildozer (if needed)**

If you need to create a new buildozer.spec file:

```bash
buildozer init
```

A `buildozer.spec` file is already included in this project.

### **Step 3: Edit buildozer.spec (Optional)**

Customize the following settings in `buildozer.spec`:

```ini
[app]
title = Canadian IPTV Simulator
package.name = canadianiptv
package.domain = org.iptv
version = 1.0.0
requirements = python3,kivy
```

### **Step 4: Build the APK**

Navigate to the project directory and run:

```bash
# Build debug APK (faster)
buildozer -v android debug

# Or build release APK (for production)
buildozer -v android release
```

**First build may take 15-30 minutes** as it downloads Android SDK, NDK, and other dependencies.

### **Step 5: Locate Your APK**

After building, your APK will be in:

```
bin/canadianiptv-1.0.0-debug.apk
```

Or for release:

```
bin/canadianiptv-1.0.0-release.apk
```

### **Step 6: Install on Android Device**

**Option A: Using ADB (Android Debug Bridge)**

```bash
# Connect your Android device via USB
# Enable USB debugging on your device

# Deploy and run
buildozer -v android debug deploy run

# Or manually install
adb install -r bin/canadianiptv-1.0.0-debug.apk
```

**Option B: Manual Installation**

1. Transfer the APK to your Android device
2. Open file manager on your device
3. Locate the APK and tap to install
4. Grant necessary permissions

### **Troubleshooting**

#### **Build Fails with "Java not found"**
```bash
sudo apt-get install openjdk-11-jdk-headless
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
```

#### **"buildozer: not found"**
```bash
pip install --user buildozer
export PATH=$PATH:~/.local/bin
```

#### **Cython/Build errors**
```bash
pip install --upgrade cython
```

#### **Out of Memory during build**
Reduce the number of parallel jobs:
```bash
buildozer -v android debug -- --ndk-api 21 --private /tmp/buildozer
```

### **Advanced Options**

**Build with verbose output:**
```bash
buildozer -v android debug
```

**Clean and rebuild:**
```bash
buildozer android clean
buildozer -v android debug
```

**Specify NDK/SDK versions:**
Edit `buildozer.spec`:
```ini
android.ndk = 25b
android.sdk = 31
android.api = 31
android.minapi = 21
```

### **APK Structure**

The APK includes:
- Main IPTV simulator application
- 50+ Canadian TV channels database
- EPG (Electronic Program Guide) with 7-day schedule
- Channel search and filtering
- Settings configuration

### **Permissions**

The APK requests these permissions:
- `INTERNET` - For streaming content
- `ACCESS_NETWORK_STATE` - To check network connectivity

### **Using the Android App**

Once installed, the app provides:

1. **Channel Listing** - Browse all Canadian channels by category
2. **EPG Viewer** - See current and upcoming programs
3. **Channel Player** - Simulate playing channels
4. **Program Search** - Find programs by title or keyword
5. **Settings** - Adjust provider, resolution, and bitrate

### **Running Main App vs Android App**

**Desktop (Terminal):**
```bash
python3 main.py
```

**Android (APK):**
```bash
python3 main_android.py
```

Or use the included `main_android.py` to generate the APK.

### **Additional Resources**

- [Kivy Documentation](https://kivy.org/doc/stable/)
- [Buildozer Documentation](https://buildozer.readthedocs.io/)
- [Python-for-Android](https://python-for-android.readthedocs.io/)
- [Android Developer Docs](https://developer.android.com/)

---

**Version:** 1.0.0  
**Last Updated:** May 2026
