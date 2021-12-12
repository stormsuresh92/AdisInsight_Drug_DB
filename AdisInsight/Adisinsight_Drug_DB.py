from requests_html import HTMLSession
import pandas as pd
from tqdm import tqdm


s = HTMLSession()

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'
    }

datas = []
file = open('Input.txt', 'r')
urls = file.readlines()
for url in tqdm(urls):
    try:
        r = s.get(url.strip(), headers=headers)
        contents = r.html.find('div.main-content')
        for item in contents:
            try:
                drug = item.find('h1#drugNameID', first=True).text
            except:
                drug = ''
            try:
                Alt_name = item.find('span.document__alt-name', first=True).text.split(':')[-1].strip()
            except:
                Alt_name = ''
            try:
                Last_Update = item.find('p.document__latest-update', first=True).text.split(':')[-1].strip()
            except:
                Last_Update = ''
            try:
                Originator = item.find('li#at-a-glance_origniator span', first=True).text
            except:
                Originator = ''
            try:
                Developer = item.find('li#at-a-glance_developer span', first=True).text
            except:
                Developer = ''
            try:
                Class = item.find('li#at-a-glance_class span', first=True).text
            except:
                Class = ''
            try:
                MOA = item.find('li#at-a-glance_mechanismOfAction span', first=True).text
            except:
                MOA = ''
            try:
                Orphan_Drug_Status = item.find('#at-a-glance_orphanStatus > li:nth-child(1) > span', first=True).text
            except:
                Orphan_Drug_Status = ''
            try:
                New_Molecular_Entity = item.find('#at-a-glance_newMolecularEntity > span', first=True).text
            except:
                New_Molecular_Entity = ''
            try:
                Available_For_Licensing = item.find('#at-a-glance_availableForLicensing > span', first=True).text
            except:
                Available_For_Licensing = ''
            try:
                Marketed = item.find('#at-a-glance > div > div > ul.data-list__content.data-list__content--highest-dev-phases > li > span', first=True).text
            except:
                Marketed = ''
            try:
                Url = url.strip()
            except:
                Url = ''
            
            dic = {
                'Drug_Name':drug,
                'Alternative_Names':Alt_name,
                'Originator':Originator,
                'Developer':Developer,
                'Class':Class,
                'Mechanism_of_Action':MOA,
                'Orphan_Drug_Status':Orphan_Drug_Status,
                'New_Molecular_Entity':New_Molecular_Entity,
                'Available_For_Licensing':Available_For_Licensing,
                'Marketed':Marketed,
                'Latest_Information_Update':Last_Update,
                'Urls':url
                }
            datas.append(dic)
    except:
        pass


df = pd.DataFrame(datas)
df.to_csv('drug profiles.csv', index=False)
print('Saved')

input()
