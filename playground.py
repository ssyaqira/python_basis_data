# my_tuple = (1, 'polban', 3.14)


# my_tuple[0] = 2
# print(my_tuple[0])

my_list = [1,2,3, 'string']
my_list [-1] = 9999
print(my_list[-1])

#jika diatas salah tapi code dibawah tetap mau dieksekusi

try:
    print(my_list[999])
except(Exception) as error:
    print("ada exception atau error")


my_dict = {
    "nama": "adit",
    "gender": "L",
    "no_tlp": 8123
}

my_dict['nama'] = 'ridha'

print(my_dict['nama'])

#dictonary
my_dict['is_active'] = True
print(my_dict)