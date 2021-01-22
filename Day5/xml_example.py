from bs4 import BeautifulSoup
import pandas as pd

with open("ipa110106.XML", "r", encoding="utf8") as patent_xml :
    xml = patent_xml.read()

soup = BeautifulSoup(xml, "lxml")

publications = soup.find_all("publication-reference")
applications = soup.find_all("application-reference")
patent_names = soup.find_all("invention-title")

rows = [[]]
for i in range(5) :
    row = []
    for publication in publications :
        public_doc_number = publication.find("doc-number")
        public_kind = publication.find("kind")
        public_date = publication.find("date")
        row.append(public_doc_number)
        row.append(public_kind)
        row.append(public_date)


    for application in applications :
        apply_doc_number = application.find("doc-number")
        apply_date = application.find("data")
        row.append(apply_doc_number)
        row.append(apply_date)

    row.append(patent_names[i])
    rows.append(row)

for row in rows :
    print(row)


