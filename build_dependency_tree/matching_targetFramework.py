
import re

NET="net"
NetCoreApp = ".NETCoreApp"
NetStandardApp = ".NETStandardApp"
NetStandard = ".NETStandard"
NetPlatform = ".NETPlatform"
DotNet = "dotnet"
Net = ".NETFramework"
NetCore = ".NETCore"
WinRT = "WinRT"
NetMicro = ".NETMicroFramework"
Portable = ".NETPortable"
WindowsPhone = "WindowsPhone"
Windows = "Windows"
WindowsPhoneApp = "WindowsPhoneApp"
Dnx = "DNX"
DnxCore = "DNXCore"
AspNet = "ASP.NET"
AspNetCore = "ASP.NETCore"
Silverlight = "Silverlight"
Native = "native"
MonoAndroid = "MonoAndroid"
MonoTouch = "MonoTouch"
MonoMac = "MonoMac"
XamarinIOs = "Xamarin.iOS"
XamarinMac = "Xamarin.Mac"
XamarinPlayStation3 = "Xamarin.PlayStation3"
XamarinPlayStation4 = "Xamarin.PlayStation4"
XamarinPlayStationVita = "Xamarin.PlayStationVita"
XamarinWatchOS = "Xamarin.WatchOS"
XamarinTVOS = "Xamarin.TVOS"
XamarinXbox360 = "Xamarin.Xbox360"
XamarinXboxOne = "Xamarin.XboxOne"
UAP = "UAP"
Tizen = "Tizen"

all_framework_list = []

all_framework_list.append(NET)
all_framework_list.append(NetCoreApp)
all_framework_list.append(NetStandardApp)
all_framework_list.append(NetStandard)
all_framework_list.append(NetPlatform)
all_framework_list.append(NetCore)
all_framework_list.append(WinRT)
all_framework_list.append(NetMicro)
all_framework_list.append(Portable)
all_framework_list.append(WindowsPhone)
all_framework_list.append(WindowsPhoneApp)
all_framework_list.append(DnxCore)
all_framework_list.append(AspNetCore)
all_framework_list.append(Silverlight)
all_framework_list.append(Native)
all_framework_list.append(MonoAndroid)
all_framework_list.append(MonoTouch)
all_framework_list.append(MonoMac)
all_framework_list.append(XamarinIOs)
all_framework_list.append(XamarinMac)
all_framework_list.append(XamarinPlayStation3)
all_framework_list.append(XamarinPlayStation4)
all_framework_list.append(XamarinPlayStationVita)
all_framework_list.append(XamarinWatchOS)
all_framework_list.append(XamarinTVOS)
all_framework_list.append(XamarinXbox360)
all_framework_list.append(XamarinXboxOne)
all_framework_list.append(Windows)
all_framework_list.append(AspNet)
all_framework_list.append(DotNet)
all_framework_list.append(Tizen)
all_framework_list.append(Net)
all_framework_list.append(UAP)
all_framework_list.append(Dnx)

#             public static readonly NuGetFramework Net11 = new NuGetFramework(FrameworkIdentifiers.Net, new Version(1, 1, 0, 0));
#             public static readonly NuGetFramework Net2 = new NuGetFramework(FrameworkIdentifiers.Net, new Version(2, 0, 0, 0));
#             public static readonly NuGetFramework Net35 = new NuGetFramework(FrameworkIdentifiers.Net, new Version(3, 5, 0, 0));
#             public static readonly NuGetFramework Net4 = new NuGetFramework(FrameworkIdentifiers.Net, new Version(4, 0, 0, 0));
#             public static readonly NuGetFramework Net403 = new NuGetFramework(FrameworkIdentifiers.Net, new Version(4, 0, 3, 0));
#             public static readonly NuGetFramework Net45 = new NuGetFramework(FrameworkIdentifiers.Net, new Version(4, 5, 0, 0));
#             public static readonly NuGetFramework Net451 = new NuGetFramework(FrameworkIdentifiers.Net, new Version(4, 5, 1, 0));
#             public static readonly NuGetFramework Net452 = new NuGetFramework(FrameworkIdentifiers.Net, new Version(4, 5, 2, 0));
#             public static readonly NuGetFramework Net46 = new NuGetFramework(FrameworkIdentifiers.Net, new Version(4, 6, 0, 0));
#             public static readonly NuGetFramework Net461 = new NuGetFramework(FrameworkIdentifiers.Net, new Version(4, 6, 1, 0));
#             public static readonly NuGetFramework Net462 = new NuGetFramework(FrameworkIdentifiers.Net, new Version(4, 6, 2, 0));
#             public static readonly NuGetFramework Net463 = new NuGetFramework(FrameworkIdentifiers.Net, new Version(4, 6, 3, 0));

