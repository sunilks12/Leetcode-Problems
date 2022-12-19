# -*- coding: utf-8 -*-


def indices_sum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target: 
             return[i,j]

indices_sum(nums=np.array([1,2,5]),target=7)

