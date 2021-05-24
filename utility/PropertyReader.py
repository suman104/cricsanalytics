from jproperties import Properties

configs = Properties()


def getYourProperty(sourcefile,prop):
    with open(sourcefile, 'rb') as read_prop:
        configs.load(read_prop)
    return configs.get(prop).data


#print(configs.get("yamlsource").data)
#prop_view = configs.items()
#print(type(prop_view))

#for item in prop_view:
    #print(item[0], '=', item[1].data)