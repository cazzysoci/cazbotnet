import os
import sys
import httpx
from colorama import Fore, init
init(autoreset=True)

fr = Fore.RED
fg = Fore.GREEN
fy = Fore.YELLOW
fw = Fore.WHITE
fre = Fore.RESET

list = [
'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt',
'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
'https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt',
'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt',
'https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt',
'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt',
'https://raw.githubusercontent.com/proxylist-to/proxy-list/main/http.txt',
'https://raw.githubusercontent.com/yuceltoluyag/GoodProxy/main/raw.txt',
'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt',
'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt',
'https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt',
'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/http_proxies.txt',
'https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt',
'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/https_proxies.txt',
'https://api.openproxylist.xyz/http.txt',
'https://api.proxyscrape.com/v2/?request=displayproxies',
'https://api.proxyscrape.com/?request=displayproxies&proxytype=http',
'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all',
'https://www.proxydocker.com/en/proxylist/download?email=noshare&country=all&city=all&port=all&type=all&anonymity=all&state=all&need=all',
'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=anonymous',
'http://worm.rip/http.txt',
'https://proxyspace.pro/http.txt',
'https://multiproxy.org/txt_all/proxy.txt',
'https://proxy-spider.com/api/proxies.example.txt',
"https://raw.githubusercontent.com/mmpx12/proxy-list/refs/heads/master/http.txt",
"https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/refs/heads/master/http.txt",
"https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/refs/heads/master/https.txt",
"https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/refs/heads/master/socks4.txt",
"https://raw.githubusercontent.com/Simatwa/free-proxies/master/files/http.json",
"https://raw.githubusercontent.com/Simatwa/free-proxies/master/files/socks5.json",
"https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt",
"https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/refs/heads/main/http_checked.txt",
"https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/refs/heads/main/http.txt",
"https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/refs/heads/main/socks5_checked.txt",
"https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks4.txt",
"https://raw.githubusercontent.com/tuanminpay/live-proxy/master/socks4.txt",
'https://raw.githubusercontent.com/jepluk/PROXYLIST/main/all.json',
'https://raw.githubusercontent.com/ProxyScraper/ProxyScraper/refs/heads/main/http.txt',
'https://raw.githubusercontent.com/Isloka/proxyscraper/refs/heads/main/proxies/http.txt',
'https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt',
'https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/https.txt',
'https://raw.githubusercontent.com/vakhov/fresh-proxy-list/refs/heads/master/http.txt',
'https://raw.githubusercontent.com/vakhov/fresh-proxy-list/refs/heads/master/https.txt',
'https://raw.githubusercontent.com/MrMarble/proxy-list/refs/heads/main/all.txt',
'https://raw.githubusercontent.com/berkay-digital/Proxy-Scraper/refs/heads/main/proxies.txt',
"https://spys.one/free-proxy-list/",
"https://www.proxy-list.download/api/v1/get?type=http&anon=elite&country=US",
"https://www.proxy-list.download/api/v1/get?type=http&anon=transparent&country=US",
"https://spys.me/socks.txt",
'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http',
'https://www.freeproxychecker.com/result/http_proxies.txt',
'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all',
'https://www.freeproxychecker.com/result/https_proxies.txt',
'https://www.proxy-list.download/api/v1/get?type=http',
'https://www.proxyscan.io/download?type=https',
'https://spys.me/proxy.txt',
'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt',
'https://api.openproxylist.xyz/http.txt',
'https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt',
'http://alexa.lr2b.com/proxylist.txt',
'http://rootjazz.com/proxies/proxies.txt',
'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt',
'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt',
'https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt',
'https://proxy-spider.com/api/proxies.example.txt',
'https://multiproxy.org/txt_all/proxy.txt',
'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt'
'https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/free.txt',
'https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/cnfree.txt',
'https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt',
'https://free-proxy.pro/proxy.txt',
'https://raw.githubusercontent.com/MrMarble/proxy-list/main/all.txt',
'https://sunny9577.github.io/proxy-scraper/proxies.txt',
'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/http_proxies.txt',
'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt',
"https://openproxylist.xyz/http.txt",
"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
"https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt",
"https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/https.txt",
"https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt",
"https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/http_proxies.txt",
"https://raw.githubusercontent.com/andigwandi/free-proxy/main/proxy_list.txt",
"https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
"https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
"https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
"https://raw.githubusercontent.com/zloi-user/hideip.me/main/connect.txt",
"https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt",
"https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/http/data.txt",
"https://raw.githubusercontent.com/zloi-user/hideip.me/main/https.txt",
"https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
"https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt",
"https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
"https://raw.githubusercontent.com/TuanMinPay/live-proxy/refs/heads/master/all.txt",
"https://raw.githubusercontent.com/roosterkid/openproxylist/refs/heads/main/HTTPS_RAW.txt",
]  
         

if __name__ == "__main__":
    file = "proxy.txt"
    
    try:
        if os.path.isfile(file):
            os.system('cls' if os.name == 'nt' else 'clear')
            os.remove(file)
            print("{}File {} Sudah Ada!\n{}Memulai Mengunduh {} Yang Baru!\n".format(fr, file, fy, file))
            with open(file, 'a') as data:
                for proxy in list:
                    data.write(httpx.get(proxy).text)
                    print(" -| mengambil {}{}".format(fg, proxy))
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            with open(file, 'a') as data:
                for proxy in list:
                    data.write(httpx.get(proxy).text)
                    print(" -| mengambil {}{}".format(fg, proxy))
    
        with open(file, 'r') as count:
            total = sum(1 for line in count)
        print("\n{}( {}{} {}) {}Proxy successfully created.". format(fw, fy, total, fw, fg))
    
    except IndexError:
        sys.exit(1)
        
