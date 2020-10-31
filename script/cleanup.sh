#!/bin/bash
set -e
SERVER_NAME="djdighost"
PROJECT_NAME="projectname"
echo -e "\n>>> Prepare Project Files In Server ..."

ssh raselrostock@$SERVER_NAME /bin/bash << EOF
    find $PROJECT_NAME/ -name *.pyc -delete
    find $PROJECT_NAME/ -name __pycache__ -delete
    find $PROJECT_NAME/ -name migrations -delete
    find $PROJECT_NAME/ -type f -print0 | xargs -0 dos2unix
EOF

echo -e "\n>>> Finished ..."