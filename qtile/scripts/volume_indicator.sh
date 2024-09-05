MODE=$1
if [ "$MODE" = "up" ]; then
    amixer set Master 5%+
elif [ "$MODE" = "down" ]; then
    amixer set Master 5%-
elif [ "$MODE" = "mute" ]; then
    amixer set Master toggle
fi
CURRENT_VOLUME=$(amixer get Master | tail -n1 | sed -r 's/.*\[(.*)%\].*/\1/')
if ["$MODE" = "mute"]; then
    notify-send "Muted"
else
    notify-send "Volume: $CURRENT_VOLUME%" -t 500
fi
