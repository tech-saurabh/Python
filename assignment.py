Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def rotatelist(l,k):
    li = len(l)
    k = k % li
    ans = l[li-k:] + l[:li-k]
    return ans
