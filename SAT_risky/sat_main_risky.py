import json

from SAT_risky import DepGraph_sat_risky,solver_sat_risky,output_depinfo_in_json_risky
from output_dep_tree import output_depinfo_in_json,change_dependency_structure_json,mysql_operation,matching_targetFramework
from build_dependency_tree import building_dependency_tree_MCTS_agile,building_dep_tree_SAT_new
import os

def start_SAT(json_file_name,obj_parameter_list):
    data = []
    file_url = "../data_risky/" + json_file_name+".txt"
    # with open('../data/test_depgraph.txt') as f:
    with open(file_url) as f:
        lines = f.readlines()
        for line in lines:
            data.append(json.loads(line))
    graph = DepGraph_sat_risky.DepGraph(data)
    # e_mid = DepGraph_sat.eMid(data)
    model = solver_sat_risky.create_model(graph,obj_parameter_list)
    # model.verbose = 0
    status = model.optimize(max_seconds=100)
    # status = model.optimize(max_seconds=100, max_solutions=5)
    print("status:", status)
    print(model.objective_values)

    return_dep_list = []
    # for k in range(model.num_solutions):


    # print('route {} with length {}'.format(k, model.objective_values[k]))
    # dep_list=[]
    for g in graph.depItemDict['ROOT'].depGroups:
        for item in g.items:
            if item.var.x >= 0.99:
                # print(item.var)
                return_dep_list.append(item.varName)

    packageDict = {}
    for k in graph.depItemDict:
        item = graph.depItemDict[k]
        if item.packageName not in packageDict:
            packageDict[item.packageName] = []
        packageDict[item.packageName].append(item)

    all_no_constraint_list = []
    for k2 in graph.depItemDict:
        item = graph.depItemDict[k2]
        for group in item.depGroups:
            group_verName_list = []
            group_item_no_constraint_list = []
            for x in group.items:
                group_verName_list.append(x.varName)
            for y in packageDict[group.packageName]:
                if y.varName not in group_verName_list:
                    group_item_no_constraint_list.append(y)
            for group_item_no_constraint in group_item_no_constraint_list:
                all_no_constraint_list.append(group_item_no_constraint)

    for k3 in all_no_constraint_list:

        if k3.var.x >= 0.99:
            if k3.varName not in return_dep_list:
                return_dep_list.append(k3.varName)
                print("k3.varName",k3.varName)





    # return_dep_list.append(dep_list)



    return return_dep_list



if __name__ == '__main__':


    json_file_name = "test12"
    targetFramework = 'net5.0'
    dependencies_list=['BuildBundlerMinifier@3.2.449', 'Newtonsoft.Json@12.0.3', 'Remotion.Linq@2.2.0', 'Serilog.AspNetCore@3.4.0', 'Serilog.Sinks.File@4.1.0', 'Microsoft.AspNetCore.Diagnostics.EntityFrameworkCore@3.1.8', 'Microsoft.AspNetCore.Identity.EntityFrameworkCore@3.1.8', 'Microsoft.Extensions.Logging.Debug@3.1.8', 'IdentityServer4@4.1.0', 'IdentityServer4.AspNetIdentity@4.1.0', 'Microsoft.EntityFrameworkCore.Sqlite@3.1.8', 'Microsoft.EntityFrameworkCore.Tools@3.1.8', 'Microsoft.VisualStudio.Web.CodeGeneration.Design@3.1.4', 'Serilog.Settings.Configuration@3.1.1-dev-00209', 'Serilog.Sinks.RollingFile@3.3.0', 'Serilog.Sinks.Seq@4.0.1-dev-00159', 'Serilog.Extensions.Logging@3.0.2-dev-10256', 'Serilog.Sinks.Console@3.1.2-dev-00823', 'Serilog.Sinks.RollingFile@3.3.1-dev-00771']




    # dependencies_list=[
    #     'Microsoft.AspNetCore.Authentication.Cookies@1.0.1',
    #     'Microsoft.AspNetCore.Diagnostics@1.0.1',
    #     'Microsoft.AspNetCore.Diagnostics.EntityFrameworkCore@1.0.1',
    #     'Microsoft.AspNetCore.Identity.EntityFrameworkCore@1.0.1',
    #     'Microsoft.AspNetCore.Mvc@1.0.2',
    #     'Microsoft.AspNetCore.Routing@1.0.2',
    #     'Microsoft.AspNetCore.Server.IISIntegration@1.0.1',
    #     'Microsoft.AspNetCore.Server.Kestrel@1.0.2',
    #     'Microsoft.AspNetCore.StaticFiles@1.0.1',
    #     'Microsoft.EntityFrameworkCore.Sqlite@1.0.2',
    #     'Microsoft.EntityFrameworkCore.Tools@1.0.0-msbuild3-final',
    #     'Microsoft.EntityFrameworkCore.Tools@1.0.0-msbuild3-final',
    #     'Microsoft.Extensions.Configuration.EnvironmentVariables@1.0.1',
    #     'Microsoft.Extensions.Configuration.Json@1.0.1',
    #     'Microsoft.Extensions.Configuration.UserSecrets@1.0.1',
    #     'Microsoft.Extensions.Logging@1.0.1',
    #     'Microsoft.Extensions.Logging.Console@1.0.1',
    #     'Microsoft.Extensions.Logging.Debug@1.0.1',
    #     'Microsoft.VisualStudio.Web.BrowserLink.Loader@14.0.1',
    #     'Microsoft.VisualStudio.Web.CodeGeneration.Design@1.0.0-msbuild3-final',
    #     'Microsoft.VisualStudio.Web.CodeGeneration.Design@1.0.0-msbuild3-final',
    #     'System.Security.Cryptography.Algorithms@4.2.0',
    #     'AspNetCore.Health@1.0.0',
    # ]
    # 框架格式修正
    targetFramework = matching_targetFramework.change_framework_structure(targetFramework)
    first_dep_list = change_dependency_structure_json.change_structure_for_sat_test(dependencies_list)
    # print("first_dep_list",first_dep_list)

    file_url = "../data_risky/" + json_file_name + ".txt"
    if os.path.exists(file_url) == False:
        # 将依赖文件写入json格式
        output_depinfo_in_json_risky.def_info_in_json(targetFramework, first_dep_list, json_file_name)
    # output_depinfo_in_json.def_info_in_json(targetFramework, first_dep_list,json_file_name)
    obj_parameter_list=[1,1,0.02,1,0.1,1]
    # 执行SAT
    best_solution_dep_list = start_SAT(json_file_name,obj_parameter_list)

    # for best_solution_dep_list in best_solution_dep_list_li:

    print("\n*****************************************************************")
    print("原始直接依赖：")
    for dependencies_info in dependencies_list:
        print(dependencies_info)
    print("*****************************************************************")
    print("SAT执行后直接依赖：")
    for best_solution_dep_info in best_solution_dep_list:
        print(best_solution_dep_info)
    print("*****************************************************************")
    for best_solution_dep_info in best_solution_dep_list:
        if best_solution_dep_info not in dependencies_list:
            print("+", best_solution_dep_info)
    print("")
    for first_de_info in dependencies_list:
        if first_de_info not in best_solution_dep_list:
            print("-", first_de_info)
    print("*****************************************************************")

    building_dependency_tree_return_list = building_dep_tree_SAT_new.building_dependency_tree(targetFramework,
                                                                                     best_solution_dep_list,
                                                                                     [])
    error_directly_dependency_list = building_dependency_tree_return_list[4]
    print("error_directly_dependency_list",error_directly_dependency_list)
