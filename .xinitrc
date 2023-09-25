# start commands in xprofile
[ -f /etc/xprofile ] && . /etc/xprofile
[ -f ~/.xprofile ] && . ~/.xprofile

xrdb -merge ~/.Xresources

exec qtile start
#exec gnome-session
