from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, DropDown, ScratchPad
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook, qtile

# dgroups_key_binder = None
# dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = True
# cursor_warp = False

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        # Match(wm_class="confirmreset"),  # gitk
        # Match(wm_class="makebranch"),  # gitk
        # Match(wm_class="maketag"),  # gitk
        # Match(wm_class="ssh-askpass"),  # ssh-askpass
        # Match(title="branchdialog"),  # gitk
        # Match(title="pinentry"),  # GPG key password entry
        # Match(wm_class="Tilda"),
        # Match(title="Guake!"),  # drop-down terminal
        Match(title="xfce4-terminal"),  # drop-down terminal
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
# reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
# auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"