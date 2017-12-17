# -*- coding:utf-8 -*-
import os
import time
import pymongo
from whoosh.fields import Schema, TEXT, ID, KEYWORD, DATETIME
from jieba.analyse import ChineseAnalyzer
from whoosh.index import create_in, open_dir
from bson.objectid import ObjectId
import jieba
jieba.load_userdict("dict.txt")
from whoosh.qparser import MultifieldParser, QueryParser
from whoosh import scoring, sorting
from datetime import datetime
from collections import Counter
analyzer = ChineseAnalyzer()


schema = Schema(
            nid=ID(unique=True, stored=True),
            url=ID(unique=True, stored=False),
            date=DATETIME(unique=False, stored=False, sortable=True),
            title=TEXT(stored=False, analyzer=analyzer),
            content=TEXT(stored=False, analyzer=analyzer)
        )

client = pymongo.MongoClient("xxx")
db = client['xxx']
collections = db['xxx']

if not os.path.exists('D:/pythonCode/whoosh/index/'):
    os.mkdir("D:/pythonCode/whoosh/index/")
    create_in("D:/pythonCode/whoosh/index/", schema)

ix = open_dir("D:/pythonCode/whoosh/index/")

# 追加排序
# with ix.writer() as w:
#     sorting.add_sortable(w, "date", sorting.FieldFacet("date"))

counts = 0

# for one in collections.find({}):
#     with ix.writer() as writer:
#         print(one)
#         writer.update_document(
#             nid=one['_id'].__str__(),
#             url=one['url'],
#             title=one['title'],
#             date=datetime.strptime(one['date'],'%Y-%m-%d'),
#             # tags=",".join(one['tags']),
#             content=one['index_content']
#         )
#         counts += 1
#         if counts == 200:
#             break



count = 0
start = time.time()
with ix.searcher(weighting=scoring.BM25F()) as searcher:
    query = MultifieldParser(["title", "content"], ix.schema).parse("xss")
    #query = QueryParser("content", ix.schema).parse("xss")

    mf = sorting.MultiFacet()
    mf.add_field("date", reverse=True)

    results = searcher.search(query, limit=10, sortedby=mf)
    #results = searcher.search_page(query, 2, pagelen=10)
    #print(results)
    print(len(results))
    #results = results[-10:]

    for one in results:
        # print(one['content'])
        # print(one.highlights("content"))
        _id = ObjectId(one['nid'])
        res = collections.find({'_id':_id})[0]
        print(res['date'] + res['title'])
        print('-----------------------\n')
        count += 1

    # keywords = [keyword for keyword, score in results.key_terms("content", docs=10, numterms=5)]
    # print(keywords)
end = time.time()
print(end - start)
print(count)

# 6