#
NetStandard_support_list = []

NETStandard21_list = []
NETStandard21_support_list = []
NETStandard21_support_list.append(".NETCoreApp3.0")
NETStandard21_list.append(".NETStandard2.1")
NETStandard21_list.append(NETStandard21_support_list)
NetStandard_support_list.append(NETStandard21_list)

NETStandard20_list = []
NETStandard20_support_list = []
NETStandard20_support_list.append(".NETFramework4.6.1")
NETStandard20_support_list.append(".NETCoreApp2.0")
NETStandard20_list.append(".NETStandard2.0")
NETStandard20_list.append(NETStandard20_support_list)
NetStandard_support_list.append(NETStandard20_list)

NETStandard16_list = []
NETStandard16_support_list = []
NETStandard16_support_list.append(".NETFramework4.6.1")
NETStandard16_support_list.append(".NETCoreApp1.0")
NETStandard16_list.append(".NETStandard1.6")
NETStandard16_list.append(NETStandard16_support_list)
NetStandard_support_list.append(NETStandard16_list)

NETStandard15_list = []
NETStandard15_support_list = []
NETStandard15_support_list.append(".NETFramework4.6.1")
NETStandard15_support_list.append(".NETCoreApp1.0")
NETStandard15_list.append(".NETStandard1.5")
NETStandard15_list.append(NETStandard16_support_list)
NetStandard_support_list.append(NETStandard15_list)

NETStandard14_list = []
NETStandard14_support_list = []
NETStandard14_support_list.append(".NETFramework4.6.1")
NETStandard14_support_list.append(".NETCoreApp1.0")
NETStandard14_list.append(".NETStandard1.4")
NETStandard14_list.append(NETStandard14_support_list)
NetStandard_support_list.append(NETStandard14_list)

NETStandard13_list = []
NETStandard13_support_list = []
NETStandard13_support_list.append(".NETFramework4.6")
NETStandard13_support_list.append(".NETCoreApp1.0")
NETStandard13_list.append(".NETStandard1.3")
NETStandard13_list.append(NETStandard13_support_list)
NetStandard_support_list.append(NETStandard13_list)

NETStandard12_list = []
NETStandard12_support_list = []
NETStandard12_support_list.append(".NETFramework4.5.1")
NETStandard12_support_list.append(".NETCoreApp1.0")
NETStandard12_list.append(".NETStandard1.2")
NETStandard12_list.append(NETStandard12_support_list)
NetStandard_support_list.append(NETStandard12_list)

NETStandard11_list = []
NETStandard11_support_list = []
NETStandard11_support_list.append(".NETFramework4.5")
NETStandard11_support_list.append(".NETCoreApp1.0")
NETStandard11_list.append(".NETStandard1.1")
NETStandard11_list.append(NETStandard11_support_list)
NetStandard_support_list.append(NETStandard11_list)

NETStandard10_list = []
NETStandard10_support_list = []
NETStandard10_support_list.append(".NETFramework4.5")
NETStandard10_support_list.append(".NETCoreApp1.0")
NETStandard10_list.append(".NETStandard1.0")
NETStandard10_list.append(NETStandard10_support_list)
NetStandard_support_list.append(NETStandard10_list)

