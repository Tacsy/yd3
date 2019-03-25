##!/usr/bin/env python
#encoding:utf-8


import re
import sys
from urllib import request
from colored import fg, attr

colors = {
    'word'          : fg('green'),
    'soundmark'     : fg('yellow'),
    'definition'    : fg('blue'),
    'example'       : fg('cyan')
}

url = 'https://dict.youdao.com/w/eng/'

def search(word):
    global url
    site = url + word
    req = request.Request(site)
    response = request.urlopen(req)

    return response.read().decode('utf-8')

def getSoundmark(html):
    pa = re.compile('<span class="phonetic">(.*?)</span>')
    soundmark = pa.findall(html)

    return soundmark

def getDefinition(html):
    pa_container = re.compile('<div class="trans-container">.*?<ul>(.*?)</ul>.*?</div>', re.S)
    ma_container = pa_container.search(html)
    str_container = ''
    definition = []

    if ma_container:
        str_container = ma_container.group(1)
    else:
        pa_wordgroup = re.compile('<p class="wordGroup">(.*?)</p>', re.S)
        ma_wordgroup = pa_wordgroup.findall(str_container)
        pa_span = re.compile('<(span|a).*?>([^<^>]*?)</(span|a)>', re.S)
        for item in ma_wordgroup:
            ma_span = pa_span.findall(item)
            exi = ''
            for w in ma_span:
                if ('.' in w[1] and len(w[1]) <= 4):
                    exi += (w[1] + ' ' * (4-len(w[1])))
                else:
                    exi += w[1]
            definition.append(exi)

    return definition

def getExamples(html):
    examples = []
    pa_bilingual = re.compile('<div id="bilingual".*?>(.*?)</div>', re.S)
    pa_group = pa_bilingual.search(html)
    if pa_group:
        ma_bilingual = pa_group.group()
    else:
        return []
    pa_p = re.compile('<p>(.*?)</p>', re.S)
    ma_p = pa_p.findall(ma_bilingual)
    pa_span = re.compile('<span.*?>(.*?)</span>', re.S)
    for item in ma_p:
        ma_span = pa_span.findall(item)
        exi = ''
        for w in ma_span:
            exi += w
        exi = re.sub('<.?\w>', '', exi)
        examples.append(exi)

    return examples

def main():
    word = sys.argv[1]



if __name__ == '__main__':
    main()

