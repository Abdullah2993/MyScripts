netsh interface ip set address name="Wi-Fi" static 192.168.24.1 255.255.255.0 192.168.24.254
netsh interface ip set dns name="Wi-Fi" static 202.83.160.41
netsh interface ip add dns name="Wi-Fi" addr=202.83.160.14 index=2
exit