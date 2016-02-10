netsh interface ip set address name="Wi-Fi" static 172.16.3.222 255.255.255.0 172.16.3.254
netsh interface ip set dns name="Wi-Fi" static 172.16.0.1
netsh interface ip add dns name="Wi-Fi" addr=172.16.3.254 index=2
exit