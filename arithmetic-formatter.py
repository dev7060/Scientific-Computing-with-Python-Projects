def arithmetic_arranger(problems, myans=False):
  # [ " sdf", "Dfsd"]
  mylen = []
  res = []
  mysign = []
  mystr = ""
  op = []
  if(len(problems)>5):
    return "Error: Too many problems."
  for i in problems:
    if i.find('*') !=-1 or i.find('/') !=-1 :
      return "Error: Operator must be '+' or '-'."
  
  for i in problems:
        if i.find("+") != -1 or i.find("-") != -1:
            if i.find("+") != -1:
                sign = "+"
            else:
                sign = "-"
            ls = i.split(sign)
            if ((ls[0].strip().isnumeric() != True ) or (ls[1].strip().isnumeric() != True)):
                return "Error: Numbers must only contain digits."
                
            if (len(ls[0].strip())>4 or len(ls[1].strip())>4):
                return "Error: Numbers cannot be more than four digits."

            ############################################################
            operand1 = int(ls[0].strip())
            operand2 = int(ls[1].strip())
            if(sign == "-"):
                res.append(operand1-operand2)
            else:
                res.append(operand1+operand2)
            if(len(ls[0].strip())>len(ls[1].strip())):
                mylen.append(len(ls[0].strip()))
                mysign.append(sign)
            else:
                mylen.append(len(ls[1].strip()))
                mysign.append(sign)
            op.append(operand1)
            op.append(operand2)
  j=0
  for i in range(0, len(op), 2):
    # mystr = mystr + "  "
    mystr = mystr + "  " + str(op[i]).rjust(mylen[j])
    # if i+1 != (len(op)):
            # mystr = mystr + "    "
    mystr = mystr + "    "
      # print(mysign[j], " ", f'{op[i]:>{mylen[j]}}', end="    ", sep="")
    j+=1
  mystr = mystr[0: len(mystr)-4]
  mystr = mystr + "\n"
  j=0
  for i in range(1, len(op), 2):
    mystr = mystr + mysign[j] + " " + str(op[i]).rjust(mylen[j])
    if i+1 != (len(op)):
      mystr = mystr + "    "
    # mystr = mystr + "    "
      # print(mysign[j], " ", f'{op[i]:>{mylen[j]}}', end="    ", sep="")
    j+=1
  # print(mystr)
  mystr = mystr + "\n"
  # print()
  for i in range(0, len(mysign)):
    for j in range(0, mylen[i]+2):
      # print("-",end="")
      mystr = mystr + "-"
    if i+1 != (len(mysign)):
      mystr = mystr + "    "
      # print("    ", end="")
    # print(mystr)
  # print()
#   mystr = mystr[0: len(mystr)-4]
  #   mystr = mystr + "\n"
  j=0
  if myans == True:
    mystr = mystr + "\n"
    for j in range(0, len(res)):
      mystr = mystr + str(res[j]).rjust(mylen[j]+2)
    # if j+1 != (len(res)):
      j+=1
      mystr = mystr + "    "
    mystr = mystr[0: len(mystr)-4]
      # print(f'{res[j]:>{mylen[j]+2}}', end="    ", sep="")
  return mystr
 
# print(arithmetic_arranger(['3801 - 2', '123 + 49'], True))
