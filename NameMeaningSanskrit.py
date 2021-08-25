import requests
import bs4

base_url='https://www.google.com/search?q={}+meaning+in+sanskrit&rlz=1C1VDKB_enIN957IN957&sxsrf=ALeKk009Mn5ajYMdyTeEp8deQ29DbDHBgw%3A1627452730107&ei=OvUAYY2FBuKq1sQPg46i8A8&oq=yashwanth+meaning+in+sanskrit&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECc6BwgjELADECc6BwgAEEcQsAM6BggAEAcQHjoICAAQBxAKEB46BAgAEB46BAgAEENKBAhBGABQkaABWOOzAWCOvQFoAXACeAKAAbIDiAHKJJIBBzItNy43LjGYAQCgAQGqAQdnd3Mtd2l6yAEJwAEB&sclient=gws-wiz&ved=0ahUKEwiNivfujYXyAhVilZUCHQOHCP4Q4dUDCA8&uact=5'
name=input('enter your single name: ')
res=requests.get(base_url.format(name))
soup=bs4.BeautifulSoup(res.text,"lxml")
sans_name=soup.select("div > span")

print(sans_name[2].getText())
print(sans_name[3].getText())



