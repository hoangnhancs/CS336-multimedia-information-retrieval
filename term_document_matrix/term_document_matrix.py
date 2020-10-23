import re
import glob
import numpy as np

# Inverted file trong bài này sẽ là biến ivt_file
# Ma trận term document sẽ có tên là term matrix

file_paths = ['/home/hnhan/hoangnhan/truyvan/boolen_inverted_file/data1.txt', '/home/hnhan/hoangnhan/truyvan/boolen_inverted_file/data2.txt', '/home/hnhan/hoangnhan/truyvan/boolen_inverted_file/data3.txt',
'/home/hnhan/hoangnhan/truyvan/boolen_inverted_file/data4.txt', '/home/hnhan/hoangnhan/truyvan/boolen_inverted_file/data5.txt', '/home/hnhan/hoangnhan/truyvan/boolen_inverted_file/data6.txt',
'/home/hnhan/hoangnhan/truyvan/boolen_inverted_file/data7.txt', '/home/hnhan/hoangnhan/truyvan/boolen_inverted_file/data8.txt', '/home/hnhan/hoangnhan/truyvan/boolen_inverted_file/data9.txt']
#B1: Tạo bộ từ vựng
ivt_file = {}
def load_file(file_path):
    f = open(file_path, 'r')
    data = f.read()
    non_impor_chars = [',', '.', '"', '(', ')']
    for char in non_impor_chars:
        data = data.replace(char, '')
    words = data.split()
    
    return words
    

i = 0
for file_path in file_paths:
    words = load_file(file_path)
    for word in words:
        if word not in ivt_file:
            ivt_file[word] = set()
            ivt_file[word].add(i)
        else:
            ivt_file[word].add(i)
    i+=1
#B2: Tạo term matrix
term_document = np.zeros((len(ivt_file), len(file_paths)))
#print(ivt_file)
term_matrix = {}
dem = 0
#for i in range ()
for word in ivt_file:
    for i in ivt_file[word]:
          term_document[dem][i]=int(1)
            #print(i)
    term_matrix[word]=term_document[dem]
    dem += 1
#print(term_matrix)  
#B3: Tạo khái niệm query
def or_query(a, b):
    result = []
    for i in range (len(a)):
        if (a[i]==1 or b[i]==1):
            result.append(1)
        else:
            result.append(0)
    return result

def and_query(a, b):
    result = []
    for i in range (len(a)):
        if (a[i]==0 or b[i]==0):
            result.append(0)
        else:
            result.append(1)
    return result

def not_query(a):
    result = []
    for i in range (len(a)):
        if (a[i]==1):
            result.append(0)
        else:
            result.append(1)
    return result

def xor_query(a, b):
    result = []
    for i in range (len(a)):
        if (a[i] == b[i]):
            result.append(0)
        else:
            result.append(1)
    return result

#B4: Nhập câu truy vấn và phân tách từ truy vấn
query_doc = '"những" AND NOT "những" XOR NOT NOT NOT "Tuấn" AND "hủy"'
query_doc = query_doc.replace('"','')
#print(query_doc)
_ = query_doc.split()
#print(_)
querys = ['AND', 'OR', 'XOR', 'NOT']
stack_query = []
result = []

for i in range (len(_)):
    if _[i] not in querys:
        
        if result == []:
            result = term_matrix[_[i]]

        else:
            tmp = term_matrix[_[i]]
            while len(stack_query)!=0:
                query = stack_query[len(stack_query)-1]

                if query == 'OR':
                    result = or_query(result, tmp)
                if query == 'AND':
                    result = and_query(result, tmp)
                if query == 'XOR':
                    result = xor_query(result, tmp)
                if query == 'NOT':
                    tmp = not_query(tmp)
          
                stack_query.pop()
            
    else:
        stack_query.append(_[i])
        
print('Term document is: ', term_matrix)       

print('Kết quả truy vấn "', query_doc,'" là: ', end="")
print(result)

print('Do đó, những văn bản thỏa câu truy vấn sẽ là: ', end="")
for i in range (len(result)):
    if result[i]==1:
        print(i,', ',end="")

print(' tính từ văn bản 0')




    