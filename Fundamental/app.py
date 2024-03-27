# variable in python
# name = "Phucdn"
# age = 23

# print(name+" is a boy!")
# print(name, " is ", age)
# print(name+" is a from Ho Chi Minh")
# print(name)

# string in python
# name = "PHUCDN"
# print("Hi.\How are you")
# # print(name.lower().islower())
# # print(len(name))
# # print(name.index("P"))
# print(name.replace('P', "T"))

# Numbers in python
# co the thuc hien cac phep toan khi in ra so trong python
# print(23 / 46)
# co the thuc hien cac phep toan logic
# number = 55
# number2 = str(number)
# print(20 % 6)
# doi voi them mot bien khi su dung dau +, thi chi them dc kieu string thoi
# print("number is" + number2)
# cac ham toan hoc trong python
# print(abs(-5))
# print(max(4,2,43,100))
# from math import *
# print(sqrt(100))

# Getting user input in python
# name = input('Enter your name: ')
# # mac dinh input la string, ta co the convert input sang cac kieu khac
# age = int(input('Enter your age: '))
# print('Your name is '+name+' and your are ' ,age," years old")

# Building a simple world replacement program
# sentence = input('Enter your sentence: ')
# print('Your sentence is: ',sentence)
# word1 = input('Enter the word to replace: ')
# word2 = input('Enter the word to replace it with: ')
# print(sentence.replace(word1,word2))

# List in Python -- link tham khao : https://viettuts.vn/python-list
# khai bao list bang cach thong thuong
# countries = ["United States", 2, True, "Australia"]
# # print(countries[0][0])
# # print(countries[2:]) : in ra mang ma bo 2 phan tu cua o dau mang
# # print(countries[:2]) : in ra mang co 2 phan tu o dau
# # print(countries[1:4]) : in ra gia tri theo thu tu 1,2,3
# # print(countries[-2]) : vi tri -number tuong ung voi vi tri tu cuoi mang dem len, cuoi mang tuong duong num la 1
# # co the them cac datatype khac nhau trong cung mot mang
# # su dung list constructor de khai bao list
# countries2 = list(('Nigeria', 34, False))
# print(type(countries))
# print(type(countries2))

# List Method in Python
# list1 = [4,3,5,1,2]
# list2 = ['banana', 'apples', 'mango', 'oranges']
# # Phụ thêm các nội dung của seq vào cuối list
# # list1.extend(list2)
# # Phụ thêm đối tượng obj vào cuối list
# # list2.append('cheery')
# # Chèn đối tượng obj vào trong list tại index đã cho
# # list2.insert(0,'cheery')
# # xoa mot phan tu dc nhap vao
# # list2.remove('banana')
# # xoa toan bo mang
# # list2.clear()
# # Hàm list.index(obj) - Trả về chỉ mục thấp nhất trong list mà tại đó obj xuất hiện
# # print(list2.index("mango"))
# # dem so lan xuat hien cua phan tu trong mang
# # print(list2.count("mango"))
# # sort list
# # list1.sort()
# # dao chieu list trong python
# # list2.reverse()
# # print(list2)
# # phuong thuc copy list trong python
# # list3 = list2.copy()
# # list2.append("cherry")
# # print(list3)
# # Hàm list.pop(obj=list[-1]) - Xóa và trả về phần tử cuối cùng hoặc đối tượng obj có chỉ mục đã cung cấp từ list đã cho
# # list2.pop(0)
# # print(list2)
# # del list[index]: xoa phan tu o vi tri index dc chi dinh
# del list2
# print(list2)

# Tuple in python - https://viettuts.vn/python-tuple
# Kiểu dữ liệu Tuple trong python là một collection có thứ tự, không thể thay đổi. Cho phép chứa dữ liệu trùng lặp. 
# Sử dụng các dấu ngoặc đơn, Không giống như List sử dụng các dấu ngoặc vuông. 
# Các đối tượng trong tuple được phân biệt bởi dấu phảy và được bao quanh bởi dấu ngoặc đơn (). Giống như chỉ mục của chuỗi, chỉ mục của tuple bắt đầu từ 0.
# three_numbers = (1,2,3)
# three_numbers = (1,'Home', True,3, 1)
# strings = ('home', 'land', 'earth')
# boo = (True, False, True)
# print(three_numbers)
# print(type(three_numbers[1]))

# Function in python - https://gochocit.com/ngon-ngu-lap-trinh/ham-function-va-cach-xay-dung-ham-trong-python
# def greetings_func(name):
#     print('Welcome ',name)
    
# greetings_func("Phucdn")
# Trong một số trường hợp, chúng ta không biết trước số lượng đối số truyền vào một hàm khi gọi hàm. 
# Python cho phép truyền số lượng đối số khác cho mỗi lần gọi hàm bằng cách sử dụng các dấu hoa thị * (asterisk). 
# Có 2 cách sử dụng dấu hoa thị * trong trường hợp này là:

# *args (Non-Keyword Arguments)
# **kwargs (Keyword Arguments)
# Sử dụng *args (Non-Keyword Arguments)
# Sử dụng một dấu hoa thị * trước tên tham số để sử dụng Non-Keyword Arguments. 
# Tên tham số tuân thủ theo quy tắc đặt tên định danh (identifier).
# def greetings_func(*name):
#     print('Welcome ',name[0])
    
# greetings_func("Phucdn", 'Tim', "Tom")
# def greetings_func(name, age):
#     print('Welcome '+name+ '. You are '+str(age)+" years old.")

# name = input('Enter your name: ')
# age = input('Enter your age: ')
# greetings_func(name, age)

# The return keyword in python
def my_test_func(num1 , num2):
    return num1+num2

num1 = int(input('Enter your num1: '))
num2 = int(input('Enter your num2: '))
print(my_test_func(num1,num2))