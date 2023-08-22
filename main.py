from TikiClawer import TikiClawer
from data import *
import time 

# Const
tiki_url = "https://tiki.vn/search?q="

keywords = "balo"

tiki = TikiClawer()

tiki.getUrl(tiki_url + keywords)
links = tiki.getProductLinks(productLinksXpath)
#print(links)

total_products = []

time.sleep(3)

for link in links:
    # Vào chi tiết sản phẩm
    tiki.getUrl(link)
    
    # Lấy brand
    tiki.getBrand(brand_xpath)
    
    # Lấy name
    tiki.getName(name_xpath)

    # Lấy giá
    tiki.getPrices(price_xpath)

    # them vao danh sach
    tiki.appendtoTotalProduct(total_products)

for i in total_products:
    tiki.print_product_info(i)

tiki.stopProcess()