import re

my_string = "<li class=aa><img src=bb><br/>아무 태그도 없는 텍스트<br/><em>em태그 텍스트</em></li><li class=aa><span>span텍스트</span><br/>아무 태그도 없는 텍스트</li>"

filt = re.compile('(<[^>]+>[^<]+</[^>]+>)')

hello = filt.sub('',my_string)
# filt2 = re.compile('(</[^>]+>)')
# hello = filt2.sub('', hello)
print(hello)