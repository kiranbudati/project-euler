import time
def recSumAtRow(rowData, rowNum):
    for i in range(len(rowData[rowNum])):
        rowData[rowNum][i] += max([rowData[rowNum+1][i],rowData[rowNum+1][i+1]])
    if len(rowData[rowNum])==1: return rowData[rowNum][0]
    else: return recSumAtRow(rowData, rowNum-1)
rows = []
with open('tri.txt') as f:
    for line in f:
        rows.append([int(i) for i in line.rstrip('\n').split(" ")])
 
start = time.time()
result = recSumAtRow(rows, len(rows)-2) # start at second to last row
elapsed = time.time() - start
 
 
print "%s found in %s seconds" % (result ,elapsed)