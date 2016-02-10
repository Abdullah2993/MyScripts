netsh interface ip set address name="Ethernet" static 172.16.3.223 255.255.255.0 172.16.3.254
netsh interface ip set dns name="Ethernet" static 172.16.0.1
netsh interface ip add dns name="Ethernet" addr=172.16.3.254 index=2
exit