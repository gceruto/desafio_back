function merge(array1, array2)
{
    let result = [];  
    while (array1.length && array2.length) {
      if (array1[0] < array2[0])
        result.push(array1.shift());
      else
        result.push(array2.shift());
    };      
    return [...result, ...array1, ...array2];
  }
  
  function mergeSort(array)
  {
    if (array.length <= 1)
        return array;
    let mid = Math.floor(array.length / 2),
        left = mergeSort(array.slice(0, mid)),
        right = mergeSort(array.slice(mid));
  
    return merge(left, right); 
  };
