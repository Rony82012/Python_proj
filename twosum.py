def twosum(nums,target):
	for i in range(len(nums)):
		d = target - nums[i]
		if d in nums and i != nums.index(d):
			print([i,nums.index(d)])
			

twosum([2,7,11,13], 9)

