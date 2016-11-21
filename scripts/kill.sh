#!/usr/bin/env bash
echo "Killing all processes"
echo
sudo ps auxww | grep 'celery -A backend.settings worker' | awk '{print $2}' | xargs kill -9
echo
sudo pkill redis-server
echo
sudo pkill flower
echo "Done"