'''
 * Reto #39
 * TOP ALGORITMOS: QUICK SORT
 * Fecha publicación enunciado: 27/09/22
 * Fecha publicación resolución: 03/10/22
 * Dificultad: MEDIA
 *
 * Enunciado: Implementa uno de los algoritmos de ordenación más famosos: el "Quick Sort",
 * creado por C.A.R. Hoare.
 * - Entender el funcionamiento de los algoritmos más utilizados de la historia nos ayuda a
 *   mejorar nuestro conocimiento sobre ingeniería de software. Dedícale tiempo a entenderlo,
 *   no únicamente a copiar su implementación.
 * - Esta es una nueva serie de retos llamada "TOP ALGORITMOS", donde trabajaremos y entenderemos
 *   los más famosos de la historia.
'''

'''
PSEUDO CODE: QUICK SORT
// low  --> Starting index,
// high  --> Ending index
quickSort(arr[], low, high) {

  // Till starting index is lesser than ending index
  if (low < high) {

    // pi is partitioning index,
    // arr[p] is now at right place
    pi = partition(arr, low, high);

    // Before pi
    quickSort(arr, low, pi - 1);
    // After pi
    quickSort(arr, pi + 1, high);
  }
}
'''

# Function to find the partition position
def partition(array, low, high):
 
    # choose the rightmost element as pivot
    pivot = array[high]
 
    # pointer for greater element
    i = low - 1
 
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 
# function to perform quicksort
 
 
def quick_sort(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
 
        # Recursive call on the left of pivot
        quick_sort(array, low, pi - 1)
 
        # Recursive call on the right of pivot
        quick_sort(array, pi + 1, high)


data = [9,5,4,3,7,8,2,6,5,8,4,3,1,8,0,3]

print("Unsorted:")
print(data)

quick_sort(data, 0, len(data) - 1)

print("Sorted:")
print(data)