# TIME TAKEN:

def binary_search_find_median(array1,array2):
    if len(array1) > len(array2):
        array1 , array2 = array2, array1
    
    m, n = len(array1), len(array2)
    low, high = 0, m
    i = 1
    while low <= high:
        print(f"iteration{i}:")
        partitionX = (low + high) // 2
        partitionY = (m + n + 1) // 2 - partitionX
        
        maxX = float('-inf') if partitionX == 0 else array1[partitionX - 1]
        minX = float('inf') if partitionX == m else array1[partitionX]
        
        maxY = float('-inf') if partitionY == 0 else array2[partitionY - 1]
        minY = float('inf') if partitionY == n else array2[partitionY]
    
        if maxX <= minY and maxY <= minX:
           
            if (m + n) % 2 == 1:
                return max(maxX, maxY)
            
            else:
                return (max(maxX, maxY) + min(minX, minY)) / 2
        elif maxX > minY:
            # Move left in nums1
            high = partitionX - 1
        else:
            # Move right in nums1
            low = partitionX + 1

        i+=1
    
def insert_into_array(prompt):
    while True:
        try:
            array = input(prompt).split()
            if not array:
                print("Input cannot be empty! Please enter at least one number.")
                continue
            array = [int(x) for x in array]
            return array
        except ValueError:
            print("Invalid input! Please enter numbers only.")
if __name__ == "__main__":
    array1 = sorted(insert_into_array("Enter the first array (numbers separated by spaces): "))
    array2 = sorted(insert_into_array("Enter the second array (numbers separated by spaces): "))
    
    print(f"the median is {binary_search_find_median(array1,array2)}")
    