# Rest-HAPI

Build up rest api fast!

[TOC]

# Quick Start

## Install the latest [MongoDB](https://www.mongodb.com/download-center?&_ga=2.173400227.1846048751.1530057377-1187271852.1530057377#enterprise) following [this link](https://docs.mongodb.com/manual/installation/) 

```bash
# Examples on OSX
tar -zxvf mongodb-osx-ssl-x86_64-enterprise-3.6.5.tgz
Go to the target directory
mkdir -p mongodb
cp -R -n mongodb-osx-ssl-x86_64-enterprise-3.6.5/ mongodb

# Add mongodb path to environment
vim ~/.bash_profile
source ~/.bash_profile

# Create db path
mkdir -p ./db

# Start mongo db service
mongod --dbpath ./db

# Verify mongo db
mongo --host 127.0.0.1:27017
```

## Install rest-hapi

```bash
git clone https://github.com/JKHeadley/rest-hapi-demo.git
cd rest-hapi-demo
npm install
./node_modules/.bin/rest-hapi-cli seed
npm start
```

