
def sub_downcase(text, from_text, to):
    result = ""
    for i in range(from_text, to): 
        result += text[i].lower()
    return result

def match(text, subtext = ""):
    result = []
    if(len(subtext) == 0) or (len(text) < len(subtext)):
        return "<no matches>"
    _end = len(text) - len(subtext) + 1
    sub_end = len(subtext)

    for index in range(0,_end - 1):
        # import ipdb;ipdb.set_trace()
        if(sub_downcase(text, index, sub_end) == subtext.lower()):
            result.append(str(index + 1))
        sub_end = sub_end + 1
    return "<no matches>" if len(result) == 0 else ', '.join(result)

# print match("Google is a search engine service, google is also an engine for a lot of other services and tools", "a")