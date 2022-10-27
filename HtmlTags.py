import re
from Variables import list_of_tags, list_of_ids, list_of_items, list_of_element, list_of_types

def print_element(difflist):    
    for index in range(len(list_of_tags)):
        for item in difflist:
            if item.find(list_of_tags[index]) != -1:
                if item.find("id =") != -1:
                    ids = re.findall('(id =*.?\")(.*?)(\")', format(item))
                    types = re.findall('(type=*.?\")(.*?)(\")', format(item))
                    list_of_ids.append(ids)
                    list_of_items.append(format(item))
                    list_of_element.append(list_of_tags[index])
                    list_of_types.append(types)
                elif item.find("id=") != -1:
                    ids = re.findall('(id=*.?\")(.*?)(\")', format(item))
                    types = re.findall('(type=*.?\")(.*?)(\")',format(item))
                    list_of_ids.append(ids)
                    list_of_items.append(format(item))
                    list_of_element.append(list_of_tags[index])
                    list_of_types.append(types)
                elif item.find("id= ") != -1:
                    ids = re.findall('(id= *.?\")(.*?)(\")', format(item))
                    types = re.findall('(type=*.?\")(.*?)(\")', format(item))
                    list_of_ids.append(ids)
                    list_of_items.append(format(item))
                    list_of_types.append(types)
                    list_of_element.append(list_of_tags[index])
                elif item.find("id = ") != -1:
                    ids = re.findall('(id = *.? \")(.*?)(\")', format(item))
                    types = re.findall('(type=*.?\")(.*?)(\")', format(item))
                    list_of_ids.append(ids)
                    list_of_items.append(format(item))
                    list_of_element.append(list_of_tags[index])
                    list_of_types.append(types)

