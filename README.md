# Background

This script used to be very hacky with a cache save, and then mighty dev Build 3116 came:

`API: Added functions to get/set the minimap, status bar, tabs and menu`

Hurray, no more hacking :)

# How it works ?

Automatically - just install and whenever you split window to more than 1 views - minimap will close. Go back to single mode and it will show up.

# Settings

There is only one setting that controls what layout change should impact minimap hide - by default minimap will be hidden only if more than one column is visible. You can change it to 'rows' only or 'cells' which will trigger for both columns and rows changes

# TODO

1. Still no detection of desired state though - if user started with minimap switched off - it will show back :)