# .NETFramework ['1','1','0','0']

matching_framework_list = []

# .NETFramework
Net_version_list = []
Net_version_list.append(".NETFramework4.8")
Net_version_list.append(".NETFramework4.7.2")
Net_version_list.append(".NETFramework4.7.1")
Net_version_list.append(".NETFramework4.7")
Net_version_list.append(".NETFramework4.6.2")
Net_version_list.append(".NETFramework4.6.1")
Net_version_list.append(".NETFramework4.6")
Net_version_list.append(".NETFramework4.5.2")
Net_version_list.append(".NETFramework4.5.1")
Net_version_list.append(".NETFramework4.5")
Net_version_list.append(".NETFramework4.0.3")
Net_version_list.append(".NETFramework4.0")
Net_version_list.append(".NETFramework3.5")
Net_version_list.append(".NETFramework2.0")
Net_version_list.append(".NETFramework1.1")
Net_list = []
Net_list.append(Net)
Net_list.append(Net_version_list)
matching_framework_list.append(Net_list)

# .NETStandard
NetStandard_version_list = []
NetStandard_version_list.append(".NETStandard2.1")
NetStandard_version_list.append(".NETStandard2.0")
NetStandard_version_list.append(".NETStandard1.6")
NetStandard_version_list.append(".NETStandard1.5")
NetStandard_version_list.append(".NETStandard1.4")
NetStandard_version_list.append(".NETStandard1.3")
NetStandard_version_list.append(".NETStandard1.2")
NetStandard_version_list.append(".NETStandard1.1")
NetStandard_version_list.append(".NETStandard1.0")
NetStandard_list = []
NetStandard_list.append(NetStandard)
NetStandard_list.append(NetStandard_version_list)
matching_framework_list.append(NetStandard_list)

# .NetCoreApp
NetCoreApp_version_list = []
NetCoreApp_version_list.append(".NETCoreApp3.1")
NetCoreApp_version_list.append(".NETCoreApp3.0")
NetCoreApp_version_list.append(".NETCoreApp2.2")
NetCoreApp_version_list.append(".NETCoreApp2.1")
NetCoreApp_version_list.append(".NETCoreApp2.0")
NetCoreApp_version_list.append(".NETCoreApp1.1")
NetCoreApp_version_list.append(".NETCoreApp1.0")
NetCoreApp_list = []
NetCoreApp_list.append(NetCoreApp)
NetCoreApp_list.append(NetCoreApp_version_list)
matching_framework_list.append(NetCoreApp_list)



#net5.0
Net_version_list = []
Net_version_list.append("net5.0")
Net_list = []
Net_list.append(NetCoreApp)
Net_list.append(Net_version_list)
matching_framework_list.append(Net_list)


