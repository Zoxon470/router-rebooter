# Router-Rebooter

I use a neighbor's wifi router sometimes it crashes, but solve problems with unstable Internet I need to restart the router. 
The problem is that physically I do not have access to the router because my neighbor lives in another apartment, therefore I cannot restart the physical router. But I can also reboot the router inside the wifi point network, which I do. But it happens that the router, either because of the heavy load of the network, or because of the power supply, stops giving signs of life for 2-3 hours, which is critical for me, and I cannot restart the router inside the network, because the router is not working. 
In this case, I solved this problem by turning off all electricity from the neighbor, so the Wi-Fi router turned off, turned on itself, and could continue to work. But I got tired of manually turning off the lights every time, and sometimes I forgot to restart the router manually. Therefore, I decided to write a script that entered the router's control panel for me and rebooted itself several times a day. And I will run the script inside the docker container on my home server that runs inside the wifi network of the neighbor.

I have not tested the script for other versions and models of routers, but everything works for my neighbor's wifi router:

### Router information
  - Router model: `TL-WR841N / TL-WR841ND`
  - Firmware version: `3.15.9 Build 140625 Rel.64271n`
  - Hardware version: `WR841N v9 00000000`

### Technologies used
  - `Python 3.8`
  - `Selenium==3.141.0`
  - `Chromedriver`
  - `Docker`

### How to run

For the script to work, you just need to run the docker container. The automatic reboot of the router occurs every 2 hours via crontab. To change the start time of the script see the `crontab` file.

```sh
$ git clone https://github.com/Zoxon470/router-rebooter && cd router-rebooter
$ docker build -t rebooter .
$ docker run -d --name rebooter rebooter
$ docker logs -f rebooter # See logs for rebooting router
```

### Environments

Name | Value | Description
------------ | ------------- | -------------
`ROUTER_URL` | http://192.168.0.1/ | URL for router admin panel 
`ROUTER_LOGIN` | admin | Login for admin account
`ROUTER_ADMIN` | admin | Password for admin account

Example running docker container via environments

```sh
docker run -d -e ROUTER_URL=http://192.168.0.1/ -e ROUTER_LOGIN=admin -e ROUTER_PASSWORD=admin --name rebooter rebooter
```
