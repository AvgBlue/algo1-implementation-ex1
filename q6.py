import math

def add_arrays(arr1, arr2):
    # Get the lengths of the input arrays
    n1 = len(arr1)
    n2 = len(arr2)
    
    # Initialize an array to store the result
    result = []
    
    # Add the contents of the input arrays element-wise
    for i in range(max(n1, n2)):
        # If both arrays have elements at the current index, add them
        if i < n1 and i < n2:
            result.append(arr1[i] + arr2[i])
        # If only the first array has an element, add it
        elif i < n1:
            result.append(arr1[i])
        # If only the second array has an element, add it
        else:
            result.append(arr2[i])
    
    return result


def multiply_polynomials(poly1, poly2):
    # Get the lengths of the input arrays
    m = len(poly1)
    n = len(poly2)
    
    # Initialize an array to store the coefficients of the result polynomial
    result = [0] * (m + n - 1)
    
    # Multiply the coefficients of the polynomials
    for i in range(m):
        for j in range(n):
            result[i + j] += poly1[i] * poly2[j]
    
    return result

def swapTo1(arr, n):
    for i in range(len(arr)):
        if arr[i] == n:
            arr[i] = 1
        else:
            arr[i] = 0
    return arr

def swapTo3(arr, n):
    for i in range(len(arr)):
        if abs(arr[i]-n) <= 3:
            arr[i] = 1
        else:
            arr[i] = 0
    return arr




def ex6(text):
    copyText=list(text)
    if(len(copyText)==1):
        copyText[0]*=-1
        copyText.append(1)
        return copyText
    p1=ex6(copyText[0:math.ceil(len(copyText)/2):])
    p2=ex6(copyText[math.ceil(len(copyText)/2):len(copyText):])
    result=multiply_polynomials(p1,p2)
    return result
    

def main():
    poly1 = [-2,-1,0,1,2]
    result = ex6(poly1)
    print("result = ", result)


if __name__ == "__main__":
    # Check if the script is being run directly
    main()
