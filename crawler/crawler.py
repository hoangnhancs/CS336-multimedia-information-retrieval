import urllib.request
from bs4 import BeautifulSoup 
import requests
import re
dem = 0
print('CHÍNH TRỊ')
for i in range (1, 300):
  url = "https://vietnamnet.vn/vn/thoi-su/chinh-tri/trang{}".format(i)   #Load từ trang 1 đến trang 500 mục chính trị
  
  page = requests.get(url).content
  soup = BeautifulSoup(page, 'html.parser')
  contents = soup.findAll("div", {"class":"d-ib w-400"})     #Tìm mục
  

  for content in contents:  
      arr = re.split('[<> ]',str(content))
      pattern = re.compile("[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]")
  

      for _ in arr:
        if pattern.search(_):
          __ = _.split('/')
          __[2] = re.split('[.<>,"]', __[2])[0]
          if (int(__[1])>=9 and int(__[2])>=2020):
            print("Ngày viết: ",_,",Tiêu đề: ",content.find('a').text,",Link: ", arr[10][6:])
            dem += 1
 

print(dem)
#------------------------------------------------------------#
#Sức khỏe
print('SỨC KHỎE')
dem = 0
for i in range (1, 300):
  url = "https://vietnamnet.vn/vn/suc-khoe/trang{}".format(i)   #Load từ trang 1 đến trang 500
  
  page = requests.get(url).content
  soup = BeautifulSoup(page, 'html.parser')
  contents = soup.findAll("div", {"class":"d-ib w-400"})     #Tìm mục chứa các nội dung quan tâm


  for content in contents:  
      arr = re.split('[<> ]',str(content))
      pattern = re.compile("[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]")
      

      for _ in arr:
        if pattern.search(_):
          __ = _.split('/')
          __[2] = re.split('[.<>,"]', __[2])[0]
          try: 
            if (int(__[1])>=9 and int(__[2])>=2020): #bỏ những trường hợp sau khi split các phần tử không phải số
              print("Ngày viết: ",_,",Tiêu đề: ",content.find('a').text,",Link: ", arr[10][6:])
              dem += 1
          except:
            continue
sum+=dem
print(dem)
#--------------------------------------------------------------------#
#Thời sự
print('THỜI SỰ')
dem = 0
for i in range (1, 300):
  url = "https://vietnamnet.vn/vn/thoi-su/trang{}".format(i)   #Load từ trang 1 đến trang 500 
  
  page = requests.get(url).content
  soup = BeautifulSoup(page, 'html.parser')
  contents = soup.findAll("div", {"class":"d-ib w-400"})     #Tìm mục chứa các nội dung quan tâm


  for content in contents:  
      arr = re.split('[<> ]',str(content))
      pattern = re.compile("[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]")

      for _ in arr:
        if pattern.search(_):
          __ = _.split('/')
          __[2] = re.split('[.<>,"]', __[2])[0]
          try:
            if (int(__[1])>=9 and int(__[2])>=2020):
                print("Ngày viết: ",_,",Tiêu đề: ",content.find('a').text,",Link: ", arr[10][6:])
                dem += 1
          except:
            continue
sum+=dem
print(dem)
#-------------------------------------------------------------------#
#Kinh doanh
print('KINH DOANH')
dem = 0
for i in range (1, 300):
  url = "https://vietnamnet.vn/vn/kinh-doanh/trang{}".format(i)   #Load từ trang 1 đến trang 500
 
  page = requests.get(url).content
  soup = BeautifulSoup(page, 'html.parser')
  contents = soup.findAll("div", {"class":"d-ib w-400"})     #Tìm mục chứ các nội dung quan tâm


  for content in contents:  
      arr = re.split('[<> ]',str(content))
      pattern = re.compile("[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]") #kiểm tra có phải định dạng ngày tháng hay không
      

      for _ in arr:
        if pattern.search(_):
          __ = re.split('[/.<>,"…]', _)
          try:
            if (int(__[1])>=9 and int(__[2])>=2020):
                print("Ngày viết: ",_,",Tiêu đề: ",content.find('a').text,",Link: ", arr[10][6:]) #sau khi tách content thì mục link sẽ nằm ở vị trí thứ 11 trong mảng
                dem += 1
          except:
            continue
