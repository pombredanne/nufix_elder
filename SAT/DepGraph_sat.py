class DepGraph:
    def __init__(self, raw_data):
        depItemDict = {}
        for x in raw_data:
            if x['Dependency'] == 'ROOT':
                depItemDict['ROOT'] = DepItem('ROOT', '', x['Children'])
            else:
                depItemDict[x['Dependency'] + ' ' + x['Version']] = DepItem(x['Dependency'], x['Version'], x['Children'])
        for k in depItemDict:
            for group in depItemDict[k].depGroups:
                group.items = [depItemDict[group.packageName + ' ' + version] for version in group.items]
        self.depItemDict = depItemDict


# class eMid:
#     def __init__(self,raw_data):
#         eDict = {}
#         for x in raw_data:
#             x_packageName = x['Dependency']
#             if x['Dependency'] != 'ROOT':
#                 x_Version = x['Version']
#                 children_info = x['Children']
#                 for c in children_info:
#                     version_list = children_info[c]
#                     for version in version_list:
#                         j_packageName = c
#                         j_Version = version
#                         e_key = x_packageName +"@"+ x_Version +"$"+ j_packageName +"@"+ j_Version
#                         eDict[e_key] = eMidItem(e_key)
#
#             # for j in raw_data:
#             #     x_packageName = x['Dependency']
#             #     if x['Dependency'] == 'ROOT':
#             #         x_Version=''
#             #     else:
#             #         x_Version = x['Version']
#             #     j_packageName = j['Dependency']
#             #     if j['Dependency'] == 'ROOT':
#             #         j_Version=''
#             #     else:
#             #         j_Version = j['Version']
#             #     eDict[x_packageName+x_Version+j_packageName+j_Version] = eMidItem(x_packageName+x_Version+j_packageName+j_Version)
#
#         self.eDict = eDict
#
# class eMidItem:
#     def __init__(self, itemKey):
#         self.itemKey = itemKey
#         self.var = None


class DepItem:
    def __init__(self, packageName, version, children):
        self.packageName = packageName
        self.version = version
        self.varName = (packageName + '@' + version).strip()
        self.var = None
        self.depGroups = []
        for x in children:
            version_list = children[x]
            self.depGroups.append(DepGroup(self, x, version_list))

            # for name in x:
            #     if len(name) == 0:
            #         continue
            #     version_list = x[name]
            #     self.depGroups.append(DepGroup(self, name, version_list))


class DepGroup:
    def __init__(self, parent: DepItem, packageName, version_list):
        self.packageName = packageName
        self.items = version_list
        # self.varName = parent.packageName + ' ' + parent.version + ' ' + packageName
        # self.var = None
