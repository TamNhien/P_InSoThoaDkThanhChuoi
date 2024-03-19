# Tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5 trong đoạn từ 2000 đến 3200
result = [str(x) for x in range(2000, 3201) if x % 7 == 0 and x % 5 != 0]

# In các số tìm được thành chuỗi trên một dòng, cách nhau bằng dấu phẩy
print(",".join(result))

