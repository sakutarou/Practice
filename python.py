# -*- coding: utf-8 -*-
# 印字
print("Python test")

# 數字運算
x = 3**(3) # 次方
y = 3/7    # 小數結果
z = 3//7   # 商
w = 7%3    # 餘數
w += 1     # w = w+1
        
# 文字運算
w = 'hello \"' + "world" "!" "\nTo me" + """ I love
 the world."""
w = "hello"*3
y=w[2:11]
z=w[:4]

# 列表
z = [23,15,66,78,12]; z[0]=89;z[3:4]=[];z=z+[32,71]; y=len(z)
z = z + [33,[51,14,16]]; z[7][0:1]=[1,2,4,5]
tuple = (1,3,5) 不可變的列表

# 集合與字典的使用 the use of set and dictionary
s1 = {3,4,5};s2 = {3,5,6}; sand= s1&s2; scross = s1|s2
smin = s1 - s2; santi = s1 ^ s2; s = set("hello")
ans = 3 not in sand
d = {"a":"1","b":"鳳梨"}; dans = "b" in d; del d["a"]

# if 範例
# x = input("請輸入數字："); x = int(x);
# if x > 200: z = 'yes'
# elif x >= 100: z = 'ya'
# else: z = 'no'

# while for loop範例
# i=1
# while i<5:
#     i+=1
#for x in [1,4,2,"hello"]:
   # print(x)
#for y in "hello":
   # print(y)
# for z in range(3,8):
# #    if z==7:
# #        break
# #    if z==5:
# #        continue
# #    print(z)
#     x=z
# else:
#     x = x*2
# x = int(input("輸入正整數求平方根："))
# x = x**(1/2)

#def example
# def hello(name = "Jack"):
#     print("你好ㄚ！" + name)
# def divide(n1=0,n2=1):
#     return n1/n2
# print(divide(n2=2,n1=4))
# def say(*msg):
#     for m in msg:
#         print(m)

# say("hello","world")
# Module 使用
# import sys as s
# print(s.platform)
# print(s.maxsize)

# import sys
# sys.path.append("./module")
# print(sys.path)
# import module.geometry as geo
# print(geo.distance(0,0,3,4))

# file = open("data.txt",mode='w',encoding = "utf-8")
# file.write("hello")
# file.close()
# with open("math.txt",mode='w',encoding="utf-8") as file:
#    file.write("5\n6") 
# with open("data.txt",mode='r',encoding="utf-8") as file:
#    data=file.read()
# print(data)
# with open("math.txt",mode='r',encoding="utf-8") as file:
#    sum=0
#    for line in file:
#       sum += int(line)
#    print(sum)
# import json
# with open("config.json",mode="r") as file:
#    data = json.load(file)
# print("name:",data["Name"])
# data["Name"] = "Leo"
# with open("config.json",mode="w") as file:
#    json.dump(data,file)

# import random
# data = random.choice([1,5,7,8]);data = random.sample([1,5,7,8],3);
# random.shuffle(data)
# data = random.random();data = random.uniform(0,5)
# data = random.normalvariate(100,10)
# print(data)

# import statistics as sta
# d = sta.mean([1,4,6,9]); d=sta.median([1,4,7,9]);d=sta.stdev([1,1,7,12])
# import urllib.request as request
# import json
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context  
# src = "https://data.taipei/api/v1/dataset/c9286411-93cb-4b4b-98f3-d1a0ea241423?scope=resourceAquire"
# with request.urlopen(src) as response:
#    data = json.load(response)
#print(data)

# clist = data["result"]["results"]
# #print(clist)
# with open("data.txt","w",encoding="utf-8") as file:
#    for company in clist:
#       file.write(company["公司名稱"]+"\n")


# class IO:
#    name = ["Jack","Rose"]
#    def say(per):
#       print("Hello, " + per + "!")

# print(IO.name)
# IO.say("Jam")


# class Fullname:
#    def __init__(self,first,last):
#       self.fn = first
#       self.fl = last
#    def showname(self):
#       print(self.fn,self.fl)

# John = Fullname("John","white")
# Lisa = Fullname("Lisa","Rose")
# K = Fullname("Kevin")
# K.showname()

