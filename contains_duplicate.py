from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
            
def main():
    test_list = [1, 3, 2, 4, 5, 7, 0]
    solution = Solution()
    print(solution.containsDuplicate(test_list))

if __name__ == "__main__":
    main()