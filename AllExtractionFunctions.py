# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 17:50:18 2023

@author: Riya
"""
import whois
from urllib.parse import urlparse,urlencode
import requests
import pandas as pd
from urllib.parse import urlparse,urlencode
import ipaddress
import re

# Finding the length of URL and categorizing (URL_Length)
def getLength(url):
    if len(url)<54:
        length=0
    else:
        length=1
    return length


def getDepth(url):
    s = urlparse(url).path.split('/')
    depth = 0
    for j in range(len(s)):
       if len(s[j]) != 0:
         depth = depth+1
    return depth

# Checking for redirection '//' in the url (Redirection)
def redirection(url):
  pos = url.rfind('//')
  if (pos == 6):
    return 0  # https
  else:
    return 1 # http



def httpsDomain(url):
  domain = urlparse(url).netloc
  if 'https' in domain:
    return 1
  else:
    return 0


# count number of dots in host name (domain name) of the URL
def count_dots_in_host(url):
    # Parse the URL to extract the host name
    parsed_url = urlparse(url)
    host_name = parsed_url.netloc

    # Count the number of dots in the host name
    dot_count = host_name.count('.')
    if dot_count > 5:
      return 1    #phishing
    else:
      return 0
    #return dot_count



# code to find number of terms in the host name of the URL
def count_terms_in_host(url):
    # Parse the URL to extract the host name
    parsed_url = urlparse(url)
    host_name = parsed_url.hostname

    # Check if the host name is None (i.e., invalid or missing host name)
    if host_name is None:
        return 0

    # Split the host name into its individual parts (subdomains)
    subdomains = host_name.split('.')

    # Count the number of terms (subdomains) in the host name
    term_count = len(subdomains)
    if term_count > 4:
      return 1    #phishing
    else:
      return 0
    #return term_count



# length of the host name
def host_name_length(url):
    # Parse the URL to extract the host name
    parsed_url = urlparse(url)
    host_name = parsed_url.hostname

    # Calculate the length of the host name
    host_name_length = len(host_name)
    if host_name_length > 30:
      return 1    #phishing
    else:
      return 0
    #return host_name_length

# Checks the presence of @ in URL (Have_At)
def haveAtSign(url):
  if "@" in url:
    at = 1
  else:
    at = 0
  return at




def is_registered(url):
    # x = 1
    # try:
    #     domainname = whois.whois(urlparse(url).netloc)

    # except Exception:
    #     x = 0
    # return x
    x = 1
    try:
        domain_name = urlparse(url).netloc
        if not domain_name:
            return 0

        # Use the whois.query() function to retrieve domain information
        domain_info = whois.whois(domain_name)
        # You can check for specific properties in the domain_info object to
        # determine if the domain is registered or not. For example:
        if not domain_info.status or 'pending' in domain_info.status.lower():
            x = 0
    except Exception:
        x = 0
    return x

#Checks the status of the right click attribute (Right_Click)
def rightClick(response):
  if response == "":
    return 1
  else:
    if re.findall(r"event.button ?== ?2", response.text):
      return 0
    else:
      return 1

#re.findall() function from the re module to search for the string pattern event.button ?== ?2 in the response.text.
# The regular expression r"event.button ?== ?2" looks for occurrences of the string "event.button == 2" with optional spaces before and after the "==" operator.
# The number 2 in this context often represents the right-click of the mouse, which is associated with context menus.



def has_valid_tld(url):
    # List of known top-level domains (TLDs)
    valid_tlds = r"com|org|net|edu|gov|mil|int|info|biz|name|us|uk|ca|de|fr|jp|au|in|br|cn"
    match=re.search(valid_tlds,url)
    if match:
        return 1
    else:
        return 0
# url1 = "http://www.example.com/path/to/page"
# print(has_valid_tld(url1))


# Checks for IP address in URL (Have_IP)

# If the domain part of URL has IP address, the value assigned to this feature is 1 (phishing) or else 0 (legitimate)
def havingIP(url):
  try:
    ipaddress.ip_address(url)
    ip = 1
  except:
    ip = 0
  return ip

# Survival time of domain: The difference between termination time and creation time (Domain_Age)

from datetime import datetime
# domain_name object contain domain registration information obtained from a WHOIS query
def domainAge(domain_name):
  creation_date = domain_name.creation_date
  expiration_date = domain_name.expiration_date
  # These dates are assumed to be in either datetime format or string format (e.g., "YYYY-MM-DD").

  # Convert dates to datetime objects if they are in string format
  if (isinstance(creation_date,str) or isinstance(expiration_date,str)):
    try:
      creation_date = datetime.strptime(creation_date,'%Y-%m-%d')
      expiration_date = datetime.strptime(expiration_date,"%Y-%m-%d")
    except:
      return 1

  # Check if either creation_date or expiration_date is missing or none, if so then phishing
  if ((expiration_date is None) or (creation_date is None)):
      return 1


  # Check if creation_date or expiration_date is a list (potentially indicating multiple records with different dates)
  elif ((type(expiration_date) is list) or (type(creation_date) is list)):
      return 1
  else:
    # Calculate the age of the domain in days
    ageofdomain = abs((expiration_date - creation_date).days)
    # Convert age to months and check if it is less than 6 months
    if ((ageofdomain/30) < 6):
      age = 1 #phishing
    else:
      age = 0 # legitimate
  return age
 # The whois library is a Python module that allows you to query WHOIS databases. WHOIS stands for "Who is?".
# The WHOIS database contains detailed information about the entities that have registered or own these resources,
# including domain name registrants, domain registration dates, expiration dates, nameservers, contact details, and more

# If the URL is using Shortening Services, the value assigned to this feature is 1 (phishing) or else 0 (legitimate).





# Checking for Shortening Services in URL (Tiny_URL)
def shortURL(url):
  #listing shortening services
  shortening_services = r"bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|db\.tt|qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|x\.co|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|tr\.im|link\.zip\.net"
  match=re.search(shortening_services,url)
  if match:
      return 1
  else:
      return 0
