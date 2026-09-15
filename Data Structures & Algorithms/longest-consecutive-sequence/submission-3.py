class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set=set(nums)
        max_len=0
        for i in range(len(nums)):
            current_sum=0
            if nums[i]-1 not in num_set:
                num=nums[i]
                while num in num_set:
                    current_sum+=1
                    num += 1
                max_len=max(max_len, current_sum)
        return max_len

                

        # hashmap = defaultdict(list)
        # index=0
        # for i in range(len(nums)):
        #     hashmap[nums[i]]=i
        # for i in range(len(nums)):
        #     while nums[i]-1 not in hashmap:
        #         index=hashmap(num[i]-1).value()

        