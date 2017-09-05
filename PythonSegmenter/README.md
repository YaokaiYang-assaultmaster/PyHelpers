# PySegmenter      
This model is used for segmenting various kinds of object in Python.

***

1. `list_segment` is used for segmenting a list or tuple.    
2. `dict_segment` is used for segmenting a dictionary.     
3. `file_segment` is used for segmenting a file-like object with a buildin `read` attribute.     
4. `general_segment` is used for segmenting a general iterable object.    
5. `safe_segment` is used for segmenting something without raising an error. It will returns empty result based on given input.

All of the segmenting functions run within `O(n)` time.     