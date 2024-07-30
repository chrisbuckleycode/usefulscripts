#!/bin/bash
##
## FILE: move_files.sh
##
## DESCRIPTION: Organizes local files: moves by extension.
##
## AUTHOR: Chris Buckley (github.com/chrisbuckleycode)
##
## USAGE: move_files.sh
##

# TODO(chrisbuckleycode): Add checks for pre-existing target directories

mv -v {*.mp3,*.ogg,*.wav} ../Music
mv -v {*.mp4,*.flv,*.mkv,*.srt} ../Videos
mv -v {*.epub,*.pdf} ../Documents/BOOKS
mv -v {*.jpg,*.jpeg,*.png,*.gif,*.webm,*.tif} ../Pictures
mv -v {*.csv,*.exe,*.html,*.htm,*.AppImage,*.svg,*.doc,*.tar.gz,*.txt,*.pem,*.docx,*.odg,*.ods,*.odt,*.iso} ../Documents
