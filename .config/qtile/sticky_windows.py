raise NotImplementedError()

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

# groups.append(ScratchPad("scratchpad", DropDown("term", "alacritty", opacity=0.8)))
# keys.append(Key([mod], 'F12', lazy.group['scratchpad'].dropdown_toggle('scratchpad')))


Key([mod], "o", lazy.function(stick_win), desc="stick win"),
    Key([mod, "shift"], "o", lazy.function(unstick_win), desc="unstick win"),