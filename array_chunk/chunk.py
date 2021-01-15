from math import ceil


def chunk(ls, size):
    """Given an array and chunk size, divide the array into many subarrays
    where each subarray is of length size. (slices)"""
    chunks = []
    for i in range(0, len(ls), size):
        chunks.append(ls[i: i + size])

    return chunks


def chunk_option_1(ls, size):
    """Given an array and chunk size, divide the array into many subarrays
    where each subarray is of length size. (slice + list comprenhension)"""
    return [ls[i: i + size] for i in range(0, len(ls), size)]


def chunk_option_2(ls, size):
    """Given an array and chunk size, divide the array into many subarrays
    where each subarray is of length size. (for loop all items)"""
    chunks = [[]]
    for i in ls:
        last_chunk = chunks[-1]
        if len(last_chunk) == 0 | len(last_chunk) == size:
            chunks.append([i])
        else:
            chunks[-1].append(i)
    return chunks
