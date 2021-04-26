import json

from SAT import DepGraph_sat,solver_sat
from output_dep_tree import output_depinfo_in_json,change_dependency_structure_json,mysql_operation,matching_targetFramework
from build_dependency_tree import building_dependency_tree_MCTS_agile
import os

def start_SAT(json_file_name,obj_parameter_list):
    data = []
    file_url = "../data/" + json_file_name+".txt"
    # with open('../data/test_depgraph.txt') as f:
    with open(file_url) as f:
        lines = f.readlines()
        for line in lines:
            data.append(json.loads(line))
    graph = DepGraph_sat.DepGraph(data)
    # e_mid = DepGraph_sat.eMid(data)
    model = solver_sat.create_model(graph,obj_parameter_list)
    # model.verbose = 0
    status = model.optimize(max_seconds=100, max_solutions=5)
    # status = model.optimize(max_seconds=100, max_solutions=5)
    print("status:", status)
    print(model.objective_values)


    return_dep_list = []
    for k in range(model.num_solutions):
        print('route {} with length {}'.format(k, model.objective_values[k]))
        dep_list=[]
        for g in graph.depItemDict['ROOT'].depGroups:
            for item in g.items:
                if item.var.xi(k) >= 0.99:
                    # print(item.var)
                    dep_list.append(item.varName)
        return_dep_list.append(dep_list)

    return return_dep_list



if __name__ == '__main__':

    # json_file_name = "test03"
    # targetFramework = '.NETCoreApp2.1'
    # dependencies_list=['Amazon.CDK@1.15.0-devpreview', 'Amazon.CDK.AWS.ApplicationAutoScaling@1.15.0-devpreview',
    #                    'Amazon.CDK.AWS.ECR@1.15.0-devpreview', 'Amazon.CDK.AWS.ECS.Patterns@1.15.0-devpreview',
    #                    'Amazon.CDK.AWS.ElasticLoadBalancingV2@1.15.0-devpreview', 'Amazon.CDK.AWS.IAM@1.15.0-devpreview',
    #                    'Amazon.CDK.AWS.RDS@1.15.0-devpreview', 'Amazon.CDK.AWS.S3@1.15.0-devpreview',
    #                    'Amazon.CDK.AWS.ECS@1.15.0-devpreview', 'Amazon.CDK.AWS.SSM@1.15.0-devpreview']


    # json_file_name = "test06"
    # targetFramework = '.NETCoreApp2.0'
    # dependencies_list=['Microsoft.Data.SQLite@1.0.0-beta1', 'MySql.Data@6.10.5', 'Microsoft.NET.Test.Sdk@15.5.0', 'NUnit@3.0.0-alpha', 'Newtonsoft.Json@10.0.3', 'NUnit3TestAdapter@3.9.0', 'System.Data.SQLite@1.0.100']

    json_file_name = "LykkeCity-Lykke.Service.HftInternalService_Lykke_Service_HftInternalService_Services_csproj_"
    targetFramework = '.NETCoreApp2.1'
    dependencies_list=['Lykke.Cqrs@4.6.0', 'Lykke.RabbitMqBroker@7.0.1', 'Lykke.Service.ClientAccount.Client@1.4.1', 'MessagePack@1.7.3.4']



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

    file_url = "../data/" + json_file_name + ".txt"
    if os.path.exists(file_url) == False:
        # 将依赖文件写入json格式
        output_depinfo_in_json.def_info_in_json(targetFramework, first_dep_list, json_file_name)
    # output_depinfo_in_json.def_info_in_json(targetFramework, first_dep_list,json_file_name)
    obj_parameter_list=[1,1,1,1]
    # 执行SAT
    best_solution_dep_list_li = start_SAT(json_file_name,obj_parameter_list)

    for best_solution_dep_list in best_solution_dep_list_li:

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

        # building_dependency_tree_return_list = building_dependency_tree_MCTS_agile.building_dependency_tree(targetFramework,best_solution_dep_list,
        #                                                                                  [])
        # error_directly_dependency_list = building_dependency_tree_return_list[4]
        # print("error_directly_dependency_list",error_directly_dependency_list)
