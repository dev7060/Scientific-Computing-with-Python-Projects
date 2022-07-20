class Category:
  funds = 0
  total_spent = 0
  def check_funds(self, amount):
    if self.funds < amount:
      return False
    else:
      return True
  def __str__(self):
    mystr = self.category.center(30, '*') + "\n"
    for i in self.ledger:
      mystr = mystr + "{:<23}".format(i["description"][0: 23])  + format(i["amount"], '.2f').rjust(7) + "\n"
    mystr = mystr + "Total: " + str(self.funds)
    return mystr
  def __init__(self, category):
    self.ledger = []
    self.category = category
    self.category_spent = 0
  def deposit(self, amount, description=''):
    self.funds = self.funds + amount
    self.ledger.append({"amount": amount, "description": description})
  def withdraw (self, amount, description=''):
    if self.check_funds(amount):
      self.category_spent = self.category_spent + amount
      Category.total_spent = Category.total_spent + amount
      self.funds = self.funds - amount
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False
  def get_balance (self):
    return self.funds
  def transfer(self, amount, budget_category):
    transfer_to = "Transfer to " + budget_category.category
    transfer_from = "Transfer from " + self.category
    if self.check_funds(amount):
      self.withdraw(amount, transfer_to)
      budget_category.deposit(amount, transfer_from)
      return True
    else:
      return False


def create_spend_chart(categories):
  mystr = "Percentage spent by category" + "\n"
  mylist = []
  horizontal_len = len(categories)
  myobjects = []
  for i in categories:
    myobjects.append(i)
#   print(myobjects)
  mypercentages = []
  for i in range(0, horizontal_len):
    per = (categories[i].category_spent/Category.total_spent)*100
    per = int(per)
    val = per - (per%10)
    mypercentages.append(val)
#   print(mypercentages)
  for i in range(0, (horizontal_len+1)*11):
    mylist.append([])
  m = 100
  for i in range(0, (horizontal_len+1)*11, 4):
    mylist[i].append(m)
    m = m-10
  for _ in range(0, horizontal_len):
    k=0
    for i in range(_+1, (horizontal_len+1)*11, 4):
      if(mylist[k][0]<=mypercentages[_]):
        mylist[i] = "o"
      else:
        mylist[i]=None
      k = k + 4
#   for i in range(0, 4):
#     print(" ", end = "")
#   print("-", end = "")
#   for i in range(0, horizontal_len):
#     print("---", end = "")
#   print (mylist)
  #biggest length
  maxl = 0
  for i in range(0, horizontal_len):
    if(len(categories[i].category) > maxl):
        maxl = len(categories[i].category)
#   print(maxl)
  lmatrix = []
  for i in range(0, maxl*horizontal_len):
    lmatrix.append([])
#   print(lmatrix)
#   for i in range(0, horizontal_len):
#     for j in range(0, len(categories[i].category)):
#       # print(j, end="")
#       print(categories[i].category[j], end="")
#       pass
#     print()
  for kr in range(0, len(categories)):
    k = kr
    m = kr
    n = 0
    for i in range(0, len(categories[kr].category)):
      if(m < len(categories[m].category)):
        lmatrix [k] = categories[m].category[n:n+1]
        n+=1
      k+=len(categories)
  for i in range(0, len(lmatrix)):
    if isinstance(lmatrix[i], list):
      lmatrix[i]=None
#   print(lmatrix)
  temp = 0
  for i in mylist:
      if i != 'o' and i!=None:
        if i[0] == 100:
          mystr = mystr + str(i[0]) + "| "
        elif i[0] == 0:
          mystr = mystr + "  "  + str(i[0]) + "| "  
        else:
          mystr = mystr + " "  + str(i[0]) + "| "  
      if i == None:
        mystr = mystr + "   " 
        
      if i == 'o':
        mystr = mystr + 'o  '
      temp = temp + 1
      if (temp % (horizontal_len+1))==0:
        mystr = mystr + "\n"
    
  mystr = mystr + "    "
  mystr = mystr + "-"
  temp = 0
  for i in range(0, horizontal_len):
    # print("---", end = "")
    mystr = mystr + "---"
  mystr = mystr + "\n"    
  mystr = mystr + "     "
  for i in lmatrix:
    if i == None:
      mystr = mystr + "   "
    if i!= None:
      mystr = mystr + i + "  "
    temp = temp +1
    if ((temp % horizontal_len) == 0 and i!=(maxl*horizontal_len)):
      mystr = mystr + "\n" + "     "
#   print(mystr)
  mystr = mystr[0:len(mystr)-6]    
  return mystr
  
