# Subdomain-Enumeration

Here's an example of a simple Python script for subdomain enumeration using the "requests" and "dnspython" libraries:

This script uses the "dns.resolver" library to query the domain's nameservers and gather a list of subdomains. Then it uses the "requests" library to check the HTTP status code of each subdomain by sending a GET request. If the status code is
