def decimalToBinary(ip_val):
    if ip_val >= 1:
    # recursive function call
        decimalToBinary(ip_val // 2)
    
    # printing remainder from each function call
    print(ip_val % 2, end = '')
 
# Driver Code
if __name__ == '__main__':
    # decimal value
    ip_val = int(input())
     
    # Calling special function
    decimalToBinary(ip_val)
