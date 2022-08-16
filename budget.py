class Category:
  def __init__(self, description):
    self.description = description
    self.ledger = []
    self.__balance = 0.0

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})
    self.__balance += amount

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      self.__balance -= amount
      return True
    else:
      return False

  def get_balance(self):
    return self.__balance

  def transfer(self, amount, category):
    if self.withdraw(amount, f'Transfer to {category.description}'):
      category.deposit(amount, f'Transfer from {self.description}')
      return True
    else: 
      return False

  def check_funds(self, amount):
    if self.__balance >= amount :
      return True
    else:
      return False

  def __str__(self):
    catText = self.description.center(30, "*") + "\n"
    items = ""
    for item in self.ledger :
      items += item['description'][:23].ljust(23," ")
      items += "{:.2f}".format(item['amount'])[:7].rjust(7," ")+"\n"
    total = f'Total: {self.__balance}'
    return catText + items + total
    
def create_spend_chart(categories):
  spentBudget = []
  header = "Percentage spent by category\n"
  content=""
  footer=""
  maxFooter = 0
  for category in categories :
    if len(category.description) > maxFooter:
      maxFooter = len(category.description)
    spending = 0
    for item in category.ledger :
      if item['amount'] < 0 :
        spending += -item['amount']
    spentBudget.append(spending)
  total = sum(spentBudget)
  for i in range(100,-10,-10):
    content += str(i).rjust(3," ")+"|"
    for spend in spentBudget :
      if(spend/total) > i/100:
        content += " o "
      else :
        content += "   "
    content +=" \n"
  
  footer += ("-"*(3*len(categories)+1)).rjust(5+(3*len(categories))," ") +"\n"
  for i in range(maxFooter):
    Line = ""
    for j in range(len(categories)):
      if len(categories[j].description) > i:
        Line += f" {categories[j].description[i]} "
      else :
        Line += "   "
    footer += Line.rjust(4+(3*len(categories))," ") +" \n"
    
  return (header+content+footer).rstrip("\n")
    
  
  