def change_framework_structure(targetFramework):


    if targetFramework=="net11":
        targetFramework=".NETFramework1.1"
    elif targetFramework=="net20":
        targetFramework =".NETFramework2.0"
    elif targetFramework=="net35":
        targetFramework =".NETFramework3.5"
    elif targetFramework=="net40":
        targetFramework =".NETFramework4.0"
    elif targetFramework=="net403":
        targetFramework =".NETFramework4.0.3"
    elif targetFramework=="net45":
        targetFramework =".NETFramework4.5"
    elif targetFramework=="net451":
        targetFramework =".NETFramework4.5.1"
    elif targetFramework=="net452":
        targetFramework =".NETFramework4.5.2"
    elif targetFramework=="net46":
        targetFramework =".NETFramework4.6"
    elif targetFramework=="net461":
        targetFramework =".NETFramework4.6.1"
    elif targetFramework=="net462":
        targetFramework =".NETFramework4.6.2"
    elif targetFramework=="net47":
        targetFramework =".NETFramework4.7"
    elif targetFramework=="net471":
        targetFramework =".NETFramework4.7.1"
    elif targetFramework=="net472":
        targetFramework =".NETFramework4.7.2"
    elif targetFramework=="net48":
        targetFramework =".NETFramework4.8"

    # NetStandard_version_list.append(".NETStandard2.1")
    # NetStandard_version_list.append(".NETStandard2.0")
    # NetStandard_version_list.append(".NETStandard1.6")
    # NetStandard_version_list.append(".NETStandard1.5")
    # NetStandard_version_list.append(".NETStandard1.4")
    # NetStandard_version_list.append(".NETStandard1.3")
    # NetStandard_version_list.append(".NETStandard1.2")
    # NetStandard_version_list.append(".NETStandard1.1")
    # NetStandard_version_list.append(".NETStandard1.0")

    elif targetFramework=="netstandard1.0":
        targetFramework=".NETStandard1.0"
    elif targetFramework=="netstandard1.1":
        targetFramework =".NETStandard1.1"
    elif targetFramework=="netstandard1.2":
        targetFramework =".NETStandard1.2"
    elif targetFramework=="netstandard1.3":
        targetFramework =".NETStandard1.3"
    elif targetFramework=="netstandard1.4":
        targetFramework =".NETStandard1.4"
    elif targetFramework=="netstandard1.5":
        targetFramework =".NETStandard1.5"
    elif targetFramework=="netstandard1.6":
        targetFramework =".NETStandard1.6"
    elif targetFramework=="netstandard2.0":
        targetFramework =".NETStandard2.0"
    elif targetFramework=="netstandard2.1":
        targetFramework =".NETStandard2.1"



    elif targetFramework=="netcoreapp1.0":
        targetFramework =".NETCoreApp1.0"
    elif targetFramework=="netcoreapp1.1":
        targetFramework =".NETCoreApp1.1"
    elif targetFramework=="netcoreapp2.0":
        targetFramework =".NETCoreApp2.0"
    elif targetFramework=="netcoreapp2.1":
        targetFramework =".NETCoreApp2.1"
    elif targetFramework=="netcoreapp2.2":
        targetFramework =".NETCoreApp2.2"
    elif targetFramework=="netcoreapp3.0":
        targetFramework =".NETCoreApp3.0"
    elif targetFramework=="netcoreapp3.1":
        targetFramework =".NETCoreApp3.1"

    elif targetFramework=="netcoreapp5.0":
        targetFramework ="net5.0"
    elif targetFramework=="net50":
        targetFramework ="net5.0"
    elif targetFramework==".NETCoreApp5.0":
        targetFramework ="net5.0"
    elif targetFramework=="net5.0-windows":
        targetFramework = "net5.0"
    elif targetFramework=="net50-windows":
        targetFramework = "net5.0"
    elif targetFramework=="net5":
        targetFramework = "net5.0"


    elif targetFramework=="netcoreapp6.0":
        targetFramework ="net6.0"
    elif targetFramework=="net60":
        targetFramework ="net6.0"
    elif targetFramework==".NETCoreApp6.0":
        targetFramework ="net6.0"
    elif targetFramework=="net6.0-windows":
        targetFramework = "net6.0"
    elif targetFramework=="net60-windows":
        targetFramework = "net6.0"
    elif targetFramework=="net6":
        targetFramework = "net6.0"

    return targetFramework


# Net_list.append(['1','1','0','0'])

