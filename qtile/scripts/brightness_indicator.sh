MODE=$1
if [ "$MODE" = "up" ]; then
	brightnessctl set 10%+
elif [ "$MODE" = "down" ]; then
	brightnessctl set 10%-
fi