sum+=dem
print(dem)
#-------------------------------------------------------#
#Giải trí
print('GIẢI TRÍ')
dem = 0
for i in range (1,300):
  url = "https://vietnamnet.vn/vn/giai-tri/trang{}".format(i)   #Load từ trang 1 đến trang 500 mục chính trị

  page = requests.get(url).content
  soup = BeautifulSoup(page, 'html.parser')
  contents = soup.findAll("div", {"class":"box-subcate-style4-caption"})     #Tìm mục
  

  for content in contents:  
      arr = re.split('[<> ]',str(content))
     
      pattern = re.compile("[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]")
    

      for _ in arr:
        if pattern.search(_):
          __ = _.split('/')
          __[2] = re.split('[.<>,"…]', __[2])[0]
          try:
              if (int(__[1])>=9 and int(__[2])>=2020): #kiểm tra thời gian có hợp lệ trong 1 tháng trở lại hay không
                print("Ngày viết: ",_,",Tiêu đề: ",content.find('a').text,",Link: ", arr[8][6:])
                dem += 1
          except:
              continue
sum+=dem
print(dem)
#---------------------------------------------------#
#Thể thao
print('THỂ THAO')
dem = 0
for i in range (1, 300):
  url = "https://vietnamnet.vn/vn/the-thao/trang{}".format(i)   #Load từ trang 1 đến trang 500 mục chính trị
  
  page = requests.get(url).content
  soup = BeautifulSoup(page, 'html.parser')
  h3_contents = soup.findAll("div", {"class":"box-subcate-style4-caption"})     #Tìm mục 


  for content in contents:  
      arr = re.split('[<> ]',str(content))
      pattern = re.compile("[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]")
      

      for _ in arr:
        if pattern.search(_):
          __ = _.split('/')
          __[2] = re.split('[.<>,"]', __[2])[0]
          try:
            if (int(__[1])>=9 and int(__[2])>=2020):
              print("Ngày viết: ",_,",Tiêu đề: ",content.find('a').text,",Link: ", arr[8][6:])
              dem += 1
          except:
            continue
sum+=dem
print(dem)
#------------------------------------------------------#
#Pháp luật:
print('PHÁP LUẬT')
dem = 0
for i in range (1, 300):
  url = "https://vietnamnet.vn/vn/phap-luat/trang{}".format(i)   #Load từ trang 1 đến trang 500 mục chính trị

  page = requests.get(url).content
  soup = BeautifulSoup(page, 'html.parser')
  contents = soup.findAll("div", {"class":"d-ib w-400"})     


  for content in contents:  
      arr = re.split('[<> ]',str(content))
      pattern = re.compile("[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]")
      

      for _ in arr:
        if pattern.search(_):
          __ = _.split('/')
          __[2] = re.split('[.<>,"]', __[2])[0]
          
          if (int(__[1])>=9 and int(__[2])>=2020):
            print("Ngày viết: ",_,",Tiêu đề: ",content.find('a').text,",Link: ", arr[10][6:])
            dem += 1
          
sum+=dem
print(dem)
#--------------------------------------------------------#
#Thế giới
print('THẾ GIỚI')
dem = 0
for i in range (1, 300):
  url = "https://vietnamnet.vn/vn/the-gioi/trang{}".format(i)   #Load từ trang 1 đến trang 500 

  page = requests.get(url).content
  soup = BeautifulSoup(page, 'html.parser')
  contents = soup.findAll("div", {"class":"d-ib w-400"})     

  for content in contents:  
      arr = re.split('[<> ]',str(content))
      pattern = re.compile("[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]")

      for _ in arr:
        if pattern.search(_):
          __ = _.split('/')
          __[2] = re.split('[.<>,"]', __[2])[0]
          try:
            if (int(__[1])>=9 and int(__[2])>=2020):
              print("Ngày viết: ",_,",Tiêu đề: ",content.find('a').text,",Link: ", arr[10][6:])
              dem += 1
          except:
            continue
sum+=dem
print(dem)
#------------------------------------------------------#
#Công nghệ
print('CÔNG NGHỆ')
dem = 0
for i in range (1, 300):
  url = "https://vietnamnet.vn/vn/cong-nghe/trang{}".format(i)   #Load từ trang 1 đến trang 500 

  page = requests.get(url).content
  soup = BeautifulSoup(page, 'html.parser')
  contents = soup.findAll("div", {"class":"d-ib w-400"})     


  for content in contents:  
      arr = re.split('[<> ]',str(content))
      pattern = re.compile("[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]")
      

      for _ in arr:
        if pattern.search(_):
          __ = _.split('/')
          __[2] = re.split('[.<>,"]', __[2])[0]
          try:
            if (int(__[1])>=9 and int(__[2])>=2020):
              print("Ngày viết: ",_,",Tiêu đề: ",content.find('a').text,",Link: ", arr[10][6:])
              dem += 1
          except:
            continue
sum+=dem 
print(dem)

print('Tổng cộng có', sum, 'tiêu đề')