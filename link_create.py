
array1 = [
'https://leetcode.com/problems/distribute-candies/',
'https://leetcode.com/problems/groups-of-special-equivalent-strings/',
'https://leetcode.com/problems/intersection-of-two-arrays/',
'https://leetcode.com/problems/valid-sudoku/',
'https://leetcode.com/problems/isomorphic-strings/',
'https://leetcode.com/problems/word-pattern/',
'https://leetcode.com/problems/design-hashmap/',
'https://leetcode.com/problems/design-hashset/]'
]

array2 = [
'https://leetcode.com/problems/find-all-anagrams-in-a-string/',
'https://leetcode.com/problems/first-unique-character-in-a-string/',
'https://leetcode.com/problems/subdomain-visit-count/',
'https://leetcode.com/problems/find-the-difference/',
'https://leetcode.com/problems/most-common-word/',
'https://leetcode.com/problems/sort-characters-by-frequency/',
'https://leetcode.com/problems/set-mismatch/',
'https://leetcode.com/problems/number-of-atoms/'
]

array3 = [
'https://leetcode.com/problems/longest-word-in-dictionary',
'https://leetcode.com/problems/implement-trie-prefix-tree',
'https://leetcode.com/problems/word-search-ii'
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
