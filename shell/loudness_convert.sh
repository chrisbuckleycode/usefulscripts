#!/bin/bash
##
## FILE: loudness_convert.sh
##
## DESCRIPTION: Converts loudness of mkv, mp3 files to -14 dB LUFS.
##
## AUTHOR: Chris Buckley (github.com/chrisbuckleycode)
##
## USAGE: loudness_convert.sh
##

suffix="-14LUFS"

for source_file in *.mkv; do
  if [[ -f "$source_file" ]]; then
    destination_file="${source_file%.*}$suffix.${source_file##*.}"
    ffmpeg -i "$source_file" -vcodec copy -filter:a loudnorm=i=-14 "$destination_file"
  fi
done

for source_file in *.mp3; do
  if [[ -f "$source_file" ]]; then
    destination_file="${source_file%.*}$suffix.${source_file##*.}"
    ffmpeg -i "$source_file" -filter:a loudnorm=i=-14 "$destination_file"
  fi
done
