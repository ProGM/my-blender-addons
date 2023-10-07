# Blender add-ons
A collection of blender add-ons I've created for my workflow and a list of useful ones from the internet.

## In this repo
- `keyframes_to_linear.py`: It adds two simple commands: "Set All Keyframes to Linear" and "Set Selected Keyframes to Linear".

## From the internet
- https://github.com/gnastacast/bendy_bone_handles

## Scripting utilities

### Listing all available context menus
Paste this in the blender python console:
```python
[name for name in dir(bpy.types) if "MT" in name]
```
Example output:
```python
['ALL_MT_editormenu', 'ASSETBROWSER_MT_asset', 'ASSETBROWSER_MT_catalog', 'ASSETBROWSER_MT_context_menu', 'ASSETBROWSER_MT_editor_menus', 'ASSETBROWSER_MT_metadata_preview_menu', 'ASSETBROWSER_MT_select', 'ASSETBROWSER_MT_view', ...]
```
