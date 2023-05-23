test_file = open('D:/TuHocLapTrinh/python/Fundamental/les01/les03FileIO/text.txt', 'r')

for line in test_file.readlines():
    print(line)

test_file.close()