def isListOfInts(list1):
    if isinstance(list1, list):

      if all(isinstance(item, int) for item in list1):
        print(list1,'-->true');
      else:
        print(list1,'-->false');
    else:
        print("ValueError: ",list1," - arg not of <list> type");

def testList(list1):
    if list1==[]:
        print([],'-->true');
    else:
      return isListOfInts(list1)


testList([])
testList([1])
testList([1, 2])
testList([0])
testList(['1'])
testList([1, 'a'])
testList(['a', 1])
testList([1, 1.])
testList([1., 1.])
testList((1, 2))
