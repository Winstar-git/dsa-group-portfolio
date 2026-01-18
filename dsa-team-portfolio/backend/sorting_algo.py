# Goal: Finish raw python code for sorting algorithms
# Bubble sort
print("Bubble Sort Steps:")
class BubbleSort:

    def __init__(self, data):
        self.original = data.copy()
        self.data = data
        self.steps = []

    def sort(self):
        n = len(self.data)

        for i in range(n):
            for j in range(0, n - i - 1):

                self.steps.append({
                    "action": "compare",
                    "indices": [j, j + 1],
                    "array": self.data.copy()
                })

                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]

                    self.steps.append({
                        "action": "swap",
                        "indices": [j, j + 1],
                        "array": self.data.copy()
                    })

        return {
            "algorithm": "Bubble Sort",
            "original": self.original,
            "steps": self.steps,
            "sorted": self.data
        }

numbers = [5, 3, 8, 4, 1]
sorter = BubbleSort(numbers)
result = sorter.sort()

def format_array(array):
    width = max(len(str(x)) for x in array)
    return " | ".join(f"{x:>{width}}" for x in array)

print("Original:", result["original"])
for step in result["steps"]:
    print(f"{step['action'].capitalize():<8} | Indices: {step['indices']} | {format_array(step['array'])}")
print("Sorted:", result["sorted"])


# Selection sort
print("Selection Sort Steps:")
class SelectionSort:

    def __init__(self, data):
        self.original = data.copy()
        self.data = data
        self.steps = []

    def sort(self):
        n = len(self.data)

        for i in range(n):
            min_index = i

            for j in range(i + 1, n):
                self.steps.append({
                    "action": "compare",
                    "indices": [min_index, j],
                    "array": self.data.copy()
                })

                if self.data[j] < self.data[min_index]:
                    min_index = j

            if min_index != i:
                self.data[i], self.data[min_index] = self.data[min_index], self.data[i]

                self.steps.append({
                    "action": "swap",
                    "indices": [i, min_index],
                    "array": self.data.copy()
                })

        return {
            "algorithm": "Selection Sort",
            "original": self.original,
            "steps": self.steps,
            "sorted": self.data
        }

numbers = [5, 3, 8, 4, 1]
sorter = SelectionSort(numbers)
result = sorter.sort()

def format_array(array):
    width = max(len(str(x)) for x in array)
    return " | ".join(f"{x:>{width}}" for x in array)

print("Original:", result["original"])
for step in result["steps"]:
    print(f"{step['action'].capitalize():<8} | Indices: {step['indices']} | {format_array(step['array'])}")
print("Sorted:", result["sorted"])

# Insertion sort
print("Insertion Sort Steps:")
class InsertionSort:

    def __init__(self, data):
        self.original = data.copy()
        self.data = data
        self.steps = []

    def sort(self):
        n = len(self.data)

        for i in range(1, n):
            key = self.data[i]
            j = i - 1

            while j >= 0 and self.data[j] > key:
                self.steps.append({
                    "action": "compare",
                    "indices": [j, j + 1],
                    "array": self.data.copy()
                })

                self.data[j + 1] = self.data[j]

                self.steps.append({
                    "action": "shift",
                    "indices": [j, j + 1],
                    "array": self.data.copy()
                })

                j -= 1

            self.data[j + 1] = key

            self.steps.append({
                "action": "insert",
                "indices": [j + 1],
                "array": self.data.copy()
            })

        return {
            "algorithm": "Insertion Sort",
            "original": self.original,
            "steps": self.steps,
            "sorted": self.data
        }
    
numbers = [5, 3, 8, 4, 1]
sorter = InsertionSort(numbers)
result = sorter.sort()

def format_array(array):
    width = max(len(str(x)) for x in array)
    return " | ".join(f"{x:>{width}}" for x in array)

print("Original:", result["original"])
for step in result["steps"]:
    print(f"{step['action'].capitalize():<8} | Indices: {step['indices']} | {format_array(step['array'])}")
print("Sorted:", result["sorted"])

# Merge sort
print("Merge Sort Steps:")
class MergeSort:

    def __init__(self, data):
        self.original = data.copy()
        self.data = data.copy()
        self.steps = []

    def sort(self):
        self.data = self._merge_sort(self.data)
        return {
            "algorithm": "Merge Sort",
            "original": self.original,
            "steps": self.steps,
            "sorted": self.data
        }

    def _merge_sort(self, array):
        if len(array) <= 1:
            return array

        mid = len(array) // 2
        left = self._merge_sort(array[:mid])
        right = self._merge_sort(array[mid:])

        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            self.steps.append({
                "action": "compare",
                "indices": [i, j],
                "array": merged + left[i:] + right[j:],
            })

            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        while i < len(left):
            merged.append(left[i])
            i += 1
        while j < len(right):
            merged.append(right[j])
            j += 1

        self.steps.append({
            "action": "merge",
            "indices": list(range(len(merged))),
            "array": merged.copy()
        })

        return merged

numbers = [5, 3, 8, 4, 1]
sorter = MergeSort(numbers)
result = sorter.sort()

def format_array(array):
    width = max(len(str(x)) for x in array)
    return " | ".join(f"{x:>{width}}" for x in array)

print("Original:", result["original"])
for step in result["steps"]:
    print(f"{step['action'].capitalize():<8} | Indices: {step.get('indices', [])} | {format_array(step['array'])}")
print("Sorted:", result["sorted"])

# Quick sort
print("Quick Sort Steps:")
class QuickSort:

    def __init__(self, data):
        self.original = data.copy()
        self.data = data
        self.steps = []

    def sort(self):
        self.data = self._quick_sort(self.data, 0, len(self.data) - 1)
        return {
            "algorithm": "Quick Sort",
            "original": self.original,
            "steps": self.steps,
            "sorted": self.data
        }

    def _quick_sort(self, array, low, high):
        if low < high:
            pi = self._partition(array, low, high)
            self._quick_sort(array, low, pi - 1)
            self._quick_sort(array, pi + 1, high)
        return array

    def _partition(self, array, low, high):
        pivot = array[high]
        i = low - 1

        for j in range(low, high):
            self.steps.append({
                "action": "compare",
                "indices": [j, high],
                "array": array.copy(),
                "pivot": pivot
            })

            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
                self.steps.append({
                    "action": "swap",
                    "indices": [i, j],
                    "array": array.copy(),
                    "pivot": pivot
                })

        array[i + 1], array[high] = array[high], array[i + 1]
        self.steps.append({
            "action": "swap",
            "indices": [i + 1, high],
            "array": array.copy(),
            "pivot": pivot
        })

        return i + 1

numbers = [5, 3, 8, 4, 1]
sorter = QuickSort(numbers)
result = sorter.sort()

def format_array(array):
    width = max(len(str(x)) for x in array)
    return " | ".join(f"{x:>{width}}" for x in array)

print("Original:", result["original"])
for step in result["steps"]:
    indices = step.get('indices', [])
    pivot = step.get('pivot', None)
    pivot_info = f" | Pivot: {pivot}" if pivot is not None else ""
    print(f"{step['action'].capitalize():<8} | Indices: {indices}{pivot_info} | {format_array(step['array'])}")
print("Sorted:", result["sorted"])
