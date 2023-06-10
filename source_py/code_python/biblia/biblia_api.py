#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import requests
import sys

head = { 
   'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IkZyaSBBcHIgMTQgMjAyMyAxNzoxNDoyNSBHTVQrMDAwMC5yYW1vbmJhcmJvc2FmcmVpdGFzQGdtYWlsLmNvbSIsImlhdCI6MTY4MTQ5MjQ2NX0.7FOF2EzeWV91gn1lRS7xVHCb9VfSzMuibeJRYWNDJ3w'
}
user = requests.get('https://www.abibliadigital.com.br/api/users/ramonbarbosafreitas@gmail.com',
                    headers=head)

req = requests.get('https://www.abibliadigital.com.br/api/requests/day',
                   headers=head).json()
books = requests.get('https://www.abibliadigital.com.br/api/books',
                     headers=head).json()
list_of_books = [book['abbrev']['pt'] for book in books]

verse = requests.get('https://www.abibliadigital.com.br/api/verses/nvi/%s/1/1' % list_of_books[30]).json()['text']
print(verse)


