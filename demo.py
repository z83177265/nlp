import math

dictionary = [('羽毛球', 2), ('羽毛', 2.3), ('毛球', 5), ('球', 2.6), ('球拍', 2), ('拍', 2), ('拍卖', 3.1), ('卖', 2), ('完了', 3.6), ('卖完了', 2), ('羽', 10), ('毛', 10), ('完', 10), ('了', 10),]
string = '羽毛球拍卖完了'
max_length = 3 #词典最长词

def getAllIncomingPoints(point:int, string:str, dictionary:list):
  results = []
  end = point
  start = 0
  if end - max_length >= 0:
    start = end - max_length

  while start < end:
    if string[start:end] in dict(dictionary):
      results.append(start)
    start += 1
  return results

def getPathValue(start:int, end:int, string:str, dictionary:list):
  if start > end:
    return None

  if string[start:end] in dict(dictionary):
    return dict(dictionary)[string[start:end]]
  else:
    return None

# 规划路径
pathList = [(0, 0)]

for current in range(1, len(string) + 1):
  incomingPoints = getAllIncomingPoints(current, string, dictionary)
  if len(incomingPoints) == 0:
    pathList.append((None, None))
    continue

  minValue = math.inf
  formPoint = 0
  for incoming in incomingPoints:
    value = pathList[incoming][0] + getPathValue(incoming, current, string, dictionary) 
    if value < minValue:
      minValue = value
      formPoint = incoming
  pathList.append((minValue, formPoint))

print(pathList)

# 反推最佳路径
bestPath = []
currentPoint = len(pathList) - 1

bestPath.append(currentPoint)
while currentPoint != 0:
  currentPoint = pathList[currentPoint][1]
  bestPath.append(currentPoint)
bestPath.reverse()

print(bestPath)

# 打印结果
startingIndex = 0
endingIndex = 1
while (endingIndex < len(bestPath)):
  print(string[bestPath[startingIndex]:bestPath[endingIndex]])
  startingIndex = endingIndex
  endingIndex += 1
