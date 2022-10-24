frame = input("Enter the frame received : ")
crc = input("Enter the polynomial : ")
decoded=frame
i = 0
while crc[i]!='1':
	i+=1
crc = crc[i:]
for i in range(len(frame)):
	if decoded[i]=='1':
		j=i
		k=0
		while(k<len(crc)):
			if crc[k] == decoded[j]:
				decoded = decoded[:j]+'0'+decoded[j+1:]
			else:
				decoded = decoded[:j]+'1'+decoded[j+1:]
			k+=1
			j+=1
if '1' in decoded:
	print("error")
else:
	print("correct")