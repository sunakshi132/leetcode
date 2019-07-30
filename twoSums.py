def twoSums(nums, target):
    hash_map={}
    for i in range(len(nums)):
        j = target - nums[i]
        if j in hash_map.keys():
            return hash_map[j],i
        hash_map[nums[i]] = i