# ASTERISKS & OBELIX

**Email prediction asterisks** is a script that allows you to identify the emails hidden behind asterisks. It is a perfect application for osint analysts and security forces. It allows to intelligently predict, using Intelx leaks, which emails are related to the person we are looking for. It also allows you to automatically obtain information from emails for manual analysis through a CSV dataset that is generated with the results.

## Example of email with asterisks on Twitter
![](images/email-asterisks.png)

## DEMO
![](images/demo.gif)

## Installation

It's necessary to install the intelx library for python

```bash
git clone https://github.com/Quantika14/email-prediction-asterisks
pip3 install -r requiriments.txt

git clone https://github.com/IntelligenceX/SDK
pip3 install SDK/Python
```
You must put your api key here
```python
# Directory: m/key.py
intelx = "HERE"
emailrep = "HERE"
```
## Autor
- Twitter: @JorgeWebsec
- web: www.quantika14.com
