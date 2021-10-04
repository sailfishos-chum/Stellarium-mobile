#!/bin/bash

# Create translation files
# .po files in po/
# Convert them to qm
LANGS=`ls po/stellarium/*.po | cut -d "." -f 1 | cut -d "/" -f 3`
mkdir -p mobileData/translations/stellarium
mkdir -p mobileData/translations/stellarium-skycultures
for lang in $LANGS; do
    lconvert -i po/stellarium/$lang.po \
             -o mobileData/translations/stellarium/$lang.qm
    echo "converted po/stellarium/$lang.po to mobileData/translations/stellarium/$lang.qm"
done

LANGS=`ls po/stellarium-skycultures/*.po | cut -d "." -f 1 | cut -d "/" -f 3`
for lang in $LANGS; do
  lconvert -i po/stellarium-skycultures/$lang.po \
               -o mobileData/translations/stellarium-skycultures/$lang.qm
  echo "po/stellarium-skycultures/$lang.po to mobileData/translations/stellarium-skycultures/$lang.qm"
done