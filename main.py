listOfItems = ['apple', 'banana', 'pear', 'grape']
costOfItem = [2, 1.7, .5, 3]

def addItemToList(item, price, knowUpdateing):
  global listOfItems
  global costOfItem
  if not knowUpdateing:
    if item in listOfItems:
      print 'I already know that item'
      a = raw_input('Would you like to update the price?')
      if a == 'Yes' or a == 'yes':
        place = listOfItems.index(item)
        costOfItem[place] = price
        main()
    else:
      listOfItems += [item]
      costOfItem += [price]
      main()
  else:
    place = listOfItems.index(item)
    costOfItem[place] = price
    main()
    
def removeItemFromList(item):
  global listOfItems
  if item in listOfItems:
    place = listOfItems.index(item)
    x = costOfItem[place]
    listOfItems.remove(item)
    costOfItem.remove(x)
    main()

def costOf(item, amount ):
    return costOfItem[item] * int(amount)

def cost(name, amount):
  place = 0
  try:
    if float(amount).is_integer():
      if name in listOfItems:
        place = listOfItems.index(name)
        return costOf(place, amount)
      else:
        return 'I am not that smart'
        main()
    else:
      print "I can only sell whole items"
      main()
  except ValueError:
    print 'please enter an integer'
    main()

def main():
  print ''
  print 'What would you like to do?'
  print 'Check price of item?'
  print 'Change price of item?'
  toDo = raw_input('')
  if toDo.lower() in 'check' :
    print listOfItems
    item = raw_input('What item? ')
    if item not in listOfItems:
      print 'I must not know jack'
      if type(item) == int:
         print 'please input a name with no numbers'
         main()
      print 'But would you like to add ' +item+ ' to known items'
      responce = raw_input('')
      if responce == 'yes':
        price = raw_input('At what price')
        addItemToList(item, price, False)
        main()
      elif responce == 'no':
        main()
  
    amount = raw_input('How many? ')
  
    if item in listOfItems:
      print 'Your cost will be $' + str(cost(item, amount)) + ' for ' + amount + ' ' + item +"s"
      main()
  elif toDo.lower() in 'change':
    print 'remove or update?'
    x = raw_input('')
    if x.lower() == 'update':
      print listOfItems
      a = raw_input('What item? ')
      if a in listOfItems:
        print 'The price of '+a+ ' is $'+ str(costOfItem[listOfItems.index(a)])
        try:
          newPrice = raw_input('New price?')
          if float(newPrice).is_integer():
            input = float(newPrice)
            addItemToList(a, input, True)
            main()
          else:
              main()
        except ValueError:
          print 'Please enter a number'
          main()
      else:
        main()
    elif x.lower() == 'remove':
      print listOfItems
      removeItemFromList(raw_input('what to remove? '))
      main()
    else:
      main()
  else:
    main()
main()
