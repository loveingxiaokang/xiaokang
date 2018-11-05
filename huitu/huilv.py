import csv
filename = r'C:\Users\22240\Desktop\lianxi\zhong_guo.csv'
with open(filename) as f:
    reader = csv.reader(f)
    head_row = next(reader)
    print(head_row)