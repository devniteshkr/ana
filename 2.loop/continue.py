cart=[110,20,30,500,600,80,50]
for item in cart:
    if item >=500:
      print("we can't process your item: ",item)
      continue
    print(item)