[app]

# (str) Title of your application
title = Canadian IPTV Simulator

# (str) Package name
package.name = canadianiptv

# (str) Package domain (needed for android/ios packaging)
package.domain = org.iptv

# (source.dir) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# Android permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# (int) Target Android API
android.api = 31

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 31

# (str) Android NDK version to use
android.ndk = 25b

# (str) The Android arch to build for
android.archs = arm64-v8a

# (bool) Enable AndroidX support
android.enable_androidx = True

# (str) launchMode to set on the main activity
android.launchmode = singleTask

# (bool) Copy library instead of making a libpymodules.so
android.copy_libs = 1

p4a.bootstrap = sdl2

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
