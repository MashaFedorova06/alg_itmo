import psutil
import time

t_start = time.perf_counter()
with open ("input.txt","r") as file:
    n= int(file.readline())
    s=[i for i in file.readline()]
def palindrome(n, s):
    dict = {}
    for letter in s:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
    half_palindrome = []
    center_char = ''
    for char in sorted(dict.keys()): 
        count = dict[char]
        half_palindrome.append(char * (count // 2))
        if count % 2 == 1 and (center_char == '' or char < center_char):
            center_char = char
    left_half = ''.join(half_palindrome)
    palindrome_result = left_half + center_char + left_half[::-1]
    return palindrome_result
with open("output.txt","w") as file:
        str_palindrome=palindrome(n,s)
        file.write(str_palindrome)
print ("Время работы: %s секунд " % (time.perf_counter () - t_start))
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")




