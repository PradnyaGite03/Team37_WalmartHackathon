Read me
This project is aimed to detect phishing website. Data breaching is a significant concern in various types of fraud, as it involves unauthorized access or acquisition of sensitive information from individuals or organizations. The compromised data can be used for fraudulent activities, leading to severe consequences for the victims. Data breaches can occur due to a variety of reasons, including cyber-attacks, phishing websites, insider threats, accidental exposure, and vulnerabilities in systems or applications. We will be considering Phishing Websites Detection to identify potential data breaches by detecting fraudulent websites.
 
Collection of data:
We are collecting a dataset of all phishing websites from a open-source service called PhishTank. PhishTank is a service that collects and shares data about known phishing URLs (that gets updated hourly) to help protect users from online phishing attacks. Download the dataset from website http://data.phishtank.com/data/online-valid.csv 
This is a link to a CSV file named ‘online-valid.csv’. We are using random 5000 phishing urls.
We are collecting legitimate urls from a open datasets of the University of New Brunswick, https://www.unb.ca/cic/datasets/url-2016.html. We are using random 5000 legitimate urls.
All above mentioned datasets are uploaded to the datasets folder of this repository.
Feature extraction:
It is one of the most important steps in our project because URLs often contain valuable information that can provide insights into the nature of a website and its potential malicious intent. By analysing specific features in URLs, machine learning models can identify patterns associated with phishing websites and distinguish them from legitimate ones.
The features we have extracted from the urls:
1.	Length of the url
2.	Depth of the url
3.	Position of redirection in the url
4.	https present in url or not
5.	number of dots in the url –
The number of dot in hostname is analyzed for phishing and legitimate URLs. The presence of dots in both phishing and legitimate URLs are analyzed using description of phishing and legitimate datasets. The result shows that the suspicious URL has more than five dots and the number of dots in legitimate URL is almost four.
6.	Number of terms in domain name of url –
The number of terms in hostname are also analyzed using description of phishing and legitimate datasets. The result shows that the suspicious URL has more than four dots and the number of dots in legitimate URL is almost three.
7.	Domain name length –
After analysing it is found that url with domain name length greater than 30 is phishing website.
8.	Does url have @ sign
9.	Does url have valid Top Level Domain
10.	Does url have IP instead of domain name
11.	Are shortening services used in the url
The features are referenced from -  https://hcis-journal.springeropen.com/articles/10.1186/s13673-016-0064-3 
Models & Training
The data is split into 70-30 i.e., 7000 training samples & 3000 testing samples. This is supervised machine learning task with binary classification.
The input URL is classified as phishing (1) or legitimate (0). We are considering 3 supervised machine learning models to train the dataset in this project:
•	Decision Tree
•	Random Forest
•	Multilayer Perceptron
Results 
From the obtained results of the above models, multilayer perceptron has maximum accuracy of 84.9 % hence final model chosen is MLP.


