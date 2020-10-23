
import glob
import numpy as np
import re
from math import *


#-------------INVERTED_FILE------------#

data_paths = ['/home/hnhan/hoangnhan/truyvan/tf_idf/data1.txt', '/home/hnhan/hoangnhan/truyvan/tf_idf/data2.txt', '/home/hnhan/hoangnhan/truyvan/tf_idf/data3.txt']

for data_path in data_paths:
    f = open(data_path, 'r')
    data = f.read()
    data = data.split("\n")
    print(len(data))

def load_data_in_a_directory(file_paths):
    #file_paths = glob.glob(data_path)
    lst_contents = []
    for file_path in file_paths:
        f = open(file_path, 'r')
        data = f.read()
        special_char = ['"', '.', ',', "'", ':']
        for _ in special_char:
            data.replace(_, ' ')
        words = data.lower().split()
        #words = set(words)
        lst_contents.append(words)
    return (lst_contents, file_paths)


def build_dictionary(contents):
    dictionary = set()
    for content in contents:
        dictionary.update(content)
    return dictionary
#---------------------------------
def build_inverted_file(contents, vocab):
    inverted_file = {}
    for word in vocab:
        tmp_dic = {}
        for i in range (len(contents)):  
            if word in contents[i]:
                tmp_dic[str(i)] = contents[i].count(word)
        inverted_file[word] = tmp_dic
    return inverted_file
#----------------------------------
lst_contents, file_paths = load_data_in_a_directory(data_paths)
query="những"
qcontent = query.split()
#print(lst_contents)
vocab = build_dictionary(lst_contents)
#print(vocab)
ivt_file = build_inverted_file(lst_contents, vocab)
#print(ivt_file)
q_ivt_file = build_inverted_file(qcontent, vocab)
#-----------------------------------
def calc_tf_weighting(vocab, ivt_file):
    tf_weight = {}
    for word in vocab:
        tmp_dic = {}
        for doc in ivt_file[word]:
            try:
                tmp_dic[doc] = ivt_file[word][doc]/len(lst_contents[int(doc)])
            except:
                tmp_dic[doc] = 999999999999
        tf_weight[word] = tmp_dic
    return tf_weight
#--------------------------------------

tf_weight = calc_tf_weighting(vocab, ivt_file)
#print(tf_weight)
q_tf_weight = calc_tf_weighting(vocab, q_ivt_file)

#---------------------------------------
def calc_df_weighting(ivt_file, word):
    return len(ivt_file[word])

def calc_idf_weighting(ivt_file, vocab):
    idf_weight = {}
    for word in vocab:
        try:
            idf_weight[word] = 1 + log(len(lst_contents)/len(ivt_file[word]))
        except:
            idf_weight[word] = -9999999999999
    return idf_weight
#---------------------------------------

idf_weight = calc_idf_weighting(ivt_file, vocab)
#print(idf_weight)

#------------------------------------------

def cal_tf_idf_weighting(tf_weight, idf_weight, vocab):
    tf_idf_weight ={}
    for word in vocab:
        tmp_dic = {}
        for doc in tf_weight[word]:
            tmp_dic[doc] = tf_weight[word][doc]*idf_weight[word]
        tf_idf_weight[word] = tmp_dic
    return tf_idf_weight
#----------------------------------------------

tf_idf_weight = cal_tf_idf_weighting(tf_weight, idf_weight, vocab)
#print(tf_idf_weight)
q_tf_idf_weight = cal_tf_idf_weighting(q_tf_weight, idf_weight, vocab)
#print(q_tf_tdf_weight)

#----------------------------------------------
def cal_distance(tf_idf_1, tf_idf_2, vocab):
    distance = {}
    for _ in range(len(lst_contents)):
        pow_2_sum = 0
        _ = str(_)
        for word in vocab:
            
            if _ not in tf_idf_1[word]:
                tf_idf_1[word][_] = 0
            if _ not in tf_idf_2[word]:
                tf_idf_2[word][_] = 0
            pow_2_sum = pow_2_sum + (tf_idf_1[word][_] - tf_idf_2[word][_])**2
        distance[_] = sqrt(pow_2_sum)
    return distance
# for word in vocab:
#     print(word)
#------------------------------------------------

distance = cal_distance(tf_idf_weight, q_tf_idf_weight, vocab)
print(distance)
