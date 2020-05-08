import requests
from bs4 import BeautifulSoup


def flipkart_api(productName):
     Url = "https://www.flipkart.com/search?q=" + productName #Search URL on flipkart
     response = requests.get(Url)
     soup = BeautifulSoup(response.content, 'html.parser') 

     Product = dict() # All the products with name, price, rating and specifications will stored as key value pair...
     # {Title : {'Price':'12,xxx', 'Rating':'4.4', 'Specifications':[list of specs]}}
     
     # Fetching products from soup with class name
     for box in soup.find_all('div',{'class':'_1UoZlX'}): 
          # Extract product name as title, price and rating from the product removing html tag with .text method
          title = box.find('div', class_="_3wU53n").text 
          price = box.find('div', class_="_1vC4OE _2rQ-NK").text  
          rating = box.find('div', class_="hGSR34").text
          spec = [] # list of specs for each product
          for elem in box.find_all('li', {'class':'tVe95H'}):
               spec.append(elem.text)
          Product[title] = {'Price':price,'Rating':rating ,'Specification':spec}

     for key, value in Product.items():
          print(key+": ")
          print(f"Price: {value['Price']} Rating: {value['Rating']}")
          for i,v in enumerate(value['Specification']):
               print(f"{i+1}) {v}")
          print("")
          
if __name__ == "__main__":
     productName = input("Search for products, brands and more: ")
     flipkart_api(productName)
