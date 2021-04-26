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



class DepGroup:
    def __init__(self, parent: DepItem, packageName, version_list):
        self.packageName = packageName
        self.items = version_list

