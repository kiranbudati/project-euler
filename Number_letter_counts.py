singles = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
doubles = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
thribles =  ['hundred', 'thousand', 'and']

result = 0

for i in range(1,1001):
    single = i % 10
    double = (i//10) % 10
    thrible = (i//100) % 10
    fours = (i//1000) % 10

    if fours != 0:
        result += len(singles[0]) + len(thribles[1])
    if i%1000 != 0:
        if thrible != 0:
            result += len(singles[thrible-1]) + len(thribles[0])
            if i % 100 != 0:
                result += len(thribles[2])
        if i % 100 != 0:
            if double < 2:
                result += len(singles[i%100-1])
            else:
                result += len(doubles[double-2])
                if single !=0:
                    result += len(singles[single-1])
print result