#!/bin/bash
declare -a arr=("track_events" "weather")

for i in "${arr[@]}"
do
   python3.7 main.py "$i"
done
