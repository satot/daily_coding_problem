import heapq

def merge(lists):
    merged_list = []
    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst] # first element must be element of lst
    heapq.heapify(heap) # destructive

    while heap:
        print heap
        val, list_idx, element_idx = heapq.heappop(heap) # get minimum val
        merged_list.append(val)
        if element_idx + 1 < len(lists[list_idx]):
            next_tuple = (lists[list_idx][element_idx + 1],
                          list_idx,
                          element_idx + 1)
            heapq.heappush(heap, next_tuple)
    return merged_list

ls = [[10, 15, 30], [12, 15, 20], [17, 20, 32]]
print ls
print merge(ls)
