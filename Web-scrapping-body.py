#!/usr/bin/env python
# coding: utf-8

# <h1 style='font-family:courier; font-size:30px; color:navy'><br><center>Web Scraping Project</h1>

# In[3]:


import requests
from bs4 import BeautifulSoup

url = 'https://brokers.interexo.com/search?country%5B0%5D=United%20States&state%5B0%5D=Georgia&state%5B1%5D=Florida&state%5B2%5D=Texas&state%5B3%5D=Nevada&city%5B0%5D=A%20Boca%20Raton&city%5B1%5D=Addison&city%5B2%5D=Allen&city%5B3%5D=Alpharetta&city%5B4%5D=Alpharetta%20-%20Atlanta&city%5B5%5D=Atlanta&city%5B6%5D=Atlanta%20%28Marietta%29&city%5B7%5D=Atlanta%20-%20Gainesville&city%5B8%5D=Austin&city%5B9%5D=Bellaire&city%5B10%5D=Boca%20Raton&city%5B11%5D=Boca%20Raton%2C%20Fl&city%5B12%5D=Carrollton&city%5B13%5D=Carrolton%20-%20Dallas&city%5B14%5D=Coral%20Gables&city%5B15%5D=Coppell&city%5B16%5D=Colleyville&city%5B17%5D=Coral%20Springs&city%5B18%5D=Coral%20Springs%2C%20Fl&city%5B19%5D=Dallas%20County&city%5B20%5D=Dallas&city%5B21%5D=Dallas%2C&city%5B22%5D=Dallas%2C%20Tx%2075240&city%5B23%5D=Dallas%2FAddison&city%5B24%5D=Dania%20Beach&city%5B25%5D=Decatur&city%5B26%5D=Deerfield%20Beach&city%5B27%5D=Dekalb&city%5B28%5D=Delray%20Beach&city%5B29%5D=Farmers%20Branch&city%5B30%5D=Fort%20Myers&city%5B31%5D=Fort%20Lauderdale&city%5B32%5D=Fort%20Worth&city%5B33%5D=Frisco&city%5B34%5D=Ft%20Lauderdale&city%5B35%5D=Ft.%20Lauderdale&city%5B36%5D=Ft.%20Worth&city%5B37%5D=Garland&city%5B38%5D=Grand%20Prairie&city%5B39%5D=Grapevine&city%5B40%5D=Hallandale&city%5B41%5D=Hallandale%20Beach&city%5B42%5D=Henderson&city%5B43%5D=Hollywood&city%5B44%5D=Housotn&city%5B45%5D=Houston&city%5B46%5D=Houston%2FClear%20Lake%20Area&city%5B47%5D=Irving&city%5B48%5D=Humble&city%5B49%5D=Irving%20%28Las%20Colinas%29&city%5B50%5D=Jensen%20Beach&city%5B51%5D=Johns%20Creek&city%5B52%5D=Jupiter&city%5B53%5D=Katy&city%5B54%5D=Key%20Largo&city%5B55%5D=Kingwood&city%5B56%5D=Las%20Vegas&city%5B57%5D=Lauderdale&city%5B58%5D=League%20City&city%5B59%5D=Lewisville&city%5B60%5D=Marietta&city%5B61%5D=Mckinney&city%5B62%5D=Mesquite&city%5B63%5D=Miami&city%5B64%5D=Miami%20Beach&city%5B65%5D=Miami%20Lakes&city%5B66%5D=Miami-Dade&city%5B67%5D=N.Miami%20Beach&city%5B68%5D=South%20Miami&city%5B69%5D=N.Richland%20Hills&city%5B70%5D=Norcross&city%5B71%5D=North%20Palm%20Beach&city%5B72%5D=North%20Plam%20Beach&city%5B73%5D=North%20Richland%20Hills&city%5B74%5D=Palm%20Beach&city%5B75%5D=Palm%20Beach%20Gardens&city%5B76%5D=Plano&city%5B77%5D=Plantation&city%5B78%5D=Pembroke%20Pines&city%5B79%5D=Pompano%20Beach&city%5B80%5D=Richardson&city%5B81%5D=Roswell&city%5B82%5D=Rowlett&city%5B83%5D=Southlake&city%5B84%5D=Spring&city%5B85%5D=Sugar%20Land&city%5B86%5D=Sunny%20Isles%20Beach&city%5B87%5D=Vero%20Beach&city%5B88%5D=Woodlands&city%5B89%5D=West%20Palm%20Beach&city%5B90%5D=West%20Palm&page=35'

res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
tag = soup.body
tag


# In[4]:


for string in tag.strings:
    print(string)


# In[5]:


brs = soup.find_all('div', class_="grid-cell p-2")
brs


# In[6]:


for br in brs: # for every table rows
    for td in br.find_all('a'): # find td in the rows
        print(td)


# In[7]:


rows = []
for br in brs: # for every table row
    for td in br.find_all('a'):
        rows.append((td.get_text(strip=True))) # strip = True is if space include, skip it
rows


# In[8]:


rows = []
for br in brs: # for every table row
    for td in br.find_all('a'):
        rows.append([td.get_text(strip=True)]) # make list [ ]
rows


# In[9]:


rows = []
for br in brs: # for every table row
    for td in br.find_all('a'):
        rows.append([td.get_text(strip=True) for td in br.find_all('a')]) # make list [ ]
rows


# In[41]:


import pandas as pd
df = pd.DataFrame(rows[0:], columns=rows[0])
df.rename(columns={'Tom Mchugh':'Name'}, inplace=True)
df.head()


# In[42]:


y = df.Name.values
df = pd.DataFrame({'Name' : y[::2], 'Company_Name' : y[1::2]})
df


# In[43]:


# df.to_excel('project.xlsx')

