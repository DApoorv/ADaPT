#!/bin/bash -ex
#build image
# cd ./UI
ls -all
whoami
which aws
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 161789953208.dkr.ecr.us-east-1.amazonaws.com
docker build -t ui-bitbucket .
docker rm -f adapt-ui
docker tag ui-bitbucket:latest 161789953208.dkr.ecr.us-east-1.amazonaws.com/ui-bitbucket:latest
docker push 161789953208.dkr.ecr.us-east-1.amazonaws.com/ui-bitbucket:latest
pwd
# sudo mkdir /home/ec2-user/testautomationchart
# cd /home/ec2-user/testautomationchart
# sudo cp -r /home/ec2-user/charts/ .
cd ..
cd ..
cd ..
cd ..
cd ..
pwd
cd /home/ec2-user/charts/
/usr/local/bin/helm3 uninstall uichart
/usr/local/bin/helm3 install uichart mychart/


