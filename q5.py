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




def ex5(text):

    copyText=list(text)
    counter=0
    result=multiply_polynomials(copyText,copyText)
    for num in result:
        if(num%2==1 and 3<=num):
            counter+=(num-1)/2
    return counter

    

def main():
    poly1 = [1,1,1,1,0,0,1]
    result = ex5(poly1)
    print("result = ", result)


if __name__ == "__main__":
    # Check if the script is being run directly
    main()
