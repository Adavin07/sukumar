hi sukumar do changes

# # print('welcome to thunder bank')
# # class Account_details():
# #     def __init__(self, Account_no, Pancard_Details, Aadhar_card_Details ):
# #         self.Account_no = Account_no
# #         self.Pancard_Details = Pancard_Details
# #         self.Aadhar_card_Details = Aadhar_card_Details
# #
# #
# #     def display(self):
# #         print(' your details in thunder bank is',self.Account_no, self.Pancard_Details, self.Aadhar_card_Details)
# #
# #     def Account_name(self,name):
# #         self.name = name
# #         print('your name is missing ' )
# #         print('now check your account details : ', self.name,self.Account_no)
# #
# # acc = Account_details(input('enter your account details: '),input('enter your pancard details: '),input('enter your aadhar card details: '))
# # acc.display()
# # acc.Account_name(input('enter your name '))
#
# print('hii welcome store')
# d = {'car': 30, 'plane': 100, 'train': 40, 'doll': 90}
# class toy_store:
#     def __init__(self, toy_name, price, billing ):
#         self.toy_name = toy_name
#         self.price = price
#         self.billing = billing
#
#
#     def display(self):
#
#         print('please select your toy')
#         for i, j in d.items():
#             print(i,'=','rs.',j)
#
# class price1(toy_store):
#
#         def price2(self):
#             print('please let select your toy')
#             a = input('enter your toy to buy ')
#             no_toy = int(input('how much toy you want to buy'))
#             b = int(input('enter your quantity'))
#             for i,j in d.items():
#                 if i == a:
#                     total = no_toy * j
#                     print('rs.',total)
#                     print(total*b)
#
#
# e = 0
# while e < 3:
#     toy = toy_store('plane',25,45)
#     bill = price1('plane',25,45)
#     bill.display()
#     bill.price2()
#     e+=1


print('hi welcome to karthii hotel')
hotel_menu= {'dosa': 30 , 'idli': 20}
#
# class karti_hotel:
#
#     def __init__(self):
#         pass
#
#
#     def display(self):
#         print('below is the menu')
#         for i,j in hotel_menu.items():
#             print(i ," = rs.",j)
#
#     def bill(self):
#         a = input('enter your order')
#         while a:
#         for i,j in hotel_menu.items():
#             if a == i:
#                 print('your amount for dosa is ',j)
#                 b = int(input('enter your order quantity'))
#                 c = j * b
#                 print('your total amount for your order is ',c)
#
# waiter = karti_hotel()
# waiter.display()
# waiter.bill()
#
# # Map two lists into a dictionary
# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
# a.extend(b)
# print(a)
# c = {}
# for i in a:
#     print(i)
#     c[i] = 0
# print(c)

#
# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
# c = {}
# for i in range(len(a)):
#     for j in range(len(b)):
#         if i == j:
#             c[a[i]] = b[j]
# print(c)

# Sort a dictionary by key
# d = {'car': 30, 'plane': 100, 'train': 40, 'doll': 90}
# c = []
# for i in d.keys():
#     c.append(i)
#     for i in c:
#         for j in c:
#             print(j)
#             if len(i) > len(j):
#                 c[i],c[j] = c[j],c[i]
#
# print(c)


# Get the maximum and minimum value in a dictionary.
# d = {'car': 30, 'plane': 100, 'train': 40, 'doll': 90}
# c = []
# for i in d.values():
#     c.append(i)
# for i in range(len(c)):
#     for j in range(len(c)):
#         if c[i] < c[j]:
#             c[i],c[j] = c[j],c[i]
# print(c)

# Remove duplicates from Dictionary
# d = {'car': 30, 'plane': 100, 'train': 40, 'doll': 90, 'bike':40}
# c = {}
# for i,j in d.items():
#     if j not in c.values():
#         c[i] = j
# print(c)

# having = 50
# choclate = 3
# wrapper = 3
#
# d = having/choclate
# print(int(d))
# e = d / wrapper
# print(int(e))
#
# if e >= 3:
#     t = e/3
#     print(int(t))
# print(d + e + t)


# # Combine two dictionary adding values for common keys.
# a = {'car': 30, 'plane': 100, 'train': 40, 'doll': 90, 'bike':40}
# b = {'rocket':70, 'doll': 90, 'bike':40}
# d = {}
#
# for i,m in a.items():
#     for k,j in b.items():
#         if i == k:
#             d[i]= m+j
# print(d)
# a.update(d)
# print(a)


#
# # Print all unique values in a dictionary
# a = {'car': 30, 'plane': 100, 'train': 40, 'doll': 90, 'bike':40}
# b = {}
# c = []
# for i,j in a.items():
#     c.append(j)
#     if c.count(j) == 2:
#         print(j)
#     if j == 40:
#         b[i] = j
# print(b)


# # Create and display all combinations of letters, selecting each letter from a different key in a dictionary
# x="edwiin1234"
# l=[]
# s=""
# s1=""
# for i in x:
#     if i not in l:
#         l.append(i)
#         s1+=i
# print(s1)

#
# class travels:
#
#     def __init__(self,bus,route,pngr):
#         self.bus=bus
#         self.route=route
#         self.pngr=pngr
#     def display(self):
#         print(self.bus)
#         print(self.route)
#     def passenger(self):
#         print(self.pngr)
#
# x=input("enter bus name:")
# y=input("enter your route :")
# z=int(input("enter passenger count :"))
# obj=travels(x,y,z)
# obj.display()
# obj.passenger()