# class File:
#    def __init__(self,name):
#       self.name = name
#       self.file = None
#    def open(self):
#       self.file = open(self.name,"r",encoding="utf-8")
#    def read(self):
#       return self.file.read()

# f1 = File("math.txt")
# f1.open()
# print(f1.read())

# Web Crawler 
# import urllib.request as req
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context 
# url = "https://www.ptt.cc/bbs/movie/index.html"
# requ = req.Request(url,headers={"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15"
# })
# with req.urlopen(requ) as res:
#    data = res.read().decode("utf-8")
# #print(data)
# import bs4
# root = bs4.BeautifulSoup(data,"html.parser")
# #print(root.title)
# titles = root.find_all("div",class_="title")
# #print(titles)
# for title in titles:
#    if title.a != None:
#       print(title.a.string)
# with open("data.txt","w",encoding="utf-8") as file:
#    for title in titles:
#       if title.a != None:
#          file.write(title.a.string + "\n") 
   
      

# import urllib.request as req
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context 

# def getData(url):
#    requ = req.Request(url,headers={
#       "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
#       "cookie":"over18=1"
#    })
#    with req.urlopen(requ) as res:
#       data = res.read().decode("utf-8")
#    #print(data)
#    import bs4
#    root = bs4.BeautifulSoup(data,"html.parser")
#    #print(root.title)
#    titles = root.find_all("div",class_="title")
#    #print(titles)
#    for title in titles:
#       if title.a != None:
#          print(title.a.string)
#    nextLink = root.find("a",string="‹ 上頁")
#    return nextLink["href"]

# Pageurl = "https://www.ptt.cc/bbs/Gossiping/index.html"
# count = 0
# while count < 3:
#    Pageurl = "https://www.ptt.cc"+ getData(Pageurl)
#    count +=1

# import urllib.request as req
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context 
# url = "https://api.sosreader.com/api/hot-articles?from=2021-06-22T23:39:37&to=2021-06-23T23:39:37&lmt=20&num=5"
# request = req.Request(url,headers={
#    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15"
# })
# with req.urlopen(request) as response:
#    data = response.read().decode("utf-8")

# import json
# datas = json.loads(data)
# for data in datas:
#    print(data["title"])


