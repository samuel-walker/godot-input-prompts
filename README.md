# Godot Input Prompts

New nodes providing easy-to-use input prompts.

The current version supports the following icons:
- Keyboard and mouse
- Xbox
- PlayStation
- Nintendo Switch

Please note that the PlayStation icons must be completed manually in an editor.

## Installation

To install, follow the latest instructions for [installing
plugins](https://docs.godotengine.org/en/stable/tutorials/plugins/editor/installing_plugins.html)
in the Godot documentation.

## Getting Started

- **ActionPrompt** nodes display prompts based on the InputMap and an icon
preference. When set to "Automatic", the prompts update to match the input
device.

- **JoypadButtonPrompt** nodes display prompts corresponding to a button index.

- **JoypadMotionPrompt** nodes display prompts corresponding to an axis and an
  axis value.

- **KeyPrompt** nodes display prompts corresponding to a key scancode.

- **MouseButtonPrompt** nodes display prompts corresponding to a button index.

Additional documentation is available in Godot's help window after installing
the plugin.

## Icon Notes

- The 64px and 128px icons are missing:
	- mouse/wheel_left.png
	- mouse/wheel_right.png
- 64px and 128px support white or colored buttons and an outline style
- There is not perfect overlap between 16px and other sizes for keyboard keys.
- 16px contains the following extra keyboard keys:
	- at.png
	- cent.png
	- dollar.png
	- media_back.png
	- media_forward.png
	- media_next.png
	- media_pause.png
	- media_play.png
	- media_previous.png
	- media_record.png
	- media_stop.png
	- meta.png
	- nbsp.png
	- percent.png
	- pipe.png
	- scroll.png
	- tile_0504.png
	- underscore.png
- 16px\sony\ps.png does not exist in new size due to changes in Sony controllers
- The updated Kenney pack includes many more buttons than in the original.
	- Those have not been included here.

## License

The plugin is distributed under the MIT license. See [LICENSE](LICENSE) for
more information.

Prompt icons (in the icons directory) are in the [public domain][2], originally
released by [Kenney][3].

[2]:https://creativecommons.org/publicdomain/zero/1.0/
[3]:https://kenney.nl/

