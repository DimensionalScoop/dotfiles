import os
import subprocess
from typing import DefaultDict, List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import (
    Click,
    Drag,
    Group,
    Key,
    Match,
    Screen,
    DropDown,
    ScratchPad,
)
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook, qtile


mod = "mod4"
terminal = guess_terminal()


from keys import keys
from screens import screens, widget_defaults, extension_defaults
from layout import layouts
from misc import *


groups = [
    Group(
        "Z",
        spawn=["kotatogram-desktop", "schildichat-desktop"],
    ),
    Group(
        "U",
        spawn="bash -c 'MOZ_DISABLE_RDD_SANDBOX=1 MOZ_WEBRENDER=1 firefox'",
    ),
    Group("I", spawn=["xfce4-clipman"]),
    Group("O"),
    Group("P"),
    Group("N"),
    Group("M"),
    ScratchPad(
        "scratchpad",
        [
            DropDown("term", "alacritty"),
        ],
    ),
    ScratchPad(
        "stackpad",
        [
            DropDown("term", "alacritty -e vim ~/stack.md", x=0.5,y=0.05, width=0.48, height=0.90),
        ],
    ),
]

alternative_keybinds = {
    "z": "asciicircum",
    "u": "1",
    "i": "2",
    "o": "3",
    "p": "4",
    "n": "q",
    "m": "r",
}


def create_group_shortcut(name, key_name):
    yield Key(
        [mod],
        key_name,
        lazy.group[name].toscreen(),
        desc="Switch to group {}".format(i.name),
    )
    yield Key(
        [mod, "shift"],
        key_name,
        lazy.window.togroup(i.name, switch_group=True),
        desc="Switch to & move focused window to group {}".format(name),
    )
    yield Key(
        [mod, "control"],
        key_name,
        lazy.window.togroup(name),
        desc="move focused window to group {}".format(name),
    )


for i in groups:
    key_name = i.name.lower()

    if key_name == "scratchpad" or key_name == "stackpad":
        continue  # don't give the scratchpad a group shortcut

    keys.extend(create_group_shortcut(i.name, key_name))
    if key_name in alternative_keybinds:
        alt_key = alternative_keybinds[key_name].lower()
        keys.extend(create_group_shortcut(i.name, alt_key))


# Drag floating layouts
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod],
        "Button2",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size(),
    ),
    Click([mod], "Button3", lazy.window.toggle_floating()),
]