# import urllib.request as req
# import ssl
# import json
# ssl._create_default_https_context = ssl._create_unverified_context 
# url = "https://medium.com/_/graphql"
# requestData = {"operationName":"ExtendedFeedQuery","variables":{"items":[{"postId":"be5b53cdfd5f","topicId":""},{"postId":"3492a48be47b","topicId":""},{"postId":"ec4123afad8f","topicId":""},{"postId":"e90431463924","topicId":""},{"postId":"e5d2b1983470","topicId":""},{"postId":"da8c118768a5","topicId":""},{"postId":"d6f47143faf3","topicId":""},{"postId":"ea59f95ef99d","topicId":""},{"postId":"93b5f3e13715","topicId":""},{"postId":"26ab7a193e03","topicId":""},{"postId":"87f350ad186a","topicId":""},{"postId":"b83285a3a8e7","topicId":""},{"postId":"2ac178fa8428","topicId":""},{"postId":"f9aabc04804a","topicId":""},{"postId":"a7fafbe451a5","topicId":""},{"postId":"1dbcf14a49e4","topicId":""},{"postId":"76f1442c8074","topicId":""},{"postId":"368edf009a62","topicId":""},{"postId":"6f362d4e6493","topicId":""},{"postId":"8e1b056fedbd","topicId":""}]},"query":"query ExtendedFeedQuery($items: [ExtendedFeedItemOptions!]!) {\n  extendedFeedItems(items: $items) {\n    post {\n      ...PostListModulePostPreviewData\n      __typename\n    }\n    metadata {\n      topic {\n        id\n        name\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment PostListModulePostPreviewData on Post {\n  id\n  firstPublishedAt\n  readingTime\n  createdAt\n  mediumUrl\n  previewImage {\n    id\n    __typename\n  }\n  title\n  collection {\n    id\n    domain\n    slug\n    name\n    navItems {\n      url\n      __typename\n    }\n    logo {\n      id\n      __typename\n    }\n    avatar {\n      id\n      __typename\n    }\n    __typename\n  }\n  creator {\n    id\n    name\n    username\n    imageId\n    mediumMemberAt\n    ...userUrl_user\n    __typename\n  }\n  visibility\n  isProxyPost\n  isLocked\n  ...HomeFeedItem_post\n  ...HomeReadingListItem_post\n  ...HomeTrendingModule_post\n  __typename\n}\n\nfragment HomeFeedItem_post on Post {\n  __typename\n  id\n  title\n  firstPublishedAt\n  mediumUrl\n  collection {\n    id\n    name\n    domain\n    logo {\n      id\n      __typename\n    }\n    __typename\n  }\n  creator {\n    id\n    name\n    username\n    imageId\n    mediumMemberAt\n    __typename\n  }\n  previewImage {\n    id\n    __typename\n  }\n  previewContent {\n    subtitle\n    __typename\n  }\n  readingTime\n  tags {\n    ...TopicPill_tag\n    __typename\n  }\n  ...BookmarkButton_post\n  ...CreatorActionOverflowPopover_post\n  ...PostPresentationTracker_post\n  ...PostPreviewAvatar_post\n}\n\nfragment TopicPill_tag on Tag {\n  __typename\n  id\n  displayTitle\n}\n\nfragment BookmarkButton_post on Post {\n  ...SusiClickable_post\n  ...WithSetReadingList_post\n  ...AddToCatalogBookmarkButton_post\n  __typename\n  id\n}\n\nfragment SusiClickable_post on Post {\n  id\n  mediumUrl\n  ...SusiContainer_post\n  __typename\n}\n\nfragment SusiContainer_post on Post {\n  id\n  __typename\n}\n\nfragment WithSetReadingList_post on Post {\n  ...ReadingList_post\n  __typename\n  id\n}\n\nfragment ReadingList_post on Post {\n  __typename\n  id\n  viewerEdge {\n    id\n    readingList\n    __typename\n  }\n}\n\nfragment AddToCatalogBookmarkButton_post on Post {\n  ...AddToCatalogBase_post\n  __typename\n  id\n}\n\nfragment AddToCatalogBase_post on Post {\n  id\n  viewerEdge {\n    catalogsConnection {\n      catalogsContainingThis(type: LISTS) {\n        catalogId\n        catalogItemIds\n        __typename\n      }\n      predefinedContainingThis {\n        catalogId\n        predefined\n        catalogItemIds\n        __typename\n      }\n      __typename\n    }\n    ...editCatalogItemsMutation_postViewerEdge\n    ...useAddItemToPredefinedCatalog_postViewerEdge\n    __typename\n    id\n  }\n  ...WithToggleInsideCatalog_post\n  __typename\n}\n\nfragment useAddItemToPredefinedCatalog_postViewerEdge on PostViewerEdge {\n  id\n  catalogsConnection {\n    predefinedContainingThis {\n      catalogId\n      version\n      predefined\n      catalogItemIds\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment editCatalogItemsMutation_postViewerEdge on PostViewerEdge {\n  id\n  catalogsConnection {\n    catalogsContainingThis(type: LISTS) {\n      catalogId\n      version\n      catalogItemIds\n      __typename\n    }\n    predefinedContainingThis {\n      catalogId\n      predefined\n      version\n      catalogItemIds\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment WithToggleInsideCatalog_post on Post {\n  id\n  viewerEdge {\n    catalogsConnection {\n      catalogsContainingThis(type: LISTS) {\n        catalogId\n        __typename\n      }\n      predefinedContainingThis {\n        predefined\n        __typename\n      }\n      __typename\n    }\n    __typename\n    id\n  }\n  __typename\n}\n\nfragment CreatorActionOverflowPopover_post on Post {\n  allowResponses\n  id\n  statusForCollection\n  isLocked\n  isPublished\n  clapCount\n  mediumUrl\n  pinnedAt\n  pinnedByCreatorAt\n  curationEligibleAt\n  mediumUrl\n  responseDistribution\n  visibility\n  ...useIsPinnedInContext_post\n  pendingCollection {\n    id\n    name\n    creator {\n      id\n      __typename\n    }\n    avatar {\n      id\n      __typename\n    }\n    domain\n    slug\n    __typename\n  }\n  creator {\n    id\n    ...MutePopoverOptions_creator\n    ...auroraHooks_publisher\n    __typename\n  }\n  collection {\n    id\n    name\n    creator {\n      id\n      __typename\n    }\n    avatar {\n      id\n      __typename\n    }\n    domain\n    slug\n    ...MutePopoverOptions_collection\n    ...auroraHooks_publisher\n    __typename\n  }\n  ...ClapMutation_post\n  __typename\n}\n\nfragment MutePopoverOptions_creator on User {\n  id\n  __typename\n}\n\nfragment MutePopoverOptions_collection on Collection {\n  id\n  __typename\n}\n\nfragment ClapMutation_post on Post {\n  __typename\n  id\n  clapCount\n  ...MultiVoteCount_post\n}\n\nfragment MultiVoteCount_post on Post {\n  id\n  ...PostVotersNetwork_post\n  __typename\n}\n\nfragment PostVotersNetwork_post on Post {\n  id\n  voterCount\n  recommenders {\n    name\n    __typename\n  }\n  __typename\n}\n\nfragment useIsPinnedInContext_post on Post {\n  id\n  collection {\n    id\n    __typename\n  }\n  pendingCollection {\n    id\n    __typename\n  }\n  pinnedAt\n  pinnedByCreatorAt\n  __typename\n}\n\nfragment auroraHooks_publisher on Publisher {\n  __typename\n  ... on Collection {\n    isAuroraEligible\n    isAuroraVisible\n    viewerEdge {\n      id\n      isEditor\n      __typename\n    }\n    __typename\n    id\n  }\n  ... on User {\n    isAuroraVisible\n    __typename\n    id\n  }\n}\n\nfragment PostPresentationTracker_post on Post {\n  id\n  visibility\n  previewContent {\n    isFullContent\n    __typename\n  }\n  collection {\n    id\n    slug\n    __typename\n  }\n  __typename\n}\n\nfragment PostPreviewAvatar_post on Post {\n  __typename\n  id\n  collection {\n    id\n    name\n    ...CollectionAvatar_collection\n    ...collectionUrl_collection\n    __typename\n  }\n  creator {\n    id\n    username\n    name\n    ...UserAvatar_user\n    ...userUrl_user\n    __typename\n  }\n}\n\nfragment CollectionAvatar_collection on Collection {\n  name\n  avatar {\n    id\n    __typename\n  }\n  ...collectionUrl_collection\n  __typename\n  id\n}\n\nfragment collectionUrl_collection on Collection {\n  id\n  domain\n  slug\n  __typename\n}\n\nfragment UserAvatar_user on User {\n  __typename\n  username\n  id\n  name\n  imageId\n  mediumMemberAt\n  ...userUrl_user\n}\n\nfragment userUrl_user on User {\n  __typename\n  id\n  customDomainState {\n    live {\n      domain\n      __typename\n    }\n    __typename\n  }\n  username\n  hasSubdomain\n}\n\nfragment HomeReadingListItem_post on Post {\n  id\n  title\n  creator {\n    id\n    name\n    username\n    ...UserAvatar_user\n    __typename\n  }\n  mediumUrl\n  createdAt\n  readingTime\n  collection {\n    id\n    name\n    navItems {\n      url\n      __typename\n    }\n    ...CollectionAvatar_collection\n    __typename\n  }\n  visibility\n  __typename\n}\n\nfragment HomeTrendingModule_post on Post {\n  id\n  ...HomeTrendingPostPreview_post\n  __typename\n}\n\nfragment HomeTrendingPostPreview_post on Post {\n  id\n  title\n  mediumUrl\n  readingTime\n  firstPublishedAt\n  ...PostPreviewAvatar_post\n  ...PostPresentationTracker_post\n  __typename\n}\n"}
# request = req.Request(url, headers={
#    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
#    "Content-Type":"application/json"
# },
#    data = json.dumps(requestData).encode("utf-8"))
# with req.urlopen(request) as response:
#    result = response.read().decode("utf-8")
# result = json.loads(result)   
# items = result["data"]["extendedFeedItems"]
# for item in items:
#    print(item["post"]["title"])
