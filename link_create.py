
array1 = [
'https://leetcode.com/problems/powx-n',
'https://leetcode.com/problems/best-time-to-buy-and-sell-stock',
'https://leetcode.com/problems/edit-distance',
'https://leetcode.com/problems/house-robber-ii',
'https://leetcode.com/problems/regular-expression-matching/'
]

array2 = [
'https://leetcode.com/problems/best-time-to-buy-and-sell-stock',
'https://leetcode.com/problems/edit-distance',
'https://leetcode.com/problems/house-robber-ii',
'https://leetcode.com/problems/regular-expression-matching/'
]

array3 = [

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
