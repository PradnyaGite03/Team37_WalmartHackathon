# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 18:07:17 2023

@author: Riya
"""

# import FeatureExtraction
import whois
from urllib.parse import urlparse,urlencode
import requests
import pandas as pd
from urllib.parse import urlparse,urlencode
import ipaddress
import re
import AllExtractionFunctions


# The whois library is a Python module that allows you to query WHOIS databases. WHOIS stands for "Who is?".
# The WHOIS database contains detailed information about the entities that have registered or own these resources,
# including domain name registrants, domain registration dates, expiration dates, nameservers, contact details, and more


def Feature_Extraction(url):
    features = []
    features.append(AllExtractionFunctions.getLength(url))
    features.append(AllExtractionFunctions.getDepth(url))
    features.append(AllExtractionFunctions.redirection(url))
    features.append(AllExtractionFunctions.httpsDomain(url))
    features.append(AllExtractionFunctions.count_dots_in_host(url))
    features.append(AllExtractionFunctions.count_terms_in_host(url))
    features.append(AllExtractionFunctions.host_name_length(url))
    features.append(AllExtractionFunctions.haveAtSign(url))
    features.append(AllExtractionFunctions.has_valid_tld(url))
    features.append(AllExtractionFunctions.havingIP(url))
    features.append(AllExtractionFunctions.shortURL(url))
    return features
    #features.append(is_registered(url))
    # try:
    #     response = requests.get(url)
    # except:
    #     response = ""
  #  features.append(FeatureExtraction.rightClick(url))
   
  #   x = 1
  #   try:
  #       domainname = whois.whois(urlparse(url).netloc)

  #   except Exception:
  #       x = 0
  #   features.append(1 if x==0 else domainAge(domainname))
   
    #features.append(target)
  