# in any unknown range.
# Here we will use the unordered map to maintain a frequency count of all elements and return the ones with frequency>1

def find_duplicates(arr):
    freq = {} # use a dictionary to store frequency values
    for i in range(len(arr)):
        try:
            freq[arr[i]]+=1
        except:
            freq[arr[i]] = 1
    duplicates = [item for item in freq if freq[item]>1]
    return duplicates
