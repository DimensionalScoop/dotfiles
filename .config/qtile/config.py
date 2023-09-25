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

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, DropDown, ScratchPad
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook, qtile


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.run([home])


# sticky windows
win_list = []


def stick_win(qtile):
    global win_list
    win_list.append(qtile.current_window)


def unstick_win(qtile):
    global win_list
    if qtile.current_window in win_list:
        win_list.remove(qtile.current_window)


@hook.subscribe.setgroup
def move_win():
    for w in win_list:
        w.togroup(qtile.current_group.name)


mod = "mod4"
terminal = guess_terminal()

keys = [
    Key([mod], "o", lazy.function(stick_win), desc="stick win"),
    Key([mod, "shift"], "o", lazy.function(unstick_win), desc="unstick win"),
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "control"],
        "Tab",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "d", lazy.spawn("rofi -show run"), desc="Run Dmenu"),
    Key([mod], "x", lazy.spawn("/home/elayn/bin/rofi_run -l"), desc="Run logoff dmenu"),
    Key([mod], "e", lazy.spawn("dolphin"), desc="Run thunar"),
    Key(
        [mod],
        "F2",
        lazy.spawn("systemctl reboot --boot-loader-entry=auto-windows"),
        desc="reboot to windows",
    ),
    Key( [mod],"XF86Explorer", lazy.spawn("systemctl suspend"), desc="suspend"),
    Key(
        [mod],
        "a",
        lazy.spawn("/home/elayn/bin/rofi-dolphin.sh"),
        desc="Run thunar dmenu",
    ),
    # Key(
    # [mod],
    # "Escape",
    # lazy.spawn('i3lock -f -i "/home/elayn/Pictures/walp/zxqcgr1rxwo61.png"'),
    # lazy.spawn("systemctl suspend"),
    # desc="Suspend",)
    # ,  # "sh ' & '" []
    # Key([mod], "m", lazy.spawn('i1lock -f -i "/home/elayn/Pictures/walp/zxqcgr1rxwo61.png"'), desc="Lock Screens"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    # Key([mod], "asciicircum", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key(
        [mod, "control"],
        "Return",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget",
    ),
    # Sound
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([mod], "Next", lazy.spawn("pamixer -d 5")),
    Key([mod], "Prior", lazy.spawn("pamixer -i 5")),
    # Key([], "XF86AudioPlay", lazy.spawn("playerctl -i chromium,kdeconnect,firefox play-pause")),
    # Key([], "XF86AudioNext", lazy.spawn("playerctl -i chromium,kdeconnect,firefox next")),
    # Key([], "XF86AudioPrev", lazy.spawn("playerctl -i chromium,kdeconnect,firefox previous")),
    # Key([], "XF86AudioStop", lazy.spawn("playerctl -i chromium,kdeconnect,firefox stop")),
    Key([mod], "s", lazy.spawn("pactl set-source-mute @DEFAULT_SOURCE@ toggle")),
    Key([mod], "minus", lazy.spawn("/home/elayn/bin/screenshot-to-clip.sh")),
    # Key([], "", lazy.spawn("")),
    Key([mod], "numbersign", lazy.spawn("/home/elayn/bin/hamster-stop.sh")),
    # Key([], "XF86AudioMicMute",lazy.),
]

groups = [
    Group("C", spawn=["kotatogram-desktop"]),
    Group("1", spawn="firefox"),
    Group("2", spawn=["xfce4-clipman"]),
    Group("3"),
    Group("4"),
    Group("Q"),
    Group("R"),
]


# keys.extend([Key([mod],"asciicircum",lazy.group[groups[0].name].toscreen())])

for i in groups:
    key_name = i.name.lower()
    if key_name == "c":
        key_name = "asciicircum"
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                key_name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                key_name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

# groups.append(ScratchPad("scratchpad", DropDown("term", "alacritty", opacity=0.8)))
# keys.append(Key([mod], 'F12', lazy.group['scratchpad'].dropdown_toggle('scratchpad')))

