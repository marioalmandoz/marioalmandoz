#!/bin/bash
 
# script para realizar una copia de seguridad del dia anterior
SOURCE=/home/mario/Escritorio/seguridad
# directorio realizar la copia
DESTBASE=/var/tmp/Backups
 
#directorio de la copia de hoy
DEST="$DESTBASE/$(date +%d-%m-%Y)"
# donde encontrar la copia del dia anterior
YESTERDAY="$DESTBASE/$(date -d yesterday +%Y-%m-%d)/"
 
# realizar una copia del dia anterior en el cado de que exista
if [ -d "$YESTERDAY" ]
then
	OPTS="--link-dest $YESTERDAY"
fi
 
# Run the rsync
rsync -av $OPTS "$SOURCE" "$DEST"
