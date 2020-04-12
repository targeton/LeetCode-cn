# update files's information of floder(.\Solutions)
import os
import re

_dir = "./Solutions/"
_txt = "./README.md"
_HyperLink_Pattern = r"((http|ftp|https)://)(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,4})*(/[a-zA-Z0-9\&%_\./-~-]*)?"
_Language_Pattern = r"lang=.*"
_Level_Pattern = r"(Easy|Medium|Hard)"

_HYPERLINK_TEMPLE = "[%s](%s)"
_LINK_TEMPLE = "[%s](./Solutions/%s)"
_ROW_TEMPLE = "%s|%s|%s"
_README_TEMPLE = """
# LeetCode-CN Solutions
Solved problems of [LeetCode](https://leetcode-cn.com/problemset/all/)

All(%d)  Easy(%d)  Medium(%d)  Hard(%d)

Problem|Solution|Level
:---|:---:|:---:
%s
"""

def update():
    dic = {}
    counter = [0,0,0]
    posDic = {'Easy':0, 'Medium':1, 'Hard':2}
    for file_name in os.listdir(_dir):
        tmp = file_name.split('.')
        k = tmp[0]
        with open(os.path.join(_dir,file_name),'r',encoding='utf-8') as f:
            content = f.read()
            result = re.search(_HyperLink_Pattern, content)
            row1 = _HYPERLINK_TEMPLE % (k+'.'+tmp[1], content[result.start():result.end()])
            result = re.search(_Language_Pattern, content)
            row2 = _LINK_TEMPLE % (content[result.start():result.end()][5:], file_name)
            result = re.search(_Level_Pattern, content)
            row3 = content[result.start():result.end()]
            if k in dic:
                dic[k][1].append(row2)
            else:
                dic[k] = [row1,[row2],row3]
                counter[posDic[row3]] += 1
    lst = [_ROW_TEMPLE % (x[1][0], ' '.join(x[1][1]), x[1][2]) for x in sorted(dic.items(), key=lambda item: int(item[0]))]
    write_content = _README_TEMPLE % (sum(counter), counter[0], counter[1], counter[2], "\n".join(lst))
    with open('./README.md','w',encoding='utf-8') as f:
        f.write(write_content)

if __name__ == "__main__":
    update()