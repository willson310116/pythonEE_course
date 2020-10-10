import sys
import os
from math import floor
# submit version 

def print_level_two_tree():
  maxlen = find_middle(2)[1]
  for i in range(7):
    if i < 3:  #i=0~2
      curlen = 2*i+3
      front = " "*int((maxlen-curlen)/2)
      mid  = "*"*(2*i+1)
      print(f"{front}/{mid}\\")
    elif i < 6:  #i=3~5
      curlen = 2*i+7
      front = " "*int((maxlen-curlen)/2)
      mid = "*"*(2*i+5)
      print(f"{front}/{mid}\\")
    else:
      mid = "*"*8 + "|" + "*"*8
      print(f"/{mid}\\")

def find_middle(n):
  index = 1
  layers = 3
  first_len = 1+2
  maxlen = first_len + (layers-1)*2
  midlen = (maxlen+1)/2
  diff = 3
  if n == 1:
    return int(midlen),int(maxlen)
  else:
    # index += 1
    while index < n:
      layers+=1
      index+=1
      diff = floor(index/2)+2
      first_len = maxlen + diff*2
      maxlen = first_len + (layers-1)*2
      midlen = (maxlen+1)/2
      # print(maxlen)
  # response = f"""
  # The first return value is the mid_len {int(midlen)},
  # and the second is the maxlen {int(maxlen)}
  # I need to use maxlen length in other functions, sorry for that.
  # """
  # print(response)
  return int(midlen), int(maxlen)

def print_level_n_tree(n):
  """
  This function will print a n level christmas tree.
  """
  midlen, maxlen = find_middle(n)
  for i in range(1,n+1):  # 4 = 3+1 (N+1)
    # 每一大層的設定
    layers = i+2
    diff = floor(i/2)+2 if i>1 else 0
    if i ==1:
      first_len = 3
      
    else:
      first_len = loc_maxlen+diff*2
    loc_maxlen = first_len + (layers-1)*2
    door = i if i%2 == 1 else i-1
    
    # 印door以上的
    for j in range(1,i+3-door):  # j=1~i+2 (if i=1第一大層,j=1~3 印3層，if i=2第二大層，j=1~4 印4層)
      curlen = first_len if j==1 else first_len+((j-1)*2)
      front = " "*int((maxlen-curlen)/2)
      mid  = "*"*(curlen-2)
      print(f"{front}/{mid}\\")

    # 只有最後一大層有door
    if i < n:
      for k in range(i+3-door,i+3):
        curlen = first_len+((k-1)*2)
        front = " "*int((maxlen-curlen)/2)
        mid  = "*"*(curlen-2)
        print(f"{front}/{mid}\\")
     # 只有5大層以上才有門把
    else:
      if n < 5:
        for k in range(i+3-door,i+3): 
          curlen = first_len+((k-1)*2) 
          front = " "*int((maxlen-curlen)/2)
          star_num = int(((curlen-2-door)/2))
          mid = "*"*star_num + "|"*door + "*"*star_num
          print(f"{front}/{mid}\\")
      else:
        start = i+3-door
        mid_row = start + int((door+1)/2)
        # above door hand
        for k in range(start, mid_row-1): 
          curlen = first_len+((k-1)*2) 
          front = " "*int((maxlen-curlen)/2)
          star_num = int(((curlen-2-door)/2))
          mid = "*"*star_num + "|"*door + "*"*star_num
          print(f"{front}/{mid}\\")

        # door with hand
        curlen = first_len+((mid_row-2)*2) 
        front = " "*int((maxlen-curlen)/2)
        star_num = int(((curlen-2-door)/2))
        mid = "*"*star_num + "|"*(door-2) + "@|" + "*"*star_num
        print(f"{front}/{mid}\\")

        # below door hand
        for k in range(mid_row,i+3): 
          curlen = first_len+((k-1)*2) 
          front = " "*int((maxlen-curlen)/2)
          star_num = int(((curlen-2-door)/2))
          mid = "*"*star_num + "|"*door + "*"*star_num
          print(f"{front}/{mid}\\")

# order = input("R for run, Q for quit\n >")
# while order.lower() != "q":
# 	x = int(input("How many level?\n> "))
# 	print_level_n_tree(x)
# 	order = input("R for run, Q for quit\n >")


def Diffie_Hellman_cracker(p, g, A, B):
  a, b = 1, 1
  while (g**a)%p != A:
    a+=1
  while (g**b)%p != B:
    b+=1
  k = (g**(a*b))%p
  return a,b,k

response = f"""
  For function find_middle(n), I need to use maxlen length in other functions, so
  the first return value is the midlen, and the second return value is the maxlen.
  For example when executing find_middle(2), it will return (10, 19),
  and 10 is the midlen which is the answer of find_middle() while 19 is the maxlen.
  """
print(response)

