def build_heap(data):
    n = len(data)
    swaps = []
    for i in range((n-1)//2, -1, -1):
        j = i
        while True:
            k = 2*j + 1
            if k >= n:
                break
            if k+1 < n and data[k+1] < data[k]:
                k += 1
            if data[k] < data[j]:
                data[j], data[k] = data[k], data[j]
                swaps.append((j, k))
                j = k
            else:
                break
    return swaps

def heap_sort(data):
    swaps = build_heap(data)
    n = len(data)
    for i in range(n-1, 0, -1):
        data[0], data[i] = data[i], data[0]
        j = 0
        while True:
            k = 2*j + 1
            if k >= i:
                break
            if k+1 < i and data[k+1] < data[k]:
                k += 1
            if data[k] < data[j]:
                data[j], data[k] = data[k], data[j]
                swaps.append((j, k))
                j = k
            else:
                break
    return swaps
def main():
    source = input().strip()
    if source == "I":
        n = input()
    elif source == "F":
        file_name = input().strip()
        if "a" in file_name:
            sys.exit()
        try:
            with open(file_name, "r") as file:
                n = int(file.readline().strip())
                parents = list(map(int, file.readline().strip().split()))
        except FileNotFoundError:
            sys.exit()
    else:
        sys.exit()
        
    data = list(map(int, input().split()))
    swaps = heap_sort(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

        
if __name__ == "__main__":
    main()