def matching_framework(targetFramework, dependency_frameworkList):
    targetFramework_name = ''
    targetFramework_version = ''
    flresult = ''
    flresult_list = []
    matching_targetFramework = ''
    if dependency_frameworkList==[] or dependency_frameworkList is None:
        dependency_frameworkList=[]
        dependency_frameworkList.append(targetFramework)

    if targetFramework=="net6.0" or targetFramework==".NETCoreApp6.0" or targetFramework=="net60" or targetFramework=="netcoreapp6.0":

        if "net6.0" in dependency_frameworkList or ".NETCoreApp6.0" in targetFramework or "net60" in targetFramework :
            return targetFramework
        if "net5.0" in dependency_frameworkList or ".NETCoreApp5.0" in targetFramework or "net50" in targetFramework :
            return targetFramework
        else:
            for NetCoreApp_version in NetCoreApp_version_list:
                if NetCoreApp_version in dependency_frameworkList:
                    return NetCoreApp_version
            for NetStandard_version in NetStandard_version_list:
                if NetStandard_version in dependency_frameworkList:
                    return NetStandard_version

    if targetFramework=="net5.0" or targetFramework==".NETCoreApp5.0" or targetFramework=="net50" or targetFramework=="netcoreapp5.0":

        if "net5.0" in dependency_frameworkList or ".NETCoreApp5.0" in targetFramework or "net50" in targetFramework :
            return targetFramework
        else:
            for NetCoreApp_version in NetCoreApp_version_list:
                if NetCoreApp_version in dependency_frameworkList:
                    return NetCoreApp_version
            for NetStandard_version in NetStandard_version_list:
                if NetStandard_version in dependency_frameworkList:
                    return NetStandard_version


    for fw in all_framework_list:
        patt = r'%s' % fw
        pattern = re.compile(patt)
        result = pattern.findall(targetFramework)
        if result != []:
            targetFramework_name = result[0]
            targetFramework_version_list = re.split(targetFramework_name, targetFramework)[1].split(".")
            for i in range(len(targetFramework_version_list), 4):
                targetFramework_version_list.append("0")
            break
    # # 目标框架和版本
    # print("targetFramework_name: ",targetFramework_name)
    # print("targetFramework_version_list: ",targetFramework_version_list)
    # .NETFramework
    # 4.5

    # 支持的框架列表
    for fl in dependency_frameworkList:
        # print(fl)
        patt_targetFramework = r'%s' % targetFramework_name
        # print("patt_targetFramework",patt_targetFramework)
        # patt_Standard = r'.NETStandard'
        pattern_targetFramework = re.compile(patt_targetFramework)
        # pattern_Standard = re.compile(patt_Standard)

        flresult1 = pattern_targetFramework.findall(fl)
        # flresult2 = pattern_Standard.findall(fl)

        if flresult1 != []:
            flresult_list.append(fl)
        # if flresult2 != []:
        #     flresult_list.append(fl)

    # if flresult_list == []:
    #     # 支持的.NETStandard列表
    #     for fl in dependency_frameworkList:
    #         # patt_targetFramework = r'%s' % targetFramework_name
    #         patt_Standard = r'.NETStandard'
    #         # pattern_targetFramework = re.compile(patt_targetFramework)
    #         pattern_Standard = re.compile(patt_Standard)
    #
    #         # flresult1 = pattern_targetFramework.findall(fl)
    #         flresult2 = pattern_Standard.findall(fl)
    #         # print("flresult2:",flresult2)
    #         # if flresult1 != []:
    #         #     flresult_list.append(fl)
    #         if flresult2 != []:
    #             flresult_list.append(fl)

    # 支持的.NETStandard列表

    for fl in dependency_frameworkList:
        # patt_targetFramework = r'%s' % targetFramework_name
        patt_Standard = r'.NETStandard'
        # pattern_targetFramework = re.compile(patt_targetFramework)
        pattern_Standard = re.compile(patt_Standard)

        # flresult1 = pattern_targetFramework.findall(fl)
        flresult2 = pattern_Standard.findall(fl)

        # if flresult1 != []:
        #     flresult_list.append(fl)
        if flresult2 != []:
            flresult_list.append(fl)


    # print(flresult_list)
    # flresult_list包含支持目标框架和版本
    # ['.NETFramework2.0', '.NETFramework3.5']
    # .NETFramework4.5
    flresult_list_inorder = []

    for matching_framework in matching_framework_list:
        if targetFramework_name == matching_framework[0]:
            framework_version_list = matching_framework[1]
            for framework_version in framework_version_list:
                # print(framework_version)
                if framework_version in flresult_list:
                    flresult_list_inorder.append(framework_version)

    # if flresult_list_inorder == []:
    for matching_framework in matching_framework_list:

        if '.NETStandard' == matching_framework[0]:
            framework_version_list = matching_framework[1]
            for framework_version in framework_version_list:
                # print(framework_version)
                if framework_version in flresult_list:
                    flresult_list_inorder.append(framework_version)
    # 版本匹配
    # ['.NETFramework3.5', '.NETFramework2.0']

    for fll in flresult_list_inorder:

        status = 0
        fll_patt = r'%s' % targetFramework_name
        fll_patt2 = r'.NETStandard'
        fll_pattern = re.compile(fll_patt)
        fll_result = fll_pattern.findall(fll)

        fll_pattern2 = re.compile(fll_patt2)
        fll_result2 = fll_pattern2.findall(fll)



        if fll_result != []:
            # .NETFramework
            fll_name = fll_result[0]
            # ['3', '5', '0', '0']
            fll_version_list = re.split(targetFramework_name, fll)[1].split(".")
            for i in range(len(fll_version_list), 4):
                fll_version_list.append("0")
            # print(fll_name)
            # print(fll_version_list)

            for j in range(4):
                if fll_version_list[j] < targetFramework_version_list[j]:
                    status = 1
                    break
                if fll_version_list[j] > targetFramework_version_list[j]:
                    status = -1
                    break
            if status != -1:
                matching_targetFramework = fll
                break

        elif fll_result2 != []:
            status = 0
            fll_name = fll_result2[0]
            fll_version_list = re.split('.NETStandard', fll)[1].split(".")
            supportFramework_name = ""
            supportFramework_version_list = ""
            # 遍历NetStandard支持的框架
            for NetStandard_support in NetStandard_support_list:
                # 匹配NetStandard版本
                # print(NetStandard_support)
                if fll == NetStandard_support[0]:
                    support_list = NetStandard_support[1]

                    for support in support_list:
                        patt_s = r'%s' % targetFramework_name
                        pattern_s = re.compile(patt_s)
                        result = pattern_s.findall(support)

                        if result != []:
                            supportFramework_version_list = re.split(result[0], support)[1].split(".")

                            for i in range(len(supportFramework_version_list), 4):
                                supportFramework_version_list.append("0")
                            # print("supportFramework_version_list :", supportFramework_version_list)
                            # print("targetFramework_version_list :", targetFramework_version_list)
                            # print("fll :", fll)
                            version_status = 0
                            for j in range(4):
                                if supportFramework_version_list[j] < targetFramework_version_list[j]:
                                    version_status = 1
                                    break
                                if supportFramework_version_list[j] > targetFramework_version_list[j]:
                                    version_status = -1
                                    break
                            if version_status != -1:
                                # print("matching_targetFramework :",fll)
                                matching_targetFramework = fll
                                status = 2
                                break
                if status == 2:
                    break
            if status == 2:
                break

            # for j in range(4):
            #     if supportFramework_version_list[j] > targetFramework_version_list[j]:
            #         status = 1
            #         break
            # if status != 1:
            #     matching_targetFramework = fll
            #     break
            # print(NetStandard_support[1]) #.NETFramework4.6.1

            # print(fll)#.NETStandard2.0
            # print(fll_name)
            # print(fll_version_list)

    # print(flresult_list)
    # print(flresult_list_inorder)
    # print(matching_targetFramework)

    # line = "this hdr-biz model args= server= server"
    # patt = r'= server'
    # pattern = re.compile(patt)
    # result = pattern.findall(line)
    # print(result)

    return matching_targetFramework

#
# dependency_frameworkList = ['.NETCoreApp3.1', '.NETStandard2.0']
# # # dependency_frameworkList = [".NETFramework4.5", ".NETFramework3.5", ".NETStandard1.0", ".NETStandard2.0",
# # #                             ".NETPortable0.0-Profile328"]
# print(matching_framework(".NETCoreApp3.0", dependency_frameworkList))

