import requests
from bs4 import BeautifulSoup


def flipkart_api(productName:str, main_class:str, title_class:str, price_class:str):
     Url = "https://www.flipkart.com/search?q=" + productName #Search URL on flipkart
     response = requests.get(Url)
     soup = BeautifulSoup(response.content, 'html.parser') 

     catagory = soup.find_all('a', {'class':'_1KHd47'})[-1].text

     Product = dict() # All the products with name, price, rating and specifications will stored as key value pair...
     # {Title : {'Price':'12,xxx', 'Rating':'4.4', 'Specifications':[list of specs]}}  _1UoZlX
     
     # Fetching products from soup with class name
     for box in soup.find_all('div',{'class':main_class}): #_3O0U0u for redmi 5a
          # Extract product name as title, price and rating from the product removing html tag with .text method
          title = box.find('div', class_=title_class).text # _3wU53n for redmi 5a
          price = box.find('div', class_=price_class).text  # _1vC4OE _2rQ-NK for redmi 5a
          # rating = box.find('div', {'class':'hGSR34'}).text
          if catagory.lower() == "mobiles":
               spec = [] # list of specs for each product
               for elem in box.find_all('li', {'class':'tVe95H'}):
                    spec.append(elem.text)
               Product[title] = {'Price':price ,'Specification':spec}
          else:
               Product[title] = {'Price':price}

     print(catagory)
     for key, value in Product.items():
          print(key+": ")
          # print(f"Price: {value['Price']} Rating: {value['Rating']}")
          print(f"Price: {value['Price']}")
          if catagory.lower() == "mobiles":
               for i,v in enumerate(value['Specification']):
                    print(f"{i+1}) {v}")
          print("")

flipkart_api("redmi 5a","_3O0U0u", "_3wU53n","_1vC4OE _2rQ-NK" )
# url = "https://www.flipkart.com/search?q=shoes"
# response = requests.get(url)

# soup = BeautifulSoup(response.content, 'html.parser')
# pos = 1

# # for box in soup.find('div', {'class':'_3O0U0u'}): IIdQZO _1SSAGr
# #      print(box.get('style').split(":")[1])
# for box in soup.find_all('div', {'class':'IIdQZO _1SSAGr'}):
#      title = box.find('div', {'class':'_2B_pmu'}).text
#      price = box.find('div', {'class':'_1vC4OE'}).text
#      print(f"{pos}) {title} {price}")
#      # price = box.find('div', {'class':'_2B_pmu'})
#      pos +=1
     



