
heights_str = input("Input all student's height  ").split()

total = 0
''' ver1
for height in heights_str:
    total += int(height)
'''
#heights = []
for i in range(0, len(heights_str)):
    heights_str[i] = int(heights_str[i])
for height in heights_str:
    total += height

total /= len(heights_str)
avg = round(total)
print(f"Average height is {avg}")