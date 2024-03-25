#!/bin/bash

# Prompt user for Elasticsearch username
read -p "Enter Elasticsearch username: " username

# Prompt user for Elasticsearch password (without showing input)
read -sp "Enter Elasticsearch password: " password

# Export username and password as environment variables
export ELASTIC_USER="$username"
export ELASTIC_PASS="$password"

# Print confirmation message
echo -e "\nElasticsearch credentials have been set."