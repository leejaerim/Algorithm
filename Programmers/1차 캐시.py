def solution(cacheSize, cities):
    # LRU를 만든다.
    # counter 가 필요하다.
    # cache size 를 입력받아. check
    cache = []
    res = 0 
    # list Comprehension
    # citie = [city.lower() for city in cities] 
    # collections.deque([], maxlen = cacheSize)
    if cacheSize == 0 :
        return 5*len(cities)
    for city in cities:
        city = city.upper()
        # 캐시 존재
        if city in cache :
            res += 1
            del cache[cache.index(city)]
            cache.append(city)
        # 캐시 missed
        else :
            res += 5    
            if len(cache) < cacheSize : 
                cache.append(city)
            else : 
                del cache[0]
                cache.append(city)
    return res