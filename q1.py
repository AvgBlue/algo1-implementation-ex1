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



def ex1(text,pattern):
    copyPattern0=list(pattern)
    copyPattern1=list(pattern)
    copyPattern2=list(pattern)

    copyPattern0.reverse()
    copyPattern1.reverse()
    copyPattern2.reverse()

    copyText0=list(text)
    copyText1=list(text)
    copyText2=list(text)

    copyPattern0=swapTo1(copyPattern0,0)
    copyText0=swapTo1(copyText0,0)

    copyPattern1=swapTo1(copyPattern1,1)
    copyText1=swapTo1(copyText1,1)

    copyPattern2=swapTo1(copyPattern2,2)
    copyText2=swapTo1(copyText2,2)

    result0 = multiply_polynomials(copyPattern0,copyText0)
    result1 = multiply_polynomials(copyPattern1,copyText1)
    result2 = multiply_polynomials(copyPattern2,copyText2)
    

    result=add_arrays(result0,add_arrays(result1,result2))
    returnResult=[]
    for i in range(len(result)):
        if(result[i]==len(pattern)):
            returnResult.append(i-len(pattern)+1)
    return returnResult

    


    
        

def main():
	poly1 = [1, 2,0,2,1,1,2,1,1,1]
	poly2 = [2,1]
	poly3 = ex1(poly1,poly2)
	print(poly3)


if __name__ == "__main__":
    # Check if the script is being run directly
    main()
