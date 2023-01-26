import dns.resolver
import requests

def subdomain_enum(domain):
    subdomains = []
    try:
        dns_resolver = dns.resolver.Resolver()
        dns_resolver.nameservers = ['8.8.8.8', '8.8.4.4']
        dns_answers = dns_resolver.query(domain, 'NS')
        for rdata in dns_answers:
            subdomain_name = str(rdata)
            subdomains.append(subdomain_name)
    except:
        pass
    return subdomains

def check_http_status(subdomain):
    url = "http://" + subdomain
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f'{subdomain} is active')
    except:
        pass

domain = input("Enter the domain name: ")
subdomains = subdomain_enum(domain)

for subdomain in subdomains:
    check_http_status(subdomain)
