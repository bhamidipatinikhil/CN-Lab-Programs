crc = input("Enter the crc:: ")
msg = input("enter the message:: ")
encoded=""
red=""
i = 0
while crc[i]!='1':
	i+=1
crc = crc[i:]
encoded = msg
for i in range(len(crc)-1):
	encoded+='0'
print(encoded)
for i in range(len(msg)):
	if encoded[i]=='1':
		j=i
		k=0
		while(k<len(crc)):
			if crc[k] == encoded[j]:
				encoded = encoded[:j]+'0'+encoded[j+1:]
			else:
				encoded = encoded[:j]+'1'+encoded[j+1:]
			k+=1
			j+=1		
encoded = msg + encoded[len(msg):]
print(encoded)