layouts = [
    layout.Columns(
        border_focus="7D894D",  # "c68538ff",
        border_focus_stack="ffff3fff",
        border_normal="370926",
        border_normal_stack="42113C",
        border_width=2,
        margin=25,
        split=True,
        num_columns=2,
    ),
    layout.Max(),
    # layout.Tile(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(margin=25),
    layout.MonadTall(
        margin=25,
        align=layout.MonadTall._left,
        ratio=0.5,
    ),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Iosevka Term Medium Extended", fontsize=20, padding=5, color="c8c6c5ff"
)
extension_defaults = widget_defaults.copy()


class NetMax(widget.Net):
    def _format(self, down, down_letter, up, up_letter, total, total_letter):
        lenght = int(6)
        max_len_down = lenght - len(down_letter)
        max_len_up = lenght - len(up_letter)
        max_len_total = lenght - len(total_letter)

        down_prec = 0 if down_letter == "kB" or down_letter == "B" else 1
        up_prec = 0 if up_letter == "kB" or up_letter == "B" else 1

        down = ("{val:{max_len}." + str(down_prec) + "f}").format(
            val=down, max_len=max_len_down
        )
        up = ("{val:{max_len}." + str(up_prec) + "f}").format(
            val=up, max_len=max_len_up
        )
        total = "{val:{max_len}.1f}".format(val=total, max_len=max_len_total)

        return down[:max_len_down], up[:max_len_up], total[:max_len_total]

    def convert_b(self, num_bytes: float):
        return num_bytes / 1e6, " MB"  # converted_bytes, unit


screens = [
    Screen(
        # top = bar.Bar([widget.Sep()],3),
        left=bar.Bar([widget.Sep()], 3),
        right=bar.Bar([widget.Sep()], 3),
        bottom=bar.Bar(
            [
                widget.WindowName(max_chars=100),
                widget.Notify(parse_text=lambda t: t.replace("\n", " "), max_chars=300),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # widget.Canto(feeds=["https://www.deutschlandfunk.de/die-nachrichten.353.de.xml"]),
                NetMax(format=" {down:>2.1f} ↓↑ {up:>2.1f}", update_interval=1),
                widget.CPU(format="𝛹 {load_percent:>2.0f}%"),
                widget.ThermalSensor(tag_sensor="Composite"),
                widget.ThermalSensor(tag_sensor="edge"),
                widget.ThermalSensor(tag_sensor="Tctl"),
                widget.Memory(format="🐏 {MemUsed:.1f} GB", measure_mem="G"),
                widget.DF(
                    format="💾 {uf} GB",
                    update_interval=10,
                    partition="/",
                    visible_on_warn=False,
                ),
                widget.PulseVolume(fmt="🎧 {}", volume_app="pavucontrol"),
                widget.Systray(icon_size=26, padding=2),
                widget.Clock(format=r"%a %m/%d %H%M"),
                widget.Sep(),
                widget.GroupBox(
                    borderwidth=2,
                    highlight_method="line",
                    margin=0,
                    margin_y=5,
                    rounded=False,
                    highlight_color=["241d19ff", "9f6e3aff"],
                    active="c8c6c5ff",
                    inactive="676767",
                    this_current_screen_border="9f6e3aff",
                    urgent_border="c8c6c5ff",
                ),
                widget.CurrentLayoutIcon(scale=0.5),
            ],
            35,
            background="241d19ff",
        ),
    ),
]

# Drag floating layouts
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button2", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button3", lazy.window.toggle_floating()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False

default_float_rules = [
         Match(wm_type="utility"),
         Match(wm_type="notification"),
         Match(wm_type="toolbar"),
         Match(wm_type="splash"),
         Match(wm_type="dialog"),
         Match(wm_class="file_progress"),
         Match(wm_class="confirm"),
         Match(wm_class="dialog"),
         Match(wm_class="download"),
         Match(wm_class="error"),
         Match(wm_class="notification"),
         Match(wm_class="splash"),
         Match(wm_class="toolbar"),
         #Match(func=lambda c: c.has_fixed_size()),
         #Match(func=lambda c: c.has_fixed_ratio()),
     ]

floating_layout = layout.Floating(
    float_rules=[
        *default_float_rules,
        # Run the utility of `xprop` to see the wm class and name of an X client.
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="Tilda"),
        # Match(title="Guake!"),  # drop-down terminal
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
