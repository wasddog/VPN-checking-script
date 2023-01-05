import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

key = "**** YOUR API KEY FOR https://vpnapi.io/ ******"
key2 = f'?key={key}'
url = r'https://vpnapi.io/api/'
ips = open("ips.txt", "r").read().split('\n')
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def remove_duplicates(l):
    return list(set(l))


ips = remove_duplicates(ips)
# print(len(ips))
vpns = []
tors = []
proxies = []
fixes = []
countries = []
print(len(ips))
for ip in ips:
    if len(ip) >= 7:
        r = requests.get(url + ip + key2, verify=False)
        # print(r.json())
        # print(r.json()["network"]['autonomous_system_organization'])
        # print(r.json()['security']['proxy'])
        # print(type(r.json()['security']['proxy']))
        try:
            if r.json()['security']['proxy'] == True:
                print(f"{ip} - {r.json()['location']['country']} - is Proxy")
                proxies.append(ip)
            elif r.json()['security']['vpn'] == True:
                print(f"{ip} - {r.json()['location']['country']} - is VPN")
                if ip not in vpns:
                    countries.append(r.json()['location']['country'])
                    vpns.append(ip)
            elif r.json()['security']['tor'] == True:
                print(f"{ip} - {r.json()['location']['country']} - is TOR")
                tors.append(ip)
            else:
                print(f"{ip} - {r.json()['location']['country']} - is FIX")
                countries.append(r.json()['location']['country'])
                fixes.append(ip)
        except:
            pass
    else:
        pass


if len(vpns) > 0:
    print('\ncountry list', countries)
    print('\nVPN addresses - ', ', '.join(vpns))
if len(tors) > 0:
    print('\nTOR addresses', tors)
if len(proxies) > 0:
    print('\nPROXY addresses', proxies)


# for i in range(len(fixes)):
#     print(f'{fixes[i]} - {countries[i]} - is Fixed')
# for i in range(len(vpns)):
#     print(f'{vpns[i]} - {countries[i]} - is VPN')
# for i in range(len(proxies)):
#     print(f'{proxies[i]} - {countries[i]} - is Proxy')


#    print(f'{vpns[i]} - {countries[i]} - is VPN ----- https://ip2location.com/{vpns[i]}')

