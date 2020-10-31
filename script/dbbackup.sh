#!/bin/bash
set -e
# Backing up Database
echo -e "\n >>> Backing Up Database .."
TIME=$(date "+%s")
DBNAME="db.$TIME.sqlite3"
mkdir -p ../backup
cp ../db.sqlite3 ../backup/$DBNAME

echo -e "\n >>> Backup Completed.."