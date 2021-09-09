# Quicksort

Parses an apache log file, counts the number of times a URL is seen - then uses quicksort to find the top 5 used URLS.

Quicksort, runs at worst O(n), at best O(n log n)

In total, this program parses the whole log at O(n), then does a quicksort of at worst O(n log n). In total this program runs at O(n)

```
806 /favicon.ico
546 /style2.css
538 /reset.css
533 /images/jordan-80.png
516 /images/web/2009/banner.png
9986
==============================
Quicksort Runtime: 0.04662132263183594  
Linear sort Runtime: 0.04684591293334961
```

## Edges

You can break things pretty badly by running the reset script, as the random function geneates uniqe keys it break after a lot of uniqe ones - the quicksort just cant handle it. 