import datetime

end_time = datetime.datetime(2026, 11, 8)
site_block = "www.wscubetech.com"
host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect_ip = "127.0.0.1"

while True:
    if datetime.datetime.now() < end_time:
        with open(host_path, 'r+') as file:
            content = file.read()
            for website in site_block:
                if website in content:
                    file.write(f"{redirect_ip} {site_block}\n")
                else:
                    pass

    else:
        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in site_block):
                    file.write(line)
            file.truncate()
        datetime.datetime.sleep(5)