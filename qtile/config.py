# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.widget import backlight
from libqtile import hook
import os
import subprocess


## Startup ---------------------------------------

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/scripts/qtile_autostart.sh")
    subprocess.call([home])








mod = "mod4"
#terminal = guess_terminal()
terminal = "kitty"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows

    

    Key([], "XF86AudioRaiseVolume",lazy.spawn("sh /home/wen/.config/qtile/scripts/volume_indicator.sh up")),
    Key([], "XF86AudioLowerVolume",lazy.spawn("sh /home/wen/.config/qtile/scripts/volume_indicator.sh down")),

    # brighness > doesn't work
    Key(
        [],
        "XF86MonBrightnessUp",
        lazy.spawn("sh /home/wen/.config/qtile/scripts/brightness_indicator.sh up")
    ),
    Key(
        [],
        "XF86MonBrightnessDown",
        lazy.spawn("sh /home/wen/.config/qtile/scripts/brightness_indicator.sh down")
    ),



    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )


var_bg_color = '#2e3440'
var_active_bg_color = '#81A1C1'
var_active_fg_color = '#2e3440'
var_inactive_bg_color = '#3d4555'
var_inactive_fg_color = '#D8DEE9'
var_urgent_bg_color = '#BF616A'
var_urgent_fg_color = '#D8DEE9'
var_section_fg_color = '#EBCB8B'
var_active_color = '#81A1C1'
var_normal_color = '#3d4555'
var_border_width = 2
var_margin = [5,5,5,5]
var_gap_top = 45
var_gap_bottom = 5
var_gap_left = 5
var_gap_right = 5
var_font_name = 'JetBrainsMono Nerd Font'



