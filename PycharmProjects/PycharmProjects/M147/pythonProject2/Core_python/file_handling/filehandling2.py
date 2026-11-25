#----------------------------------------------------------------------------
#cleaning the data,storing the unique data,count and max count
def read_txt():
    records = []
    with open(r'access-log.txt','r') as obj:
        for line in obj:
            clean_line = line.strip()
            if clean_line:
                words = clean_line.split()[0]
                records.append(words)
    return records

print(read_txt())

def unique_ip():
    data = read_txt()  # list od records
    _unique_ip = []
    for item in data:
        if item not in _unique_ip:
            _unique_ip.append(item)
    return _unique_ip
print(unique_ip())

def ip_count_pair():
    data = read_txt()
    return {item:data.count(item) for item in data}
print(ip_count_pair())
d = {'67.218.116.165': 2, '66.249.71.65': 3, '65.55.106.183': 2, '66.249.65.12': 32, '65.55.106.131': 2, '08:06': 1, '65.55.106.186': 1, '74.52.245.146': 2, '66.249.65.43': 3, '65.55.207.25': 2, '65.55.207.94': 2, '65.55.207.71': 1, '98.242.170.241': 1, '66.249.65.38': 100, '65.55.207.126': 2, '82.34.9.20': 2, '65.55.106.155': 2, '65.55.207.77': 2, '208.80.193.28': 1, '89.248.172.58': 22, '67.195.112.35': 16, '65.55.207.50': 3, '65.55.215.75': 2}

# f={ip:d.count(ip)for ip in d}
# print(sorted(d.items(),key=lambda i:i[1]))


d = {
    '67.218.116.165': 2, '66.249.71.65': 3, '65.55.106.183': 2, '66.249.65.12': 32,
    '65.55.106.131': 2, '08:06': 1, '65.55.106.186': 1, '74.52.245.146': 2,
    '66.249.65.43': 3, '65.55.207.25': 2, '65.55.207.94': 2, '65.55.207.71': 1,
    '98.242.170.241': 1, '66.249.65.38': 100, '65.55.207.126': 2, '82.34.9.20': 2,
    '65.55.106.155': 2, '65.55.207.77': 2, '208.80.193.28': 1, '89.248.172.58': 22,
    '67.195.112.35': 16, '65.55.207.50': 3, '65.55.215.75': 2
}

# Sort the dictionary by value (frequency of the IP or key) using lambda
sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)

# Get the maximum frequency value
max_count = sorted_d[0][1]     #sorted_d[0]=====('66.249.65.38', 100)

print(f"Maximum count of records: {max_count}")
#('66.249.65.38', 100)
#100

##############################################################
def read_log():
    records = []
    with open(r'sample.log','r')as f:
        for line in f:
            clean_line = line.strip()  # to remove the leading and trailing spaces
            if clean_line:    # to remove the empty line
                word = clean_line.split()[2]
                records.append(word)
    return records
print(read_log())

def message_count():
    data = read_log()
    return {item:data.count(item)for item in data}

print(message_count())

def point():
    records = []
    with open(r'points.txt','r') as obj:
        for line in obj:
            clean_line = line.strip()
            if clean_line:
                word = clean_line.split()
                convert = [float(i) for i in word]
                records.append(convert)
    return records
print(point())

# min,max,avg
def minimum():
    data=point()
    X_min=min([item[0]for item in data])
    Y_min =min([item[1] for item in data])
    z_min = min([item[2] for item in data])
    return X_min,Y_min,z_min
print(minimum())

def maximum():
    data=point()
    X_max=max([item[0]for item in data])
    Y_max =max([item[1] for item in data])
    z_max = max([item[2] for item in data])
    return X_max,Y_max,z_max
print(maximum())

def average():
    data=point()
    X_axis=[item[0] for item in data]
    X_avg=(sum(X_axis)) / (len(X_axis))
    Y_axis = [item[1] for item in data]
    Y_avg = (sum(Y_axis)) / (len(Y_axis))
    Z_axis = [item[2] for item in data]
    Z_avg = (sum(Z_axis)) / (len(Z_axis))
    return X_avg,Y_avg,Z_avg
print(average())
##################################CSV######################################################



