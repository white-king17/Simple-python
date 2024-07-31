class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:  #shelfwidth is max width of the shelf
        n=len(books)
        f=[0]*(n+1)
        for i , (w,h) in enumerate (books,1):   # w & h are the width and height of the books
            f[i]=f[i-1]+h
            for j in range (i-1,0,-1):
                w+=books[j-1][0]
                if w>shelfWidth:
                    break
                h=max(h,books[j-1][1])
                f[i]=min(f[i],f[j-1]+h)
        return f[n]