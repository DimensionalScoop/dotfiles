from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, DropDown, ScratchPad
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook, qtile


widget_defaults = dict(
    # font="Iosevka Term Medium Extended", fontsize=15, padding=5, color="c8c6c5ff"
    font="Jost*",
    fontsize=15,
    padding=5,
    color="c8c6c5ff",
)
extension_defaults = widget_defaults.copy()


class NetMax(widget.Net):
    def _format(self, down, down_letter, up, up_letter, total, total_letter):
        lenght = 2  # int(6)
        max_len_down = 2 - len(down_letter)
        max_len_up = 1 - len(up_letter)
        max_len_total = lenght - len(total_letter)

        down_prec = 0 if down_letter == "kB" or down_letter == "B" else 1
        up_prec = 0 if up_letter == "kB" or up_letter == "B" else 1

        down_prec = 0
        up_prec = 0
        max_len = 2

        down = ("{val:{max_len}." + str(down_prec) + "f}").format(
            val=down, max_len=max_len_down
        )
        up = ("{val:{max_len}." + str(up_prec) + "f}").format(
            val=up, max_len=max_len_up
        )
        total = "{val:{max_len}.1f}".format(val=total, max_len=max_len_total)

        return down[:max_len_down], up[:max_len_up], total[:max_len_total]

    def convert_b(self, num_bytes: float):
        return num_bytes / 1e6, ""  # converted_bytes, unit


screens = [
    Screen(
        # only for 4k with very thin margins
        # top = bar.Bar([widget.Sep()],3),
        # left=bar.Bar([widget.Sep()], 3),
        # right=bar.Bar([widget.Sep()], 3),
        bottom=bar.Bar(
            [
                # widget.WindowName(max_chars=100),
                widget.Notify(parse_text=lambda t: t.replace("\n", " "), max_chars=100),
                widget.Spacer(length=bar.STRETCH),
                widget.Battery(format="β {percent:2.0%} {watt:.1f} W"),                widget.CPU(format="𝛹 {load_percent:>2.0f}%"),
                widget.ThermalSensor(tag_sensor="Package id 0"),
                NetMax(format="{down}/{up}", update_interval=1, prefix="M"),
                # widget.ThermalSensor(tag_sensor="edge"),
                # widget.ThermalSensor(tag_sensor="Tctl"),
                # widget.Memory(format="🐏 {MemUsed:.1f} GB", measure_mem="G"),
                # widget.DF(
                #    format="💾 {uf} GB",
                #    update_interval=10,
                #    partition="/",
                #    visible_on_warn=False,
                # ),
                widget.PulseVolume(
                    fmt="🎧 {}",
                    volume_app="pavucontrol",
                    update_interval=0.1,
                    get_volume_command="wpctl get-volume @DEFAULT_AUDIO_SINK@",
                ),
                widget.Systray(icon_size=16, padding=2),
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
            24,
            background="241d19ff",
        ),
    ),
]
