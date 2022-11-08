#! /bin/bash
#precondicion:
# Instrucción cron (crontab -e): 
# 00 12 * * * bash /home/mario/Escritorio/seguridad/backups.bash

dir_copia="/var/tmp/Backups/"
origen="/home/mario/Escritorio/seguridad"

function getDiaAnt(){
    echo $(date --date="1 day ago" +%d-%m-%Y)
}

function getDia(){
    echo $(date +%d-%m-%Y)
}

function make_backup(){
    ayer="$dir_copia$(getDiaAnt)"
    hoy="$dir_copia$(getDia)"

    # Si no existe el directorio del backup anterior lo creamos
    [ ! -d "$ayer" ] && mkdir $ayer 
    mkdir $hoy

    rsync -av --link-dest=$ayer $origen $hoy
}

echo "Creating backup of "$origen
make_backup
