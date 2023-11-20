def merge_arrays(array1, array2):
    result = []
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] <= array2[j]:
            result.append(array1[i])            
            i+=1
        else:
            result.append(array2[j])            
            j+=1
    
    result.extend(array1[i:])
    result.extend(array2[j:])
    return result

# Variante simple usando la función sorted()
def merge_arrays1(array1, array2):      
    result = array1+array2
    return sorted(result)


