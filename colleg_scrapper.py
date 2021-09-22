import requests,json
from bs4 import BeautifulSoup
url=requests.get("https://www.collegedekho.com/btech-colleges-in-india/")
soup=BeautifulSoup(url.text,"html.parser")
link=soup.find("div",class_="middle-container").find_all('div',class_="box")
for i in (link):
        clg_link=("https://www.collegedekho.com/"+i.find('a').get('href'))
        name=i.find("div",class_="title").find("a").text
        ff=name.replace("(","").replace(")","").strip("\n")
            #type of clg
        m=i.find("ul",class_="info").text
        urll=requests.get(clg_link)
        soup=BeautifulSoup(urll.text,"html.parser")
        # ranking_college=soup.findP("span",class_="text").get("href")
        # print(ranking_college.text) 
        detial=soup.find("div",class_="collegeAddress").text.split('\n')
        phone_no=detial[3].strip()
        email_id=detial[7].strip()
        adress_clg=detial[11].strip()
        # print()
        fac_clg=[]
        fac=soup.find(class_="block facilitiesBlock").find(class_="box").find_all(class_="title")
        for i in fac:
            cc=i.text
            fac_clg.append(cc)
        #
lll=["College_Name","Phone_no","Email_ID","Clg_ADD","Clg_Fac","Clg_type"]
ooo=[ff,phone_no,email_id,adress_clg,fac_clg,m]
Detial_of_Clg=dict(zip(lll,ooo))
print(Detial_of_Clg)
print()
print()

            