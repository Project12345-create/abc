Sudo apt update
Sudo apt –fix-missing update
Sudo apt –fix-broken install
Sudo apt install apache2 -y
Sudo systemctl enable apache2
Sudo systemctl start apache2
Sudo systemctl status apache2
Sudo apt install net-tools -y
Ifconfig
Sudo apt install haproxy -y
Sudo systemctl enable haproxy
Nano /etc/haproxy/haproxy.cfg
Frontend http_front
	Bind *:80
	Default_backend http_back
Backend http_back
	Balance roundrobin
	Server vm1 ip:80 check
Close file
Sudo systemctl restart haproxy
Sudo systemctl enable haproxy
Nano script.sh
Echo “hello priyan”
Close file
Chmod +x script.sh
Crontab -e
*/1 * * * * ./script.sh >> ./output.log 2>&1
Cat output.log
Rsync -av /home/ubuntu/check/ ubuntu@ip:/home/ubuntu/check/
Sudo apt install openssh-server -y
Sudo systemctl enable ssh
Sudo systemctl start ssh

