
array1 = [
'https://leetcode.com/problems/top-k-frequent-elements',
'https://leetcode.com/problems/merge-k-sorted-lists'
]

array2 = [
'https://leetcode.com/problems/subsets',
'https://leetcode.com/problems/permutations',
'https://leetcode.com/problems/combinations',
'https://leetcode.com/problems/generate-parentheses',
'https://leetcode.com/problems/gray-code'
]

array3 = [
'https://leetcode.com/problems/combination-sum',
'https://leetcode.com/problems/partition-equal-subset-sum',
'https://leetcode.com/problems/partition-to-k-equal-sum-subsets',
'https://leetcode.com/problems/sudoku-solver'
]

def create_links(array: [str]) -> str:
    print("\nArray:")
    for link in array:
        print('<a href="{link}"></a><br>'.format(link=link))
    print('end array')


if __name__ == "__main__":
    create_links(array1)
    create_links(array2)
    create_links(array3)
