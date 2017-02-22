#!/bin/bash
java -server -XX:+UseConcMarkSweepGC -Xms1G -Xmx4G -jar server.jar nogui
