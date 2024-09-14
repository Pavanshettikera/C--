n=10
if n>0:
    print("positiove")
else:
    print("Negative")
    
n=10
if n%2==0:
    print("even")
else:
    print("odd")
    
n=100
sum=0
for i in range(n+1):
    sum+=i
print(sum)

n1=10
n2=100
sum=0
for i in range(n1,n2+1):
    sum+=i
print(sum)

year=100
if (year%400==0) and (year%4==0 or year%100!=0):
    print("leap year")
else:
    print("Not leap year")
    
def prime_number(n,i=2):
    if n==i:
        return True
    elif n%i==0:
        return False
    return prime_number(n,i+1)
n=13
if prime_number(n):
    print("prime")
else:
    print("not prime number")
    
start=10
end=100
primes=[]
for i in range(start,end+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            primes.append(i)
print(primes)

def prime(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=13
print(prime(n))

number=12345
sum=0
for i in str(number):
    sum+=int(i)
print(sum)

def reverse(s):
    temp=s
    reverse=0
    while temp>0:
        remainder=temp%10
        reverse=(reverse*10)+remainder
        temp//=10
    return reverse
s=12345
print(reverse(s))

def reverse_string(string):
    reversed_string=""
    for i in string:
        reversed_string=i+reversed_string
    return reversed_string
string='pavan'
print(reverse_string(string))

def is_palindrome(s):
    temp=s
    reverse=0
    while temp>0:
        remainder=temp%10
        reverse=(reverse*10)+remainder
        temp//=10
    if (s==reverse):
        print("palindrome")
    else:
        print("Not palindrome")
s=1234321
print(is_palindrome(s))

def palindrome(s):
    left=0
    right=len(s)-1
    while left<=right:
        mid=(left+right)//2
        if not s[left].isalnum():
            left+=1
        elif not s[right].isalnum():
            right-=1
        elif s[left].lower()!=s[right].lower():
            return False
        else:
            left+=1
            right-=1
    return True
s='pavanavap'
if palindrome(s):
    print("aplindrome string")
else:
    print("not palindrome string")
    
def armstrong_number(number):
    original_number=number
    sum_of_digits=0
    num_digits=len(str(number))
    while number>0:
        remainder=number%10
        sum_of_digits+=remainder**num_digits
        number//=10
    return sum_of_digits==original_number
number=153
if armstrong_number(number):
    print("armstrong number")
else:
    print("not armstrong numbwr")
    
def fibanocci(s):
    fib_seq=[0,1]
    if n<=1:
        return fib_seq[:n+1]
    for i in range(2,n+1):
        fib_seq.append(fib_seq[i-1]+fib_seq[i-2])
    return fib_seq
n=10
print(fibanocci(n))

def factorial_iterative(s):
    result=1
    for i in range(1,s+1):
        result*=i
    return result
s=5
print(factorial_iterative(s))

def power(a,b):
    if b!=0:
        return a*power(a,b-1)
    else:
        return 1
a=2
b=2
print(power(a,b))

def findMaxRec(arr,n):
    if n==1:
        return arr[0]
    else:
        return max(arr[n-1],findMaxRec(arr,n-1))
arr=[10,20,30,40,50]
n=len(arr)
print(findMaxRec(arr,n))

def findMinRec(arr,n):
    if n==1:
        return arr[0]
    else:
        return min(arr[n-1],findMinRec(arr,n-1))
arr=[10,20,30,40,50]
n=len(arr)
print(findMinRec(arr,n))

def reverse_array(arr):
    reverseed_arr=[]
    for i in arr:
        reverseed_arr=[i]+reverseed_arr
    return reverseed_arr
arr=[10,20,30]
print(reverse_array(arr))

def hcf(a,b):
    if b==0:
        return a
    else:
        return hcf(b,a%b)
def lcm(a,b):
    return (a*b)//hcf(a,b)
a=23
b=69
print(hcf(a,b))
print(lcm(a,b))

def calc_length(string):
    if string=="":
        return 1
    return 1+calc_length(string[1:])
string='pavan kumar'
print(calc_length(string))

def get_permutations(string):
    if len(string)<=1:
        return string
    perms=get_permutations(string[1:])
    char=string[0]
    result=[]
    for perm in perms:
        for i in range(len(perm)+1):
            result.append(perm[:i]+char+perm[i:])
    return result
string='pa'
print(get_permutations(string))

def recursive_delete(s):
    if len(s)<=1:
        return s
    i=1
    while i<len(s) and s[i]==s[i-1]:
        i+=1
    if i==1:
        return s[i]+recursive_delete(s[1:])
    else:
        return recursive_delete(s[0])
s='pavan'
print(recursive_delete(s))

def find_largest_element_in_arr(arr):
    if len(arr)<=1:
        return arr
    max_element=arr[0]
    min_element=arr[0]
    for i in range(len(arr)):
        if arr[i]>max_element:
            max_element=arr[i]
        if arr[i]<min_element:
            min_element=arr[i]
    return max_element,min_element
arr=[10,20,30,40,50,60]
print(find_largest_element_in_arr(arr))

def second_largest_elements(arr):
    if len(arr)<=1:
        return None, None
    first_largest=first_smallest=float('-inf')
    second_largest=second_smallest=float('inf')
    for num in arr:
        if num>first_largest:
            second_largest=first_largest
            first_largest=num
        elif num>second_largest and num!=first_largest:
            second_largest=num
        if num<first_smallest:
            second_smallest=first_smallest
            first_smallest=num
        elif num<second_smallest and num!=first_smallest:
            second_smallest=num
    return second_largest,second_smallest
arr=[10,20,30,40,50,60,70,80,90]
print(second_largest_elements(arr))

def reverse_arrayy(arr):
    start=0
    end=len(arr)-1
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
    return arr
arr=[10,20,30,40,50]
print(reverse_arrayy(arr))

def calculate_sum_of_the_array(arr):
    if len(arr)<=1:
        return arr
    sum=0
    for i in arr:
        sum+=i
    return sum
arr=[10,20,30,40,50]
print(calculate_sum_of_the_array(arr))

def printOrder(arr,n):
    n=len(arr)
    for i in range(n//2):
        print(arr[i],end=" ")
    for j in range(n-1,n//2-1,-1):
        print(arr[j],end=" ")
arr=[10,20,30,40,50]
n=len(arr)
print(arr,n)

def count_freq(arr,n):
    visited=[False for i in range(n)]
    for i in range(n):
        if (visited[i]==True):
            continue
        count=1
        for j in range(i+1,n,1):
            if (arr[i]==arr[j]):
                visited[j]=True
                count+=1
        print(arr[i],count)
arr=[10,20,30,40,50,60,10,20]
n=len(arr)
print(count_freq(arr,n))

def onother_way(arr,n):
    freq_dict={}
    for num in arr:
        if num in freq_dict:
            freq_dict[num]+=1
        else:
            freq_dict[num]=1
    for num, count in freq_dict.items():
        print(num, count)
arr=[10,20,30,40,50,60]
n=len(arr)
print(onother_way(arr,n))

def find_palindrome(arr):
    if len(arr)<=1:
        return arr
    left=0
    right=len(arr)-1
    while left<=right:
        if arr[left]!=arr[right]:
            return False
        left+=1
        right-=1
    return True
arr=[10,20,30,20,10]
is_palindrome=find_palindrome(arr)
print("Palindrome" if is_palindrome else "not palindrome")

def is_palindromee(s):
    original=s
    temp=s
    reverse=0
    while temp>0:
        remainder=temp%10
        reverse=(reverse*10)+remainder
        temp//=10
    return original==reverse

def find_longest_palindrome(arr):
    if len(arr)<=1:
        return arr
    longest_palindrome=None
    for num in arr:
        if is_palindromee(num):
            if longest_palindrome is None or len(str(num))>len(str(longest_palindrome)):
                longest_palindrome=num
    return longest_palindrome
arr=[101,1001,10001,121,1012]
print(find_longest_palindrome(arr))

def find_repeating_elements(arr,n):
    visited=[False for i in range(n)]
    for i in range(n):
        if (visited[i]==True):
            continue
        count=1
        for j in range(i+1,n,1):
            if (arr[i]==arr[j]):
                visited[j]=True
                count+=1
        if count!=1:
            print(arr[i],end=" ")
arr=[10,20,30,40,10,20]
n=len(arr)
print(find_repeating_elements(arr,n))

def find_non_repeating_element(arr,n):
    visited=[False for i in range(n)]
    for i in range(n):
        if (visited[i]==True):
            continue
        count=1
        for j in range(i+1,n,1):
            if (arr[i]==arr[j]):
                visited[j]=True
                count+=1
        if count==1:
            print(arr[i],end=" ")
arr=[10,20,30,40,40,50,60]
n=len(arr)
print(find_non_repeating_element(arr,n))

def find_repe(arr):
    if len(arr)<=1:
        return arr
    seen=set()
    repeated=[]
    for element in arr:
        if element in seen:
            repeated.append(element)
        else:
            seen.add(element)
    return list(repeated)
arr=[10,20,30,40,50,10,20]
print(find_repe(arr))

def find_non_repe(arr):
    if len(arr)<=1:
        return arr
    seen=set()
    repeated=[]
    for element in arr:
        if element in seen:
            repeated.append(element)
        else:
            seen.add(element)
    non_repeated=[element for element in arr if element not in repeated]
    return non_repeated
arr=[10,20,30,40,50,10,20]
print(find_non_repe(arr))

def remove_duplicates(arr):
    if len(arr)<=1:
        return arr
    seen=set()
    result=[]
    for element in arr:
        if element not in seen:
            result.append(element)
            seen.add(element)
    return result
arr=[10,20,30,40,50,10,20]
print(remove_duplicates(arr))

def kadane(arr):
    max_so_far=float('-inf')
    max_ending_here=0
    for x in arr:
        max_ending_here=max(x, max_ending_here+x)
        max_so_far=max(max_so_far,max_ending_here)
    return max_so_far
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print(kadane(arr))

def merge_two_array(arr1, arr2,n1,n2):
    for i in arr2:
        arr1.append(i)
    arr1=list(set(sorted(arr1)))
    arr2=arr1[len(arr1)-n2:]
    arr1=arr1[:len(arr2)-n2]
    print(arr1, "\n", arr2)
arr1 = [1, 2, 3, 5, 8, 9, 10, 13, 15, 20]
arr2 = [2, 3, 8, 13]
merge_two_array(arr1,arr2, len(arr1), len(arr2))
    