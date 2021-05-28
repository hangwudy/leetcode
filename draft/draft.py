a = [1, 2, 3, 4, 45, 56]
ad_list = []
for i in a:
    ad_list.append(id(i))

    print(id(i))

print(id(a[0]))
ad_list.remove(id(a[0]))
print(ad_list)