layouts = [
        layout.Columns(
		border_focus=var_active_color,
		border_normal=var_normal_color,
		border_on_single=False,
		border_width=var_border_width,
		fair=False,
		grow_amount=10,
		insert_position=0,
		margin=var_margin,
		margin_on_single=None,
		num_columns=2,
		split=True,
		wrap_focus_columns=True,
		wrap_focus_rows=True,
		wrap_focus_stacks=True
	),

	# Layout inspired by bspwm
    layout.Bsp(
		border_focus=var_active_color,
		border_normal=var_normal_color,
		border_on_single=False,
		border_width=var_border_width,
		fair=True,
		grow_amount=10,
		lower_right=True,
		margin=var_margin,
		margin_on_single=None,
		ratio=1.6,
		wrap_clients=False
    ),

	# This layout divides the screen into a matrix of equally sized cells and places one window in each cell.
    layout.Matrix(
		border_focus=var_active_color,
		border_normal=var_normal_color,
		border_width=var_border_width,
		columns=2,
		margin=var_margin
    ),

	# Maximized layout
    layout.Max(
		border_focus=var_active_color,
		border_normal=var_normal_color,
		border_width=var_border_width,
		margin=0
    ),

	# Emulate the behavior of XMonad's default tiling scheme.
    layout.MonadTall(
		align=0,
		border_focus=var_active_color,
		border_normal=var_normal_color,
		border_width=var_border_width,
		change_ratio=0.05,
		change_size=20,
		margin=0,
		max_ratio=0.75,
		min_ratio=0.25,
		min_secondary_size=85,
		new_client_position='after_current',
		ratio=0.5,
		single_border_width=None,
		single_margin=None
    ),

	# Emulate the behavior of XMonad's ThreeColumns layout.
    layout.MonadThreeCol(
		align=0,
		border_focus=var_active_color,
		border_normal=var_normal_color,
		border_width=var_border_width,
		change_ratio=0.05,
		change_size=20,
		main_centered=True,
		margin=0,
		max_ratio=0.75,
		min_ratio=0.25,
		min_secondary_size=85,
		new_client_position='top',
		ratio=0.5,
		single_border_width=None,
		single_margin=None
    ),

	# Emulate the behavior of XMonad's horizontal tiling scheme.
    layout.MonadWide(
		align=0,
		border_focus=var_active_color,
		border_normal=var_normal_color,
		border_width=var_border_width,
		change_ratio=0.05,
		change_size=20,
		margin=0,
		max_ratio=0.75,
		min_ratio=0.25,
		min_secondary_size=85,
		new_client_position='after_current',
		ratio=0.5,
		single_border_width=None,
		single_margin=None
    ),

	# Tries to tile all windows in the width/height ratio passed in
    layout.RatioTile(
		border_focus=var_active_color,
		border_normal=var_normal_color,
		border_width=var_border_width,
		fancy=False,
		margin=var_margin,
		ratio=1.618,
		ratio_increment=0.1
    ),

	# This layout cuts piece of screen_rect and places a single window on that piece, and delegates other window placement to other layout
    layout.Slice(
		match=None,
		side='left',
		width=256
    ),

	# A mathematical layout, Renders windows in a spiral form by splitting the screen based on a selected ratio.
    layout.Spiral(
		border_focus=var_active_color,
		border_normal=var_normal_color,
		border_width=var_border_width,
		clockwise=True,
		main_pane='left',
		main_pane_ratio=None,
		margin=0,
		new_client_position='top',
		ratio=0.6180469715698392,
		ratio_increment=0.1
    ),

	# A layout composed of stacks of windows
    layout.Stack(
		autosplit=False,
		border_focus=var_active_color,
		border_normal=var_normal_color,
		border_width=var_border_width,
		fair=False,
		margin=var_margin,
		num_stacks=2
    ),

	# A layout with two stacks of windows dividing the screen
    layout.Tile(
		add_after_last=False,
		add_on_top=True,
		border_focus=var_active_color,
		border_normal=var_normal_color,
		border_on_single=False,
		border_width=var_border_width,
		expand=True,
		margin=var_margin,
		margin_on_single=None,
		master_length=1,
		master_match=None,
		max_ratio=0.85,
		min_ratio=0.15,
		ratio=0.618,
		ratio_increment=0.05,
		shift_windows=False
    ),

	# This layout works just like Max but displays tree of the windows at the left border of the screen_rect, which allows you to overview all opened windows.
    layout.TreeTab(
		active_bg=var_active_bg_color,
		active_fg=var_active_fg_color,
		bg_color=var_bg_color,
		border_width=var_border_width,
		font=var_font_name,
		fontshadow=None,
		fontsize=14,
		inactive_bg=var_inactive_bg_color,
		inactive_fg=var_inactive_fg_color,
		level_shift=0,
		margin_left=0,
		margin_y=0,
		padding_left=10,
		padding_x=10,
		padding_y=10,
		panel_width=200,
		place_right=False,
		previous_on_rm=False,
		section_bottom=0,
		section_fg=var_section_fg_color,
		section_fontsize=14,
		section_left=10,
		section_padding=10,
		section_top=10,
		sections=['Default'],
		urgent_bg=var_urgent_bg_color,
		urgent_fg=var_urgent_fg_color,
		vspace=5
    ),

	# Tiling layout that works nice on vertically mounted monitors
    layout.VerticalTile(
		border_focus=var_active_color,
		border_normal=var_normal_color,
		border_width=var_border_width,
		margin=var_margin
    ),

	# A layout with single active windows, and few other previews at the right
    layout.Zoomy(
		columnwidth=300,
		margin=var_margin,
		property_big='1.0',
		property_name='ZOOM',
		property_small='0.1'
    ),

	# Floating layout, which does nothing with windows but handles focus order
    layout.Floating(
		border_focus=var_active_color,
		border_normal=var_normal_color,
		border_width=var_border_width,
		fullscreen_border_width=0,
		max_border_width=0
	)
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        background="#000000",
        top=bar.Bar(
            [
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#000000", "#000000"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Sep(),
                widget.Battery(),
                widget.Sep(),
                widget.CPU(),
                widget.Memory(measure_mem="G"),
                widget.Sep(),
                # widget.BatteryIcon(),
                widget.Systray(),
                widget.Sep(),
                widget.Volume(),
                widget.Sep(),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                widget.Sep(),
                widget.QuickExit(),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
        border_color="#000000",
        border_width=10,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
