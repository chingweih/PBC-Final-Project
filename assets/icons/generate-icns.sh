# Source: https://gist.github.com/ahmed-musallam/0ba94853fcba39b01e4f5083daca7567

# Required deps:
# imagemagick: https://imagemagick.org/script/download.php

# name of your master icon, must be at least 512X512
PNG_MASTER="icon.png"

ICONSET_FOLDER="AppIcon.iconset"
sizes=(
  16x16
  32x32
  128x128
  256x256
)

# Generate renditions at the sizes in "sizes" above, put all in ICONSET_FOLDER
mkdir -p $ICONSET_FOLDER
for size in "${sizes[@]}"; do
  icon="icon_${size}.png"
  ICON_FILES="$ICON_FILES $ICONSET_FOLDER/$icon"
  echo Generating $ICONSET_FOLDER/$icon
  convert $PNG_MASTER -quality 100 -resize $size $ICONSET_FOLDER/$icon
  
  icon="icon_${size}@2x.png"
  ICON_FILES="$ICON_FILES $ICONSET_FOLDER/$icon"
  echo Generating $ICONSET_FOLDER/$icon
  convert $PNG_MASTER -quality 100 -resize $size $ICONSET_FOLDER/$icon
done

# generate icon.icns for mac app (this only works on mac)
echo Generating icon.icns
iconutil -c icns $ICONSET_FOLDER -o icon.icns

# Generate .ico file for windows
ICON_FILES=""
for size in "${sizes[@]}"; do
  ICON_FILES="$ICON_FILES $ICONSET_FOLDER/icon_${size}.png"
  ICON_FILES="$ICON_FILES $ICONSET_FOLDER/icon_${size}@2x.png"
done
echo Generating icon.ico
convert $ICON_FILES icon.ico 

# remove generated renditions
echo removing $ICONSET_FOLDER folder
rm -rf $ICONSET_FOLDER