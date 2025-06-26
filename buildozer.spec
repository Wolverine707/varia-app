[app]

# (str) Title of your application
title = Varia

# (str) Package name
package.name = varia

# (str) Package domain (reverse DNS style)
package.domain = org.varia.app

# (str) Source code where the main.py lives
source.dir = .

# (str) Application entry point file
source.main = main.py

# (list) List of inclusions using pattern matching
source.include_exts = py,png,jpg,kv,atlas

# (str) Icon of the application
icon.filename = icon.png

# (str) Supported orientation (portrait, landscape, all)
orientation = portrait

# (list) Application requirements
requirements = python3,kivy,requests

# (bool) Whether to copy the entire source directory or just what is needed
copy_modedir = false

# (str) Presplash image (optional)
# presplash.filename = %(source.dir)s/data/presplash.png

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (list) Permissions
android.permissions = INTERNET

# (int) Android API to target
android.api = 33

# (int) Minimum Android API supported
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (int) Android NDK version to use
android.ndk = 25b

# (bool) Whether to use Android X support libraries
android.use_androidx = True

# (list) Java classes to add
# android.add_jars =

# (str) Android entry point, default is org.kivy.android.PythonActivity
# android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default is '@android:style/Theme.NoTitleBar'
# android.theme = '@android:style/Theme.NoTitleBar'

# (list) Garden requirements (if you use garden packages)
# garden_requirements =

# (str) Extra source folders to include
# extra_sources =

# (bool) Enable Android logcat
android.logcat = True

# (int) Number of bootstrap threads
# android.bootstrap_threads = 2

# (list) Presplash requirements
# presplash.color =

# (str) Orientation of the splash screen
# presplash.orientation = portrait

# (list) List of Android permissions required
# android.permissions = INTERNET

# (str) Command to run when app is built (optional)
# build_command =

# (bool) Enable or disable debug symbols
# android.debug_symbols =

# (bool) Use pip to install dependencies instead of setup.py
# use_pip = True

# (list) Supported platforms
# supported_platforms = android

---

[buildozer]

# (str) Path to build directory (default '.buildozer')
build_dir = .buildozer

# (str) Path to the buildozer log file
log_level = 2

# (str) Command to clean build (optional)
# clean_command =


