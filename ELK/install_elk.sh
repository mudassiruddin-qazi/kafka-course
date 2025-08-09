#!/bin/bash
set -e  # Exit if any command fails

# Variables
ES_VERSION="8.15.2"
KIBANA_VERSION="8.15.2"

echo "[+] Downloading Elasticsearch..."
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-${ES_VERSION}-amd64.deb
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-${ES_VERSION}-amd64.deb.sha512

echo "[+] Verifying Elasticsearch checksum..."
shasum -a 512 -c elasticsearch-${ES_VERSION}-amd64.deb.sha512

echo "[+] Installing Elasticsearch..."
sudo dpkg -i elasticsearch-${ES_VERSION}-amd64.deb

echo "[+] Downloading Kibana..."
wget https://artifacts.elastic.co/downloads/kibana/kibana-${KIBANA_VERSION}-amd64.deb
wget https://artifacts.elastic.co/downloads/kibana/kibana-${KIBANA_VERSION}-amd64.deb.sha512

echo "[+] Verifying Kibana checksum..."
shasum -a 512 -c kibana-${KIBANA_VERSION}-amd64.deb.sha512

echo "[+] Installing Kibana..."
sudo dpkg -i kibana-${KIBANA_VERSION}-amd64.deb

echo "[+] Adding Elastic GPG key..."
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo gpg --dearmor -o /usr/share/keyrings/elastic-keyring.gpg

echo "[+] Installing prerequisites..."
sudo apt-get install -y apt-transport-https

echo "[+] Adding Elastic APT repository..."
echo "deb [signed-by=/usr/share/keyrings/elastic-keyring.gpg] https://artifacts.elastic.co/packages/8.x/apt stable main" | \
sudo tee -a /etc/apt/sources.list.d/elastic-8.x.list

echo "[+] Updating and installing Logstash..."
sudo apt-get update && sudo apt-get install -y logstash

echo "[+] All installations completed successfully!"
