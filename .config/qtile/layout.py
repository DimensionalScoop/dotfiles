from libqtile import bar, layout, widget

layouts = [
    layout.Columns(
        border_focus="#75f0ac",  # "c68538ff",
        border_focus_stack="#c6fe20",
        border_normal="#370926",
        border_normal_stack="#42113C",
        border_width=2,
        margin=5,
        split=False,
        num_columns=2,
    ),
    layout.Max(),
    # layout.Tile(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(margin=25),
    #layout.MonadWide(
    #    margin=5,
    #    border_width=2,
    #    ratio=0.5,
    #),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]
