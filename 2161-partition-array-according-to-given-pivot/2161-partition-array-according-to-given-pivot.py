class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left_pivot = list()
        right_pivot = list()
        center_pivot = list()

        for a in nums:
            if a < pivot:
                left_pivot.append(a)
            elif a == pivot:
                center_pivot.append(a)
            else:
                right_pivot.append(a)
        
        left_pivot.extend(center_pivot)
        left_pivot.extend(right_pivot)
        return left_pivot