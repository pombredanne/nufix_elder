Deriving optimal dependency configurations for .NET projects.

### INTRODUCTION

.NET is an open-source development platform for building projects and sharing packages among them. As at March 2021, there are nine actively used and updated .NET platform variations available in 220 versions. A .NET package is often designed to assume a set of dependencies, which correspond to specific versions of .NET platforms and additional depended packages. These dependencies change as the .NET platforms and packages evolve, inducing compatibility issues. We call such issues Dependency Maze (DM) issues. We observe that multiple types of DM issues often occur in building a .NET project. Fixing a DM issue tends to introduce new DM issues. As a result, many fixes involve a set of changes made to a project's dependencies. Identifying these changes is challenging due to the large search space of finding possible dependency combinations.

To help .NET developers tackle the DM issues, we empirically studied a set of real DM issues, learning their common fixing strategies and developers' preferences in adopting these strategies. Based on these findings, we develop NuFix, an automated technique to repair DM issues. NuFix formulates the repair task as a binary integer linear optimization problem to effectively derive an optimal fix in line with the learnt developers' preferences. We applied NuFix to our benchmark containing 354 real DM issues with documented fixes. The evaluation results show that NuFix successfully generates fixes for all these DM issues.  The generated fixes are highly similar to the documented ones. Besides, we invited ten .NET experts to manually validate NuFix's generated fixes. Their feedback indicates that the fixes meet developers' desired properties for the build management of .NET projects.


### EMPIRICAL STUDY DATASET

EMPIRICAL STUDY EMPIRICAL STUDY EMPIRICAL STUDY EMPIRICAL STUDY

### BENCHMARK

<a href="https://github.com/nufix-dependency-maze/nufix/blob/gh-pages/Benchmark.zip?raw=true">Benchmark.zip</a>

<table style="text-align: center; white-space: nowrap; width: max-content; border-color: #000000">
        <tbody>
<tr>
  <td>id</td>
  <td>repository_full_name</span></td>
  <td>html_url</td>
  <td>title_info</td>
  <td>commit_date</span></td>
  <td>targetFramework</span></td>
  <td>directly_dependencies_count</span></td>
  <td>total_dep_count</span></td>
  <td>NU1605_count</span></td>
  <td>NU1107_count</span></td>
  <td>NU1202_count</span></td>
  <td>NU1608_count</span></td>
  <td>NU1103_count</span></td>
  <td>NU1701_count</span></td>
  <td>developer_directly_dependencies_count</span></td>
  <td>developer_total_dep_count</span></td>
  <td>developer_NU1608_count</span></td>
  <td>developer_NU1103_count</span></td>
  <td>developer_NU1701_count</span></td>
  <td>developer_major_count</span></td>
  <td>developer_change_directly_count</span></td>
  <td>SAT_directly_dependencies_count</span></td>
  <td>SAT_total_dep_count</span></td>
  <td>SAT_NU1608_count</span></td>
  <td>SAT_NU1103_count</span></td>
  <td>SAT_NU1701_count</span></td>
  <td>SAT_major_count</span></td>
  <td>SAT_change_directly_count</span></td>
  <td>difference_value_directly_dependencies_count</span></td>
  <td>difference_value_total_dep_count</span></td>
  <td>difference_value_warning_count</span></td>
  <td>difference_value_major_count</span></td>
  <td>difference_value_change_directly_count</span></td>
  <td >same_packageName_proportion</span></td>
  <td>same_packageMajorVersion_proportion</span></td>
  <td>same_dependencies_proportion</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9014</td>
  <td>arnoldasgu<span style='display:none'>das/Hangfire.MySqlStorage</span></td>
  <td>https://git<span style='display:none'>hub.com/arnoldasgudas/Hangfire.MySqlStorage/commit/a07d9d5273dfb87a2631c73b34658a87bfc43145</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Hangfire.MySql.Tests/<span
  style='display:none'>Hangfire.MySql.Tests.csproj</span></td>
  <td>.NETFrame<span style='display:none'>work4.5</span></td>
  <td align=right>8</td>
  <td align=right>9</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>7</td>
  <td align=right>7</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>-7</td>
  <td align=right>-1</td>
  <td align=right>-4</td>
  <td align=right>-1</td>
  <td align=right>-3</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.5714285<span style='display:none'>714285714</span></td>
  <td>0.5714285<span style='display:none'>714285714</span></td>
  <td>0.375</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9017</td>
  <td>Sharebook<span style='display:none'>BR/sharebook-backend</span></td>
  <td>https://git<span style='display:none'>hub.com/SharebookBR/sharebook-backend/commit/9b6e87d57feb5e6d0bfda6323a7f9cd7a3b2be21</span></td>
  <td colspan=2 style='mso-ignore:colspan'>ShareBook/ShareBook.<span
  style='display:none'>Tests.BDD/ShareBook.Tests.BDD.csproj</span></td>
  <td>net5.0</td>
  <td align=right>8</td>
  <td align=right>78</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>45</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>7</td>
  <td align=right>7</td>
  <td align=right>73</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td align=right>-7</td>
  <td align=right>28</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td align=right>-3</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.5714285<span style='display:none'>714285714</span></td>
  <td>0.375</td>
  <td>0.375</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9025</td>
  <td>threenine/<span style='display:none'>swcApi</span></td>
  <td>https://git<span style='display:none'>hub.com/threenine/swcApi/commit/48026b0cfd2ced740afad4cb803caa183320cf94</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Api.Database/Api.<span
  style='display:none'>Database.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>6</td>
  <td align=right>64</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>74</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>40</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>4</td>
  <td align=right>-5</td>
  <td align=right>-34</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.8</td>
  <td>0.8</td>
  <td colspan=2 style='mso-ignore:colspan'>0.2857142857142857</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9030</td>
  <td>R2D221/W<span style='display:none'>ebView2.DOM</span></td>
  <td>https://git<span style='display:none'>hub.com/R2D221/WebView2.DOM/commit/5ba200267beb7822ad86d03267de4065e0db50cd</span></td>
  <td colspan=2 style='mso-ignore:colspan'>WebView2.DOM/Web<span
  style='display:none'>View2.DOM.csproj</span></td>
  <td>net5.0</td>
  <td align=right>7</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>5</td>
  <td align=right>7</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>-7</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>-2</td>
  <td align=right>-2</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.3333333<span style='display:none'>333333333</span></td>
  <td>0.3333333<span style='display:none'>333333333</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.3333333333333333</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9031</td>
  <td>TodorStam<span style='display:none'>enov/GameBox</span></td>
  <td>https://git<span style='display:none'>hub.com/TodorStamenov/GameBox/commit/a738cffa6b9e1a22927b7c7b9f52380646cbd536</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Server/GameBox.Sche<span
  style='display:none'>duler/GameBox.Scheduler.csproj</span></td>
  <td>net5.0</td>
  <td align=right>5</td>
  <td align=right>36</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>46</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>5</td>
  <td align=right>37</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>-5</td>
  <td align=right>-9</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.8</td>
  <td>0.8</td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9039</td>
  <td>logcorner/L<span style='display:none'>ogCorner.EduSync.Speech.Command</span></td>
  <td>https://git<span style='display:none'>hub.com/logcorner/LogCorner.EduSync.Speech.Command/commit/d676918357650f9e3b8d3294cd220f38db55bf22</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/LogCorner.EduSync<span
  style='display:none'>.Speech/LogCorner.EduSync.Speech.Presentation/LogCorner.EduSync.Speech.Presentation.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>5</td>
  <td align=right>94</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>3</td>
  <td align=right>3</td>
  <td align=right>4</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>3</td>
  <td align=right>-4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>1.0</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9042</td>
  <td>enisn/Auto<span style='display:none'>Filterer</span></td>
  <td>https://git<span style='display:none'>hub.com/enisn/AutoFilterer/commit/a97399a53a06888dcd4d9d151f450b15653c2bd0</span></td>
  <td colspan=2 style='mso-ignore:colspan'>sandbox/WebApplicati<span
  style='display:none'>on.API/WebApplication.API.csproj</span></td>
  <td>net5.0</td>
  <td align=right>5</td>
  <td align=right>38</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>37</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>37</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>-5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.75</td>
  <td>0.75</td>
  <td>0.4</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9043</td>
  <td>rockfordlh<span style='display:none'>otka/Cloud-Native-HOL</span></td>
  <td>https://git<span style='display:none'>hub.com/rockfordlhotka/Cloud-Native-HOL/commit/4c655ccf40c8932a1ab74ac8e65ca8d80c54bfe8</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Lab03/End/BreadS<span
  style='display:none'>ervice/BreadService.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.0</span></td>
  <td align=right>5</td>
  <td align=right>75</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>24</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>4</td>
  <td align=right>24</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>-4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.3333333333333333</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9049</td>
  <td>signumsoft<span style='display:none'>ware/southwind</span></td>
  <td>https://git<span style='display:none'>hub.com/signumsoftware/southwind/commit/db5736eff63bd240d78f27a6db71ab693c5903f8</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Southwind.React/Sout<span
  style='display:none'>hwind.React.csproj</span></td>
  <td>net5.0</td>
  <td align=right>6</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>10</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>10</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>-5</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.6666666<span style='display:none'>666666666</span></td>
  <td>0.6666666<span style='display:none'>666666666</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.6666666666666666</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9067</td>
  <td>pekkah/tan<span style='display:none'>ka-graphql-samples</span></td>
  <td>https://git<span style='display:none'>hub.com/pekkah/tanka-graphql-samples/commit/20d0856841f0010b7a88051c2693c53335dfbdea</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Host/Host.csproj</td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>8</td>
  <td align=right>84</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>87</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>7</td>
  <td align=right>9</td>
  <td align=right>84</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>6</td>
  <td align=right>-9</td>
  <td align=right>-3</td>
  <td align=right>-2</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.4444444<span style='display:none'>444444444</span></td>
  <td>0.4444444<span style='display:none'>444444444</span></td>
  <td colspan=3 style='mso-ignore:colspan'>0.18181818181818182</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9071</td>
  <td>ismaelham<span style='display:none'>ed/akka-cluster-management</span></td>
  <td>https://git<span style='display:none'>hub.com/ismaelhamed/akka-cluster-management/commit/fa190f5c13008ec2b54693c37c683c73ae02b8ad</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Akka.Cluster.Mana<span
  style='display:none'>gement/Akka.Cluster.Management.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>6</td>
  <td align=right>109</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>119</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>6</td>
  <td align=right>119</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>-6</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.8</td>
  <td>0.8</td>
  <td>0.125</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9078</td>
  <td>ysmoradi/B<span style='display:none'>itSampleApp</span></td>
  <td>https://git<span style='display:none'>hub.com/ysmoradi/BitSampleApp/commit/6e89f190d0421149f36e8ea0d8cc2ab70764e901</span></td>
  <td colspan=2 style='mso-ignore:colspan'>SampleApp/SampleAp<span
  style='display:none'>p.csproj</span></td>
  <td>net5.0</td>
  <td align=right>8</td>
  <td align=right>162</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>179</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>6</td>
  <td align=right>8</td>
  <td align=right>182</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>5</td>
  <td align=right>-8</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.5714285<span style='display:none'>714285714</span></td>
  <td>0.5714285<span style='display:none'>714285714</span></td>
  <td>0.375</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9079</td>
  <td>ysmoradi/B<span style='display:none'>itSampleApp</span></td>
  <td>https://git<span style='display:none'>hub.com/ysmoradi/BitSampleApp/commit/4d9891d0d99571a64c9a26e8f927643da6b821bf</span></td>
  <td colspan=2 style='mso-ignore:colspan'>SampleApp/SampleAp<span
  style='display:none'>p.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>11</td>
  <td align=right>217</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>51</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>8</td>
  <td align=right>124</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>-8</td>
  <td align=right>73</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.8571428<span style='display:none'>571428571</span></td>
  <td>0.8571428<span style='display:none'>571428571</span></td>
  <td>0.625</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9081</td>
  <td>net-daemo<span style='display:none'>n/net-hassclient</span></td>
  <td>https://git<span style='display:none'>hub.com/net-daemon/net-hassclient/commit/0bf4f7dee4b766e81f7059598d05794f235497b6</span></td>
  <td colspan=2 style='mso-ignore:colspan'>tests/HassClient.Unit.T<span
  style='display:none'>ests/HassClient.Unit.Tests.csproj</span></td>
  <td>net5.0</td>
  <td align=right>8</td>
  <td align=right>47</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>81</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>4</td>
  <td align=right>9</td>
  <td align=right>81</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>-9</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>1</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.5</td>
  <td>0.5</td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9085</td>
  <td>ricardocma<span style='display:none'>rtin/3d-social-backend</span></td>
  <td>https://git<span style='display:none'>hub.com/ricardocmartin/3d-social-backend/commit/ec478ff4cc2cc298d470170cd7ae4e9b35aed4b8</span></td>
  <td colspan=2 style='mso-ignore:colspan'>3dSocial.Api/3dSocial.<span
  style='display:none'>Api.Test/3dSocial.Api.Test.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.0</span></td>
  <td align=right>5</td>
  <td align=right>94</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>43</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>4</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>3</td>
  <td align=right>-4</td>
  <td align=right>-39</td>
  <td align=right>-3</td>
  <td align=right>1</td>
  <td align=right>-1</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.75</td>
  <td>0.4</td>
  <td>0.4</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9086</td>
  <td>Nedevski/P<span style='display:none'>anasonicACRemote.VoiceControlLambda</span></td>
  <td>https://git<span style='display:none'>hub.com/Nedevski/PanasonicACRemote.VoiceControlLambda/commit/1e67a2b059db347ce24671af3c4e17397e2e4e17</span></td>
  <td colspan=2 style='mso-ignore:colspan'>PanasonicACVoiceRem<span
  style='display:none'>ote/PanasonicACVoiceRemote.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.1</span></td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>41</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>4</td>
  <td align=right>41</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>-4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.6666666<span style='display:none'>666666666</span></td>
  <td>0.6666666<span style='display:none'>666666666</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.6666666666666666</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9099</td>
  <td>SkillsFundi<span style='display:none'>ngAgency/dss-changefeedsqlprocessor</span></td>
  <td>https://git<span style='display:none'>hub.com/SkillsFundingAgency/dss-changefeedsqlprocessor/commit/9eb6b51b3eecc7fa83c5dd8bbda746fda56d585b</span></td>
  <td colspan=2 style='mso-ignore:colspan'>NCS.DSS.ChangeFeedS<span
  style='display:none'>qlProcessor/NCS.DSS.ChangeFeedSqlProcessor.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>8</td>
  <td align=right>143</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>146</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>8</td>
  <td align=right>141</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>-8</td>
  <td align=right>-5</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.7142857<span style='display:none'>142857143</span></td>
  <td>0.7142857<span style='display:none'>142857143</span></td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9100</td>
  <td>latinoneto<span style='display:none'>nline/LatinoNETOnline.App</span></td>
  <td>https://git<span style='display:none'>hub.com/latinonetonline/LatinoNETOnline.App/commit/082804a120ca6c3a4f1e3c87e82f121263f68349</span></td>
  <td colspan=2 style='mso-ignore:colspan'>LatinoNETOnline.App/<span
  style='display:none'>Server/LatinoNETOnline.App.Server.csproj</span></td>
  <td>net5.0</td>
  <td align=right>6</td>
  <td align=right>13</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td align=right>-5</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>-1</td>
  <td align=right>-1</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.8</td>
  <td>0.8</td>
  <td>0.8</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9101</td>
  <td>latinoneto<span style='display:none'>nline/LatinoNETOnline.App</span></td>
  <td>https://git<span style='display:none'>hub.com/latinonetonline/LatinoNETOnline.App/commit/fcb560e7ab085e73eae9d1e773449c4fbe642d75</span></td>
  <td colspan=2 style='mso-ignore:colspan'>LatinoNETOnline.App/<span
  style='display:none'>Server/LatinoNETOnline.App.Server.csproj</span></td>
  <td>net5.0</td>
  <td align=right>6</td>
  <td align=right>13</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>1</td>
  <td align=right>2</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td align=right>-5</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>-1</td>
  <td align=right>-1</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.8</td>
  <td>0.8</td>
  <td>0.8</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9105</td>
  <td>pact-found<span style='display:none'>ation/pact-net</span></td>
  <td>https://git<span style='display:none'>hub.com/pact-foundation/pact-net/commit/130d8b97a4aa28dd2b9361e22e51d836005ea825</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Samples/EventApi/Con<span
  style='display:none'>sumer.Tests/Consumer.Tests.csproj</span></td>
  <td>.NETFrame<span style='display:none'>work4.6</span></td>
  <td align=right>6</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>6</td>
  <td align=right>6</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>-6</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>-1</td>
  <td align=right>-1</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.8333333<span style='display:none'>333333334</span></td>
  <td>0.8333333<span style='display:none'>333333334</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.8333333333333334</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9109</td>
  <td>arcus-azure<span style='display:none'>/arcus.eventgrid.proxy</span></td>
  <td>https://git<span style='display:none'>hub.com/arcus-azure/arcus.eventgrid.proxy/commit/637fbcac8afe933f0be934f001b65a53546091af</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Arcus.EventGrid.Pr<span
  style='display:none'>oxy.Api/Arcus.EventGrid.Proxy.Api.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>6</td>
  <td align=right>119</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>102</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>4</td>
  <td align=right>8</td>
  <td align=right>115</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>5</td>
  <td align=right>-8</td>
  <td align=right>13</td>
  <td align=right>-1</td>
  <td align=right>-3</td>
  <td align=right>1</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.2857142<span style='display:none'>857142857</span></td>
  <td>0.0</td>
  <td>0.0</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9122</td>
  <td>Fresa/Port</td>
  <td>https://git<span style='display:none'>hub.com/Fresa/Port/commit/cf9af696b854d7f8ee8fa13ff4e158ee6fb67f03</span></td>
  <td colspan=2 style='mso-ignore:colspan'>tests/Kubernetes.Test.<span
  style='display:none'>API.Server/Kubernetes.Test.API.Server.csproj</span></td>
  <td>net5.0</td>
  <td align=right>6</td>
  <td align=right>69</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>64</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td align=right>7</td>
  <td align=right>64</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>6</td>
  <td align=right>-7</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.6666666<span style='display:none'>666666666</span></td>
  <td>0.6666666<span style='display:none'>666666666</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.6666666666666666</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9123</td>
  <td>Fresa/Port</td>
  <td>https://git<span style='display:none'>hub.com/Fresa/Port/commit/cf9af696b854d7f8ee8fa13ff4e158ee6fb67f03</span></td>
  <td colspan=2 style='mso-ignore:colspan'>tests/Port.Server.Integ<span
  style='display:none'>rationTests/Port.Server.IntegrationTests.csproj</span></td>
  <td>net5.0</td>
  <td align=right>11</td>
  <td align=right>96</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>87</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>5</td>
  <td align=right>14</td>
  <td align=right>97</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>6</td>
  <td align=right>-14</td>
  <td align=right>10</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>1</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.375</td>
  <td>0.375</td>
  <td>0.375</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9126</td>
  <td>ops-ai/Bey<span style='display:none'>ondAuth</span></td>
  <td>https://git<span style='display:none'>hub.com/ops-ai/BeyondAuth/commit/6a5de6939f7bcc586d214994503deaa60c78ea4d</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Bridges/DiameterS<span
  style='display:none'>erver/DiameterServer.csproj</span></td>
  <td>net5.0</td>
  <td align=right>6</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>74</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>29</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>5</td>
  <td align=right>-5</td>
  <td align=right>-45</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=3 style='mso-ignore:colspan'>0.42857142857142855</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9127</td>
  <td>ops-ai/Bey<span style='display:none'>ondAuth</span></td>
  <td>https://git<span style='display:none'>hub.com/ops-ai/BeyondAuth/commit/6a5de6939f7bcc586d214994503deaa60c78ea4d</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Bridges/RadiusServ<span
  style='display:none'>er/RadiusServer.csproj</span></td>
  <td>net5.0</td>
  <td align=right>7</td>
  <td align=right>30</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>28</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>5</td>
  <td align=right>7</td>
  <td align=right>30</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>6</td>
  <td align=right>-7</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.8333333<span style='display:none'>333333334</span></td>
  <td>0.8333333<span style='display:none'>333333334</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.8333333333333334</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9142</td>
  <td>jamerst/Op<span style='display:none'>enLD</span></td>
  <td>https://git<span style='display:none'>hub.com/jamerst/OpenLD/commit/01d161808e9476ba6b7f2a120035e504acfeee5c</span></td>
  <td colspan=2 style='mso-ignore:colspan'>openld.Tests/openld.T<span
  style='display:none'>ests.csproj</span></td>
  <td>net5.0</td>
  <td align=right>12</td>
  <td align=right>112</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>114</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>11</td>
  <td align=right>11</td>
  <td align=right>107</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>8</td>
  <td align=right>-11</td>
  <td align=right>-7</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-3</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.7272727<span style='display:none'>272727273</span></td>
  <td>0.4615384<span style='display:none'>6153846156</span></td>
  <td colspan=3 style='mso-ignore:colspan'>0.46153846153846156</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9148</td>
  <td>dr1rrb/sma<span style='display:none'>rthome.net</span></td>
  <td>https://git<span style='display:none'>hub.com/dr1rrb/smarthome.net/commit/943a70c58726bf466c3e6e942be52bbd1464e115</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/SmartHomeDotNet<span
  style='display:none'>Host/SmartHomeDotNetHost.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>11</td>
  <td align=right>56</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>46</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>2</td>
  <td align=right>3</td>
  <td align=right>10</td>
  <td align=right>10</td>
  <td align=right>50</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>8</td>
  <td align=right>-10</td>
  <td align=right>4</td>
  <td align=right>-2</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.8</td>
  <td>0.6363636<span style='display:none'>363636364</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.6363636363636364</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9150</td>
  <td>dr1rrb/sma<span style='display:none'>rthome.net</span></td>
  <td>https://git<span style='display:none'>hub.com/dr1rrb/smarthome.net/commit/646232e0a1c757b89a40c7ed25b9a54ee929506f</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/SmartHomeDotNet<span
  style='display:none'>Host/SmartHomeDotNetHost.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>11</td>
  <td align=right>56</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>46</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>10</td>
  <td align=right>10</td>
  <td align=right>50</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>8</td>
  <td align=right>-10</td>
  <td align=right>4</td>
  <td align=right>-2</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.8</td>
  <td>0.6363636<span style='display:none'>363636364</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.6363636363636364</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9151</td>
  <td>stensolino/<span style='display:none'>PersonalAccounting</span></td>
  <td>https://git<span style='display:none'>hub.com/stensolino/PersonalAccounting/commit/68b3e17c772e151314ab8552871720d99cdd021f</span></td>
  <td colspan=2 style='mso-ignore:colspan'>PersonalAccounting/P<span
  style='display:none'>ersonalAccounting.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>6</td>
  <td align=right>35</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>35</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>6</td>
  <td align=right>35</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>-6</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.8333333<span style='display:none'>333333334</span></td>
  <td>0.8333333<span style='display:none'>333333334</span></td>
  <td>0.0</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9163</td>
  <td>Delirios/Ta<span style='display:none'>xiService</span></td>
  <td>https://git<span style='display:none'>hub.com/Delirios/TaxiService/commit/d33107c5ba2806a65a41ab8ec534c03676f6f113</span></td>
  <td colspan=2 style='mso-ignore:colspan'>TaxiService.News/Taxi<span
  style='display:none'>Service.News.csproj</span></td>
  <td>net5.0</td>
  <td align=right>5</td>
  <td align=right>105</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>104</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>4</td>
  <td align=right>104</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>-4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.3333333333333333</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9165</td>
  <td>daxnet/aba<span style='display:none'>cuza</span></td>
  <td>https://git<span style='display:none'>hub.com/daxnet/abacuza/commit/b0835392a2c65ea95793e23bc6ebb6a872383932</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/services/clusters/A<span
  style='display:none'>bacuza.Clusters.ApiService/Abacuza.Clusters.ApiService.csproj</span></td>
  <td>net5.0</td>
  <td align=right>7</td>
  <td align=right>35</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>31</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>7</td>
  <td align=right>34</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>-7</td>
  <td align=right>3</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.6</td>
  <td>0.6</td>
  <td colspan=2 style='mso-ignore:colspan'>0.3333333333333333</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9167</td>
  <td>daxnet/aba<span style='display:none'>cuza</span></td>
  <td>https://git<span style='display:none'>hub.com/daxnet/abacuza/commit/b0835392a2c65ea95793e23bc6ebb6a872383932</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/services/projects/A<span
  style='display:none'>bacuza.Projects.ApiService/Abacuza.Projects.ApiService.csproj</span></td>
  <td>net5.0</td>
  <td align=right>5</td>
  <td align=right>31</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>30</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td align=right>4</td>
  <td align=right>30</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>-4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>-2</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.5</td>
  <td>0.5</td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9170</td>
  <td>pact-found<span style='display:none'>ation/pact-net</span></td>
  <td>https://git<span style='display:none'>hub.com/pact-foundation/pact-net/commit/470f7020d763905c85816167ef21466fc46ced74</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Samples/EventApi/Con<span
  style='display:none'>sumer.Tests/Consumer.Tests.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>5</td>
  <td align=right>77</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>6</td>
  <td align=right>6</td>
  <td align=right>78</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>-6</td>
  <td align=right>72</td>
  <td align=right>-2</td>
  <td align=right>-1</td>
  <td align=right>-1</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.8333333<span style='display:none'>333333334</span></td>
  <td>0.8333333<span style='display:none'>333333334</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.8333333333333334</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9175</td>
  <td>MicrosoftL<span style='display:none'>earning/AI-100-Design-Implement-Azure-AISol</span></td>
  <td>https://git<span style='display:none'>hub.com/MicrosoftLearning/AI-100-Design-Implement-Azure-AISol/commit/14cbd42faef0637fefc4a2acc0e2cba81715c334</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Lab3-Basic_Filter_Bot/<span
  style='display:none'>code/Finished/PictureBot/PictureBot.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.1</span></td>
  <td align=right>7</td>
  <td align=right>91</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>79</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>5</td>
  <td align=right>6</td>
  <td align=right>126</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>-6</td>
  <td align=right>47</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>-2</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.6</td>
  <td>0.6</td>
  <td colspan=2 style='mso-ignore:colspan'>0.3333333333333333</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9176</td>
  <td>JuergenGut<span style='display:none'>sch/graphql-aspnetcore</span></td>
  <td>https://git<span style='display:none'>hub.com/JuergenGutsch/graphql-aspnetcore/commit/3ce31196e0a691c66156248c57a861bf4db48430</span></td>
  <td colspan=2 style='mso-ignore:colspan'>GraphQl.AspNetCore/<span
  style='display:none'>GraphQl.AspNetCore.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>6</td>
  <td align=right>86</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>189</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>7</td>
  <td align=right>129</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>6</td>
  <td align=right>-7</td>
  <td align=right>-60</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>1</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.5714285<span style='display:none'>714285714</span></td>
  <td>0.375</td>
  <td>0.375</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9180</td>
  <td>revaturexy<span style='display:none'>z/housingxyz</span></td>
  <td>https://git<span style='display:none'>hub.com/revaturexyz/housingxyz/commit/ec81ef6623c39fce35f74bc0d6354ca9d5149f5b</span></td>
  <td colspan=2 style='mso-ignore:colspan'>account/src/Revature.<span
  style='display:none'>Account.Tests/Revature.Account.Tests.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>7</td>
  <td align=right>58</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>97</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>6</td>
  <td align=right>93</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>4</td>
  <td align=right>-6</td>
  <td align=right>-4</td>
  <td align=right>-1</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.6</td>
  <td>0.6</td>
  <td>0.6</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9181</td>
  <td>revaturexy<span style='display:none'>z/housingxyz</span></td>
  <td>https://git<span style='display:none'>hub.com/revaturexyz/housingxyz/commit/82041eede0256cdf326e1084fa4a85287126eb0e</span></td>
  <td colspan=2 style='mso-ignore:colspan'>account/src/Revature.<span
  style='display:none'>Account.Tests/Revature.Account.Tests.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>7</td>
  <td align=right>58</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>97</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>6</td>
  <td align=right>93</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>4</td>
  <td align=right>-6</td>
  <td align=right>-4</td>
  <td align=right>-1</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.6</td>
  <td>0.6</td>
  <td>0.6</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9187</td>
  <td>hsourcer/h<span style='display:none'>sourcer-backend</span></td>
  <td>https://git<span style='display:none'>hub.com/hsourcer/hsourcer-backend/commit/b890e24eef5bafd86c6472c0d6bc26e36c8875a3</span></td>
  <td colspan=2 style='mso-ignore:colspan'>HsourcerXUnitTest/Hs<span
  style='display:none'>ourcerXUnitTest.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.2</span></td>
  <td align=right>6</td>
  <td align=right>95</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>78</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>71</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td align=right>-5</td>
  <td align=right>-7</td>
  <td align=right>-3</td>
  <td align=right>1</td>
  <td align=right>-1</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.8</td>
  <td>0.5</td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9188</td>
  <td>phongnguy<span style='display:none'>end/Practical.CleanArchitecture</span></td>
  <td>https://git<span style='display:none'>hub.com/phongnguyend/Practical.CleanArchitecture/commit/202604d7a6c3817966e3988634398697ff1cb3f5</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Microservices/Serv<span
  style='display:none'>ices.Storage/ClassifiedAds.Services.Storage.Api/ClassifiedAds.Services.Storage.Api.csproj</span></td>
  <td>net5.0</td>
  <td align=right>442</td>
  <td align=right>55</td>
  <td align=right>28</td>
  <td align=right>2</td>
  <td align=right>4</td>
  <td align=right>2</td>
  <td align=right>16</td>
  <td align=right>0</td>
  <td align=right>13</td>
  <td align=right>83</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>95</td>
  <td align=right>8</td>
  <td align=right>12</td>
  <td align=right>85</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>46</td>
  <td align=right>9</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>-1</td>
  <td align=right>-49</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>1.0833333<span style='display:none'>333333333</span></td>
  <td>0.6666666<span style='display:none'>666666666</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.3888888888888889</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9189</td>
  <td>MichaCo/A<span style='display:none'>spNetCore.Services</span></td>
  <td>https://git<span style='display:none'>hub.com/MichaCo/AspNetCore.Services/commit/333cb490f2ec922b3d70de3592946ca8ee62cc9d</span></td>
  <td colspan=2 style='mso-ignore:colspan'>ConsulExample/src/ser<span
  style='display:none'>vices/DataService/DataService.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.0</span></td>
  <td align=right>264</td>
  <td align=right>175</td>
  <td align=right>60</td>
  <td align=right>2</td>
  <td align=right>3</td>
  <td align=right>4</td>
  <td align=right>18</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>175</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>5</td>
  <td align=right>8</td>
  <td align=right>172</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>-3</td>
  <td align=right>-2</td>
  <td align=right>-5</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.125</td>
  <td>0.8888888<span style='display:none'>888888888</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.4166666666666667</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9190</td>
  <td>JonPSmith/<span style='display:none'>EfCoreinAction-SecondEdition</span></td>
  <td>https://git<span style='display:none'>hub.com/JonPSmith/EfCoreinAction-SecondEdition/commit/e8baacf0651b3797175858d588e95b699900df5a</span></td>
  <td colspan=2 style='mso-ignore:colspan'>BookApp/BookApp.csp<span
  style='display:none'>roj</span></td>
  <td>net5.0</td>
  <td align=right>272</td>
  <td align=right>99</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>137</td>
  <td align=right>2</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>137</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-3</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>0.8333333<span style='display:none'>333333334</span></td>
  <td>0.8333333<span style='display:none'>333333334</span></td>
  <td>0.375</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9191</td>
  <td>theolivenb<span style='display:none'>aum/h5</span></td>
  <td>https://git<span style='display:none'>hub.com/theolivenbaum/h5/commit/49ad367527f5a82d9db8fea851704ae91b77e14b</span></td>
  <td colspan=2 style='mso-ignore:colspan'>H5/Compiler/Compiler<span
  style='display:none'>.Service/H5.Compiler.Service.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.1</span></td>
  <td align=right>858</td>
  <td align=right>140</td>
  <td align=right>8</td>
  <td align=right>2</td>
  <td align=right>11</td>
  <td align=right>2</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>27</td>
  <td align=right>140</td>
  <td align=right>2</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>15</td>
  <td align=right>27</td>
  <td align=right>129</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>13</td>
  <td align=right>0</td>
  <td align=right>-11</td>
  <td align=right>-1</td>
  <td align=right>-3</td>
  <td align=right>-2</td>
  <td>1:1:0.01</td>
  <td>0.9285714<span style='display:none'>285714286</span></td>
  <td>0.8620689<span style='display:none'>655172413</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.8620689655172413</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9192</td>
  <td>Djohnnie/<span style='display:none'>MijnSauna</span></td>
  <td>https://git<span style='display:none'>hub.com/Djohnnie/MijnSauna/commit/afb175f255c45830a15fe43d4c1d7ccbce1b9f8a</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/MijnSauna.Fronten<span
  style='display:none'>d.Phone/MijnSauna.Frontend.Phone/MijnSauna.Frontend.Phone.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>272</td>
  <td align=right>79</td>
  <td align=right>39</td>
  <td align=right>2</td>
  <td align=right>6</td>
  <td align=right>2</td>
  <td align=right>14</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>32</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>6</td>
  <td align=right>8</td>
  <td align=right>78</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>46</td>
  <td align=right>0</td>
  <td align=right>-4</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>0.7142857<span style='display:none'>142857143</span></td>
  <td>0.5</td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9193</td>
  <td>EvolutionPl<span style='display:none'>ugins/Dummy</span></td>
  <td>https://git<span style='display:none'>hub.com/EvolutionPlugins/Dummy/commit/a2866da31ce9c9609313cbbc9defcc1d7acadf84</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Dummy/Dummy.csproj</td>
  <td>.NETFrame<span style='display:none'>work4.6.1</span></td>
  <td align=right>153</td>
  <td align=right>139</td>
  <td align=right>3</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>134</td>
  <td align=right>2</td>
  <td align=right>1</td>
  <td align=right>1</td>
  <td align=right>3</td>
  <td align=right>6</td>
  <td align=right>7</td>
  <td align=right>132</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>-1</td>
  <td align=right>-3</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.7777777<span style='display:none'>777777778</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.7777777777777778</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9194</td>
  <td>by-pinja/p<span style='display:none'>df-storage</span></td>
  <td>https://git<span style='display:none'>hub.com/by-pinja/pdf-storage/commit/7252bed70c7b3b2d2bddf6a50e6cd50abf16b34b</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Pdf.Storage.csproj</td>
  <td>.NETCoreA<span style='display:none'>pp2.2</span></td>
  <td align=right>647</td>
  <td align=right>319</td>
  <td align=right>14</td>
  <td align=right>2</td>
  <td align=right>24</td>
  <td align=right>4</td>
  <td align=right>104</td>
  <td align=right>0</td>
  <td align=right>20</td>
  <td align=right>307</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>131</td>
  <td align=right>8</td>
  <td align=right>20</td>
  <td align=right>303</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>117</td>
  <td align=right>12</td>
  <td align=right>0</td>
  <td align=right>-4</td>
  <td align=right>0</td>
  <td align=right>-14</td>
  <td align=right>4</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.9047619<span style='display:none'>047619048</span></td>
  <td colspan=3 style='mso-ignore:colspan'>0.42857142857142855</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9195</td>
  <td>Q42/Dyna<span style='display:none'>micDataCMS</span></td>
  <td>https://git<span style='display:none'>hub.com/Q42/DynamicDataCMS/commit/35fb66f8455a31e1a982b290209b3feed68b5ecc</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/QMS.Core.Services<span
  style='display:none'>/QMS.Core.Services.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.1</span></td>
  <td align=right>299</td>
  <td align=right>90</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>3</td>
  <td align=right>2</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>65</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>8</td>
  <td align=right>94</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>29</td>
  <td align=right>0</td>
  <td align=right>-3</td>
  <td align=right>2</td>
  <td>1:1:0.01</td>
  <td>0.8888888<span style='display:none'>888888888</span></td>
  <td>0.5454545<span style='display:none'>454545454</span></td>
  <td colspan=3 style='mso-ignore:colspan'>0.21428571428571427</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9196</td>
  <td>govau/digit<span style='display:none'>almarketplace</span></td>
  <td>https://git<span style='display:none'>hub.com/govau/digitalmarketplace/commit/ea3648dccc2ccce1aba8b24bf14a49627cb1cc7f</span></td>
  <td colspan=2 style='mso-ignore:colspan'>subscribers/email.logg<span
  style='display:none'>er/worker/worker.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>849</td>
  <td align=right>113</td>
  <td align=right>8</td>
  <td align=right>2</td>
  <td align=right>9</td>
  <td align=right>2</td>
  <td align=right>10</td>
  <td align=right>0</td>
  <td align=right>21</td>
  <td align=right>55</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>10</td>
  <td align=right>13</td>
  <td align=right>21</td>
  <td align=right>57</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>12</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>-7</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>0.9090909<span style='display:none'>090909091</span></td>
  <td>0.68</td>
  <td colspan=2 style='mso-ignore:colspan'>0.6153846153846154</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9197</td>
  <td>jcapellman<span style='display:none'>/DMTP</span></td>
  <td>https://git<span style='display:none'>hub.com/jcapellman/DMTP/commit/b05340ad53379623b53710e1ef3566d8fc51a28e</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/DMTP.REST/DMTP.<span
  style='display:none'>REST.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>700</td>
  <td align=right>182</td>
  <td align=right>28</td>
  <td align=right>2</td>
  <td align=right>3</td>
  <td align=right>2</td>
  <td align=right>14</td>
  <td align=right>0</td>
  <td align=right>17</td>
  <td align=right>181</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>88</td>
  <td align=right>4</td>
  <td align=right>16</td>
  <td align=right>181</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>44</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>-44</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0625</td>
  <td>0.8333333<span style='display:none'>333333334</span></td>
  <td>0.65</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9198</td>
  <td>LykkeCity/L<span style='display:none'>ykke.Service.HftInternalService</span></td>
  <td>https://git<span style='display:none'>hub.com/LykkeCity/Lykke.Service.HftInternalService/commit/63c1a10a7bb63b4d0c4c51379c6d851da8a992c2</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Lykke.Service.HftIn<span
  style='display:none'>ternalService.Services/Lykke.Service.HftInternalService.Services.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.1</span></td>
  <td align=right>135</td>
  <td align=right>338</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>1</td>
  <td align=right>2</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>297</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>4</td>
  <td align=right>6</td>
  <td align=right>329</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>32</td>
  <td align=right>-1</td>
  <td align=right>-2</td>
  <td align=right>2</td>
  <td>1:1:0.01</td>
  <td>0.8571428<span style='display:none'>571428571</span></td>
  <td>0.8571428<span style='display:none'>571428571</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.4444444444444444</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9199</td>
  <td>LykkeCity/L<span style='display:none'>ykke.Service.HftInternalService</span></td>
  <td>https://git<span style='display:none'>hub.com/LykkeCity/Lykke.Service.HftInternalService/commit/57b7bdc1ab6bf3c0e3e9f3e96178e60a55a99dc7</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Lykke.Service.HftIn<span
  style='display:none'>ternalService.Services/Lykke.Service.HftInternalService.Services.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.1</span></td>
  <td align=right>135</td>
  <td align=right>338</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>1</td>
  <td align=right>2</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>297</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>4</td>
  <td align=right>6</td>
  <td align=right>329</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>32</td>
  <td align=right>-1</td>
  <td align=right>-2</td>
  <td align=right>2</td>
  <td>1:1:0.01</td>
  <td>0.8571428<span style='display:none'>571428571</span></td>
  <td>0.8571428<span style='display:none'>571428571</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.4444444444444444</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9200</td>
  <td>matand/ba<span style='display:none'>nkor</span></td>
  <td>https://git<span style='display:none'>hub.com/matand/bankor/commit/82605778955c716a7d92f2dde267a936e0b2a988</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Bancor.Api/Bancor<span
  style='display:none'>.Api.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.0</span></td>
  <td align=right>326</td>
  <td align=right>264</td>
  <td align=right>8</td>
  <td align=right>5</td>
  <td align=right>3</td>
  <td align=right>2</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>124</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>8</td>
  <td align=right>7</td>
  <td align=right>121</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>-3</td>
  <td align=right>-1</td>
  <td align=right>-1</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>0.875</td>
  <td>0.6666666<span style='display:none'>666666666</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.6666666666666666</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9201</td>
  <td>aiba1805/T<span style='display:none'>askTrackingSystem</span></td>
  <td>https://git<span style='display:none'>hub.com/tsukidaime/TaskTrackingSystem/commit/2856879ba01f77b2558e9eef4c7bb93ca34c0718</span></td>
  <td colspan=2 style='mso-ignore:colspan'>TTS.Web/TTS.Web.csp<span
  style='display:none'>roj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.0</span></td>
  <td align=right>655</td>
  <td align=right>129</td>
  <td align=right>1</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>15</td>
  <td align=right>130</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>3</td>
  <td align=right>14</td>
  <td align=right>13</td>
  <td align=right>127</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>-3</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>-7</td>
  <td>1:1:0.01</td>
  <td>0.8666666<span style='display:none'>666666667</span></td>
  <td>0.8666666<span style='display:none'>666666667</span></td>
  <td>0.75</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9202</td>
  <td>guigomesa<span style='display:none'>/ScrapyTibiaCSharp</span></td>
  <td>https://git<span style='display:none'>hub.com/guigomesa/ScrapyTibiaCSharp/commit/b7f6c6908b7faca54f6e9f1269f88424a6ca41ba</span></td>
  <td colspan=2 style='mso-ignore:colspan'>TibiaApi/TibiaApi.Web<span
  style='display:none'>.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>762</td>
  <td align=right>294</td>
  <td align=right>2</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>19</td>
  <td align=right>327</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>10</td>
  <td align=right>18</td>
  <td align=right>326</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>10</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>0.9473684<span style='display:none'>210526315</span></td>
  <td>0.85</td>
  <td>0.48</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9203</td>
  <td>JanKnipp/T<span style='display:none'>emplate_NET_5_WORKER</span></td>
  <td>https://git<span style='display:none'>hub.com/JanKnipp/Template_NET_5_WORKER/commit/b05d6a11b72283444cbb916bf86852e307253297</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Template_NET_CO<span
  style='display:none'>RE_3_WORKER.CoreService/Template_NET_CORE_3_WORKER.CoreService.csproj→src/Template_NET_5_WORKER.CoreService/Template_NET_5_WORKER.CoreService.csproj</span></td>
  <td>net5.0</td>
  <td align=right>1348</td>
  <td align=right>174</td>
  <td align=right>33</td>
  <td align=right>2</td>
  <td align=right>16</td>
  <td align=right>2</td>
  <td align=right>15</td>
  <td align=right>0</td>
  <td align=right>38</td>
  <td align=right>104</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>17</td>
  <td align=right>24</td>
  <td align=right>37</td>
  <td align=right>168</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>13</td>
  <td align=right>23</td>
  <td align=right>0</td>
  <td align=right>64</td>
  <td align=right>-1</td>
  <td align=right>-4</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>1.0270270<span style='display:none'>27027027</span></td>
  <td>0.9736842<span style='display:none'>105263158</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.6304347826086957</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9204</td>
  <td>mp1011/Jir<span style='display:none'>aGraphThing</span></td>
  <td>https://git<span style='display:none'>hub.com/mp1011/JiraGraphThing/commit/50b8349a2f1a136672fcf62c05c66178b78f976c</span></td>
  <td colspan=2 style='mso-ignore:colspan'>JiraDataLayer/JiraData<span
  style='display:none'>Layer.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>276</td>
  <td align=right>57</td>
  <td align=right>4</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>10</td>
  <td align=right>32</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>1</td>
  <td align=right>3</td>
  <td align=right>6</td>
  <td align=right>9</td>
  <td align=right>45</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>13</td>
  <td align=right>-1</td>
  <td align=right>-2</td>
  <td align=right>-2</td>
  <td>1:1:0.01</td>
  <td>0.9</td>
  <td>0.9</td>
  <td>0.9</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9205</td>
  <td>Maarten88<span style='display:none'>/rrod</span></td>
  <td>https://git<span style='display:none'>hub.com/Maarten88/rrod/commit/478759819ce2d44ec321064aa777fdc7908719be</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Webapp/Webapp.<span
  style='display:none'>csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.1</span></td>
  <td align=right>309</td>
  <td align=right>269</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>331</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>5</td>
  <td align=right>8</td>
  <td align=right>333</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>0.6</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9206</td>
  <td>dotnet-pre<span style='display:none'>sentations/aspnetcore-app-workshop</span></td>
  <td>https://git<span style='display:none'>hub.com/dotnet-presentations/aspnetcore-app-workshop/commit/ce5bf9d06acf04aba73656a9c8c5462c487737c3</span></td>
  <td colspan=2 style='mso-ignore:colspan'>save-points/6-Deploy<span
  style='display:none'>ment-docker/ConferencePlanner/BackEnd/BackEnd.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>427</td>
  <td align=right>124</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>134</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>7</td>
  <td align=right>134</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=3 style='mso-ignore:colspan'>0.16666666666666666</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9207</td>
  <td>dotnet-pre<span style='display:none'>sentations/aspnetcore-app-workshop</span></td>
  <td>https://git<span style='display:none'>hub.com/dotnet-presentations/aspnetcore-app-workshop/commit/ce5bf9d06acf04aba73656a9c8c5462c487737c3</span></td>
  <td colspan=2 style='mso-ignore:colspan'>save-points/6-Deploy<span
  style='display:none'>ment-docker/ConferencePlanner/FrontEnd/FrontEnd.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>485</td>
  <td align=right>116</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>94</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>7</td>
  <td align=right>8</td>
  <td align=right>94</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=3 style='mso-ignore:colspan'>0.23076923076923078</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9208</td>
  <td>phongnguy<span style='display:none'>end/Practical.CleanArchitecture</span></td>
  <td>https://git<span style='display:none'>hub.com/phongnguyend/Practical.CleanArchitecture/commit/202604d7a6c3817966e3988634398697ff1cb3f5</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Microservices/Com<span
  style='display:none'>mon/ClassifiedAds.Infrastructure/ClassifiedAds.Infrastructure.csproj</span></td>
  <td>net5.0</td>
  <td align=right>1660</td>
  <td align=right>271</td>
  <td align=right>18</td>
  <td align=right>0</td>
  <td align=right>13</td>
  <td align=right>0</td>
  <td align=right>10</td>
  <td align=right>0</td>
  <td align=right>46</td>
  <td align=right>290</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>10</td>
  <td align=right>37</td>
  <td align=right>46</td>
  <td align=right>279</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>34</td>
  <td align=right>0</td>
  <td align=right>-11</td>
  <td align=right>0</td>
  <td align=right>-7</td>
  <td align=right>-3</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.7692307<span style='display:none'>692307693</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.6140350877192983</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9209</td>
  <td>phongnguy<span style='display:none'>end/Practical.CleanArchitecture</span></td>
  <td>https://git<span style='display:none'>hub.com/phongnguyend/Practical.CleanArchitecture/commit/202604d7a6c3817966e3988634398697ff1cb3f5</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/ModularMonolith/<span
  style='display:none'>ClassifiedAds.Infrastructure/ClassifiedAds.Infrastructure.csproj</span></td>
  <td>net5.0</td>
  <td align=right>1610</td>
  <td align=right>267</td>
  <td align=right>18</td>
  <td align=right>0</td>
  <td align=right>12</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>0</td>
  <td align=right>46</td>
  <td align=right>290</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>10</td>
  <td align=right>38</td>
  <td align=right>46</td>
  <td align=right>279</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>34</td>
  <td align=right>0</td>
  <td align=right>-11</td>
  <td align=right>0</td>
  <td align=right>-7</td>
  <td align=right>-4</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.7692307<span style='display:none'>692307693</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.6140350877192983</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9210</td>
  <td>phongnguy<span style='display:none'>end/Practical.CleanArchitecture</span></td>
  <td>https://git<span style='display:none'>hub.com/phongnguyend/Practical.CleanArchitecture/commit/42f0e227185092642a1ccedb7e9c4df952d3eb37</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Monolith/Classifie<span
  style='display:none'>dAds.BlazorServerSide/ClassifiedAds.BlazorServerSide.csproj</span></td>
  <td>net5.0</td>
  <td align=right>310</td>
  <td align=right>132</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>132</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>132</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=3 style='mso-ignore:colspan'>0.42857142857142855</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9211</td>
  <td>phongnguy<span style='display:none'>end/Practical.CleanArchitecture</span></td>
  <td>https://git<span style='display:none'>hub.com/phongnguyend/Practical.CleanArchitecture/commit/42f0e227185092642a1ccedb7e9c4df952d3eb37</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Monolith/Classifie<span
  style='display:none'>dAds.Infrastructure/ClassifiedAds.Infrastructure.csproj</span></td>
  <td>net5.0</td>
  <td align=right>1690</td>
  <td align=right>271</td>
  <td align=right>18</td>
  <td align=right>0</td>
  <td align=right>13</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>0</td>
  <td align=right>46</td>
  <td align=right>290</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>10</td>
  <td align=right>38</td>
  <td align=right>46</td>
  <td align=right>279</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>34</td>
  <td align=right>0</td>
  <td align=right>-11</td>
  <td align=right>0</td>
  <td align=right>-7</td>
  <td align=right>-4</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.7692307<span style='display:none'>692307693</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.6140350877192983</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9212</td>
  <td>asc-lab/dot<span style='display:none'>netcore-microservices-poc</span></td>
  <td>https://git<span style='display:none'>hub.com/asc-lab/dotnetcore-microservices-poc/commit/268f768d2ad043275f04ac59f907c37d0eb03bd4</span></td>
  <td colspan=2 style='mso-ignore:colspan'>PricingService/PricingS<span
  style='display:none'>ervice.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>373</td>
  <td align=right>129</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>132</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>3</td>
  <td align=right>8</td>
  <td align=right>9</td>
  <td align=right>128</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>-4</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>-2</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9213</td>
  <td>asc-lab/dot<span style='display:none'>netcore-microservices-poc</span></td>
  <td>https://git<span style='display:none'>hub.com/asc-lab/dotnetcore-microservices-poc/commit/07960a3d26dbf92e19b2c2d6dc60fba416384044</span></td>
  <td colspan=2 style='mso-ignore:colspan'>PricingService/PricingS<span
  style='display:none'>ervice.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.0</span></td>
  <td align=right>358</td>
  <td align=right>278</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>128</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>3</td>
  <td align=right>8</td>
  <td align=right>9</td>
  <td align=right>128</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>0.875</td>
  <td>0.6666666<span style='display:none'>666666666</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.6666666666666666</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9214</td>
  <td>Sharebook<span style='display:none'>BR/sharebook-backend</span></td>
  <td>https://git<span style='display:none'>hub.com/SharebookBR/sharebook-backend/commit/9b6e87d57feb5e6d0bfda6323a7f9cd7a3b2be21</span></td>
  <td colspan=2 style='mso-ignore:colspan'>ShareBook/ShareBook.<span
  style='display:none'>Api/ShareBook.Api.csproj</span></td>
  <td>net5.0</td>
  <td align=right>781</td>
  <td align=right>241</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>4</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>19</td>
  <td align=right>231</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>11</td>
  <td align=right>19</td>
  <td align=right>209</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>-22</td>
  <td align=right>-1</td>
  <td align=right>-5</td>
  <td align=right>-6</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.6521739<span style='display:none'>130434783</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.6521739130434783</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9215</td>
  <td>Sharebook<span style='display:none'>BR/sharebook-backend</span></td>
  <td>https://git<span style='display:none'>hub.com/SharebookBR/sharebook-backend/commit/9b6e87d57feb5e6d0bfda6323a7f9cd7a3b2be21</span></td>
  <td colspan=2 style='mso-ignore:colspan'>ShareBook/ShareBook.<span
  style='display:none'>Service/ShareBook.Service.csproj</span></td>
  <td>net5.0</td>
  <td align=right>176</td>
  <td align=right>98</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>32</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>6</td>
  <td align=right>110</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>78</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.5</td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9216</td>
  <td>damienbod<span style='display:none'>/AspNetCoreWindowsAuth</span></td>
  <td>https://git<span style='display:none'>hub.com/damienbod/AspNetCoreWindowsAuth/commit/af171de45b0f700182235ed6abe1c996ced443f9</span></td>
  <td colspan=2 style='mso-ignore:colspan'>StsServer/StsServer.cs<span
  style='display:none'>proj</span></td>
  <td>net5.0</td>
  <td align=right>752</td>
  <td align=right>145</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>18</td>
  <td align=right>155</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>12</td>
  <td align=right>14</td>
  <td align=right>18</td>
  <td align=right>155</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-6</td>
  <td align=right>-6</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.5</td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9217</td>
  <td>damienbod<span style='display:none'>/AspNetCoreWindowsAuth</span></td>
  <td>https://git<span style='display:none'>hub.com/damienbod/AspNetCoreWindowsAuth/commit/fc7caf370af8d2070fb73d266771b8d4f2c7b8a8</span></td>
  <td colspan=2 style='mso-ignore:colspan'>StsServer/StsServer.cs<span
  style='display:none'>proj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>752</td>
  <td align=right>148</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>18</td>
  <td align=right>155</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>16</td>
  <td align=right>18</td>
  <td align=right>155</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>16</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.8823529<span style='display:none'>411764706</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.7777777777777778</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9218</td>
  <td>damienbod<span style='display:none'>/AspNetCoreWindowsAuth</span></td>
  <td>https://git<span style='display:none'>hub.com/damienbod/AspNetCoreWindowsAuth/commit/0f05e99a58771118fd4ac629f681b86649c96c94</span></td>
  <td colspan=2 style='mso-ignore:colspan'>StsServer/StsServer.cs<span
  style='display:none'>proj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>752</td>
  <td align=right>148</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>18</td>
  <td align=right>155</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>16</td>
  <td align=right>18</td>
  <td align=right>155</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>16</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.8823529<span style='display:none'>411764706</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.7777777777777778</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9219</td>
  <td>AutomateT<span style='display:none'>hePlanet/Meissa</span></td>
  <td>https://git<span style='display:none'>hub.com/AutomateThePlanet/Meissa/commit/427e3761b95a5a0f7aa472dbd194d9f35101520f</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Meissa/Meissa.csproj</td>
  <td>.NETCoreA<span style='display:none'>pp2.1</span></td>
  <td align=right>450</td>
  <td align=right>61</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>12</td>
  <td align=right>62</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>12</td>
  <td align=right>12</td>
  <td align=right>92</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>30</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.7142857<span style='display:none'>142857143</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.7142857142857143</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9220</td>
  <td>SlalomBuil<span style='display:none'>d/blackslope.net</span></td>
  <td>https://git<span style='display:none'>hub.com/SlalomBuild/blackslope.net/commit/8552b30589b9ba57e05ec80b67f6b2c2350912aa</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/BlackSlope.Api/Bla<span
  style='display:none'>ckSlope.Api.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>327</td>
  <td align=right>94</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>43</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td align=right>6</td>
  <td align=right>33</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>-10</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.7142857<span style='display:none'>142857143</span></td>
  <td>0.2</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9221</td>
  <td>sphildreth/<span style='display:none'>roadie</span></td>
  <td>https://git<span style='display:none'>hub.com/sphildreth/roadie/commit/2e0759ab2122ec4fdef7c7d107544b64f62b4f70</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Roadie.Api/Roadie.Api<span
  style='display:none'>.csproj</span></td>
  <td>net5.0</td>
  <td align=right>952</td>
  <td align=right>111</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>23</td>
  <td align=right>161</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>12</td>
  <td align=right>18</td>
  <td align=right>23</td>
  <td align=right>177</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>14</td>
  <td align=right>0</td>
  <td align=right>16</td>
  <td align=right>0</td>
  <td align=right>-8</td>
  <td align=right>-4</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.5862068<span style='display:none'>965517241</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.5333333333333333</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9222</td>
  <td>rzander/jai<span style='display:none'>ndb</span></td>
  <td>https://git<span style='display:none'>hub.com/rzander/jaindb/commit/efc4593fece4f5b68fbf0c42a51d3493cf06de9a</span></td>
  <td colspan=2 style='mso-ignore:colspan'>source/Plugin_AzureBl<span
  style='display:none'>ob/Plugin_AzureBlob.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>118</td>
  <td align=right>13</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>4</td>
  <td align=right>5</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>0.8</td>
  <td>0.8</td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9223</td>
  <td>rzander/jai<span style='display:none'>ndb</span></td>
  <td>https://git<span style='display:none'>hub.com/rzander/jaindb/commit/efc4593fece4f5b68fbf0c42a51d3493cf06de9a</span></td>
  <td colspan=2 style='mso-ignore:colspan'>source/Plugin_Cosmos<span
  style='display:none'>DB/Plugin_CosmosDB.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>120</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>54</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>4</td>
  <td align=right>5</td>
  <td align=right>54</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>0.8</td>
  <td>0.8</td>
  <td>0.8</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9224</td>
  <td>rzander/jai<span style='display:none'>ndb</span></td>
  <td>https://git<span style='display:none'>hub.com/rzander/jaindb/commit/efc4593fece4f5b68fbf0c42a51d3493cf06de9a</span></td>
  <td colspan=2 style='mso-ignore:colspan'>source/Plugin_Memor<span
  style='display:none'>yCache/Plugin_MemoryCache.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>124</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>73</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>4</td>
  <td align=right>5</td>
  <td align=right>74</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>0.8</td>
  <td>0.5</td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9225</td>
  <td>rzander/jai<span style='display:none'>ndb</span></td>
  <td>https://git<span style='display:none'>hub.com/rzander/jaindb/commit/efc4593fece4f5b68fbf0c42a51d3493cf06de9a</span></td>
  <td colspan=2 style='mso-ignore:colspan'>source/Plugin_Redis/Pl<span
  style='display:none'>ugin_Redis.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>110</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>78</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>2</td>
  <td align=right>4</td>
  <td align=right>5</td>
  <td align=right>78</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>0.8</td>
  <td>0.8</td>
  <td>0.8</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9226</td>
  <td>rzander/jai<span style='display:none'>ndb</span></td>
  <td>https://git<span style='display:none'>hub.com/rzander/jaindb/commit/efc4593fece4f5b68fbf0c42a51d3493cf06de9a</span></td>
  <td colspan=2 style='mso-ignore:colspan'>source/Plugin_Rethink<span
  style='display:none'>DB/Plugin_RethinkDB.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>107</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>79</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>4</td>
  <td align=right>5</td>
  <td align=right>69</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>-10</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>0.8</td>
  <td>0.8</td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9227</td>
  <td>rzander/jai<span style='display:none'>ndb</span></td>
  <td>https://git<span style='display:none'>hub.com/rzander/jaindb/commit/efc4593fece4f5b68fbf0c42a51d3493cf06de9a</span></td>
  <td colspan=2 style='mso-ignore:colspan'>source/Plugin_SQLCac<span
  style='display:none'>he/Plugin_SQLCache.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>157</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>78</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>6</td>
  <td align=right>32</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>-46</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>0.8333333<span style='display:none'>333333334</span></td>
  <td>0.5714285<span style='display:none'>714285714</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.5714285714285714</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9228</td>
  <td>rzander/jai<span style='display:none'>ndb</span></td>
  <td>https://git<span style='display:none'>hub.com/rzander/jaindb/commit/e8218c30b57f0a072b82cdc402cca434fb3596fe</span></td>
  <td colspan=2 style='mso-ignore:colspan'>source/Plugin_AzureBl<span
  style='display:none'>ob/Plugin_AzureBlob.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.2</span></td>
  <td align=right>117</td>
  <td align=right>13</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.6666666666666666</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9229</td>
  <td>rzander/jai<span style='display:none'>ndb</span></td>
  <td>https://git<span style='display:none'>hub.com/rzander/jaindb/commit/e8218c30b57f0a072b82cdc402cca434fb3596fe</span></td>
  <td colspan=2 style='mso-ignore:colspan'>source/Plugin_Cosmos<span
  style='display:none'>DB/Plugin_CosmosDB.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.2</span></td>
  <td align=right>120</td>
  <td align=right>87</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>53</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>53</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9230</td>
  <td>rzander/jai<span style='display:none'>ndb</span></td>
  <td>https://git<span style='display:none'>hub.com/rzander/jaindb/commit/e8218c30b57f0a072b82cdc402cca434fb3596fe</span></td>
  <td colspan=2 style='mso-ignore:colspan'>source/Plugin_Memor<span
  style='display:none'>yCache/Plugin_MemoryCache.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.2</span></td>
  <td align=right>124</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>75</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>73</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.6666666666666666</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9231</td>
  <td>rzander/jai<span style='display:none'>ndb</span></td>
  <td>https://git<span style='display:none'>hub.com/rzander/jaindb/commit/e8218c30b57f0a072b82cdc402cca434fb3596fe</span></td>
  <td colspan=2 style='mso-ignore:colspan'>source/Plugin_Redis/Pl<span
  style='display:none'>ugin_Redis.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.2</span></td>
  <td align=right>110</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>67</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>77</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>10</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.6666666666666666</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9232</td>
  <td>rzander/jai<span style='display:none'>ndb</span></td>
  <td>https://git<span style='display:none'>hub.com/rzander/jaindb/commit/e8218c30b57f0a072b82cdc402cca434fb3596fe</span></td>
  <td colspan=2 style='mso-ignore:colspan'>source/Plugin_Rethink<span
  style='display:none'>DB/Plugin_RethinkDB.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.2</span></td>
  <td align=right>106</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>69</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>68</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.6666666666666666</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9233</td>
  <td>rzander/jai<span style='display:none'>ndb</span></td>
  <td>https://git<span style='display:none'>hub.com/rzander/jaindb/commit/e8218c30b57f0a072b82cdc402cca434fb3596fe</span></td>
  <td colspan=2 style='mso-ignore:colspan'>source/Plugin_SQLCac<span
  style='display:none'>he/Plugin_SQLCache.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.2</span></td>
  <td align=right>127</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>81</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>6</td>
  <td align=right>6</td>
  <td align=right>33</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>-48</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9234</td>
  <td>PiranhaCM<span style='display:none'>S/piranha.core.templates</span></td>
  <td>https://git<span style='display:none'>hub.com/PiranhaCMS/piranha.core.templates/commit/be8c3fd921595cc6a14e4a6c4dd2199d72d01874</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/web/mvc/MvcWeb<span
  style='display:none'>.csproj</span></td>
  <td>net5.0</td>
  <td align=right>632</td>
  <td align=right>111</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>16</td>
  <td align=right>0</td>
  <td align=right>16</td>
  <td align=right>111</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>16</td>
  <td align=right>16</td>
  <td align=right>111</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>16</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9235</td>
  <td>PiranhaCM<span style='display:none'>S/piranha.core.templates</span></td>
  <td>https://git<span style='display:none'>hub.com/PiranhaCMS/piranha.core.templates/commit/be8c3fd921595cc6a14e4a6c4dd2199d72d01874</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/web/razor/RazorW<span
  style='display:none'>eb.csproj</span></td>
  <td>net5.0</td>
  <td align=right>632</td>
  <td align=right>111</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>16</td>
  <td align=right>0</td>
  <td align=right>16</td>
  <td align=right>111</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>16</td>
  <td align=right>16</td>
  <td align=right>111</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>16</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9236</td>
  <td>dennisdoo<span style='display:none'>men/EffectiveTddDemo</span></td>
  <td>https://git<span style='display:none'>hub.com/dennisdoomen/EffectiveTddDemo/commit/6ef172c78ab08ca915cf45c944838acdc3639ce1</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Tests/DocumentMana<span
  style='display:none'>gement.Specs/DocumentManagement.Specs.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.2</span></td>
  <td align=right>340</td>
  <td align=right>105</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>12</td>
  <td align=right>105</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>9</td>
  <td align=right>12</td>
  <td align=right>105</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>-4</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9237</td>
  <td>adamradoc<span style='display:none'>z/boinc-manager</span></td>
  <td>https://git<span style='display:none'>hub.com/adamradocz/boinc-manager/commit/a35470012d244a2f9d8dd2ef41559aa3750de218</span></td>
  <td colspan=2 style='mso-ignore:colspan'>BoincManagerWeb/Bo<span
  style='display:none'>incManagerWeb.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>681</td>
  <td align=right>122</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>11</td>
  <td align=right>148</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>10</td>
  <td align=right>11</td>
  <td align=right>146</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>0</td>
  <td align=right>-3</td>
  <td align=right>-2</td>
  <td>1:1:0.01</td>
  <td>0.8</td>
  <td>0.6363636<span style='display:none'>363636364</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.6363636363636364</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9238</td>
  <td>thanhxuan<span style='display:none'>hd/BlogSimpleAPI</span></td>
  <td>https://git<span style='display:none'>hub.com/thanhxuanhd/BlogSimpleAPI/commit/dcd2f6da7e0d20cdc80440082a8004dc643af31d</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Blog.WebApi/Blog.We<span
  style='display:none'>bApi.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>888</td>
  <td align=right>169</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>18</td>
  <td align=right>168</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>13</td>
  <td align=right>18</td>
  <td align=right>168</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>-2</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.8</td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9239</td>
  <td>niaher/uim<span style='display:none'>f-app</span></td>
  <td>https://git<span style='display:none'>hub.com/niaher/uimf-app/commit/eba305f738df7ba4af0e86a63fc44b623b6f2837</span></td>
  <td colspan=2 style='mso-ignore:colspan'>UimfApp.Infrastructur<span
  style='display:none'>e/UimfApp.Infrastructure.csproj</span></td>
  <td>net5.0</td>
  <td align=right>508</td>
  <td align=right>157</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>10</td>
  <td align=right>104</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>9</td>
  <td align=right>10</td>
  <td align=right>83</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>0</td>
  <td align=right>-21</td>
  <td align=right>0</td>
  <td align=right>-6</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.25</td>
  <td>0.25</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9240</td>
  <td>viniciusdua<span style='display:none'>rtereis/Corporate-Chat</span></td>
  <td>https://git<span style='display:none'>hub.com/viniciusduartereis/Corporate-Chat/commit/062130e570d21395ce2c5fe933e4f9ab9bc5b608</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Corporate.Chat.API<span
  style='display:none'>/Corporate.Chat.API.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>1038</td>
  <td align=right>305</td>
  <td align=right>11</td>
  <td align=right>2</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>21</td>
  <td align=right>308</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>11</td>
  <td align=right>21</td>
  <td align=right>295</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>10</td>
  <td align=right>0</td>
  <td align=right>-13</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.9090909090909091</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9241</td>
  <td>viniciusdua<span style='display:none'>rtereis/Corporate-Chat</span></td>
  <td>https://git<span style='display:none'>hub.com/viniciusduartereis/Corporate-Chat/commit/3e8c2e534c1ad0aebe2543dbe33b2642c123a22b</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Corporate.Chat.API<span
  style='display:none'>/Corporate.Chat.API.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>1038</td>
  <td align=right>305</td>
  <td align=right>11</td>
  <td align=right>2</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>21</td>
  <td align=right>308</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>3</td>
  <td align=right>11</td>
  <td align=right>21</td>
  <td align=right>295</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>10</td>
  <td align=right>0</td>
  <td align=right>-13</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.9090909090909091</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9242</td>
  <td>zhangchao<span style='display:none'>za/corert-samples</span></td>
  <td>https://git<span style='display:none'>hub.com/zhangchaoza/corert-samples/commit/f74c71e0eb92f3f9785a4c89d41ce79628e72d47</span></td>
  <td colspan=2 style='mso-ignore:colspan'>CommandLineUtilsDe<span
  style='display:none'>mo/AdvancedAttributesCoreRTDemo/AdvancedAttributesCoreRTDemo.csproj</span></td>
  <td>net5.0</td>
  <td align=right>483</td>
  <td align=right>8</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>17</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>7</td>
  <td align=right>7</td>
  <td align=right>73</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>56</td>
  <td align=right>0</td>
  <td align=right>-6</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.0769230<span style='display:none'>7692307693</span></td>
  <td colspan=3 style='mso-ignore:colspan'>0.07692307692307693</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9243</td>
  <td>innvistech/<span style='display:none'>dotnetcore-microservices-poc</span></td>
  <td>https://git<span style='display:none'>hub.com/innvistech/dotnetcore-microservices-poc/commit/268f768d2ad043275f04ac59f907c37d0eb03bd4</span></td>
  <td colspan=2 style='mso-ignore:colspan'>PricingService/PricingS<span
  style='display:none'>ervice.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>373</td>
  <td align=right>129</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>132</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>8</td>
  <td align=right>9</td>
  <td align=right>128</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>-4</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>-2</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9244</td>
  <td>innvistech/<span style='display:none'>dotnetcore-microservices-poc</span></td>
  <td>https://git<span style='display:none'>hub.com/innvistech/dotnetcore-microservices-poc/commit/07960a3d26dbf92e19b2c2d6dc60fba416384044</span></td>
  <td colspan=2 style='mso-ignore:colspan'>PricingService/PricingS<span
  style='display:none'>ervice.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.0</span></td>
  <td align=right>358</td>
  <td align=right>278</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>128</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>8</td>
  <td align=right>9</td>
  <td align=right>128</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>0.875</td>
  <td>0.6666666<span style='display:none'>666666666</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.6666666666666666</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9245</td>
  <td>CharlesRea<span style='display:none'>/clud</span></td>
  <td>https://git<span style='display:none'>hub.com/CharlesRea/clud/commit/9d42def2d09d143a150e110085a26d3649865f50</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Api/Api.csproj</td>
  <td>net5.0</td>
  <td align=right>354</td>
  <td align=right>107</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>122</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>8</td>
  <td align=right>9</td>
  <td align=right>113</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>-9</td>
  <td align=right>0</td>
  <td align=right>-3</td>
  <td align=right>-4</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.6363636<span style='display:none'>363636364</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.6363636363636364</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9246</td>
  <td>FightCore/<span style='display:none'>Backend</span></td>
  <td>https://git<span style='display:none'>hub.com/FightCore/Backend/commit/0a644dd3588f8543bb56882007d23dfecc19369a</span></td>
  <td colspan=2 style='mso-ignore:colspan'>FightCore.Backend/Fig<span
  style='display:none'>htCore.Backend/FightCore.Backend.csproj</span></td>
  <td>net5.0</td>
  <td align=right>821</td>
  <td align=right>180</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>0</td>
  <td align=right>10</td>
  <td align=right>0</td>
  <td align=right>19</td>
  <td align=right>177</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>10</td>
  <td align=right>17</td>
  <td align=right>19</td>
  <td align=right>177</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>13</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-5</td>
  <td align=right>-4</td>
  <td>1:1:0.01</td>
  <td>0.6666666<span style='display:none'>666666666</span></td>
  <td>0.5</td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9247</td>
  <td>DiyazY/ser<span style='display:none'>vice-log</span></td>
  <td>https://git<span style='display:none'>hub.com/DiyazY/service-log/commit/dbec477fde310985f42169d82bfc6a22e9d3d9b7</span></td>
  <td colspan=2 style='mso-ignore:colspan'>sl.web/sl.web.csproj</td>
  <td>net5.0</td>
  <td align=right>244</td>
  <td align=right>106</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>54</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>4</td>
  <td align=right>4</td>
  <td align=right>111</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>57</td>
  <td align=right>0</td>
  <td align=right>-3</td>
  <td align=right>-2</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.1428571<span style='display:none'>4285714285</span></td>
  <td colspan=3 style='mso-ignore:colspan'>0.14285714285714285</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9248</td>
  <td>ops-ai/Bey<span style='display:none'>ondAuth</span></td>
  <td>https://git<span style='display:none'>hub.com/ops-ai/BeyondAuth/commit/6a5de6939f7bcc586d214994503deaa60c78ea4d</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/AuditServer/AuditS<span
  style='display:none'>erver.csproj</span></td>
  <td>net5.0</td>
  <td align=right>642</td>
  <td align=right>210</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>17</td>
  <td align=right>214</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>14</td>
  <td align=right>17</td>
  <td align=right>193</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>-21</td>
  <td align=right>0</td>
  <td align=right>-5</td>
  <td align=right>-3</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.5454545<span style='display:none'>454545454</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.3076923076923077</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9249</td>
  <td>MattRyder<span style='display:none'>/LifeCMS</span></td>
  <td>https://git<span style='display:none'>hub.com/MattRyder/LifeCMS/commit/877a4ef726f7105b2748d8678e71570d2898b913</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Services/ContentCr<span
  style='display:none'>eation/ContentCreation.API/ContentCreation.API.csproj</span></td>
  <td>net5.0</td>
  <td align=right>573</td>
  <td align=right>156</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>16</td>
  <td align=right>110</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>11</td>
  <td align=right>16</td>
  <td align=right>160</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>50</td>
  <td align=right>0</td>
  <td align=right>-4</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.6</td>
  <td colspan=2 style='mso-ignore:colspan'>0.5238095238095238</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9250</td>
  <td>nojkhiepps<span style='display:none'>o/dotnetcore-microservices</span></td>
  <td>https://git<span style='display:none'>hub.com/nojkhieppso/dotnetcore-microservices/commit/268f768d2ad043275f04ac59f907c37d0eb03bd4</span></td>
  <td colspan=2 style='mso-ignore:colspan'>PricingService/PricingS<span
  style='display:none'>ervice.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>373</td>
  <td align=right>129</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>132</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>8</td>
  <td align=right>9</td>
  <td align=right>128</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>-4</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>-2</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9251</td>
  <td>nojkhiepps<span style='display:none'>o/dotnetcore-microservices</span></td>
  <td>https://git<span style='display:none'>hub.com/nojkhieppso/dotnetcore-microservices/commit/07960a3d26dbf92e19b2c2d6dc60fba416384044</span></td>
  <td colspan=2 style='mso-ignore:colspan'>PricingService/PricingS<span
  style='display:none'>ervice.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.0</span></td>
  <td align=right>358</td>
  <td align=right>278</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>128</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>8</td>
  <td align=right>9</td>
  <td align=right>128</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>0.875</td>
  <td>0.6666666<span style='display:none'>666666666</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.6666666666666666</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9252</td>
  <td>LykkeCity/L<span style='display:none'>ykke.Service.HftInternalService</span></td>
  <td>https://git<span style='display:none'>hub.com/LykkeCity/Lykke.Service.HftInternalService/commit/63c1a10a7bb63b4d0c4c51379c6d851da8a992c2</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Lykke.Service.HftIn<span
  style='display:none'>ternalService/Lykke.Service.HftInternalService.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.1</span></td>
  <td align=right>561</td>
  <td align=right>239</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>17</td>
  <td align=right>188</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>13</td>
  <td align=right>17</td>
  <td align=right>186</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>12</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>0.9230769<span style='display:none'>230769231</span></td>
  <td>0.6666666<span style='display:none'>666666666</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.6666666666666666</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9253</td>
  <td>LykkeCity/L<span style='display:none'>ykke.Service.HftInternalService</span></td>
  <td>https://git<span style='display:none'>hub.com/LykkeCity/Lykke.Service.HftInternalService/commit/57b7bdc1ab6bf3c0e3e9f3e96178e60a55a99dc7</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Lykke.Service.HftIn<span
  style='display:none'>ternalService/Lykke.Service.HftInternalService.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.1</span></td>
  <td align=right>561</td>
  <td align=right>239</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>17</td>
  <td align=right>188</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>13</td>
  <td align=right>17</td>
  <td align=right>186</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>12</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>0.9230769<span style='display:none'>230769231</span></td>
  <td>0.6666666<span style='display:none'>666666666</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.6666666666666666</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9254</td>
  <td>equinor/pr<span style='display:none'>ocosys-library-api</span></td>
  <td>https://git<span style='display:none'>hub.com/equinor/procosys-library-api/commit/89874e14c935fe47918674352097f1d7d512aa1d</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Equinor.Procosys.Li<span
  style='display:none'>brary.WebApi/Equinor.Procosys.Library.WebApi.csproj</span></td>
  <td>net5.0</td>
  <td align=right>829</td>
  <td align=right>113</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>17</td>
  <td align=right>174</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>11</td>
  <td align=right>17</td>
  <td align=right>161</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>10</td>
  <td align=right>0</td>
  <td align=right>-13</td>
  <td align=right>0</td>
  <td align=right>-5</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.7894736<span style='display:none'>842105263</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.7894736842105263</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9255</td>
  <td>ElizaReiGW<span style='display:none'>CD/cutie-bot</span></td>
  <td>https://git<span style='display:none'>hub.com/ElizaReiGWCD/cutie-bot/commit/6bfb79650d89d6e59abd76b886645ecb6db93826</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/discordbot/discord<span
  style='display:none'>bot.csproj</span></td>
  <td>net5.0</td>
  <td align=right>257</td>
  <td align=right>267</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>266</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>6</td>
  <td align=right>9</td>
  <td align=right>267</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.7142857<span style='display:none'>142857143</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.7142857142857143</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9256</td>
  <td>ttu/dotnet-<span style='display:none'>fake-json-server</span></td>
  <td>https://git<span style='display:none'>hub.com/ttu/dotnet-fake-json-server/commit/077ce5d556fcef3c355c3adeb1704d9ebb93d817</span></td>
  <td colspan=2 style='mso-ignore:colspan'>FakeServer/FakeServer<span
  style='display:none'>.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.1</span></td>
  <td align=right>634</td>
  <td align=right>226</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>17</td>
  <td align=right>233</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>16</td>
  <td align=right>17</td>
  <td align=right>215</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>10</td>
  <td align=right>0</td>
  <td align=right>-18</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>-6</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.8888888<span style='display:none'>888888888</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.6190476190476191</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9257</td>
  <td>luoyuncho<span style='display:none'>ng/lin-cms-dotnetcore</span></td>
  <td>https://git<span style='display:none'>hub.com/luoyunchong/lin-cms-dotnetcore/commit/3caa119ea496db6d736f2f16c4d1aade95daf0f2</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/LinCms.Web/LinC<span
  style='display:none'>ms.Web.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>901</td>
  <td align=right>182</td>
  <td align=right>15</td>
  <td align=right>0</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>10</td>
  <td align=right>0</td>
  <td align=right>24</td>
  <td align=right>207</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>17</td>
  <td align=right>24</td>
  <td align=right>171</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>17</td>
  <td align=right>0</td>
  <td align=right>-36</td>
  <td align=right>0</td>
  <td align=right>-4</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.8461538<span style='display:none'>461538461</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.7777777777777778</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9258</td>
  <td>chayxana/<span style='display:none'>Restaurant-App</span></td>
  <td>https://git<span style='display:none'>hub.com/chayxana/Restaurant-App/commit/43ae499d618e5887781054fed4530ca91b03b811</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/backend/services/<span
  style='display:none'>menu.api/Menu.API/Menu.API.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>553</td>
  <td align=right>90</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>16</td>
  <td align=right>106</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>13</td>
  <td align=right>16</td>
  <td align=right>131</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>14</td>
  <td align=right>0</td>
  <td align=right>25</td>
  <td align=right>0</td>
  <td align=right>-6</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.6842105<span style='display:none'>263157895</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.3333333333333333</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9259</td>
  <td>asc-lab/dot<span style='display:none'>netcore-microservices-poc</span></td>
  <td>https://git<span style='display:none'>hub.com/asc-lab/dotnetcore-microservices-poc/commit/f58f7714fffce0c9de6ea6926e67989f1c18ae88</span></td>
  <td colspan=2 style='mso-ignore:colspan'>PricingService/PricingS<span
  style='display:none'>ervice.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.0</span></td>
  <td align=right>358</td>
  <td align=right>278</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>128</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>8</td>
  <td align=right>9</td>
  <td align=right>128</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>0.875</td>
  <td>0.6666666<span style='display:none'>666666666</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.6666666666666666</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9260</td>
  <td>igritco/Cle<span style='display:none'>anArchitecture</span></td>
  <td>https://git<span style='display:none'>hub.com/igritco/CleanArchitecture/commit/626a7fbd977ed31d1da84d0c1643250460156336</span></td>
  <td colspan=2 style='mso-ignore:colspan'>ToDoApp/Presentation<span
  style='display:none'>/ToDoApp.Server/ToDoApp.Server.csproj</span></td>
  <td>net5.0</td>
  <td align=right>495</td>
  <td align=right>147</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>118</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>6</td>
  <td align=right>7</td>
  <td align=right>147</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>29</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>-2</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9261</td>
  <td>Oragon/Or<span style='display:none'>agon.Contexts</span></td>
  <td>https://git<span style='display:none'>hub.com/Oragon/Oragon.Contexts/commit/a209b5bdcafbcaf74db4a6379eb94c2c5b3e9cc7</span></td>
  <td colspan=2 style='mso-ignore:colspan'>tests/Oragon.Context.<span
  style='display:none'>Tests/Oragon.Context.Tests.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.2</span></td>
  <td align=right>294</td>
  <td align=right>110</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>12</td>
  <td align=right>132</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>10</td>
  <td align=right>12</td>
  <td align=right>123</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>0</td>
  <td align=right>-9</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.7142857142857143</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9262</td>
  <td>zunath/SW<span style='display:none'>LOR_Website</span></td>
  <td>https://git<span style='display:none'>hub.com/zunath/SWLOR_Website/commit/4fb3c7471ddf3c8c0a545badb78abaab4d07f72f</span></td>
  <td colspan=2 style='mso-ignore:colspan'>SWLOR.Web/SWLOR.<span
  style='display:none'>Web.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.1</span></td>
  <td align=right>253</td>
  <td align=right>149</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>151</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>5</td>
  <td align=right>145</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>-6</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.6666666666666666</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9263</td>
  <td>TomaT3/Sp<span style='display:none'>iritSpender</span></td>
  <td>https://git<span style='display:none'>hub.com/TomaT3/SpiritSpender/commit/ec06c5d3aec22f69cf8930b3115fd5a6b0134b8c</span></td>
  <td colspan=2 style='mso-ignore:colspan'>SpiritSpenderServer/sr<span
  style='display:none'>c/SpiritSpenderServer/SpiritSpenderServer.csproj</span></td>
  <td>net5.0</td>
  <td align=right>489</td>
  <td align=right>166</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>12</td>
  <td align=right>143</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>10</td>
  <td align=right>12</td>
  <td align=right>147</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>9</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9264</td>
  <td>TomaT3/Sp<span style='display:none'>iritSpender</span></td>
  <td>https://git<span style='display:none'>hub.com/TomaT3/SpiritSpender/commit/d0f08fb1e21a4e311b3e16a2599c81ee6136874c</span></td>
  <td colspan=2 style='mso-ignore:colspan'>SpiritSpenderServer/sr<span
  style='display:none'>c/SpiritSpenderServer/SpiritSpenderServer.csproj</span></td>
  <td>net5.0</td>
  <td align=right>489</td>
  <td align=right>166</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>12</td>
  <td align=right>143</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>10</td>
  <td align=right>12</td>
  <td align=right>147</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>9</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9265</td>
  <td>hiarcdb/hia<span style='display:none'>rc</span></td>
  <td>https://git<span style='display:none'>hub.com/hiarcdb/hiarc/commit/d7ab5b3778e75fa591c30eceab6cd35465acaab3</span></td>
  <td colspan=2 style='mso-ignore:colspan'>HiarcCore/HiarcCore.cs<span
  style='display:none'>proj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>389</td>
  <td align=right>61</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>11</td>
  <td align=right>111</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>8</td>
  <td align=right>11</td>
  <td align=right>107</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>10</td>
  <td align=right>0</td>
  <td align=right>-4</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>2</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.8333333<span style='display:none'>333333334</span></td>
  <td colspan=3 style='mso-ignore:colspan'>0.29411764705882354</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9266</td>
  <td>hiarcdb/hia<span style='display:none'>rc</span></td>
  <td>https://git<span style='display:none'>hub.com/hiarcdb/hiarc/commit/cbdcdf0b0f873ad8cdd6518687492985b9fd54a8</span></td>
  <td colspan=2 style='mso-ignore:colspan'>HiarcCore/HiarcCore.cs<span
  style='display:none'>proj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>389</td>
  <td align=right>61</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>11</td>
  <td align=right>111</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>8</td>
  <td align=right>11</td>
  <td align=right>107</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>10</td>
  <td align=right>0</td>
  <td align=right>-4</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>2</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.8333333<span style='display:none'>333333334</span></td>
  <td colspan=3 style='mso-ignore:colspan'>0.29411764705882354</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9267</td>
  <td>Azure-Sam<span style='display:none'>ples/Commercial-Marketplace-SaaS-Manual-On-Boarding</span></td>
  <td>https://git<span style='display:none'>hub.com/microsoft/Commercial-Marketplace-SaaS-Manual-On-Boarding/commit/723e2b484239ea902a4ecfbc56de52ab90e514a6</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/CommandCenter/C<span
  style='display:none'>ommandCenter.csproj</span></td>
  <td>net5.0</td>
  <td align=right>695</td>
  <td align=right>205</td>
  <td align=right>10</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>16</td>
  <td align=right>193</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>9</td>
  <td align=right>16</td>
  <td align=right>182</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>-11</td>
  <td align=right>0</td>
  <td align=right>-3</td>
  <td align=right>-2</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.6842105<span style='display:none'>263157895</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.5238095238095238</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9268</td>
  <td>innvistech/<span style='display:none'>dotnetcore-microservices-poc</span></td>
  <td>https://git<span style='display:none'>hub.com/innvistech/dotnetcore-microservices-poc/commit/f58f7714fffce0c9de6ea6926e67989f1c18ae88</span></td>
  <td colspan=2 style='mso-ignore:colspan'>PricingService/PricingS<span
  style='display:none'>ervice.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.0</span></td>
  <td align=right>358</td>
  <td align=right>278</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>128</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>8</td>
  <td align=right>9</td>
  <td align=right>128</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>0.875</td>
  <td>0.6666666<span style='display:none'>666666666</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.6666666666666666</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9269</td>
  <td>brettm42/<span style='display:none'>HistoCoin</span></td>
  <td>https://git<span style='display:none'>hub.com/brettm42/HistoCoin/commit/23f72b56e1d80446b99d4b317e36d81b42dfc262</span></td>
  <td colspan=2 style='mso-ignore:colspan'>HistoCoin.csproj</td>
  <td>.NETCoreA<span style='display:none'>pp2.1</span></td>
  <td align=right>195</td>
  <td align=right>280</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>251</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>5</td>
  <td align=right>6</td>
  <td align=right>248</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>-3</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.3333333333333333</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9270</td>
  <td>matheusrm<span style='display:none'>artinez/api-datadriven-efcore3</span></td>
  <td>https://git<span style='display:none'>hub.com/matheusrmartinez/api-datadriven-efcore3/commit/8f6337ad10e0a75bfb428ef2c98a1dcb654b5411</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Shop.csproj</td>
  <td>.NETCoreA<span style='display:none'>pp3.0</span></td>
  <td align=right>274</td>
  <td align=right>76</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>61</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>1</td>
  <td align=right>5</td>
  <td align=right>61</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>2</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=3 style='mso-ignore:colspan'>0.42857142857142855</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9271</td>
  <td>nojkhiepps<span style='display:none'>o/dotnetcore-microservices</span></td>
  <td>https://git<span style='display:none'>hub.com/nojkhieppso/dotnetcore-microservices/commit/f58f7714fffce0c9de6ea6926e67989f1c18ae88</span></td>
  <td colspan=2 style='mso-ignore:colspan'>PricingService/PricingS<span
  style='display:none'>ervice.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.0</span></td>
  <td align=right>358</td>
  <td align=right>278</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>128</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>8</td>
  <td align=right>9</td>
  <td align=right>128</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>0.875</td>
  <td>0.6666666<span style='display:none'>666666666</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.6666666666666666</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9272</td>
  <td>kinderbuen<span style='display:none'>o360/SollariExchangeMoney</span></td>
  <td>https://git<span style='display:none'>hub.com/kinderbueno360/SollariExchangeMoney/commit/341536e1d4508cbdc0c1a7929b30f86d2adaeb86</span></td>
  <td colspan=2 style='mso-ignore:colspan'>solari.wallet/solari.wal<span
  style='display:none'>let.csproj</span></td>
  <td>net5.0</td>
  <td align=right>271</td>
  <td align=right>120</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>119</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>2</td>
  <td align=right>5</td>
  <td align=right>114</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>-5</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9273</td>
  <td>DominikStil<span style='display:none'>ler/Vertretungsplan</span></td>
  <td>https://git<span style='display:none'>hub.com/DominikStiller/Vertretungsplan/commit/9d11c50dcb35a3a0f181e632830b9cc4f394b04e</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Web/Web.csproj</td>
  <td>.NETCoreA<span style='display:none'>pp2.1</span></td>
  <td align=right>195</td>
  <td align=right>85</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>94</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>4</td>
  <td align=right>5</td>
  <td align=right>43</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>-51</td>
  <td align=right>0</td>
  <td align=right>-3</td>
  <td align=right>-3</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9274</td>
  <td>microsoft/<span style='display:none'>data-accelerator</span></td>
  <td>https://git<span style='display:none'>hub.com/microsoft/data-accelerator/commit/e4d6d23bd02cb0737b9edd2b78b8c5f4c0fd8d2e</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Services/DataX.Utilitie<span
  style='display:none'>s/DataX.Utilities.CosmosDB/DataX.Utilities.CosmosDB.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.2</span></td>
  <td align=right>180</td>
  <td align=right>90</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>74</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>74</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>0.75</td>
  <td>0.75</td>
  <td>0.75</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9275</td>
  <td>OData/RES<span style='display:none'>Tier</span></td>
  <td>https://git<span style='display:none'>hub.com/OData/RESTier/commit/db849518e060f4aea000cb6f82ddbb0178847db9</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Microsoft.Restier.T<span
  style='display:none'>ests.AspNet/Microsoft.Restier.Tests.AspNet.csproj</span></td>
  <td>.NETFrame<span style='display:none'>work4.7.2</span></td>
  <td align=right>198</td>
  <td align=right>16</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.6666666666666666</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9276</td>
  <td>OData/RES<span style='display:none'>Tier</span></td>
  <td>https://git<span style='display:none'>hub.com/OData/RESTier/commit/db849518e060f4aea000cb6f82ddbb0178847db9</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Microsoft.Restier.T<span
  style='display:none'>ests.Core/Microsoft.Restier.Tests.Core.csproj</span></td>
  <td>.NETFrame<span style='display:none'>work4.7.2</span></td>
  <td align=right>197</td>
  <td align=right>15</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>2</td>
  <td align=right>4</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>0.6</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9277</td>
  <td>KirillOsenk<span style='display:none'>ov/SourceBrowser</span></td>
  <td>https://git<span style='display:none'>hub.com/KirillOsenkov/SourceBrowser/commit/3d60ce2e5dc706702080fb4f46b0dbc6f0a2b788</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/HtmlGenerator.Tes<span
  style='display:none'>ts/HtmlGenerator.Tests.csproj</span></td>
  <td>.NETFrame<span style='display:none'>work4.7.2</span></td>
  <td align=right>140</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>8</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.6666666666666666</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9278</td>
  <td>danielgerla<span style='display:none'>g/workflow-core</span></td>
  <td>https://git<span style='display:none'>hub.com/danielgerlag/workflow-core/commit/19f90efafa6da0a382901d2da790c7c09413835f</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/samples/Workflow<span
  style='display:none'>Core.Sample04/WorkflowCore.Sample04.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>195</td>
  <td align=right>25</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>28</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>84</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>56</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.4285714<span style='display:none'>2857142855</span></td>
  <td colspan=3 style='mso-ignore:colspan'>0.42857142857142855</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9279</td>
  <td>danielgerla<span style='display:none'>g/workflow-core</span></td>
  <td>https://git<span style='display:none'>hub.com/danielgerlag/workflow-core/commit/fcb14346397a56dee53647370281550e9fd95cc9</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/providers/Workflo<span
  style='display:none'>wCore.Providers.AWS/WorkflowCore.Providers.AWS.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>159</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td align=right>5</td>
  <td align=right>67</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>62</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>0.8</td>
  <td>0.5</td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9280</td>
  <td>danielgerla<span style='display:none'>g/workflow-core</span></td>
  <td>https://git<span style='display:none'>hub.com/danielgerlag/workflow-core/commit/fcb14346397a56dee53647370281550e9fd95cc9</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/samples/Workflow<span
  style='display:none'>Core.Sample04/WorkflowCore.Sample04.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.0</span></td>
  <td align=right>195</td>
  <td align=right>27</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>27</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>83</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>56</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.4285714<span style='display:none'>2857142855</span></td>
  <td colspan=3 style='mso-ignore:colspan'>0.42857142857142855</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9281</td>
  <td>danielgerla<span style='display:none'>g/workflow-core</span></td>
  <td>https://git<span style='display:none'>hub.com/danielgerlag/workflow-core/commit/a96d7f618aac823b99a094aaf37102827449d187</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/providers/Workflo<span
  style='display:none'>wCore.Providers.AWS/WorkflowCore.Providers.AWS.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>159</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td align=right>5</td>
  <td align=right>67</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>62</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>0.8</td>
  <td>0.5</td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9282</td>
  <td>danielgerla<span style='display:none'>g/workflow-core</span></td>
  <td>https://git<span style='display:none'>hub.com/danielgerlag/workflow-core/commit/a96d7f618aac823b99a094aaf37102827449d187</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/samples/Workflow<span
  style='display:none'>Core.Sample04/WorkflowCore.Sample04.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.0</span></td>
  <td align=right>195</td>
  <td align=right>27</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>27</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>83</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>56</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.4285714<span style='display:none'>2857142855</span></td>
  <td colspan=3 style='mso-ignore:colspan'>0.42857142857142855</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9283</td>
  <td>danielgerla<span style='display:none'>g/workflow-core</span></td>
  <td>https://git<span style='display:none'>hub.com/danielgerlag/workflow-core/commit/73b098e115c499ee804197f3c25ab81007066fa5</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/providers/Workflo<span
  style='display:none'>wCore.Providers.AWS/WorkflowCore.Providers.AWS.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>159</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td align=right>5</td>
  <td align=right>67</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>62</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>0.8</td>
  <td>0.5</td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9284</td>
  <td>danielgerla<span style='display:none'>g/workflow-core</span></td>
  <td>https://git<span style='display:none'>hub.com/danielgerlag/workflow-core/commit/73b098e115c499ee804197f3c25ab81007066fa5</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/samples/Workflow<span
  style='display:none'>Core.Sample04/WorkflowCore.Sample04.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>195</td>
  <td align=right>25</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>28</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>84</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>56</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.4285714<span style='display:none'>2857142855</span></td>
  <td colspan=3 style='mso-ignore:colspan'>0.42857142857142855</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9285</td>
  <td>danielgerla<span style='display:none'>g/workflow-core</span></td>
  <td>https://git<span style='display:none'>hub.com/danielgerlag/workflow-core/commit/b1a0f42da4e7ff6894425de2acbd9e2fd6d9f299</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/providers/Workflo<span
  style='display:none'>wCore.Providers.AWS/WorkflowCore.Providers.AWS.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>159</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td align=right>5</td>
  <td align=right>67</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>62</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>0.8</td>
  <td>0.5</td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9286</td>
  <td>danielgerla<span style='display:none'>g/workflow-core</span></td>
  <td>https://git<span style='display:none'>hub.com/danielgerlag/workflow-core/commit/b1a0f42da4e7ff6894425de2acbd9e2fd6d9f299</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/samples/Workflow<span
  style='display:none'>Core.Sample04/WorkflowCore.Sample04.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>195</td>
  <td align=right>25</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>28</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>84</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>56</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.4285714<span style='display:none'>2857142855</span></td>
  <td colspan=3 style='mso-ignore:colspan'>0.42857142857142855</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9287</td>
  <td>aws/aws-lo<span style='display:none'>gging-dotnet</span></td>
  <td>https://git<span style='display:none'>hub.com/aws/aws-logging-dotnet/commit/17af19a7d9c490697b60f1c9f68b84f7366ea753</span></td>
  <td colspan=2 style='mso-ignore:colspan'>test/AWS.Logger.AspN<span
  style='display:none'>etCore.Tests/AWS.Logger.AspNetCore.Tests.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.0</span></td>
  <td align=right>558</td>
  <td align=right>110</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>12</td>
  <td align=right>57</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>10</td>
  <td align=right>12</td>
  <td align=right>126</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>12</td>
  <td align=right>0</td>
  <td align=right>69</td>
  <td align=right>0</td>
  <td align=right>-8</td>
  <td align=right>2</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.7142857142857143</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9288</td>
  <td>cmendible/<span style='display:none'>dotnetcore.samples</span></td>
  <td>https://git<span style='display:none'>hub.com/cmendible/dotnetcore.samples/commit/fd0a7e5388f3aee5c35baf62143b1995cb156d98</span></td>
  <td colspan=2 style='mso-ignore:colspan'>cloud.design.patterns/<span
  style='display:none'>health.endpoint.monitor/health.endpoint.monitor.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.0</span></td>
  <td align=right>1147</td>
  <td align=right>212</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>12</td>
  <td align=right>0</td>
  <td align=right>21</td>
  <td align=right>175</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>18</td>
  <td align=right>21</td>
  <td align=right>177</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>19</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>-4</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.75</td>
  <td colspan=2 style='mso-ignore:colspan'>0.2727272727272727</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9289</td>
  <td>bizanc/Biza<span style='display:none'>nc.io.Core</span></td>
  <td>https://git<span style='display:none'>hub.com/bizanc/Bizanc.io.Core/commit/f04b0a69e0dcf59e47691626146a32d24957c362</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Bizanc.io.Matching.Or<span
  style='display:none'>acle/Bizanc.io.Matching.Oracle.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.0</span></td>
  <td align=right>233</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>95</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>6</td>
  <td align=right>7</td>
  <td align=right>94</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.75</td>
  <td>0.4</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9290</td>
  <td>NTumbleBi<span style='display:none'>t/NTumbleBit</span></td>
  <td>https://git<span style='display:none'>hub.com/NTumbleBit/NTumbleBit/commit/7e283ac6d599c7bc8a06e207b3f764b495d39b2e</span></td>
  <td colspan=2 style='mso-ignore:colspan'>NTumbleBit/NTumble<span
  style='display:none'>Bit.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.1</span></td>
  <td align=right>118</td>
  <td align=right>263</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>269</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>248</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>-21</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=3 style='mso-ignore:colspan'>0.42857142857142855</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9291</td>
  <td>rzander/ru<span style='display:none'>ckzuck</span></td>
  <td>https://git<span style='display:none'>hub.com/rzander/ruckzuck/commit/c69e61ce5852a88ebed0909de717063ecd6e763d</span></td>
  <td colspan=2 style='mso-ignore:colspan'>RZ.Server/RZ.Plugin.So<span
  style='display:none'>ftware.Azure/RZ.Plugin.Software.Azure.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>146</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>78</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>80</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.6666666<span style='display:none'>666666666</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.6666666666666666</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9292</td>
  <td>rzander/ru<span style='display:none'>ckzuck</span></td>
  <td>https://git<span style='display:none'>hub.com/rzander/ruckzuck/commit/c69e61ce5852a88ebed0909de717063ecd6e763d</span></td>
  <td colspan=2 style='mso-ignore:colspan'>RZ.Server/RZ.Plugin.So<span
  style='display:none'>ftware.Proxy/RZ.Plugin.Software.Proxy.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>146</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>78</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>80</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.6666666<span style='display:none'>666666666</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.6666666666666666</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9293</td>
  <td>damienbod<span style='display:none'>/AspNetCoreWindowsAuth</span></td>
  <td>https://git<span style='display:none'>hub.com/damienbod/AspNetCoreWindowsAuth/commit/10077a81ce84bed80f1fc218da799f01f9567116</span></td>
  <td colspan=2 style='mso-ignore:colspan'>WebApi/WebApi.cspro<span
  style='display:none'>j</span></td>
  <td>net5.0</td>
  <td align=right>466</td>
  <td align=right>43</td>
  <td align=right>10</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>11</td>
  <td align=right>138</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>7</td>
  <td align=right>11</td>
  <td align=right>124</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>-14</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>0.875</td>
  <td>0.5</td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9294</td>
  <td>damienbod<span style='display:none'>/AspNetCoreWindowsAuth</span></td>
  <td>https://git<span style='display:none'>hub.com/damienbod/AspNetCoreWindowsAuth/commit/fc7caf370af8d2070fb73d266771b8d4f2c7b8a8</span></td>
  <td colspan=2 style='mso-ignore:colspan'>WebApi/WebApi.cspro<span
  style='display:none'>j</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>470</td>
  <td align=right>68</td>
  <td align=right>10</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>11</td>
  <td align=right>139</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>11</td>
  <td align=right>11</td>
  <td align=right>124</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>-15</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.8333333<span style='display:none'>333333334</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.5714285714285714</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9295</td>
  <td>Byndyusoft<span style='display:none'>/Byndyusoft.Dotnet.Core.Infrastructure</span></td>
  <td>https://git<span style='display:none'>hub.com/Byndyusoft/Byndyusoft.Dotnet.Core.Infrastructure/commit/7de6ed32ac5fd8dcb5e2fbfd080e282deb243676</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Jobs/Consumer/Co<span
  style='display:none'>nsumer.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.1</span></td>
  <td align=right>674</td>
  <td align=right>111</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>13</td>
  <td align=right>0</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>16</td>
  <td align=right>122</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>13</td>
  <td align=right>16</td>
  <td align=right>60</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>14</td>
  <td align=right>0</td>
  <td align=right>-62</td>
  <td align=right>0</td>
  <td align=right>-8</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>0.6</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9296</td>
  <td>Byndyusoft<span style='display:none'>/Byndyusoft.Dotnet.Core.Infrastructure</span></td>
  <td>https://git<span style='display:none'>hub.com/Byndyusoft/Byndyusoft.Dotnet.Core.Infrastructure/commit/7de6ed32ac5fd8dcb5e2fbfd080e282deb243676</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Web.Application/<span
  style='display:none'>Web.Application.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.1</span></td>
  <td align=right>578</td>
  <td align=right>210</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>12</td>
  <td align=right>0</td>
  <td align=right>10</td>
  <td align=right>0</td>
  <td align=right>17</td>
  <td align=right>213</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>11</td>
  <td align=right>17</td>
  <td align=right>212</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>13</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>2</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.4166666666666667</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9297</td>
  <td>shawnwild<span style='display:none'>ermuth/MetaWeblog</span></td>
  <td>https://git<span style='display:none'>hub.com/shawnwildermuth/MetaWeblog/commit/9c9040ea2238512a756e3159c183f117fea90d97</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/WilderMinds.Meta<span
  style='display:none'>Weblog.Tests/WilderMinds.MetaWeblog.Tests.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.0</span></td>
  <td align=right>174</td>
  <td align=right>111</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>103</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>103</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9298</td>
  <td>shawnwild<span style='display:none'>ermuth/MetaWeblog</span></td>
  <td>https://git<span style='display:none'>hub.com/shawnwildermuth/MetaWeblog/commit/263517ab080e2672922bc8c1bdbe9d6146c889fb</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/WilderMinds.Meta<span
  style='display:none'>Weblog.Tests/WilderMinds.MetaWeblog.Tests.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.0</span></td>
  <td align=right>174</td>
  <td align=right>111</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>103</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>103</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9299</td>
  <td>thinkabout<span style='display:none'>hub/Configuration.EntityFramework</span></td>
  <td>https://git<span style='display:none'>hub.com/thinkabouthub/Configuration.EntityFramework/commit/8faabbfa9d40f1b24b57ec64e9d0ce73e7243120</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Configuration.Entit<span
  style='display:none'>yFramework.Localization/Configuration.EntityFramework.Localization.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd1.6</span></td>
  <td align=right>321</td>
  <td align=right>113</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>124</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>6</td>
  <td align=right>7</td>
  <td align=right>124</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>0.4</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9300</td>
  <td>wwwliciou<span style='display:none'>s/servicestack-authentication-identityserver</span></td>
  <td>https://git<span style='display:none'>hub.com/wwwlicious/servicestack-authentication-identityserver/commit/2dcc7b5e0a5750b0229bdfdc4ec957e34c5dc650</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/test/IdentityServer<span
  style='display:none'>3.Contrib.ServiceStack.Tests/IdentityServer3.Contrib.ServiceStack.Tests.csproj</span></td>
  <td>.NETFrame<span style='display:none'>work4.6.2</span></td>
  <td align=right>125</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.6666666<span style='display:none'>666666666</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.6666666666666666</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9301</td>
  <td>microsoft/<span style='display:none'>SPP_Public</span></td>
  <td>https://git<span style='display:none'>hub.com/microsoft/SPP_Public/commit/37502f137a8985d61f5da4147d0003f80db208ed</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/api/Web/TPP.Web.<span
  style='display:none'>Api/TPP.Api.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp1.1</span></td>
  <td align=right>939</td>
  <td align=right>229</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>22</td>
  <td align=right>228</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>14</td>
  <td align=right>22</td>
  <td align=right>230</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>13</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>-3</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.6923076923076923</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9302</td>
  <td>theolivenb<span style='display:none'>aum/h5</span></td>
  <td>https://git<span style='display:none'>hub.com/theolivenbaum/h5/commit/49ad367527f5a82d9db8fea851704ae91b77e14b</span></td>
  <td colspan=2 style='mso-ignore:colspan'>H5/Compiler/Translato<span
  style='display:none'>r/H5.Translator.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.1</span></td>
  <td align=right>844</td>
  <td align=right>101</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>12</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>24</td>
  <td align=right>83</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>13</td>
  <td align=right>25</td>
  <td align=right>116</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>12</td>
  <td align=right>0</td>
  <td align=right>33</td>
  <td align=right>0</td>
  <td align=right>-3</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>0.96</td>
  <td>0.8148148<span style='display:none'>148148148</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.8148148148148148</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9303</td>
  <td>CadyIO/ha<span style='display:none'>ngfire-ravendb</span></td>
  <td>https://git<span style='display:none'>hub.com/CadyIO/hangfire-ravendb/commit/f19f1c17b37818656a704fcfdff262f7c6204322</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Hangfire.Raven.Tes<span
  style='display:none'>ts/Hangfire.Raven.Tests.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>170</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>71</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td align=right>4</td>
  <td align=right>71</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>0.6</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9304</td>
  <td>TechSmith/<span style='display:none'>hyde</span></td>
  <td>https://git<span style='display:none'>hub.com/TechSmith/hyde/commit/7cb23c3fa6de37300b3675d46c3a4f9916883ade</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Hyde.IntegrationTe<span
  style='display:none'>st/Hyde.IntegrationTest.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp1.0</span></td>
  <td align=right>264</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>92</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>7</td>
  <td align=right>68</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>-24</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9305</td>
  <td>TechSmith/<span style='display:none'>hyde</span></td>
  <td>https://git<span style='display:none'>hub.com/TechSmith/hyde/commit/7cb23c3fa6de37300b3675d46c3a4f9916883ade</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Hyde.Test/Hyde.Te<span
  style='display:none'>st.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp1.0</span></td>
  <td align=right>173</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>52</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>52</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9306</td>
  <td>ProjectIxia<span style='display:none'>n/Spixi</span></td>
  <td>https://git<span style='display:none'>hub.com/ProjectIxian/Spixi/commit/2133cc584eb8683fb783b9f16c48b5ffba66a89c</span></td>
  <td colspan=2 style='mso-ignore:colspan'>SPIXI/SPIXI/SPIXI.csproj</td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>221</td>
  <td align=right>70</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>69</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>6</td>
  <td align=right>69</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>0.5</td>
  <td>0.5</td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9307</td>
  <td>JudahGabri<span style='display:none'>el/RavenDB.StructuredLog</span></td>
  <td>https://git<span style='display:none'>hub.com/JudahGabriel/RavenDB.StructuredLog/commit/c873b32f7a3e425771aab525d8d86034cf627df3</span></td>
  <td colspan=2 style='mso-ignore:colspan'>RavenDB.StructuredLo<span
  style='display:none'>g/RavenDB.StructuredLog.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>240</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>66</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>6</td>
  <td align=right>6</td>
  <td align=right>73</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>-4</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9308</td>
  <td>rolfwessels<span style='display:none'>/Command.Bot</span></td>
  <td>https://git<span style='display:none'>hub.com/rolfwessels/Command.Bot/commit/30acb58d7dcdf3c8a0caaa1ddd3dfa0f2c1191bd</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Command.Bot.Con<span
  style='display:none'>sole/Command.Bot.Console.csproj</span></td>
  <td>.NETFrame<span style='display:none'>work4.6.1</span></td>
  <td align=right>162</td>
  <td align=right>9</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>2</td>
  <td align=right>6</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>2</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.7142857142857143</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9309</td>
  <td>dapplo/Da<span style='display:none'>pplo.Dopy</span></td>
  <td>https://git<span style='display:none'>hub.com/dapplo/Dapplo.Dopy/commit/1581c88ba420b1658da4e0ec62a2a33532954f55</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Dapplo.Dopy/Dapp<span
  style='display:none'>lo.Dopy.csproj</span></td>
  <td>net5.0</td>
  <td align=right>145</td>
  <td align=right>29</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>33</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>33</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>0.75</td>
  <td>0.75</td>
  <td>0.75</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9310</td>
  <td>coderrio/C<span style='display:none'>oderr.Client.WinForms</span></td>
  <td>https://git<span style='display:none'>hub.com/coderrio/Coderr.Client.WinForms/commit/ea5c0487ab8a51a32ffc8a41ad80f1aad4809a99</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Coderr.Client.WinF<span
  style='display:none'>orms.Tests/Coderr.Client.WinForms.Tests.csproj</span></td>
  <td>.NETFrame<span style='display:none'>work4.6.1</span></td>
  <td align=right>149</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>6</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>0.5</td>
  <td>0.5</td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9311</td>
  <td>mscheetz/<span style='display:none'>KuCoinApi.Net</span></td>
  <td>https://git<span style='display:none'>hub.com/mscheetz/KuCoinApi.Net/commit/56121142fe87e5bf36c3ba03dca063450c6bc10e</span></td>
  <td colspan=2 style='mso-ignore:colspan'>KuCoinApi.NetCore/Ku<span
  style='display:none'>CoinApi.NetCore/KuCoinApi.NetCore.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>143</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>0.6</td>
  <td>0.6</td>
  <td>0.6</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9312</td>
  <td>ThomasZe<span style='display:none'>man/KnxNetCore</span></td>
  <td>https://git<span style='display:none'>hub.com/ThomasZeman/KnxNetCore/commit/4501fcc9c194fad2fbfa4ad840d295ee7aa467a4</span></td>
  <td colspan=2 style='mso-ignore:colspan'>KnxNetCore.UnitTests/<span
  style='display:none'>KnxNetCore.UnitTests.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>168</td>
  <td align=right>67</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>66</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>4</td>
  <td align=right>66</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>0.6666666<span style='display:none'>666666666</span></td>
  <td>0.6666666<span style='display:none'>666666666</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.6666666666666666</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9313</td>
  <td>BK-Soft/Be<span style='display:none'>nchmark.netCoreMappers</span></td>
  <td>https://git<span style='display:none'>hub.com/BK-Soft/Benchmark.netCoreMappers/commit/427c6689be70f49ffa8849ceed50a6457bedd95a</span></td>
  <td colspan=2 style='mso-ignore:colspan'>ObjectsMapperBench<span
  style='display:none'>mark/ObjectsMapperBenchmark.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>175</td>
  <td align=right>81</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>90</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>4</td>
  <td align=right>7</td>
  <td align=right>91</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.5555555<span style='display:none'>555555556</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.5555555555555556</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9314</td>
  <td>mscheetz/<span style='display:none'>CoinbaseProApi.NetCore</span></td>
  <td>https://git<span style='display:none'>hub.com/mscheetz/CoinbaseProApi.NetCore/commit/824ebaaf9797b1209b5127c36e17178fe920d423</span></td>
  <td colspan=2 style='mso-ignore:colspan'>CoinbaseProApi.NetCo<span
  style='display:none'>re/CoinbaseProApi.NetCore/CoinbaseProApi.NetCore.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>143</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>0.6</td>
  <td>0.6</td>
  <td>0.6</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9315</td>
  <td>rhythminm<span style='display:none'>e/splunk.metrics</span></td>
  <td>https://git<span style='display:none'>hub.com/rhythminme/splunk.metrics/commit/faef6f61dc325b089372f73c95580bc551ed6ade</span></td>
  <td colspan=2 style='mso-ignore:colspan'>tests/Splunk.Metrics.<span
  style='display:none'>WebApi.Tests/Splunk.Metrics.WebApi.Tests.csproj</span></td>
  <td>.NETFrame<span style='display:none'>work4.7.2</span></td>
  <td align=right>206</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>7</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>0.75</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9316</td>
  <td>rhythminm<span style='display:none'>e/splunk.metrics</span></td>
  <td>https://git<span style='display:none'>hub.com/rhythminme/splunk.metrics/commit/eb78bc4f2942bd5ab5f764e1d22492f083a1d0a8</span></td>
  <td colspan=2 style='mso-ignore:colspan'>tests/Splunk.Metrics.<span
  style='display:none'>WebApi.Tests/Splunk.Metrics.WebApi.Tests.csproj</span></td>
  <td>.NETFrame<span style='display:none'>work4.7.2</span></td>
  <td align=right>206</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>7</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>0.75</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9317</td>
  <td>terrajobst/<span style='display:none'>sourcebrowser</span></td>
  <td>https://git<span style='display:none'>hub.com/terrajobst/sourcebrowser/commit/3d60ce2e5dc706702080fb4f46b0dbc6f0a2b788</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/HtmlGenerator.Tes<span
  style='display:none'>ts/HtmlGenerator.Tests.csproj</span></td>
  <td>.NETFrame<span style='display:none'>work4.7.2</span></td>
  <td align=right>140</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>8</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.6666666666666666</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9318</td>
  <td>WarBorg/R<span style='display:none'>ATBVFormsPrism</span></td>
  <td>https://git<span style='display:none'>hub.com/WarBorg/RATBVFormsPrism/commit/b8320b7a456c5a680641f501653d7e99c0896ba7</span></td>
  <td colspan=2 style='mso-ignore:colspan'>RATBVFormsPrism/RA<span
  style='display:none'>TBVFormsPrism/RATBVFormsPrism.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>213</td>
  <td align=right>12</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>70</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>4</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>-65</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.6666666666666666</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9319</td>
  <td>govau/digit<span style='display:none'>almarketplace</span></td>
  <td>https://git<span style='display:none'>hub.com/govau/digitalmarketplace/commit/ea3648dccc2ccce1aba8b24bf14a49627cb1cc7f</span></td>
  <td colspan=2 style='mso-ignore:colspan'>subscribers/logs/work<span
  style='display:none'>er.tests/logger.tests.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>237</td>
  <td align=right>122</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>115</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>3</td>
  <td align=right>8</td>
  <td align=right>124</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>0.6</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9320</td>
  <td>govau/digit<span style='display:none'>almarketplace</span></td>
  <td>https://git<span style='display:none'>hub.com/govau/digitalmarketplace/commit/ea3648dccc2ccce1aba8b24bf14a49627cb1cc7f</span></td>
  <td colspan=2 style='mso-ignore:colspan'>subscribers/logs/work<span
  style='display:none'>er/worker.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>706</td>
  <td align=right>108</td>
  <td align=right>9</td>
  <td align=right>0</td>
  <td align=right>10</td>
  <td align=right>0</td>
  <td align=right>10</td>
  <td align=right>0</td>
  <td align=right>20</td>
  <td align=right>54</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>17</td>
  <td align=right>21</td>
  <td align=right>57</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>16</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>-6</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>0.9523809<span style='display:none'>523809523</span></td>
  <td>0.7083333<span style='display:none'>333333334</span></td>
  <td>0.64</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9321</td>
  <td>govau/digit<span style='display:none'>almarketplace</span></td>
  <td>https://git<span style='display:none'>hub.com/govau/digitalmarketplace/commit/ea3648dccc2ccce1aba8b24bf14a49627cb1cc7f</span></td>
  <td colspan=2 style='mso-ignore:colspan'>subscribers/slack/work<span
  style='display:none'>er/worker.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>631</td>
  <td align=right>96</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>0</td>
  <td align=right>20</td>
  <td align=right>64</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>10</td>
  <td align=right>16</td>
  <td align=right>21</td>
  <td align=right>57</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>16</td>
  <td align=right>0</td>
  <td align=right>-7</td>
  <td align=right>0</td>
  <td align=right>-7</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>0.9523809<span style='display:none'>523809523</span></td>
  <td>0.7083333<span style='display:none'>333333334</span></td>
  <td>0.64</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9322</td>
  <td>nuthrash/<span style='display:none'>Minax</span></td>
  <td>https://git<span style='display:none'>hub.com/nuthrash/Minax/commit/81c27f89c93436da0cecd0efe0218f5c3306a7c4</span></td>
  <td colspan=2 style='mso-ignore:colspan'>MinaxWebTranslator/<span
  style='display:none'>MinaxWebTranslator/MinaxWebTranslator.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>249</td>
  <td align=right>12</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>12</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td align=right>7</td>
  <td align=right>12</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.1428571<span style='display:none'>428571428</span></td>
  <td>1.1428571<span style='display:none'>428571428</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.6666666666666666</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9323</td>
  <td>rolfwessels<span style='display:none'>/CoreDocker</span></td>
  <td>https://git<span style='display:none'>hub.com/rolfwessels/CoreDocker/commit/6d8619389ce97589db895a516ed1a1a5090666ae</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/CoreDocker.Api/Co<span
  style='display:none'>reDocker.Api.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.0</span></td>
  <td align=right>617</td>
  <td align=right>163</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>13</td>
  <td align=right>163</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>10</td>
  <td align=right>13</td>
  <td align=right>165</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>-7</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.8571428571428571</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9324</td>
  <td>SiroccoHub<span style='display:none'>/OneWorldDbClient</span></td>
  <td>https://git<span style='display:none'>hub.com/SiroccoHub/OneWorldDbClient/commit/0fa05658438867e0b30246e5a4b8d51e48c154c2</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/OneWorldDbClient<span
  style='display:none'>.SampleWeb/OneWorldDbClient.SampleWeb.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>418</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>37</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>6</td>
  <td align=right>6</td>
  <td align=right>36</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.7142857<span style='display:none'>142857143</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.7142857142857143</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9325</td>
  <td>awaisa/AK</td>
  <td>https://git<span style='display:none'>hub.com/awaisa/AK/commit/4f2b429dd7c299c3d7e0fbf6888935eb1ea44c5a</span></td>
  <td colspan=2 style='mso-ignore:colspan'>ak/BusinessCore/Busin<span
  style='display:none'>essCore.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.0</span></td>
  <td align=right>221</td>
  <td align=right>105</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>33</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>4</td>
  <td align=right>4</td>
  <td align=right>86</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>53</td>
  <td align=right>0</td>
  <td align=right>-4</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.3333333<span style='display:none'>333333333</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.3333333333333333</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9326</td>
  <td>awaisa/AK</td>
  <td>https://git<span style='display:none'>hub.com/awaisa/AK/commit/4f2b429dd7c299c3d7e0fbf6888935eb1ea44c5a</span></td>
  <td colspan=2 style='mso-ignore:colspan'>ak/WebApi/WebApiCo<span
  style='display:none'>re.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.0</span></td>
  <td align=right>2326</td>
  <td align=right>160</td>
  <td align=right>60</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>26</td>
  <td align=right>190</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>30</td>
  <td align=right>21</td>
  <td align=right>26</td>
  <td align=right>224</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>17</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>34</td>
  <td align=right>0</td>
  <td align=right>-13</td>
  <td align=right>-15</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.9259259259259259</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9327</td>
  <td>CityOfPhila<span style='display:none'>delphia/DPD-DocumentAPI</span></td>
  <td>https://git<span style='display:none'>hub.com/CityOfPhiladelphia/DPD-DocumentAPI/commit/3a96849fa93b9a4e787873a4ea2f2bc32bd3ebbe</span></td>
  <td colspan=2 style='mso-ignore:colspan'>DocumentAPI/Docume<span
  style='display:none'>ntAPI.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>363</td>
  <td align=right>122</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>121</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>1</td>
  <td align=right>2</td>
  <td align=right>7</td>
  <td align=right>121</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9328</td>
  <td>CityOfPhila<span style='display:none'>delphia/DPD-DocumentAPI</span></td>
  <td>https://git<span style='display:none'>hub.com/CityOfPhiladelphia/DPD-DocumentAPI/commit/4332c35b9c2118568f3245e09837a9b92faa31fb</span></td>
  <td colspan=2 style='mso-ignore:colspan'>DocumentAPI/Docume<span
  style='display:none'>ntAPI.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>363</td>
  <td align=right>122</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>2</td>
  <td align=right>7</td>
  <td align=right>121</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>2</td>
  <td align=right>7</td>
  <td align=right>121</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9329</td>
  <td>kvantetore<span style='display:none'>/tandembooking</span></td>
  <td>https://git<span style='display:none'>hub.com/kvantetore/tandembooking/commit/d2baee28fa467c3b202dd6fd261bcfd7a6934184</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/src.csproj</td>
  <td>.NETCoreA<span style='display:none'>pp1.1</span></td>
  <td align=right>979</td>
  <td align=right>228</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>10</td>
  <td align=right>0</td>
  <td align=right>22</td>
  <td align=right>217</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>3</td>
  <td align=right>16</td>
  <td align=right>22</td>
  <td align=right>219</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>19</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>-3</td>
  <td align=right>3</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.5172413793103449</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9330</td>
  <td>xerris/Xerri<span style='display:none'>s.DotNet.Core.Aws</span></td>
  <td>https://git<span style='display:none'>hub.com/xerris/Xerris.DotNet.Core.Aws/commit/02a700e28ea1eac673b09d229d8bb788c0088e2b</span></td>
  <td colspan=2 style='mso-ignore:colspan'>test/Xerris.DotNet.Cor<span
  style='display:none'>e.Aws.Test/Xerris.DotNet.Core.Aws.Test.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>233</td>
  <td align=right>49</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>68</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>5</td>
  <td align=right>9</td>
  <td align=right>82</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>14</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>0.8888888<span style='display:none'>888888888</span></td>
  <td>0.8888888<span style='display:none'>888888888</span></td>
  <td>0.7</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9331</td>
  <td>djpnewton<span style='display:none'>/xchwallet</span></td>
  <td>https://git<span style='display:none'>hub.com/djpnewton/xchwallet/commit/59637088a411950fd065047a009516765b01f983</span></td>
  <td colspan=2 style='mso-ignore:colspan'>test/test.csproj</td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>169</td>
  <td align=right>79</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>86</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>2</td>
  <td align=right>5</td>
  <td align=right>82</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>-4</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>2</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.4285714<span style='display:none'>2857142855</span></td>
  <td>0.25</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9332</td>
  <td>microsoft/<span style='display:none'>data-accelerator</span></td>
  <td>https://git<span style='display:none'>hub.com/microsoft/data-accelerator/commit/630fa78263a37ba1598dba002ddc2389301b1d1b</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Services/DataX.Utilitie<span
  style='display:none'>s/DataX.Utilities.CosmosDB/DataX.Utilities.CosmosDB.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.2</span></td>
  <td align=right>180</td>
  <td align=right>90</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>74</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>74</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>0.75</td>
  <td>0.75</td>
  <td>0.75</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9333</td>
  <td>JonPSmith/<span style='display:none'>EfCore.GenericServices</span></td>
  <td>https://git<span style='display:none'>hub.com/JonPSmith/EfCore.GenericServices/commit/087cd42b7f7a42b252d046494c02b17308d8885c</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Benchmarking/Bench<span
  style='display:none'>marking.csproj</span></td>
  <td>net5.0</td>
  <td align=right>179</td>
  <td align=right>132</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>156</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>2</td>
  <td align=right>6</td>
  <td align=right>140</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>-16</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9334</td>
  <td>quartznet/<span style='display:none'>quartznet</span></td>
  <td>https://git<span style='display:none'>hub.com/quartznet/quartznet/commit/a22915a9abac1568accb93eb24b4cce5331c8249</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Quartz.Examples.A<span
  style='display:none'>spNetCore/Quartz.Examples.AspNetCore.csproj</span></td>
  <td>net5.0</td>
  <td align=right>291</td>
  <td align=right>120</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>125</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>4</td>
  <td align=right>6</td>
  <td align=right>125</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.6</td>
  <td>0.6</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9335</td>
  <td>danielgerla<span style='display:none'>g/workflow-core</span></td>
  <td>https://git<span style='display:none'>hub.com/danielgerlag/workflow-core/commit/0f570816758dc62a3f3eab77ab1a56eff03b35b1</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/samples/Workflow<span
  style='display:none'>Core.Sample04/WorkflowCore.Sample04.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>195</td>
  <td align=right>25</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>28</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>84</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>56</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.4285714<span style='display:none'>2857142855</span></td>
  <td>0.25</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9336</td>
  <td>danielgerla<span style='display:none'>g/workflow-core</span></td>
  <td>https://git<span style='display:none'>hub.com/danielgerlag/workflow-core/commit/68a38035c210423fbd6c9f93d3cb34ce53c97943</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/samples/Workflow<span
  style='display:none'>Core.Sample04/WorkflowCore.Sample04.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>195</td>
  <td align=right>25</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>2</td>
  <td align=right>5</td>
  <td align=right>28</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>84</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>56</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.4285714<span style='display:none'>2857142855</span></td>
  <td>0.25</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9337</td>
  <td>danielgerla<span style='display:none'>g/workflow-core</span></td>
  <td>https://git<span style='display:none'>hub.com/danielgerlag/workflow-core/commit/cf2f3ed803f004903456601d9c4a49c9900e3f85</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/samples/Workflow<span
  style='display:none'>Core.Sample04/WorkflowCore.Sample04.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.0</span></td>
  <td align=right>195</td>
  <td align=right>22</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>27</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>83</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>56</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.25</td>
  <td>0.25</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9338</td>
  <td>danielgerla<span style='display:none'>g/workflow-core</span></td>
  <td>https://git<span style='display:none'>hub.com/danielgerlag/workflow-core/commit/647d9b8dfbd8cbd14a3dce02c9358a0bf8efe502</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/samples/Workflow<span
  style='display:none'>Core.Sample04/WorkflowCore.Sample04.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.0</span></td>
  <td align=right>195</td>
  <td align=right>22</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>27</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>83</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>56</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.25</td>
  <td>0.25</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9339</td>
  <td>danielgerla<span style='display:none'>g/workflow-core</span></td>
  <td>https://git<span style='display:none'>hub.com/danielgerlag/workflow-core/commit/d28b54e02b85abca0c628443b61abd005e5605ae</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/samples/Workflow<span
  style='display:none'>Core.Sample04/WorkflowCore.Sample04.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>195</td>
  <td align=right>25</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>28</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>84</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>56</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.4285714<span style='display:none'>2857142855</span></td>
  <td>0.25</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9340</td>
  <td>danielgerla<span style='display:none'>g/workflow-core</span></td>
  <td>https://git<span style='display:none'>hub.com/danielgerlag/workflow-core/commit/d7b3c65028f5badadccca8dfcdb683c0fa13d664</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/samples/Workflow<span
  style='display:none'>Core.Sample04/WorkflowCore.Sample04.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>195</td>
  <td align=right>25</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>28</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>84</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>56</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.4285714<span style='display:none'>2857142855</span></td>
  <td>0.25</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9341</td>
  <td>Accelerider<span style='display:none'>/Accelerider.Windows</span></td>
  <td>https://git<span style='display:none'>hub.com/Accelerider/Accelerider.Windows/commit/a83a3c8413a5e8c518ddf8c3cf32579c6aefff06</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Source/Accelerider.Wi<span
  style='display:none'>ndows.Infrastructure.UI/Accelerider.Windows.Infrastructure.UI.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>279</td>
  <td align=right>79</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>10</td>
  <td align=right>76</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>9</td>
  <td align=right>10</td>
  <td align=right>80</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>9</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>-3</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.8181818<span style='display:none'>181818182</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.6666666666666666</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9342</td>
  <td>Accelerider<span style='display:none'>/Accelerider.Windows</span></td>
  <td>https://git<span style='display:none'>hub.com/Accelerider/Accelerider.Windows/commit/a83a3c8413a5e8c518ddf8c3cf32579c6aefff06</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Source/Accelerider.Wi<span
  style='display:none'>ndows.InfrastructureTests/Accelerider.Windows.InfrastructureTests.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>195</td>
  <td align=right>97</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>45</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>77</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>32</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9343</td>
  <td>Accelerider<span style='display:none'>/Accelerider.Windows</span></td>
  <td>https://git<span style='display:none'>hub.com/Accelerider/Accelerider.Windows/commit/a83a3c8413a5e8c518ddf8c3cf32579c6aefff06</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Source/Accelerider.Wi<span
  style='display:none'>ndows.Modules.NetDisk/Accelerider.Windows.Modules.NetDisk.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>302</td>
  <td align=right>79</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>10</td>
  <td align=right>21</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>8</td>
  <td align=right>10</td>
  <td align=right>79</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>58</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.8181818<span style='display:none'>181818182</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.5384615384615384</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9344</td>
  <td>Accelerider<span style='display:none'>/Accelerider.Windows</span></td>
  <td>https://git<span style='display:none'>hub.com/Accelerider/Accelerider.Windows/commit/a83a3c8413a5e8c518ddf8c3cf32579c6aefff06</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Source/Accelerider.Wi<span
  style='display:none'>ndows/Accelerider.Windows.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>260</td>
  <td align=right>77</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>15</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>5</td>
  <td align=right>8</td>
  <td align=right>77</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>62</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.7777777<span style='display:none'>777777778</span></td>
  <td>0.6</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9345</td>
  <td>linys2333/<span style='display:none'>Lys.NetCore</span></td>
  <td>https://git<span style='display:none'>hub.com/linys2333/Lys.NetCore/commit/8b6f60da2a33f2248f605f6cec9981bf38578552</span></td>
  <td colspan=2 style='mso-ignore:colspan'>MyWebAPI/Host/Host.<span
  style='display:none'>csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.1</span></td>
  <td align=right>416</td>
  <td align=right>279</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>0</td>
  <td align=right>11</td>
  <td align=right>277</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>9</td>
  <td align=right>11</td>
  <td align=right>276</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>10</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td align=right>-3</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.6923076<span style='display:none'>923076923</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.5714285714285714</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9346</td>
  <td>digipost/di<span style='display:none'>gipost-api-client-dotnet</span></td>
  <td>https://git<span style='display:none'>hub.com/digipost/digipost-api-client-dotnet/commit/ae61e86d17b64e88621d0d4c7cba59ccf26d8145</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Digipost.Api.Client.Co<span
  style='display:none'>mmon/Digipost.Api.Client.Common.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>203</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>28</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>4</td>
  <td align=right>5</td>
  <td align=right>6</td>
  <td align=right>20</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>-8</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.7142857<span style='display:none'>142857143</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.7142857142857143</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9347</td>
  <td>digipost/di<span style='display:none'>gipost-api-client-dotnet</span></td>
  <td>https://git<span style='display:none'>hub.com/digipost/digipost-api-client-dotnet/commit/ae61e86d17b64e88621d0d4c7cba59ccf26d8145</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Digipost.Api.Client.Con<span
  style='display:none'>currencyTest/Digipost.Api.Client.ConcurrencyTest.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>151</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>14</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>2</td>
  <td align=right>3</td>
  <td align=right>14</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>0.6666666<span style='display:none'>666666666</span></td>
  <td>0.6666666<span style='display:none'>666666666</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.6666666666666666</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9348</td>
  <td>digipost/di<span style='display:none'>gipost-api-client-dotnet</span></td>
  <td>https://git<span style='display:none'>hub.com/digipost/digipost-api-client-dotnet/commit/ae61e86d17b64e88621d0d4c7cba59ccf26d8145</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Digipost.Api.Client/Dig<span
  style='display:none'>ipost.Api.Client.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>412</td>
  <td align=right>13</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>12</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>11</td>
  <td align=right>106</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>10</td>
  <td align=right>11</td>
  <td align=right>99</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>-7</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>0.9090909<span style='display:none'>090909091</span></td>
  <td>0.5</td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9349</td>
  <td>andrewBez<span style='display:none'>erra/Xamarin_TODO</span></td>
  <td>https://git<span style='display:none'>hub.com/andrewBezerra/Xamarin_TODO/commit/a92efbb40285f32f9c2379d104f565eaceec2a79</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Xamarin_TODO/Xamar<span
  style='display:none'>in_TODO.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>268</td>
  <td align=right>12</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>17</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>5</td>
  <td align=right>6</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>-6</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>-2</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9350</td>
  <td>andrewBez<span style='display:none'>erra/Xamarin_TODO</span></td>
  <td>https://git<span style='display:none'>hub.com/andrewBezerra/Xamarin_TODO/commit/c4900de11c042d887402fb814686e95177bfbd42</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Xamarin_TODO/Xamar<span
  style='display:none'>in_TODO.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.1</span></td>
  <td align=right>268</td>
  <td align=right>12</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>13</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>5</td>
  <td align=right>6</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>-2</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9351</td>
  <td>amzn/ion-h<span style='display:none'>ash-dotnet</span></td>
  <td>https://git<span style='display:none'>hub.com/amzn/ion-hash-dotnet/commit/883ea8ba96521cfe3017cd496d38121e75fe8844</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Amazon.IonHashDotne<span
  style='display:none'>t.Tests/Amazon.IonHashDotnet.Tests.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>141</td>
  <td align=right>10</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>9</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>3</td>
  <td align=right>4</td>
  <td align=right>9</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.6</td>
  <td>0.6</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9352</td>
  <td>ismaelham<span style='display:none'>ed/akka-cluster-management</span></td>
  <td>https://git<span style='display:none'>hub.com/ismaelhamed/akka-cluster-management/commit/7e86e1747ec6ca982ad2eabcfcc20def1bec9ebb</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Akka.Cluster.Mana<span
  style='display:none'>gement/Akka.Cluster.Management.csproj</span></td>
  <td>.NETFrame<span style='display:none'>work4.7</span></td>
  <td align=right>208</td>
  <td align=right>73</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>87</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>5</td>
  <td align=right>86</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=3 style='mso-ignore:colspan'>0.42857142857142855</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9353</td>
  <td>GeorgeLeit<span style='display:none'>head/LiLo.Lite</span></td>
  <td>https://git<span style='display:none'>hub.com/GeorgeLeithead/LiLo.Lite/commit/e5c0dd916515cf4f6f90daa43d72a24f00f5d22c</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Source/LiLo.Lite/LiLo.Li<span
  style='display:none'>te/LiLo.Lite.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.1</span></td>
  <td align=right>383</td>
  <td align=right>19</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>10</td>
  <td align=right>36</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>2</td>
  <td align=right>10</td>
  <td align=right>18</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>-18</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.8181818181818182</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9354</td>
  <td>SnowSE/pr<span style='display:none'>oject_aspen</span></td>
  <td>https://git<span style='display:none'>hub.com/SnowSE/project_aspen/commit/a2e7919e71e3c7d322833e7e30528d45e524de63</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/aspen/aspen.api/a<span
  style='display:none'>spen.api.csproj</span></td>
  <td>net5.0</td>
  <td align=right>346</td>
  <td align=right>56</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>54</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>2</td>
  <td align=right>8</td>
  <td align=right>60</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>2</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.7777777<span style='display:none'>777777778</span></td>
  <td>0.6</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9355</td>
  <td>onka13/do<span style='display:none'>tnet-core-common</span></td>
  <td>https://git<span style='display:none'>hub.com/onka13/dotnet-core-common/commit/34519c3bab2e0d597dd2dea8c039a9c1e7262474</span></td>
  <td colspan=2 style='mso-ignore:colspan'>CoreCommon.Data.Ent<span
  style='display:none'>ityFrameworkBase/CoreCommon.Data.EntityFrameworkBase.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>238</td>
  <td align=right>72</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>101</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>4</td>
  <td align=right>6</td>
  <td align=right>96</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>-5</td>
  <td align=right>0</td>
  <td align=right>-4</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>0.2</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9356</td>
  <td>matand/ba<span style='display:none'>nkor</span></td>
  <td>https://git<span style='display:none'>hub.com/matand/bankor/commit/0c6ecfef9f5e82d86df2520dea3873ed4576c7ca</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Bancor.Api/Bancor<span
  style='display:none'>.Api.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>293</td>
  <td align=right>70</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>124</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>5</td>
  <td align=right>7</td>
  <td align=right>117</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>-7</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>0.75</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9357</td>
  <td>ncosentino<span style='display:none'>/ProjectXyz</span></td>
  <td>https://git<span style='display:none'>hub.com/ncosentino/ProjectXyz/commit/37095f676c6f072611a14677fd003c434e2577e3</span></td>
  <td colspan=2 style='mso-ignore:colspan'>ProjectXyz.Framework.<span
  style='display:none'>Tests/ProjectXyz.Framework.Tests.csproj</span></td>
  <td>.NETFrame<span style='display:none'>work4.8</span></td>
  <td align=right>360</td>
  <td align=right>13</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>13</td>
  <td align=right>13</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>13</td>
  <td align=right>13</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>0.8571428<span style='display:none'>571428571</span></td>
  <td>0.8571428<span style='display:none'>571428571</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.8571428571428571</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9358</td>
  <td>ApexPreda<span style='display:none'>tor13/Nldb3</span></td>
  <td>https://git<span style='display:none'>hub.com/ApexPredator13/Nldb3/commit/8004288c7d0f7f551c184ec6ad073e7c78ee1808</span></td>
  <td colspan=2 style='mso-ignore:colspan'>tests/WebsiteTests/W<span
  style='display:none'>ebsiteTests.csproj</span></td>
  <td>net5.0</td>
  <td align=right>272</td>
  <td align=right>92</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>84</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>7</td>
  <td align=right>9</td>
  <td align=right>82</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>-2</td>
  <td>1:1:0.01</td>
  <td>0.7142857<span style='display:none'>142857143</span></td>
  <td>0.5</td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9359</td>
  <td>guigomesa<span style='display:none'>/ScrapyTibiaCSharp</span></td>
  <td>https://git<span style='display:none'>hub.com/guigomesa/ScrapyTibiaCSharp/commit/b7f6c6908b7faca54f6e9f1269f88424a6ca41ba</span></td>
  <td colspan=2 style='mso-ignore:colspan'>TibiaApi.Database/Tibi<span
  style='display:none'>aApi.Database.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>402</td>
  <td align=right>57</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>97</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td align=right>7</td>
  <td align=right>97</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.5555555555555556</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9360</td>
  <td>xclemence/<span style='display:none'>Dependencies.Viewer</span></td>
  <td>https://git<span style='display:none'>hub.com/xclemence/Dependencies.Viewer/commit/250e2ad8976a6ec6205ef6aa96dcaf3e8acf1cd7</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Dependencies.Vie<span
  style='display:none'>wer.Wpf.App/Dependencies.Viewer.Wpf.App.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>182</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>13</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>3</td>
  <td align=right>6</td>
  <td align=right>68</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>55</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.7142857142857143</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9361</td>
  <td>xclemence/<span style='display:none'>Dependencies.Viewer</span></td>
  <td>https://git<span style='display:none'>hub.com/xclemence/Dependencies.Viewer/commit/250e2ad8976a6ec6205ef6aa96dcaf3e8acf1cd7</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Dependencies.Vie<span
  style='display:none'>wer.Wpf.Controls/Dependencies.Viewer.Wpf.Controls.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>118</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>2</td>
  <td align=right>4</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>0.5</td>
  <td>0.5</td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9362</td>
  <td>mattiasnor<span style='display:none'>dqvist/Galactic-Waste-Management</span></td>
  <td>https://git<span style='display:none'>hub.com/mattiasnordqvist/Galactic-Waste-Management/commit/3d90c7032fde36f322fea3ae80e50a07b6fcc8bc</span></td>
  <td colspan=2 style='mso-ignore:colspan'>GalacticWasteManage<span
  style='display:none'>ment/GalacticWasteManagement.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>274</td>
  <td align=right>89</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>46</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>7</td>
  <td align=right>10</td>
  <td align=right>45</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td align=right>-3</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>0.9</td>
  <td>0.9</td>
  <td colspan=2 style='mso-ignore:colspan'>0.7272727272727273</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9363</td>
  <td>VPKSoft/a<span style='display:none'>mp</span></td>
  <td>https://git<span style='display:none'>hub.com/VPKSoft/amp/commit/b443ff9c4553fdb85ee06fcc5933c636fad4c137</span></td>
  <td colspan=2 style='mso-ignore:colspan'>amp/amp.csproj</td>
  <td>.NETFrame<span style='display:none'>work4.7.2</span></td>
  <td align=right>806</td>
  <td align=right>37</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>27</td>
  <td align=right>36</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>27</td>
  <td align=right>36</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.8620689655172413</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9364</td>
  <td>blackducks<span style='display:none'>oftware/blackduck-nuget-inspector</span></td>
  <td>https://git<span style='display:none'>hub.com/blackducksoftware/blackduck-nuget-inspector/commit/be1b95247c1444c7585611223e60c9a7520b33d6</span></td>
  <td colspan=2 style='mso-ignore:colspan'>BlackduckNugetInspec<span
  style='display:none'>tor/BlackduckNugetInspector.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.0</span></td>
  <td align=right>181</td>
  <td align=right>13</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>86</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>5</td>
  <td align=right>6</td>
  <td align=right>102</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>16</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.7142857142857143</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9365</td>
  <td>doghappy/<span style='display:none'>HappyDog</span></td>
  <td>https://git<span style='display:none'>hub.com/doghappy/HappyDog/commit/99c269133f93f97275225f9ea76dbea4a44052ee</span></td>
  <td colspan=2 style='mso-ignore:colspan'>HappyDog.Console.Api<span
  style='display:none'>/HappyDog.Console.Api.csproj</span></td>
  <td>net5.0</td>
  <td align=right>247</td>
  <td align=right>122</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>132</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td align=right>5</td>
  <td align=right>130</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.6666666<span style='display:none'>666666666</span></td>
  <td colspan=3 style='mso-ignore:colspan'>0.42857142857142855</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9366</td>
  <td>doghappy/<span style='display:none'>HappyDog</span></td>
  <td>https://git<span style='display:none'>hub.com/doghappy/HappyDog/commit/99c269133f93f97275225f9ea76dbea4a44052ee</span></td>
  <td colspan=2 style='mso-ignore:colspan'>HappyDog.WebUI/Hap<span
  style='display:none'>pyDog.WebUI.csproj</span></td>
  <td>net5.0</td>
  <td align=right>432</td>
  <td align=right>159</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>10</td>
  <td align=right>158</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>8</td>
  <td align=right>10</td>
  <td align=right>153</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>-5</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.8181818<span style='display:none'>181818182</span></td>
  <td colspan=3 style='mso-ignore:colspan'>0.42857142857142855</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9367</td>
  <td>mateantice<span style='display:none'>vic/ProjectIvy.Api</span></td>
  <td>https://git<span style='display:none'>hub.com/mateanticevic/ProjectIvy.Api/commit/c18daa8a0bc0b26025f56b35f9366be6bd21052f</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/ProjectIvy.Api/Proj<span
  style='display:none'>ectIvy.Api.csproj</span></td>
  <td>net5.0</td>
  <td align=right>341</td>
  <td align=right>105</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>109</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>5</td>
  <td align=right>6</td>
  <td align=right>47</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>-62</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.7142857<span style='display:none'>142857143</span></td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9368</td>
  <td>Everwealth<span style='display:none'>/ETLBox</span></td>
  <td>https://git<span style='display:none'>hub.com/Everwealth/ETLBox/commit/e52d15ae7309b5d2918c698049796f6d562f4650</span></td>
  <td colspan=2 style='mso-ignore:colspan'>ETLBox/ETLBox.csproj</td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>413</td>
  <td align=right>13</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>13</td>
  <td align=right>119</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>11</td>
  <td align=right>13</td>
  <td align=right>95</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>10</td>
  <td align=right>0</td>
  <td align=right>-24</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>0.9090909<span style='display:none'>090909091</span></td>
  <td>0.75</td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9369</td>
  <td>Everwealth<span style='display:none'>/ETLBox</span></td>
  <td>https://git<span style='display:none'>hub.com/Everwealth/ETLBox/commit/fe3e81fea2b3ddec67eb49190a573aec22be3dbf</span></td>
  <td colspan=2 style='mso-ignore:colspan'>ETLBox/ETLBox.csproj</td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>413</td>
  <td align=right>13</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>13</td>
  <td align=right>119</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>11</td>
  <td align=right>13</td>
  <td align=right>95</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>10</td>
  <td align=right>0</td>
  <td align=right>-24</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>0.9090909<span style='display:none'>090909091</span></td>
  <td>0.75</td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9370</td>
  <td>SimplerSof<span style='display:none'>tware/IBM.IAM.AWS</span></td>
  <td>https://git<span style='display:none'>hub.com/SimplerSoftware/IBM.IAM.AWS/commit/75fa7783e3cd2573a94e62294d13d2788271efdc</span></td>
  <td colspan=2 style='mso-ignore:colspan'>IBM.IAM.AWS.Security<span
  style='display:none'>Token/IBM.IAM.AWS.SecurityToken.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>217</td>
  <td align=right>6</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>34</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td align=right>6</td>
  <td align=right>35</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>0.6</td>
  <td>0.6</td>
  <td>0.6</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9371</td>
  <td>musgrosoft<span style='display:none'>/OLD-v1-Health.API</span></td>
  <td>https://git<span style='display:none'>hub.com/musgrosoft/OLD-v1-Health.API/commit/26a174623221cc7cafaba36c2aa9f4ffb1a31f42</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Repositories/Repos<span
  style='display:none'>itories.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>255</td>
  <td align=right>33</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>65</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>5</td>
  <td align=right>7</td>
  <td align=right>58</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>-7</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.75</td>
  <td>0.4</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9372</td>
  <td>pkozak2/Es<span style='display:none'>p8266VueMeteoStation</span></td>
  <td>https://git<span style='display:none'>hub.com/pkozak2/Esp8266VueMeteoStation/commit/902cc94be330c0b8cef4c3474ba230d69b6feb22</span></td>
  <td colspan=2 style='mso-ignore:colspan'>ApiAndWeb/Esp8266V<span
  style='display:none'>ueMeteo/Esp8266VueMeteo.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.2</span></td>
  <td align=right>313</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>178</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>3</td>
  <td align=right>26</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>-152</td>
  <td align=right>0</td>
  <td align=right>-5</td>
  <td align=right>-3</td>
  <td>1:1:0.01</td>
  <td>0.6</td>
  <td>0.6</td>
  <td>0.0</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9373</td>
  <td>rolfwessels<span style='display:none'>/CoreDocker</span></td>
  <td>https://git<span style='display:none'>hub.com/rolfwessels/CoreDocker/commit/39d24c9cde526d5195e464c982c8a1362c23cd6f</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/CoreDocker.Api/Co<span
  style='display:none'>reDocker.Api.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.0</span></td>
  <td align=right>617</td>
  <td align=right>163</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>13</td>
  <td align=right>163</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>10</td>
  <td align=right>13</td>
  <td align=right>165</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>-7</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.8571428571428571</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9374</td>
  <td>rolfwessels<span style='display:none'>/CoreDocker</span></td>
  <td>https://git<span style='display:none'>hub.com/rolfwessels/CoreDocker/commit/16c2907b44b9a95839a98b1940f4e0dd057139ad</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/CoreDocker.Api/Co<span
  style='display:none'>reDocker.Api.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.0</span></td>
  <td align=right>617</td>
  <td align=right>163</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>13</td>
  <td align=right>163</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>10</td>
  <td align=right>13</td>
  <td align=right>165</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>-7</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.8571428571428571</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9375</td>
  <td>countincog<span style='display:none'>nito/Zametek.Logging</span></td>
  <td>https://git<span style='display:none'>hub.com/countincognito/Zametek.Logging/commit/832b29c744583f610533679e63f0824641170c57</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Zametek.Utility.Lo<span
  style='display:none'>gging/Zametek.Utility.Logging.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd1.4</span></td>
  <td align=right>195</td>
  <td align=right>34</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>79</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>6</td>
  <td align=right>90</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.7142857<span style='display:none'>142857143</span></td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9376</td>
  <td>d-avko/Vib<span style='display:none'>echat.Core</span></td>
  <td>https://git<span style='display:none'>hub.com/d-avko/Vibechat.Core/commit/3824a57b93dc6eedc1a1ba069c27005731da0849</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Vibechat.Web/Vibecha<span
  style='display:none'>t.Web/Vibechat.Web.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.2</span></td>
  <td align=right>831</td>
  <td align=right>100</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>0</td>
  <td align=right>13</td>
  <td align=right>0</td>
  <td align=right>16</td>
  <td align=right>143</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>12</td>
  <td align=right>12</td>
  <td align=right>193</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>50</td>
  <td align=right>0</td>
  <td align=right>-9</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>0.8666666<span style='display:none'>666666667</span></td>
  <td>0.5555555<span style='display:none'>555555556</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.3333333333333333</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9377</td>
  <td>coenm/Ver<span style='display:none'>sionedPdfGenerator</span></td>
  <td>https://git<span style='display:none'>hub.com/coenm/VersionedPdfGenerator/commit/a130ed3b7885226b05f2257e805f0a8b6e1315d2</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/PdfGenerator/PdfG<span
  style='display:none'>enerator.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>145</td>
  <td align=right>5</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>67</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>4</td>
  <td align=right>5</td>
  <td align=right>67</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.6</td>
  <td>0.6</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9378</td>
  <td>howesdom<span style='display:none'>o/XamarinTestSolution</span></td>
  <td>https://git<span style='display:none'>hub.com/howesdomo/XamarinTestSolution/commit/f56bb22477b296b2a0c80cb5085882b56193d310</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Client/Client/Client.csp<span
  style='display:none'>roj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.1</span></td>
  <td align=right>552</td>
  <td align=right>18</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>12</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>13</td>
  <td align=right>45</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>9</td>
  <td align=right>13</td>
  <td align=right>23</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>9</td>
  <td align=right>0</td>
  <td align=right>-22</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>0.8</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9379</td>
  <td>nikkilocke/<span style='display:none'>CodeFirstWebFramework</span></td>
  <td>https://git<span style='display:none'>hub.com/nikkilocke/CodeFirstWebFramework/commit/819c528bb41740090fae4fc6813250fbc17c6fe1</span></td>
  <td colspan=2 style='mso-ignore:colspan'>CodeFirstWebFramew<span
  style='display:none'>ork.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>136</td>
  <td align=right>76</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>76</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>6</td>
  <td align=right>76</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>0.5</td>
  <td>0.5</td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9380</td>
  <td>jthelin/Hell<span style='display:none'>oOwin</span></td>
  <td>https://git<span style='display:none'>hub.com/jthelin/HelloOwin/commit/3a88e85e9f14b1f8ed101e6de28e38b4255715f5</span></td>
  <td colspan=2 style='mso-ignore:colspan'>HelloOwinTests/Hello<span
  style='display:none'>OwinTests.csproj</span></td>
  <td>.NETFrame<span style='display:none'>work4.7</span></td>
  <td align=right>280</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>10</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>2</td>
  <td align=right>10</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.8181818<span style='display:none'>181818182</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.6666666666666666</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9381</td>
  <td>SoluiNet/S<span style='display:none'>oluiNet.DevTools</span></td>
  <td>https://git<span style='display:none'>hub.com/SoluiNet/SoluiNet.DevTools/commit/41ac48a607dfed0ca0f662e64ad36d36f9a804d2</span></td>
  <td colspan=2 style='mso-ignore:colspan'>SoluiNet.DevTools.Cor<span
  style='display:none'>e/SoluiNet.DevTools.Core.csproj</span></td>
  <td>.NETFrame<span style='display:none'>work4.7.2</span></td>
  <td align=right>513</td>
  <td align=right>23</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>16</td>
  <td align=right>56</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>16</td>
  <td align=right>56</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.6842105263157895</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9382</td>
  <td>pact-found<span style='display:none'>ation/pact-net</span></td>
  <td>https://git<span style='display:none'>hub.com/pact-foundation/pact-net/commit/130d8b97a4aa28dd2b9361e22e51d836005ea825</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Samples/EventApi/Con<span
  style='display:none'>sumer.Tests/Consumer.Tests.csproj</span></td>
  <td>.NETFrame<span style='display:none'>work4.6</span></td>
  <td align=right>182</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>6</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>0.6</td>
  <td>0.6</td>
  <td>0.6</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9383</td>
  <td>madslundt<span style='display:none'>/NetCoreMicroservicesSample</span></td>
  <td>https://git<span style='display:none'>hub.com/madslundt/NetCoreMicroservicesSample/commit/d078dae8578aa9b791d36465d798c7dd53a4e355</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Src/MessagesService/<span
  style='display:none'>MessagesService/MessagesService.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>731</td>
  <td align=right>120</td>
  <td align=right>17</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>15</td>
  <td align=right>116</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>14</td>
  <td align=right>15</td>
  <td align=right>119</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>-3</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.875</td>
  <td colspan=2 style='mso-ignore:colspan'>0.5789473684210527</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9384</td>
  <td>madslundt<span style='display:none'>/NetCoreMicroservicesSample</span></td>
  <td>https://git<span style='display:none'>hub.com/madslundt/NetCoreMicroservicesSample/commit/d078dae8578aa9b791d36465d798c7dd53a4e355</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Src/UsersService/Users<span
  style='display:none'>Service/UsersService.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>924</td>
  <td align=right>166</td>
  <td align=right>18</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>10</td>
  <td align=right>0</td>
  <td align=right>19</td>
  <td align=right>154</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>18</td>
  <td align=right>19</td>
  <td align=right>152</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>17</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.9</td>
  <td colspan=3 style='mso-ignore:colspan'>0.46153846153846156</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9385</td>
  <td>micro-elem<span style='display:none'>ents/MicroElements.Swashbuckle.FluentValidation</span></td>
  <td>https://git<span style='display:none'>hub.com/micro-elements/MicroElements.Swashbuckle.FluentValidation/commit/e000b3d21bf7bbd15c7e30da1df02495152db202</span></td>
  <td colspan=2 style='mso-ignore:colspan'>samples/SampleWebA<span
  style='display:none'>pi/SampleWebApi.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.0</span></td>
  <td align=right>190</td>
  <td align=right>241</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>272</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>269</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>-3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>0.8</td>
  <td>0.8</td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9386</td>
  <td>bitfoundati<span style='display:none'>on/ToDoLine</span></td>
  <td>https://git<span style='display:none'>hub.com/bitfoundation/ToDoLine/commit/f544da435035322ed631a3c9fe350a048bc20b79</span></td>
  <td colspan=2 style='mso-ignore:colspan'>App/ToDoLineApp/To<span
  style='display:none'>DoLineApp.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>386</td>
  <td align=right>96</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>11</td>
  <td align=right>109</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>10</td>
  <td align=right>11</td>
  <td align=right>61</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>-48</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>0.9090909<span style='display:none'>090909091</span></td>
  <td>0.9090909<span style='display:none'>090909091</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.9090909090909091</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9387</td>
  <td>ysmoradi/X<span style='display:none'>amApp</span></td>
  <td>https://git<span style='display:none'>hub.com/ysmoradi/XamApp/commit/e346f26aa84d1f5987e1142e0cd062f8f0530bd0</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/XamApp/XamApp.<span
  style='display:none'>csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>369</td>
  <td align=right>105</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>11</td>
  <td align=right>108</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>9</td>
  <td align=right>11</td>
  <td align=right>108</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>9</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>0.8</td>
  <td>0.6363636<span style='display:none'>363636364</span></td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9388</td>
  <td>xerris/Xerri<span style='display:none'>s.DotNet.Core.Aws</span></td>
  <td>https://git<span style='display:none'>hub.com/xerris/Xerris.DotNet.Core.Aws/commit/02a700e28ea1eac673b09d229d8bb788c0088e2b</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Xerris.DotNet.Core<span
  style='display:none'>.Aws/Xerris.DotNet.Core.Aws.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>441</td>
  <td align=right>91</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>13</td>
  <td align=right>91</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>9</td>
  <td align=right>13</td>
  <td align=right>91</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>0.8888888<span style='display:none'>888888888</span></td>
  <td>0.8888888<span style='display:none'>888888888</span></td>
  <td>0.7</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9389</td>
  <td>VirtoComm<span style='display:none'>erce/vc-module-cart</span></td>
  <td>https://git<span style='display:none'>hub.com/VirtoCommerce/vc-module-cart/commit/e6126d6c7ed0cef2731bb6536b8bad37e4dc2e7b</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/VirtoCommerce.Ca<span
  style='display:none'>rtModule.Data/VirtoCommerce.CartModule.Data.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>190</td>
  <td align=right>192</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>80</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>6</td>
  <td align=right>6</td>
  <td align=right>125</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>45</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'>0.3333333333333333</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9390</td>
  <td>VirtoComm<span style='display:none'>erce/vc-module-inventory</span></td>
  <td>https://git<span style='display:none'>hub.com/VirtoCommerce/vc-module-inventory/commit/5639dae5c24d737f76f4a4f390b99762349d7f53</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/VirtoCommerce.Inv<span
  style='display:none'>entoryModule.Data/VirtoCommerce.InventoryModule.Data.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>299</td>
  <td align=right>207</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>163</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>8</td>
  <td align=right>8</td>
  <td align=right>126</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>-37</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.6</td>
  <td>0.6</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9391</td>
  <td>VirtoComm<span style='display:none'>erce/vc-module-image-tools</span></td>
  <td>https://git<span style='display:none'>hub.com/VirtoCommerce/vc-module-image-tools/commit/de7720a3e16b855c2912a38f5dfea20644a9b524</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/VirtoCommerce.Im<span
  style='display:none'>ageToolsModule.Data/VirtoCommerce.ImageToolsModule.Data.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>213</td>
  <td align=right>195</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>71</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>116</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>45</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>0.25</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9392</td>
  <td>VirtoComm<span style='display:none'>erce/vc-module-store</span></td>
  <td>https://git<span style='display:none'>hub.com/VirtoCommerce/vc-module-store/commit/e8145caab6adf6f7f8b2426670bc898ce2fc0a02</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/VirtoCommerce.St<span
  style='display:none'>oreModule.Data/VirtoCommerce.StoreModule.Data.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>308</td>
  <td align=right>218</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>203</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>8</td>
  <td align=right>9</td>
  <td align=right>183</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>9</td>
  <td align=right>0</td>
  <td align=right>-20</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>0.8888888<span style='display:none'>888888888</span></td>
  <td>0.5454545<span style='display:none'>454545454</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.5454545454545454</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9393</td>
  <td>VirtoComm<span style='display:none'>erce/vc-module-pricing</span></td>
  <td>https://git<span style='display:none'>hub.com/VirtoCommerce/vc-module-pricing/commit/088d12cf6c08aa2dc168fed9099a0000b04cd394</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/VirtoCommerce.Pri<span
  style='display:none'>cingModule.Data/VirtoCommerce.PricingModule.Data.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>572</td>
  <td align=right>234</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>10</td>
  <td align=right>0</td>
  <td align=right>14</td>
  <td align=right>211</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>13</td>
  <td align=right>14</td>
  <td align=right>191</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>14</td>
  <td align=right>0</td>
  <td align=right>-20</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>0.9285714<span style='display:none'>285714286</span></td>
  <td>0.6875</td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9394</td>
  <td>MattRyder<span style='display:none'>/LifeCMS</span></td>
  <td>https://git<span style='display:none'>hub.com/MattRyder/LifeCMS/commit/877a4ef726f7105b2748d8678e71570d2898b913</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Services/ContentCr<span
  style='display:none'>eation/ContentCreation.Infrastructure/ContentCreation.Infrastructure.csproj</span></td>
  <td>net5.0</td>
  <td align=right>581</td>
  <td align=right>132</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>14</td>
  <td align=right>155</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>11</td>
  <td align=right>14</td>
  <td align=right>160</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>10</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.8666666<span style='display:none'>666666667</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.6470588235294118</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9395</td>
  <td>microsoft/<span style='display:none'>TailwindTraders-Mobile</span></td>
  <td>https://git<span style='display:none'>hub.com/microsoft/TailwindTraders-Mobile/commit/88d7671659be19e699b87347ea1fc17e41b2dff6</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Source/TailwindTrader<span
  style='display:none'>s.Mobile/TailwindTraders.Mobile/TailwindTraders.Mobile.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>434</td>
  <td align=right>16</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>13</td>
  <td align=right>18</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>11</td>
  <td align=right>13</td>
  <td align=right>69</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>51</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.8571428571428571</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9396</td>
  <td>RickStrahl/<span style='display:none'>Westwind.Globalization</span></td>
  <td>https://git<span style='display:none'>hub.com/RickStrahl/Westwind.Globalization/commit/554ff2592d66c7f5fa3547d9691202085b73ee2a</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/NetCore/Westwind<span
  style='display:none'>.Globalization.Test.NetCore/Westwind.Globalization.Test.NetCore.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.0</span></td>
  <td align=right>177</td>
  <td align=right>93</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>52</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>7</td>
  <td align=right>7</td>
  <td align=right>71</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>19</td>
  <td align=right>0</td>
  <td align=right>-3</td>
  <td align=right>-2</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.5555555<span style='display:none'>555555556</span></td>
  <td>0.4</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9397</td>
  <td>daniellittle<span style='display:none'>dev/Enexure.MicroBus</span></td>
  <td>https://git<span style='display:none'>hub.com/daniellittledev/Enexure.MicroBus/commit/18a42c4eae6bf53d6b74bd62b5580181499b5414</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Enexure.MicroBus.<span
  style='display:none'>Saga.Autofac.Tests/Enexure.MicroBus.Saga.Autofac.Tests.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.0</span></td>
  <td align=right>151</td>
  <td align=right>74</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>73</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>66</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>-7</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=3 style='mso-ignore:colspan'>0.42857142857142855</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9398</td>
  <td>DynamicHa<span style='display:none'>nds/NodaMoney</span></td>
  <td>https://git<span style='display:none'>hub.com/DynamicHands/NodaMoney/commit/0cc1b64e32e64bd04a3d4d00ec046e3eeb5f5eed</span></td>
  <td colspan=2 style='mso-ignore:colspan'>tests/NodaMoney.Seri<span
  style='display:none'>alization.AspNet.Tests/NodaMoney.Serialization.AspNet.Tests.csproj</span></td>
  <td>.NETFrame<span style='display:none'>work4.5.2</span></td>
  <td align=right>155</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>0.8</td>
  <td>0.8</td>
  <td>0.8</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9399</td>
  <td>DynamicHa<span style='display:none'>nds/NodaMoney</span></td>
  <td>https://git<span style='display:none'>hub.com/DynamicHands/NodaMoney/commit/0cc1b64e32e64bd04a3d4d00ec046e3eeb5f5eed</span></td>
  <td colspan=2 style='mso-ignore:colspan'>tests/NodaMoney.Test<span
  style='display:none'>s/NodaMoney.Tests.csproj</span></td>
  <td>.NETFrame<span style='display:none'>work4.6.2</span></td>
  <td align=right>185</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>6</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9400</td>
  <td>NikolayIT/<span style='display:none'>MusicX</span></td>
  <td>https://git<span style='display:none'>hub.com/NikolayIT/MusicX/commit/89a68ffac5ca9a76efb594a14db03699cb9b7e05</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Tests/Sandbox/San<span
  style='display:none'>dbox.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.0</span></td>
  <td align=right>262</td>
  <td align=right>27</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>84</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>6</td>
  <td align=right>6</td>
  <td align=right>83</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.7142857<span style='display:none'>142857143</span></td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9401</td>
  <td>Sharebook<span style='display:none'>BR/sharebook-backend</span></td>
  <td>https://git<span style='display:none'>hub.com/SharebookBR/sharebook-backend/commit/9b6e87d57feb5e6d0bfda6323a7f9cd7a3b2be21</span></td>
  <td colspan=2 style='mso-ignore:colspan'>ShareBook/ShareBook.<span
  style='display:none'>Tests.BDD/ShareBook.Tests.BDD.csproj</span></td>
  <td>net5.0</td>
  <td align=right>210</td>
  <td align=right>78</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>45</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>7</td>
  <td align=right>44</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>0.8333333<span style='display:none'>333333334</span></td>
  <td>0.8333333<span style='display:none'>333333334</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.8333333333333334</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9402</td>
  <td>damienbod<span style='display:none'>/AspNetCoreWindowsAuth</span></td>
  <td>https://git<span style='display:none'>hub.com/damienbod/AspNetCoreWindowsAuth/commit/fc7caf370af8d2070fb73d266771b8d4f2c7b8a8</span></td>
  <td colspan=2 style='mso-ignore:colspan'>MvcHybridClient/Mvc<span
  style='display:none'>HybridClient.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>487</td>
  <td align=right>56</td>
  <td align=right>10</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>11</td>
  <td align=right>82</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>10</td>
  <td align=right>11</td>
  <td align=right>87</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td>1:1:0.01</td>
  <td>0.8</td>
  <td>0.8</td>
  <td>0.8</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9403</td>
  <td>alanedwar<span style='display:none'>des/Estranged.Lfs</span></td>
  <td>https://git<span style='display:none'>hub.com/alanedwardes/Estranged.Lfs/commit/c429933cbda081d28b12c28fef1b88f33fc96319</span></td>
  <td colspan=2 style='mso-ignore:colspan'>hosting/Estranged.Lfs.<span
  style='display:none'>Hosting.Lambda/Estranged.Lfs.Hosting.Lambda.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.1</span></td>
  <td align=right>678</td>
  <td align=right>168</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>16</td>
  <td align=right>125</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>12</td>
  <td align=right>16</td>
  <td align=right>16</td>
  <td align=right>175</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>10</td>
  <td align=right>16</td>
  <td align=right>0</td>
  <td align=right>50</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.6842105<span style='display:none'>263157895</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.5238095238095238</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9404</td>
  <td>dapplo/Da<span style='display:none'>pplo.Jira</span></td>
  <td>https://git<span style='display:none'>hub.com/dapplo/Dapplo.Jira/commit/bd18c9717aa57f68c93735d00c7869744aa346bf</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Dapplo.Jira.Tests/D<span
  style='display:none'>applo.Jira.Tests.csproj</span></td>
  <td>.NETFrame<span style='display:none'>work4.7.1</span></td>
  <td align=right>192</td>
  <td align=right>26</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>26</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>7</td>
  <td align=right>24</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9405</td>
  <td>Lakritzator<span style='display:none'>/Pip</span></td>
  <td>https://git<span style='display:none'>hub.com/Lakritzator/Pip/commit/9816801321f8aa128d8664f3d366a66935d8772f</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Pip/Pip.csproj</td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>574</td>
  <td align=right>47</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>18</td>
  <td align=right>48</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>18</td>
  <td align=right>18</td>
  <td align=right>49</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>15</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-3</td>
  <td>1:1:0.01</td>
  <td>0.8333333<span style='display:none'>333333334</span></td>
  <td>0.7368421<span style='display:none'>052631579</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.5714285714285714</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9406</td>
  <td>dapplo/Da<span style='display:none'>pplo.Confluence</span></td>
  <td>https://git<span style='display:none'>hub.com/dapplo/Dapplo.Confluence/commit/4804bc91e4eb8f1c2894a5ea5d12c3d38ff3bb02</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Dapplo.Confluence<span
  style='display:none'>.Tests/Dapplo.Confluence.Tests.csproj</span></td>
  <td>.NETFrame<span style='display:none'>work4.7.1</span></td>
  <td align=right>250</td>
  <td align=right>28</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>26</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>9</td>
  <td align=right>26</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.5555555555555556</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9407</td>
  <td>easyquery/<span style='display:none'>AspNetCoreSamples</span></td>
  <td>https://git<span style='display:none'>hub.com/easyquery/DotNetSamples/commit/2aa7e142cc063dfdeadeeb1c2357b324c6d08dba</span></td>
  <td colspan=2 style='mso-ignore:colspan'>AspNetCore/Razor-Mv<span
  style='display:none'>c/Razor.AdvancedSearch/EqDemo.AspNetCoreRazor.AdvancedSearch.csproj</span></td>
  <td>net5.0</td>
  <td align=right>485</td>
  <td align=right>195</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>202</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>9</td>
  <td align=right>202</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>0.8333333<span style='display:none'>333333334</span></td>
  <td>0.8333333<span style='display:none'>333333334</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.8333333333333334</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9408</td>
  <td>easyquery/<span style='display:none'>AspNetCoreSamples</span></td>
  <td>https://git<span style='display:none'>hub.com/easyquery/DotNetSamples/commit/2aa7e142cc063dfdeadeeb1c2357b324c6d08dba</span></td>
  <td colspan=2 style='mso-ignore:colspan'>AspNetCore/Razor-Mv<span
  style='display:none'>c/RazorTypeScript.AdHocReporting/EqDemo.AspNetCoreRazorTypeScript.AdhocReporting.csproj</span></td>
  <td>net5.0</td>
  <td align=right>500</td>
  <td align=right>195</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>202</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>9</td>
  <td align=right>202</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>0.8571428<span style='display:none'>571428571</span></td>
  <td>0.8571428<span style='display:none'>571428571</span></td>
  <td>0.625</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9409</td>
  <td>itinero/Op<span style='display:none'>enLR</span></td>
  <td>https://git<span style='display:none'>hub.com/itinero/OpenLR/commit/80e6ad22b00521daffe3b395e7b88ce26f55544c</span></td>
  <td colspan=2 style='mso-ignore:colspan'>test/OpenLR.Test/Ope<span
  style='display:none'>nLR.Test.csproj</span></td>
  <td>.NETFrame<span style='display:none'>work4.5.1</span></td>
  <td align=right>118</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>2</td>
  <td align=right>5</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>2</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.6666666<span style='display:none'>666666666</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.6666666666666666</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9410</td>
  <td>brminnick/<span style='display:none'>XamarinIoTWorkshop</span></td>
  <td>https://git<span style='display:none'>hub.com/brminnick/XamarinIoTWorkshop/commit/7e72e5644392540673be89dc653e153d9f657348</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Source/XamarinIoTWo<span
  style='display:none'>rkshop/XamarinIoTWorkshop.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.1</span></td>
  <td align=right>370</td>
  <td align=right>12</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>41</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>8</td>
  <td align=right>8</td>
  <td align=right>43</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>-3</td>
  <td align=right>-3</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.7777777<span style='display:none'>777777778</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.7777777777777778</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9411</td>
  <td>froko/Simp<span style='display:none'>leDomain</span></td>
  <td>https://git<span style='display:none'>hub.com/froko/SimpleDomain/commit/e53ea93a1bf85125c8804d704457dd4bc8400392</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/SimpleDomain.MS<span
  style='display:none'>MQ.Facts/SimpleDomain.MSMQ.Facts.csproj</span></td>
  <td>.NETFrame<span style='display:none'>work4.6.1</span></td>
  <td align=right>165</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>9</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>5</td>
  <td align=right>6</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.7142857142857143</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9412</td>
  <td>rookxx/Styl<span style='display:none'>eCopAnalyzers.CLI</span></td>
  <td>https://git<span style='display:none'>hub.com/rookxx/StyleCopAnalyzers.CLI/commit/aa5986a48e6971613f48b823f4ab3856fe715377</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/StyleCopAnalyzers.<span
  style='display:none'>CLI.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>349</td>
  <td align=right>71</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>88</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>8</td>
  <td align=right>9</td>
  <td align=right>21</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>-67</td>
  <td align=right>0</td>
  <td align=right>-3</td>
  <td align=right>-3</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9413</td>
  <td>rookxx/Styl<span style='display:none'>eCopAnalyzers.CLI</span></td>
  <td>https://git<span style='display:none'>hub.com/rookxx/StyleCopAnalyzers.CLI/commit/2f27891270ff9ce757817d7d91a41c83166887c5</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/StyleCopAnalyzers.<span
  style='display:none'>CLI.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>349</td>
  <td align=right>71</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>88</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>8</td>
  <td align=right>9</td>
  <td align=right>21</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>-67</td>
  <td align=right>0</td>
  <td align=right>-3</td>
  <td align=right>-3</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9414</td>
  <td>Azure/dedi<span style='display:none'>cated-hosts-manager</span></td>
  <td>https://git<span style='display:none'>hub.com/Azure/dedicated-hosts-manager/commit/a08067e1d60bf95f9d252ca4b656ae1d34fb5299</span></td>
  <td colspan=2 style='mso-ignore:colspan'>DedicatedHostsTests/<span
  style='display:none'>DedicatedHostsManagerTests.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>137</td>
  <td align=right>97</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>78</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>6</td>
  <td align=right>6</td>
  <td align=right>93</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>15</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9415</td>
  <td>aws-quicks<span style='display:none'>tart/connect-integration-aspect-wfm</span></td>
  <td>https://git<span style='display:none'>hub.com/aws-quickstart/connect-integration-aspect-wfm/commit/1eb29a7e876be6f2d2d6fc858e03552fe90f99b3</span></td>
  <td colspan=2 style='mso-ignore:colspan'>functions/source/real-<span
  style='display:none'>time-adherence/AspectKinesisLamda.Tests/AspectKinesisLamda.Tests.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.1</span></td>
  <td align=right>213</td>
  <td align=right>70</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>100</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>8</td>
  <td align=right>8</td>
  <td align=right>9</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>-91</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>-3</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.7777777777777778</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9416</td>
  <td>aws-quicks<span style='display:none'>tart/connect-integration-aspect-wfm</span></td>
  <td>https://git<span style='display:none'>hub.com/aws-quickstart/connect-integration-aspect-wfm/commit/1d49797b5c57e8393cdf6670db864126eec890f3</span></td>
  <td colspan=2 style='mso-ignore:colspan'>functions/source/real-<span
  style='display:none'>time-adherence/AspectKinesisLamda.Tests/AspectKinesisLamda.Tests.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.1</span></td>
  <td align=right>213</td>
  <td align=right>70</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>100</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>8</td>
  <td align=right>8</td>
  <td align=right>9</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>-91</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>-3</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.7777777777777778</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9417</td>
  <td>Ontica/Em<span style='display:none'>piria.Extensions</span></td>
  <td>https://git<span style='display:none'>hub.com/Ontica/Empiria.Extensions/commit/79612b758a5eca3f7b931956c3b465e5e41bacaa</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Messaging.Tests/Empi<span
  style='display:none'>ria.Messaging.Tests.csproj</span></td>
  <td>.NETFrame<span style='display:none'>work4.8</span></td>
  <td align=right>299</td>
  <td align=right>12</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>11</td>
  <td align=right>12</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>11</td>
  <td align=right>11</td>
  <td align=right>12</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>-3</td>
  <td>1:1:0.01</td>
  <td>0.7272727<span style='display:none'>272727273</span></td>
  <td>0.5833333<span style='display:none'>333333334</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.5833333333333334</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9418</td>
  <td>Ontica/Em<span style='display:none'>piria.Extensions</span></td>
  <td>https://git<span style='display:none'>hub.com/Ontica/Empiria.Extensions/commit/79612b758a5eca3f7b931956c3b465e5e41bacaa</span></td>
  <td colspan=2 style='mso-ignore:colspan'>WebApi.Client.Tests/E<span
  style='display:none'>mpiria.WebApi.Client.Tests.csproj</span></td>
  <td>.NETFrame<span style='display:none'>work4.8</span></td>
  <td align=right>299</td>
  <td align=right>12</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>11</td>
  <td align=right>12</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>11</td>
  <td align=right>11</td>
  <td align=right>12</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>-3</td>
  <td>1:1:0.01</td>
  <td>0.7272727<span style='display:none'>272727273</span></td>
  <td>0.5833333<span style='display:none'>333333334</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.5833333333333334</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9419</td>
  <td>punker76/<span style='display:none'>Popcorn</span></td>
  <td>https://git<span style='display:none'>hub.com/punker76/Popcorn/commit/f18f00a140ca145452fd92e2ad93796d06edbed6</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Popcorn/Popcorn.cspr<span
  style='display:none'>oj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>2309</td>
  <td align=right>154</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>20</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>73</td>
  <td align=right>183</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>12</td>
  <td align=right>50</td>
  <td align=right>73</td>
  <td align=right>188</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>50</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>-3</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.9729729<span style='display:none'>72972973</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.7590361445783133</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9420</td>
  <td>LBHackney<span style='display:none'>-IT/document-api</span></td>
  <td>https://git<span style='display:none'>hub.com/LBHackney-IT/document-api/commit/d3c8a31237cf16c9fc05b099a2f19f98feb3f684</span></td>
  <td colspan=2 style='mso-ignore:colspan'>document-api.Tests/d<span
  style='display:none'>ocument-api.Tests.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>193</td>
  <td align=right>104</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>36</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>6</td>
  <td align=right>8</td>
  <td align=right>72</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>36</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td>1:1:0.01</td>
  <td>1.0</td>
  <td>0.5</td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9421</td>
  <td>JustinWilki<span style='display:none'>nson/Cryptonyms</span></td>
  <td>https://git<span style='display:none'>hub.com/JustinWilkinson/Cryptonyms/commit/3682d340455adebf5e69114a96100db4cf798ce6</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Server/Cryptonyms.Ser<span
  style='display:none'>ver.csproj</span></td>
  <td>net5.0</td>
  <td align=right>363</td>
  <td align=right>91</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>10</td>
  <td align=right>41</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>10</td>
  <td align=right>34</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>-7</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td>1:1:0.01</td>
  <td>0.6666666<span style='display:none'>666666666</span></td>
  <td>0.6666666<span style='display:none'>666666666</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.6666666666666666</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>9422</td>
  <td>MechaDra<span style='display:none'>gonX/Majora</span></td>
  <td>https://git<span style='display:none'>hub.com/MechaDragonX/Majora/commit/d9d1fb96d53a60c6bbc77edd6468bb6ecd10abc9</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Majora.Desktop/Major<span
  style='display:none'>a.Desktop.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>225</td>
  <td align=right>142</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>45</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>5</td>
  <td align=right>8</td>
  <td align=right>45</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td>1:1:0.01</td>
  <td>0.5714285<span style='display:none'>714285714</span></td>
  <td>0.5714285<span style='display:none'>714285714</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.5714285714285714</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>10001</td>
  <td>fals/cqrs-cl<span style='display:none'>ean-eventual-consistency</span></td>
  <td>https://git<span style='display:none'>hub.com/fals/cqrs-clean-eventual-consistency/commit/0869f8e40bace5492202bc2d819a00d1e1195487</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Ametista.Api/Amet<span
  style='display:none'>ista.Api.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.0</span></td>
  <td align=right>8</td>
  <td align=right>278</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>40</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>1</td>
  <td align=right>6</td>
  <td align=right>7</td>
  <td align=right>15</td>
  <td align=right>36</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>14</td>
  <td align=right>-15</td>
  <td align=right>-4</td>
  <td align=right>-4</td>
  <td align=right>-2</td>
  <td align=right>7</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.8571428<span style='display:none'>571428571</span></td>
  <td>0.4444444<span style='display:none'>444444444</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.4444444444444444</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>10002</td>
  <td>robisim74/<span style='display:none'>AngularSPAWebAPI</span></td>
  <td>https://git<span style='display:none'>hub.com/robisim74/AngularSPAWebAPI/commit/8e50133188a894fdf744e5c636798e41d6a85c75</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/AngularSPAWebAP<span
  style='display:none'>I/AngularSPAWebAPI.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp1.1</span></td>
  <td align=right>24</td>
  <td align=right>221</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>10</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>230</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>22</td>
  <td align=right>26</td>
  <td align=right>227</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>23</td>
  <td align=right>-26</td>
  <td align=right>-3</td>
  <td align=right>-2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.9130434<span style='display:none'>782608695</span></td>
  <td>0.9130434<span style='display:none'>782608695</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.5714285714285714</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>10005</td>
  <td>dotnet-pre<span style='display:none'>sentations/aspnetcore-app-workshop</span></td>
  <td>https://git<span style='display:none'>hub.com/dotnet-presentations/aspnetcore-app-workshop/commit/ce5bf9d06acf04aba73656a9c8c5462c487737c3</span></td>
  <td colspan=2 style='mso-ignore:colspan'>save-points/6-Deploy<span
  style='display:none'>ment-docker/ConferencePlanner/FrontEnd/FrontEnd.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>9</td>
  <td align=right>160</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>122</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>9</td>
  <td align=right>15</td>
  <td align=right>122</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>12</td>
  <td align=right>-15</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.4615384<span style='display:none'>6153846156</span></td>
  <td>0.4615384<span style='display:none'>6153846156</span></td>
  <td colspan=3 style='mso-ignore:colspan'>0.46153846153846156</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100010</td>
  <td>phongnguy<span style='display:none'>end/Practical.CleanArchitecture</span></td>
  <td>https://git<span style='display:none'>hub.com/phongnguyend/Practical.CleanArchitecture/commit/42f0e227185092642a1ccedb7e9c4df952d3eb37</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Monolith/Classifie<span
  style='display:none'>dAds.Infrastructure/ClassifiedAds.Infrastructure.csproj</span></td>
  <td>net5.0</td>
  <td align=right>46</td>
  <td align=right>320</td>
  <td align=right>18</td>
  <td align=right>4</td>
  <td align=right>13</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>233</td>
  <td align=right>2</td>
  <td align=right>9</td>
  <td align=right>2</td>
  <td align=right>12</td>
  <td align=right>45</td>
  <td align=right>55</td>
  <td align=right>202</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>11</td>
  <td align=right>40</td>
  <td align=right>-55</td>
  <td align=right>-31</td>
  <td align=right>-11</td>
  <td align=right>-1</td>
  <td align=right>-5</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.7111111<span style='display:none'>111111111</span></td>
  <td>0.6739130<span style='display:none'>434782609</span></td>
  <td colspan=3 style='mso-ignore:colspan'>0.42592592592592593</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100012</td>
  <td>asadsahi/A<span style='display:none'>spNetCoreSpa</span></td>
  <td>https://git<span style='display:none'>hub.com/asadsahi/AspNetCoreSpa/commit/eebd2a84b06be339ead476dada31f41a05ff82e4</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Presentation/STS/S<span
  style='display:none'>TS.csproj</span></td>
  <td>net5.0</td>
  <td align=right>12</td>
  <td align=right>151</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>139</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>11</td>
  <td align=right>21</td>
  <td align=right>137</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>20</td>
  <td align=right>-21</td>
  <td align=right>-2</td>
  <td align=right>-1</td>
  <td align=right>-1</td>
  <td align=right>9</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.5</td>
  <td>0.4285714<span style='display:none'>2857142855</span></td>
  <td colspan=3 style='mso-ignore:colspan'>0.36363636363636365</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100015</td>
  <td>nguyenquy<span style='display:none'>hy/Flight-Tracker-StreamDeck</span></td>
  <td>https://git<span style='display:none'>hub.com/nguyenquyhy/Flight-Tracker-StreamDeck/commit/c93be2864d62eab727caa0c5d04511fdffc39dba</span></td>
  <td colspan=2 style='mso-ignore:colspan'>FlightStreamDeck.Add<span
  style='display:none'>On/FlightStreamDeck.AddOn.csproj</span></td>
  <td>net5.0</td>
  <td align=right>17</td>
  <td align=right>59</td>
  <td align=right>17</td>
  <td align=right>0</td>
  <td align=right>12</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>59</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>15</td>
  <td align=right>16</td>
  <td align=right>60</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>12</td>
  <td align=right>-16</td>
  <td align=right>1</td>
  <td align=right>-5</td>
  <td align=right>0</td>
  <td align=right>-3</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>1.0</td>
  <td>0.7142857<span style='display:none'>142857143</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.7142857142857143</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100018</td>
  <td>EasyAbp/A<span style='display:none'>bp.SettingUi</span></td>
  <td>https://git<span style='display:none'>hub.com/EasyAbp/Abp.SettingUi/commit/2cdea3214ffff1996cd17959d95a64614c381023</span></td>
  <td colspan=2 style='mso-ignore:colspan'>sample/MyAbpApp/src<span
  style='display:none'>/MyAbpApp.Web/MyAbpApp.Web.csproj</span></td>
  <td>net5.0</td>
  <td align=right>15</td>
  <td align=right>212</td>
  <td align=right>2</td>
  <td align=right>1</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>233</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>14</td>
  <td align=right>17</td>
  <td align=right>233</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>11</td>
  <td align=right>-17</td>
  <td align=right>0</td>
  <td align=right>-4</td>
  <td align=right>-1</td>
  <td align=right>-3</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.6</td>
  <td>0.4117647<span style='display:none'>058823529</span></td>
  <td colspan=3 style='mso-ignore:colspan'>0.14285714285714285</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100019</td>
  <td>DavidCBerr<span style='display:none'>y13/FoodTruckNationApi</span></td>
  <td>https://git<span style='display:none'>hub.com/DavidCBerry13/FoodTruckNationApi/commit/ebbc28c444e8f3a0a35d21238b2107de990a2539</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/FoodTruckNationA<span
  style='display:none'>pi.Tests.Integration/FoodTruckNationApi.Tests.Integration.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.1</span></td>
  <td align=right>7</td>
  <td align=right>103</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>134</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>6</td>
  <td align=right>72</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td align=right>-6</td>
  <td align=right>-62</td>
  <td align=right>-2</td>
  <td align=right>1</td>
  <td align=right>-2</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.8</td>
  <td>0.5</td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100020</td>
  <td>mhutch/M<span style='display:none'>onoDevelop.MSBuildEditor</span></td>
  <td>https://git<span style='display:none'>hub.com/mhutch/MonoDevelop.MSBuildEditor/commit/3b928ddb25f78649d891ac92c4eb6864ed1f5448</span></td>
  <td colspan=2 style='mso-ignore:colspan'>MonoDevelop.MSBuild<span
  style='display:none'>.Tests/MonoDevelop.MSBuild.Tests.csproj</span></td>
  <td>.NETFrame<span style='display:none'>work4.7.2</span></td>
  <td align=right>8</td>
  <td align=right>42</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>40</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>8</td>
  <td align=right>11</td>
  <td align=right>33</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>10</td>
  <td align=right>-11</td>
  <td align=right>-7</td>
  <td align=right>-2</td>
  <td align=right>-1</td>
  <td align=right>2</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.7777777<span style='display:none'>777777778</span></td>
  <td>0.7777777<span style='display:none'>777777778</span></td>
  <td>0.6</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100021</td>
  <td>aspnetrun/<span style='display:none'>run-aspnetcore-basics</span></td>
  <td>https://git<span style='display:none'>hub.com/aspnetrun/run-aspnetcore-basics/commit/b26a8bdde3ed5962cc601f3a5f7ffd770b1b133f</span></td>
  <td colspan=2 style='mso-ignore:colspan'>AspnetRunBasics/Aspn<span
  style='display:none'>etRunBasics.csproj</span></td>
  <td>net5.0</td>
  <td align=right>7</td>
  <td align=right>115</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>104</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>2</td>
  <td align=right>2</td>
  <td align=right>6</td>
  <td align=right>15</td>
  <td align=right>121</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>14</td>
  <td align=right>-15</td>
  <td align=right>17</td>
  <td align=right>-1</td>
  <td align=right>-1</td>
  <td align=right>8</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.3571428<span style='display:none'>5714285715</span></td>
  <td>0.2666666<span style='display:none'>6666666666</span></td>
  <td colspan=3 style='mso-ignore:colspan'>0.11764705882352941</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100022</td>
  <td>Azure-Sam<span style='display:none'>ples/storage-blob-upload-from-webapp</span></td>
  <td>https://git<span style='display:none'>hub.com/Azure-Samples/storage-blob-upload-from-webapp/commit/1130984c77a85b9cb5647e69ed384664a012e81b</span></td>
  <td colspan=2 style='mso-ignore:colspan'>ImageResizeWebApp/I<span
  style='display:none'>mageResizeWebApp/ImageResizeWebApp.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.0</span></td>
  <td align=right>12</td>
  <td align=right>191</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>209</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>6</td>
  <td align=right>12</td>
  <td align=right>150</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>6</td>
  <td align=right>-12</td>
  <td align=right>-59</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.5714285<span style='display:none'>714285714</span></td>
  <td>0.5714285<span style='display:none'>714285714</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.5714285714285714</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100027</td>
  <td>Jaxelr/Nan<span style='display:none'>cy.Template.Webservice</span></td>
  <td>https://git<span style='display:none'>hub.com/Jaxelr/Nancy.Template.Webservice/commit/ca1393b58c6d3107059eb28e2ffefe1b862e25d7</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Content/src/Nancy.Te<span
  style='display:none'>mplate.WebService.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.2</span></td>
  <td align=right>13</td>
  <td align=right>159</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>156</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>7</td>
  <td align=right>12</td>
  <td align=right>156</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>2</td>
  <td align=right>2</td>
  <td align=right>6</td>
  <td align=right>-12</td>
  <td align=right>0</td>
  <td align=right>-3</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>1.2</td>
  <td>1.2</td>
  <td colspan=2 style='mso-ignore:colspan'>0.8333333333333334</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100032</td>
  <td>uvasoftwar<span style='display:none'>e/scanii-dotnet</span></td>
  <td>https://git<span style='display:none'>hub.com/uvasoftware/scanii-dotnet/commit/08249aca7da83bebde7d96cc809a1f68fb0c1ad4</span></td>
  <td colspan=2 style='mso-ignore:colspan'>UvaSoftware.Scanii/Uv<span
  style='display:none'>aSoftware.Scanii.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>5</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>33</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>2</td>
  <td align=right>1</td>
  <td align=right>2</td>
  <td align=right>4</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>3</td>
  <td align=right>-4</td>
  <td align=right>-29</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.3333333333333333</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100034</td>
  <td>JerryBian/b<span style='display:none'>log.laobian.me</span></td>
  <td>https://git<span style='display:none'>hub.com/JerryBian/blog.laobian.me/commit/cd3d46471cc3f11cb3df7eec3287da145da50e1b</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/share/Laobian.Shar<span
  style='display:none'>e.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>10</td>
  <td align=right>23</td>
  <td align=right>2</td>
  <td align=right>1</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>90</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>7</td>
  <td align=right>10</td>
  <td align=right>85</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>2</td>
  <td align=right>2</td>
  <td align=right>4</td>
  <td align=right>-10</td>
  <td align=right>-5</td>
  <td align=right>-5</td>
  <td align=right>-1</td>
  <td align=right>-3</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.6666666<span style='display:none'>666666666</span></td>
  <td>0.4285714<span style='display:none'>2857142855</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.1111111111111111</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100035</td>
  <td>ryanwersal<span style='display:none'>/MorseL</span></td>
  <td>https://git<span style='display:none'>hub.com/ryanwersal/MorseL/commit/c1a080e599ba2ffee550b64510c9f712285e57d6</span></td>
  <td colspan=2 style='mso-ignore:colspan'>test/MorseL.Shared.Te<span
  style='display:none'>sts/MorseL.Shared.Tests.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>9</td>
  <td align=right>107</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>101</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>8</td>
  <td align=right>8</td>
  <td align=right>101</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>7</td>
  <td align=right>-8</td>
  <td align=right>0</td>
  <td align=right>-3</td>
  <td align=right>-1</td>
  <td align=right>-1</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.5555555555555556</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100037</td>
  <td>pluto-arch/<span style='display:none'>dotnet-project-template</span></td>
  <td>https://git<span style='display:none'>hub.com/pluto-arch/dotnet-project-template/commit/d7c860330c2e95d534a91d756e45760627d0c047</span></td>
  <td colspan=2 style='mso-ignore:colspan'>template/content/src/<span
  style='display:none'>PlutoNetCoreTemplate/PlutoNetCoreTemplate.csproj</span></td>
  <td>net5.0</td>
  <td align=right>11</td>
  <td align=right>142</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>126</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>10</td>
  <td align=right>19</td>
  <td align=right>136</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>18</td>
  <td align=right>-19</td>
  <td align=right>10</td>
  <td align=right>-2</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.5</td>
  <td>0.4210526<span style='display:none'>3157894735</span></td>
  <td colspan=3 style='mso-ignore:colspan'>0.22727272727272727</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100038</td>
  <td>yanpitangu<span style='display:none'>i/netcore-api-boilerplate</span></td>
  <td>https://git<span style='display:none'>hub.com/yanpitangui/dotnet-api-boilerplate/commit/1170fc6ba8a8999c4e57abc20e00ce79f950d794</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Boilerplate.Api/Boi<span
  style='display:none'>lerplate.Api.csproj</span></td>
  <td>net5.0</td>
  <td align=right>15</td>
  <td align=right>149</td>
  <td align=right>9</td>
  <td align=right>1</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>125</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>2</td>
  <td align=right>4</td>
  <td align=right>14</td>
  <td align=right>25</td>
  <td align=right>144</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>23</td>
  <td align=right>-25</td>
  <td align=right>19</td>
  <td align=right>-2</td>
  <td align=right>-1</td>
  <td align=right>9</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.5909090<span style='display:none'>909090909</span></td>
  <td>0.5217391<span style='display:none'>304347826</span></td>
  <td>0.25</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100044</td>
  <td>theolivenb<span style='display:none'>aum/h5</span></td>
  <td>https://git<span style='display:none'>hub.com/theolivenbaum/h5/commit/49ad367527f5a82d9db8fea851704ae91b77e14b</span></td>
  <td colspan=2 style='mso-ignore:colspan'>H5/Compiler/Compiler<span
  style='display:none'>.Service/H5.Compiler.Service.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.1</span></td>
  <td align=right>26</td>
  <td align=right>140</td>
  <td align=right>8</td>
  <td align=right>2</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>11</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>121</td>
  <td align=right>0</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>10</td>
  <td align=right>25</td>
  <td align=right>35</td>
  <td align=right>129</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>26</td>
  <td align=right>-35</td>
  <td align=right>8</td>
  <td align=right>-11</td>
  <td align=right>-6</td>
  <td align=right>1</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.6206896<span style='display:none'>551724138</span></td>
  <td>0.6206896<span style='display:none'>551724138</span></td>
  <td colspan=3 style='mso-ignore:colspan'>0.38235294117647056</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100045</td>
  <td>theolivenb<span style='display:none'>aum/h5</span></td>
  <td>https://git<span style='display:none'>hub.com/theolivenbaum/h5/commit/49ad367527f5a82d9db8fea851704ae91b77e14b</span></td>
  <td colspan=2 style='mso-ignore:colspan'>H5/Compiler/Translato<span
  style='display:none'>r/H5.Translator.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.1</span></td>
  <td align=right>26</td>
  <td align=right>101</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>12</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>101</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>0</td>
  <td align=right>11</td>
  <td align=right>24</td>
  <td align=right>30</td>
  <td align=right>105</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>22</td>
  <td align=right>-30</td>
  <td align=right>4</td>
  <td align=right>-9</td>
  <td align=right>-6</td>
  <td align=right>-2</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.6538461<span style='display:none'>538461539</span></td>
  <td>0.5357142<span style='display:none'>857142857</span></td>
  <td colspan=3 style='mso-ignore:colspan'>0.43333333333333335</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100046</td>
  <td>AngleSharp<span style='display:none'>/AngleSharp.Io</span></td>
  <td>https://git<span style='display:none'>hub.com/AngleSharp/AngleSharp.Io/commit/2970ab158c0517cd32ef3a322265b1ef52a7bd12</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/AngleSharp.Io.Test<span
  style='display:none'>s/AngleSharp.Io.Tests.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>6</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td align=right>5</td>
  <td align=right>66</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>1</td>
  <td align=right>1</td>
  <td align=right>3</td>
  <td align=right>-5</td>
  <td align=right>59</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>1.0</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100047</td>
  <td>trevoirwilli<span style='display:none'>ams/BookStore-API</span></td>
  <td>https://git<span style='display:none'>hub.com/trevoirwilliams/BookStore-API-Blazor/commit/90d6e27be923550d6dc88db249eabb18e0ad3eae</span></td>
  <td colspan=2 style='mso-ignore:colspan'>BookStore-API/BookSt<span
  style='display:none'>ore-API.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>14</td>
  <td align=right>116</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>111</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>6</td>
  <td align=right>11</td>
  <td align=right>111</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>7</td>
  <td align=right>-11</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.3333333333333333</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100048</td>
  <td>CSA-OCP-G<span style='display:none'>ER/azure-developer-college</span></td>
  <td>https://git<span style='display:none'>hub.com/CSA-OCP-GER/azure-developer-college/commit/0a7514418239addf4c753748dd446a4b7388c2c6</span></td>
  <td colspan=2 style='mso-ignore:colspan'>day2/apps/dotnetcore<span
  style='display:none'>/Scm.Resources/Adc.Scm.Resources.Api/Adc.Scm.Resources.Api.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>7</td>
  <td align=right>101</td>
  <td align=right>4</td>
  <td align=right>1</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>94</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td align=right>8</td>
  <td align=right>90</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>1</td>
  <td align=right>1</td>
  <td align=right>6</td>
  <td align=right>-8</td>
  <td align=right>-4</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.6</td>
  <td>0.6</td>
  <td>0.6</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100050</td>
  <td>excubo-ag/<span style='display:none'>Blazor.ScriptInjection</span></td>
  <td>https://git<span style='display:none'>hub.com/excubo-ag/Blazor.ScriptInjection/commit/c7b410846fdd492704fdd033c78fe2fe64ebc592</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Tests_ScriptInjection/T<span
  style='display:none'>ests_ScriptInjection.csproj</span></td>
  <td>net5.0</td>
  <td align=right>9</td>
  <td align=right>97</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>111</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>7</td>
  <td align=right>14</td>
  <td align=right>119</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>11</td>
  <td align=right>-14</td>
  <td align=right>8</td>
  <td align=right>-3</td>
  <td align=right>-1</td>
  <td align=right>4</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.6</td>
  <td>0.6</td>
  <td colspan=3 style='mso-ignore:colspan'>0.23076923076923078</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100051</td>
  <td>Tentacule/<span style='display:none'>PgsToSrt</span></td>
  <td>https://git<span style='display:none'>hub.com/Tentacule/PgsToSrt/commit/08e6b3aba9074fde829ce864890855c506084f10</span></td>
  <td colspan=2 style='mso-ignore:colspan'>PgsToSrt/PgsToSrt.cspr<span
  style='display:none'>oj</span></td>
  <td>net5.0</td>
  <td align=right>5</td>
  <td align=right>32</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>17</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>30</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>5</td>
  <td align=right>-5</td>
  <td align=right>13</td>
  <td align=right>-3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>2.5</td>
  <td>2.5</td>
  <td>2.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100052</td>
  <td>EasyAbp/A<span style='display:none'>bp.AspNetCore.Mvc.UI.Theme.LYear</span></td>
  <td>https://git<span style='display:none'>hub.com/EasyAbp/Abp.AspNetCore.Mvc.UI.Theme.LYear/commit/8a0c06eb2058ed2960f3a3bc0614c22178011b2d</span></td>
  <td colspan=2 style='mso-ignore:colspan'>samples/LYearUiSampl<span
  style='display:none'>e.Web/LYearUiSample.Web.csproj</span></td>
  <td>net5.0</td>
  <td align=right>15</td>
  <td align=right>211</td>
  <td align=right>2</td>
  <td align=right>1</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>212</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>14</td>
  <td align=right>17</td>
  <td align=right>232</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>2</td>
  <td align=right>2</td>
  <td align=right>13</td>
  <td align=right>-17</td>
  <td align=right>20</td>
  <td align=right>-6</td>
  <td align=right>-2</td>
  <td align=right>-1</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.7333333<span style='display:none'>333333333</span></td>
  <td>0.5294117<span style='display:none'>647058824</span></td>
  <td colspan=3 style='mso-ignore:colspan'>0.18181818181818182</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100058</td>
  <td>VolleyMan<span style='display:none'>agement/volley-management</span></td>
  <td>https://git<span style='display:none'>hub.com/VolleyManagement/volley-management/commit/b89ae404596892c5c61f84727c16fad32221f5da</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Client/VolleyM.API<span
  style='display:none'>/VolleyM.API.csproj</span></td>
  <td>net5.0</td>
  <td align=right>20</td>
  <td align=right>176</td>
  <td align=right>6</td>
  <td align=right>1</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>162</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>17</td>
  <td align=right>31</td>
  <td align=right>171</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>24</td>
  <td align=right>-31</td>
  <td align=right>9</td>
  <td align=right>-8</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.4814814<span style='display:none'>8148148145</span></td>
  <td>0.3333333<span style='display:none'>333333333</span></td>
  <td colspan=3 style='mso-ignore:colspan'>0.17647058823529413</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100059</td>
  <td>Particular/<span style='display:none'>NServiceBus.NHibernate</span></td>
  <td>https://git<span style='display:none'>hub.com/Particular/NServiceBus.NHibernate/commit/14a10402953d63843d9949a0f12291dfd7fcb42b</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/NServiceBus.NHibe<span
  style='display:none'>rnate.AcceptanceTests-Oracle/NServiceBus.NHibernate.AcceptanceTests-Oracle.csproj</span></td>
  <td>.NETFrame<span style='display:none'>work4.7.2</span></td>
  <td align=right>6</td>
  <td align=right>24</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>24</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>6</td>
  <td align=right>7</td>
  <td align=right>24</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>7</td>
  <td align=right>-7</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.7142857142857143</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100060</td>
  <td>bitfoundati<span style='display:none'>on/ToDoLine</span></td>
  <td>https://git<span style='display:none'>hub.com/bitfoundation/ToDoLine/commit/f544da435035322ed631a3c9fe350a048bc20b79</span></td>
  <td colspan=2 style='mso-ignore:colspan'>App/ToDoLineApp/To<span
  style='display:none'>DoLineApp.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>12</td>
  <td align=right>105</td>
  <td align=right>4</td>
  <td align=right>1</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>119</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>12</td>
  <td align=right>16</td>
  <td align=right>67</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>16</td>
  <td align=right>-16</td>
  <td align=right>-52</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.8571428<span style='display:none'>571428571</span></td>
  <td>0.8571428<span style='display:none'>571428571</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.5294117647058824</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100061</td>
  <td>bitfoundati<span style='display:none'>on/ToDoLine</span></td>
  <td>https://git<span style='display:none'>hub.com/bitfoundation/ToDoLine/commit/f544da435035322ed631a3c9fe350a048bc20b79</span></td>
  <td colspan=2 style='mso-ignore:colspan'>ToDoLine/ToDoLine.cs<span
  style='display:none'>proj</span></td>
  <td>net5.0</td>
  <td align=right>10</td>
  <td align=right>165</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>203</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>9</td>
  <td align=right>10</td>
  <td align=right>206</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>7</td>
  <td align=right>-10</td>
  <td align=right>3</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.6666666<span style='display:none'>666666666</span></td>
  <td>0.6666666<span style='display:none'>666666666</span></td>
  <td>0.25</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100062</td>
  <td>blockbasen<span style='display:none'>etwork/node</span></td>
  <td>https://git<span style='display:none'>hub.com/blockbasenetwork/node/commit/623871e66669143c17ffa2e869c586c5b813d07c</span></td>
  <td colspan=2 style='mso-ignore:colspan'>BlockBase.Network/Bl<span
  style='display:none'>ockBase.Network.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>12</td>
  <td align=right>63</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>36</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>8</td>
  <td align=right>9</td>
  <td align=right>19</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>8</td>
  <td align=right>-9</td>
  <td align=right>-17</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>1.1428571<span style='display:none'>428571428</span></td>
  <td>1.1428571<span style='display:none'>428571428</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.6666666666666666</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100063</td>
  <td>FitzyCodes<span style='display:none'>Things/core-lms</span></td>
  <td>https://git<span style='display:none'>hub.com/FitzyCodesThings/core-lms/commit/d9eb3833ee94f4fee466227ae53b29b81d4811b5</span></td>
  <td colspan=2 style='mso-ignore:colspan'>CoreLMS.Web/CoreLM<span
  style='display:none'>S.Web.csproj</span></td>
  <td>net5.0</td>
  <td align=right>10</td>
  <td align=right>145</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>49</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>9</td>
  <td align=right>16</td>
  <td align=right>130</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>2</td>
  <td align=right>3</td>
  <td align=right>14</td>
  <td align=right>-16</td>
  <td align=right>81</td>
  <td align=right>-3</td>
  <td align=right>-3</td>
  <td align=right>5</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.5384615<span style='display:none'>384615384</span></td>
  <td>0.3333333<span style='display:none'>333333333</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.1111111111111111</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100064</td>
  <td>EasyAbp/A<span style='display:none'>bp.TagHelperPlus</span></td>
  <td>https://git<span style='display:none'>hub.com/EasyAbp/Abp.TagHelperPlus/commit/cd142ac218f8b5ee698d03bf627169872edc12ce</span></td>
  <td colspan=2 style='mso-ignore:colspan'>host/EasyAbp.Abp.Tag<span
  style='display:none'>HelperPlus.Web.Unified/EasyAbp.Abp.TagHelperPlus.Web.Unified.csproj</span></td>
  <td>net5.0</td>
  <td align=right>25</td>
  <td align=right>234</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>231</td>
  <td align=right>0</td>
  <td align=right>11</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>24</td>
  <td align=right>26</td>
  <td align=right>276</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>21</td>
  <td align=right>-26</td>
  <td align=right>45</td>
  <td align=right>-11</td>
  <td align=right>-1</td>
  <td align=right>-3</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.8333333<span style='display:none'>333333334</span></td>
  <td>0.76</td>
  <td colspan=2 style='mso-ignore:colspan'>0.2222222222222222</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100068</td>
  <td>pekkah/tan<span style='display:none'>ka-graphql-samples</span></td>
  <td>https://git<span style='display:none'>hub.com/pekkah/tanka-graphql-samples/commit/20d0856841f0010b7a88051c2693c53335dfbdea</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Messages.Host/Me<span
  style='display:none'>ssages.Host.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>9</td>
  <td align=right>86</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>81</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>8</td>
  <td align=right>9</td>
  <td align=right>84</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>2</td>
  <td align=right>3</td>
  <td align=right>8</td>
  <td align=right>-9</td>
  <td align=right>3</td>
  <td align=right>-3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.875</td>
  <td>0.6666666<span style='display:none'>666666666</span></td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100069</td>
  <td>Hona/Tem<span style='display:none'>pusHub</span></td>
  <td>https://git<span style='display:none'>hub.com/Hona/TempusHub/commit/8fdb10d746c640dddfb3e7371bf268912841acc0</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/TempusHubBlazor/<span
  style='display:none'>TempusHubBlazor.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>11</td>
  <td align=right>131</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>152</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>10</td>
  <td align=right>17</td>
  <td align=right>130</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>12</td>
  <td align=right>-17</td>
  <td align=right>-22</td>
  <td align=right>-1</td>
  <td align=right>-2</td>
  <td align=right>2</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.4</td>
  <td>0.3125</td>
  <td>0.3125</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100070</td>
  <td>tom-engler<span style='display:none'>t/Equatable.Fody</span></td>
  <td>https://git<span style='display:none'>hub.com/tom-englert/Equatable.Fody/commit/fa269dc00a1153b16ca7f407e29d40c25e358af4</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Tests/Tests.csproj</td>
  <td>.NETFrame<span style='display:none'>work4.6</span></td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>5</td>
  <td align=right>-5</td>
  <td align=right>1</td>
  <td align=right>-2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>1.25</td>
  <td>1.25</td>
  <td>0.8</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100072</td>
  <td>waqaskhan<span style='display:none'>540/QuestionAnswerApp</span></td>
  <td>https://git<span style='display:none'>hub.com/waqaskhan540/QuestionAnswerApp/commit/34b4e42d618ed3afb146d92aa64a05f2b888df5d</span></td>
  <td colspan=2 style='mso-ignore:colspan'>server/Server/QnA.Aut<span
  style='display:none'>horization.Server/QnA.Authorization.Server.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>7</td>
  <td align=right>129</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>122</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>6</td>
  <td align=right>15</td>
  <td align=right>106</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>14</td>
  <td align=right>-15</td>
  <td align=right>-16</td>
  <td align=right>-2</td>
  <td align=right>1</td>
  <td align=right>8</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.5</td>
  <td>0.3846153<span style='display:none'>8461538464</span></td>
  <td>0.2</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100073</td>
  <td>dzimchuk/<span style='display:none'>book-fast-docker</span></td>
  <td>https://git<span style='display:none'>hub.com/dzimchuk/book-fast-docker/commit/8819f3a0e48418c0eabb77d2f337aeddaa29ca96</span></td>
  <td colspan=2 style='mso-ignore:colspan'>BookFast.Web/BookFa<span
  style='display:none'>st.Web.csproj</span></td>
  <td>net5.0</td>
  <td align=right>6</td>
  <td align=right>152</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>184</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>10</td>
  <td align=right>137</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>9</td>
  <td align=right>-10</td>
  <td align=right>-47</td>
  <td align=right>-1</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.8333333<span style='display:none'>333333334</span></td>
  <td>0.5714285<span style='display:none'>714285714</span></td>
  <td>0.375</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100074</td>
  <td>dzimchuk/<span style='display:none'>book-fast-docker</span></td>
  <td>https://git<span style='display:none'>hub.com/dzimchuk/book-fast-docker/commit/8ea811d249488461dc7f26896f1548f95930ca9e</span></td>
  <td colspan=2 style='mso-ignore:colspan'>BookFast.Web/BookFa<span
  style='display:none'>st.Web.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>6</td>
  <td align=right>152</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>186</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>10</td>
  <td align=right>137</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>9</td>
  <td align=right>-10</td>
  <td align=right>-49</td>
  <td align=right>-1</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.8333333<span style='display:none'>333333334</span></td>
  <td>0.5714285<span style='display:none'>714285714</span></td>
  <td>0.375</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100075</td>
  <td>ghaagh/Sti<span style='display:none'>cky</span></td>
  <td>https://git<span style='display:none'>hub.com/ghaagh/Sticky/commit/0ecb674a7f5f338319d5514b201958217e50599a</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Sticky.Services.KafkaCo<span
  style='display:none'>nsumer/Sticky.Services.KafkaConsumer.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>7</td>
  <td align=right>80</td>
  <td align=right>1</td>
  <td align=right>2</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>79</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>8</td>
  <td align=right>11</td>
  <td align=right>84</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>10</td>
  <td align=right>-11</td>
  <td align=right>5</td>
  <td align=right>-3</td>
  <td align=right>-3</td>
  <td align=right>2</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.875</td>
  <td>0.5</td>
  <td colspan=3 style='mso-ignore:colspan'>0.15384615384615385</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100076</td>
  <td>ghaagh/Sti<span style='display:none'>cky</span></td>
  <td>https://git<span style='display:none'>hub.com/ghaagh/Sticky/commit/0ecb674a7f5f338319d5514b201958217e50599a</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Sticky.Services.Respon<span
  style='display:none'>seUpdater/Sticky.Services.ResponseUpdater.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>7</td>
  <td align=right>15</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>12</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>7</td>
  <td align=right>7</td>
  <td align=right>19</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>6</td>
  <td align=right>-7</td>
  <td align=right>7</td>
  <td align=right>-3</td>
  <td align=right>-2</td>
  <td align=right>-1</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>1.2</td>
  <td>0.8333333<span style='display:none'>333333334</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.5714285714285714</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100080</td>
  <td>jahanbinali<span style='display:none'>1988/Sofa</span></td>
  <td>https://git<span style='display:none'>hub.com/jahanbinali1988/Sofa/commit/48446e13b27666acfb6ee62443689f72b0fdcba9</span></td>
  <td colspan=2 style='mso-ignore:colspan'>TestProjects/Sofa.Cour<span
  style='display:none'>seManagement.IntegratedTest/Sofa.CourseManagement.IntegratedTest.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.0</span></td>
  <td align=right>18</td>
  <td align=right>194</td>
  <td align=right>6</td>
  <td align=right>2</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>159</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>10</td>
  <td align=right>23</td>
  <td align=right>136</td>
  <td align=right>2</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>13</td>
  <td align=right>-23</td>
  <td align=right>-23</td>
  <td align=right>-4</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.6666666<span style='display:none'>666666666</span></td>
  <td>0.6666666<span style='display:none'>666666666</span></td>
  <td colspan=3 style='mso-ignore:colspan'>0.42857142857142855</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100084</td>
  <td>paulbulma<span style='display:none'>n/ParkingRota</span></td>
  <td>https://git<span style='display:none'>hub.com/paulbulman/ParkingRota/commit/017744d6e6e0daf33bc230e5ee3471a2cb2bda54</span></td>
  <td colspan=2 style='mso-ignore:colspan'>ParkingRota.Business/<span
  style='display:none'>ParkingRota.Business.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.1</span></td>
  <td align=right>7</td>
  <td align=right>20</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>7</td>
  <td align=right>7</td>
  <td align=right>20</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>4</td>
  <td align=right>-7</td>
  <td align=right>13</td>
  <td align=right>-4</td>
  <td align=right>-2</td>
  <td align=right>-3</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.8</td>
  <td>0.5</td>
  <td>0.5</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100087</td>
  <td>mcanerizci<span style='display:none'>/TradingCat</span></td>
  <td>https://git<span style='display:none'>hub.com/mcanerizci/TradingCat/commit/25582a45225f1c01a8f5a23273e201240082e4b5</span></td>
  <td colspan=2 style='mso-ignore:colspan'>TradingCat/source/Ser<span
  style='display:none'>vices/Order/Order.API/Order.API.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>5</td>
  <td align=right>112</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>113</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>7</td>
  <td align=right>111</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>-7</td>
  <td align=right>-2</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.5714285<span style='display:none'>714285714</span></td>
  <td>0.5714285<span style='display:none'>714285714</span></td>
  <td>0.375</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100088</td>
  <td>Lulubul/Ne<span style='display:none'>flixContainers</span></td>
  <td>https://git<span style='display:none'>hub.com/Lulubul/NeflixContainers/commit/fe84fa90b40ecbfd9122f1e312ddd6acfe42abc2</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Marketing.API/Market<span
  style='display:none'>ing.API.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.2</span></td>
  <td align=right>6</td>
  <td align=right>99</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>111</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>5</td>
  <td align=right>7</td>
  <td align=right>116</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>5</td>
  <td align=right>-7</td>
  <td align=right>5</td>
  <td align=right>-1</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.6</td>
  <td>0.3333333<span style='display:none'>333333333</span></td>
  <td colspan=3 style='mso-ignore:colspan'>0.14285714285714285</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100093</td>
  <td>davidandra<span style='display:none'>deduarte/simple-random-teams</span></td>
  <td>https://git<span style='display:none'>hub.com/davidandradeduarte/simple-random-teams/commit/c8057e1fb8e7a485ba92bea3bf18be47efcbf371</span></td>
  <td colspan=2 style='mso-ignore:colspan'>SimpleRandomTeams/<span
  style='display:none'>SimpleRandomTeams.csproj→src/SimpleRandomTeams/SimpleRandomTeams.csproj</span></td>
  <td>net5.0</td>
  <td align=right>9</td>
  <td align=right>92</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>84</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>8</td>
  <td align=right>8</td>
  <td align=right>81</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>6</td>
  <td align=right>-8</td>
  <td align=right>-3</td>
  <td align=right>-7</td>
  <td align=right>-2</td>
  <td align=right>-2</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>1.2</td>
  <td>1.2</td>
  <td>0.375</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>100098</td>
  <td>SkillsFundi<span style='display:none'>ngAgency/das-providerapprenticeshipsservice</span></td>
  <td>https://git<span style='display:none'>hub.com/SkillsFundingAgency/das-providerapprenticeshipsservice/commit/9e12083d0641a3ed9d9277f29197d1f6a4234000</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/SFA.DAS.PAS.Acco<span
  style='display:none'>unt.Api.ClientV2.UnitTests/SFA.DAS.PAS.Account.Api.ClientV2.UnitTests.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>8</td>
  <td align=right>75</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>78</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>7</td>
  <td align=right>8</td>
  <td align=right>77</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>7</td>
  <td align=right>-8</td>
  <td align=right>-1</td>
  <td align=right>-1</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.8571428<span style='display:none'>571428571</span></td>
  <td>0.625</td>
  <td colspan=2 style='mso-ignore:colspan'>0.4444444444444444</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>1000103</td>
  <td>gmoreno9<span style='display:none'>0/webhookhub</span></td>
  <td>https://git<span style='display:none'>hub.com/gmoreno90/webhookhub/commit/cd4cc30953a84aa582301b0660c2cd05a6f17b23</span></td>
  <td colspan=2 style='mso-ignore:colspan'>WebHookHub/WebHo<span
  style='display:none'>okHub.csproj</span></td>
  <td>net5.0</td>
  <td align=right>10</td>
  <td align=right>184</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>135</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>9</td>
  <td align=right>21</td>
  <td align=right>159</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>18</td>
  <td align=right>-21</td>
  <td align=right>24</td>
  <td align=right>-1</td>
  <td align=right>-1</td>
  <td align=right>9</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.4375</td>
  <td>0.4375</td>
  <td colspan=3 style='mso-ignore:colspan'>0.21052631578947367</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>1000108</td>
  <td>alexthissen<span style='display:none'>/HealthMonitoring</span></td>
  <td>https://git<span style='display:none'>hub.com/alexthissen/HealthMonitoring/commit/e4b854e6ecc0c67601c76ae5c03c72870ed9b7ed</span></td>
  <td colspan=2 style='mso-ignore:colspan'>RetroGamingWebAPI/<span
  style='display:none'>RetroGamingWebAPI.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>13</td>
  <td align=right>182</td>
  <td align=right>2</td>
  <td align=right>3</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>204</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>13</td>
  <td align=right>20</td>
  <td align=right>122</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>15</td>
  <td align=right>-20</td>
  <td align=right>-82</td>
  <td align=right>-1</td>
  <td align=right>-2</td>
  <td align=right>2</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.4705882<span style='display:none'>3529411764</span></td>
  <td>0.3888888<span style='display:none'>888888889</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.3888888888888889</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>1000110</td>
  <td>equinor/pr<span style='display:none'>ocosys-preservation-api</span></td>
  <td>https://git<span style='display:none'>hub.com/equinor/procosys-preservation-api/commit/7da9018fd78c912a1022a3b2956ba28a42f0a87d</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Equinor.Procosys.P<span
  style='display:none'>reservation.WebApi/Equinor.Procosys.Preservation.WebApi.csproj</span></td>
  <td>net5.0</td>
  <td align=right>19</td>
  <td align=right>189</td>
  <td align=right>5</td>
  <td align=right>3</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>199</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>15</td>
  <td align=right>25</td>
  <td align=right>180</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>18</td>
  <td align=right>-25</td>
  <td align=right>-19</td>
  <td align=right>-1</td>
  <td align=right>-1</td>
  <td align=right>3</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.6666666<span style='display:none'>666666666</span></td>
  <td>0.6666666<span style='display:none'>666666666</span></td>
  <td colspan=3 style='mso-ignore:colspan'>0.30434782608695654</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>1000113</td>
  <td>neuroglia-i<span style='display:none'>o/K8s.Eventing</span></td>
  <td>https://git<span style='display:none'>hub.com/neuroglia-io/K8s.Eventing/commit/dbd556c3f1775e411fc18519e29c3456d78461df</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Gateway/Neurogli<span
  style='display:none'>a.K8s.Eventing.Gateway.Infrastructure/Neuroglia.K8s.Eventing.Gateway.Infrastructure.csproj</span></td>
  <td>net5.0</td>
  <td align=right>5</td>
  <td align=right>91</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>90</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>4</td>
  <td align=right>8</td>
  <td align=right>82</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>6</td>
  <td align=right>-8</td>
  <td align=right>-8</td>
  <td align=right>-2</td>
  <td align=right>-2</td>
  <td align=right>2</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.5</td>
  <td>0.2857142<span style='display:none'>857142857</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.2857142857142857</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>1000115</td>
  <td>sergey-ryb<span style='display:none'>alkin/StyleCopPlus</span></td>
  <td>https://git<span style='display:none'>hub.com/sergey-rybalkin/StyleCopPlus/commit/0efc42dd9f991eab3a5dfa0abaa8bc9e5d7f41fb</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/StyleCopPlus.Test/<span
  style='display:none'>StyleCopPlus.Test.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.0</span></td>
  <td align=right>9</td>
  <td align=right>88</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>101</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>7</td>
  <td align=right>12</td>
  <td align=right>101</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>10</td>
  <td align=right>-12</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>-2</td>
  <td align=right>3</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.4545454<span style='display:none'>5454545453</span></td>
  <td>0.4545454<span style='display:none'>5454545453</span></td>
  <td colspan=3 style='mso-ignore:colspan'>0.45454545454545453</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>1000116</td>
  <td>atomiv/ato<span style='display:none'>miv-dotnet</span></td>
  <td>https://git<span style='display:none'>hub.com/atomiv/atomiv-dotnet/commit/c580e41572331e67f012974158f95768178aad8a</span></td>
  <td colspan=2 style='mso-ignore:colspan'>template/microservice<span
  style='display:none'>/src/Web/Atomiv.Template.Web.RestApi/Atomiv.Template.Web.RestApi.csproj</span></td>
  <td>net5.0</td>
  <td align=right>11</td>
  <td align=right>146</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>145</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>11</td>
  <td align=right>24</td>
  <td align=right>146</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>20</td>
  <td align=right>-24</td>
  <td align=right>1</td>
  <td align=right>-1</td>
  <td align=right>-1</td>
  <td align=right>9</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.3181818<span style='display:none'>181818182</span></td>
  <td>0.3181818<span style='display:none'>181818182</span></td>
  <td>0.16</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>1000117</td>
  <td>pluto-arch/<span style='display:none'>dotnet-project-template</span></td>
  <td>https://git<span style='display:none'>hub.com/pluto-arch/dotnet-project-template/commit/267fc4ba8d0373a746daf8617424e7611b889eda</span></td>
  <td colspan=2 style='mso-ignore:colspan'>template/content/src/<span
  style='display:none'>PlutoNetCoreTemplate/PlutoNetCoreTemplate.csproj</span></td>
  <td>net5.0</td>
  <td align=right>11</td>
  <td align=right>142</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>126</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>10</td>
  <td align=right>19</td>
  <td align=right>136</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>18</td>
  <td align=right>-19</td>
  <td align=right>10</td>
  <td align=right>-2</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.5</td>
  <td>0.4210526<span style='display:none'>3157894735</span></td>
  <td colspan=3 style='mso-ignore:colspan'>0.22727272727272727</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>1000118</td>
  <td>seekdavidl<span style='display:none'>ee/Eklee-Azure-Functions-Http</span></td>
  <td>https://git<span style='display:none'>hub.com/seekdavidlee/Eklee-Azure-Functions-Http/commit/05874438ef12aa232edaa9cad498dbde8c5c020c</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Eklee.Azure.Functions.<span
  style='display:none'>Http/Eklee.Azure.Functions.Http.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.1</span></td>
  <td align=right>10</td>
  <td align=right>51</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>92</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>9</td>
  <td align=right>9</td>
  <td align=right>94</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>9</td>
  <td align=right>-9</td>
  <td align=right>2</td>
  <td align=right>-2</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>1.2857142<span style='display:none'>857142858</span></td>
  <td>1.0</td>
  <td colspan=3 style='mso-ignore:colspan'>0.45454545454545453</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>1000119</td>
  <td>halomade<span style='display:none'>meapc/ChatBeet</span></td>
  <td>https://git<span style='display:none'>hub.com/halomademeapc/ChatBeet/commit/f62758e19ca9096e42bfcfae3f1105b364251a15</span></td>
  <td colspan=2 style='mso-ignore:colspan'>ChatBeet/ChatBeet.cs<span
  style='display:none'>proj</span></td>
  <td>net5.0</td>
  <td align=right>32</td>
  <td align=right>157</td>
  <td align=right>4</td>
  <td align=right>1</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>172</td>
  <td align=right>10</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>19</td>
  <td align=right>41</td>
  <td align=right>177</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>24</td>
  <td align=right>-41</td>
  <td align=right>5</td>
  <td align=right>-3</td>
  <td align=right>-4</td>
  <td align=right>5</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.5185185<span style='display:none'>185185185</span></td>
  <td>0.4642857<span style='display:none'>142857143</span></td>
  <td colspan=3 style='mso-ignore:colspan'>0.36666666666666664</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>1000120</td>
  <td>halomade<span style='display:none'>meapc/ChatBeet</span></td>
  <td>https://git<span style='display:none'>hub.com/halomademeapc/ChatBeet/commit/7b9f141b5ca56e9247d2a52da331543dee0ff35e</span></td>
  <td colspan=2 style='mso-ignore:colspan'>ChatBeet/ChatBeet.cs<span
  style='display:none'>proj</span></td>
  <td>net5.0</td>
  <td align=right>32</td>
  <td align=right>157</td>
  <td align=right>4</td>
  <td align=right>1</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>163</td>
  <td align=right>6</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>18</td>
  <td align=right>41</td>
  <td align=right>177</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>24</td>
  <td align=right>-41</td>
  <td align=right>14</td>
  <td align=right>-4</td>
  <td align=right>-2</td>
  <td align=right>6</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.5384615<span style='display:none'>384615384</span></td>
  <td>0.4814814<span style='display:none'>8148148145</span></td>
  <td colspan=3 style='mso-ignore:colspan'>0.42857142857142855</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>1000124</td>
  <td>ops-ai/Bey<span style='display:none'>ondAuth</span></td>
  <td>https://git<span style='display:none'>hub.com/ops-ai/BeyondAuth/commit/6a5de6939f7bcc586d214994503deaa60c78ea4d</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/AuditServer/AuditS<span
  style='display:none'>erver.csproj</span></td>
  <td>net5.0</td>
  <td align=right>18</td>
  <td align=right>234</td>
  <td align=right>2</td>
  <td align=right>3</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>208</td>
  <td align=right>2</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>16</td>
  <td align=right>33</td>
  <td align=right>222</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>24</td>
  <td align=right>-33</td>
  <td align=right>14</td>
  <td align=right>-3</td>
  <td align=right>-3</td>
  <td align=right>8</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.3214285<span style='display:none'>7142857145</span></td>
  <td>0.3214285<span style='display:none'>7142857145</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.1935483870967742</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>1000125</td>
  <td>ops-ai/Bey<span style='display:none'>ondAuth</span></td>
  <td>https://git<span style='display:none'>hub.com/ops-ai/BeyondAuth/commit/6a5de6939f7bcc586d214994503deaa60c78ea4d</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/AuthorizationServe<span
  style='display:none'>r/AuthorizationServer.csproj</span></td>
  <td>net5.0</td>
  <td align=right>16</td>
  <td align=right>205</td>
  <td align=right>2</td>
  <td align=right>1</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>190</td>
  <td align=right>4</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>13</td>
  <td align=right>23</td>
  <td align=right>153</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>18</td>
  <td align=right>-23</td>
  <td align=right>-37</td>
  <td align=right>-4</td>
  <td align=right>-2</td>
  <td align=right>5</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.6111111<span style='display:none'>111111112</span></td>
  <td>0.6111111<span style='display:none'>111111112</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.3181818181818182</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>1000129</td>
  <td>ops-ai/Bey<span style='display:none'>ondAuth</span></td>
  <td>https://git<span style='display:none'>hub.com/ops-ai/BeyondAuth/commit/6a5de6939f7bcc586d214994503deaa60c78ea4d</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/PolicyServer/Policy<span
  style='display:none'>Server.csproj</span></td>
  <td>net5.0</td>
  <td align=right>16</td>
  <td align=right>197</td>
  <td align=right>2</td>
  <td align=right>1</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>184</td>
  <td align=right>1</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>11</td>
  <td align=right>21</td>
  <td align=right>138</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>14</td>
  <td align=right>-21</td>
  <td align=right>-46</td>
  <td align=right>-1</td>
  <td align=right>-1</td>
  <td align=right>3</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.6428571<span style='display:none'>428571429</span></td>
  <td>0.6428571<span style='display:none'>428571429</span></td>
  <td>0.4375</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>1000138</td>
  <td>hbiarge/Ex<span style='display:none'>periments</span></td>
  <td>https://git<span style='display:none'>hub.com/hbiarge/Experiments/commit/f826537c9de7ed4a0b82e27421828e1f38eac610</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Messaging/Rebus/Exte<span
  style='display:none'>rnal/Acheve.External.Estimations/Acheve.External.Estimations.csproj</span></td>
  <td>net5.0</td>
  <td align=right>6</td>
  <td align=right>83</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>97</td>
  <td align=right>5</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>9</td>
  <td align=right>97</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>-9</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.7142857<span style='display:none'>142857143</span></td>
  <td>0.7142857<span style='display:none'>142857143</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.7142857142857143</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>1000139</td>
  <td>hbiarge/Ex<span style='display:none'>periments</span></td>
  <td>https://git<span style='display:none'>hub.com/hbiarge/Experiments/commit/f826537c9de7ed4a0b82e27421828e1f38eac610</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Messaging/Rebus/Exte<span
  style='display:none'>rnal/Acheve.External.ImageProcess/Acheve.External.ImageProcess.csproj</span></td>
  <td>net5.0</td>
  <td align=right>6</td>
  <td align=right>83</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>97</td>
  <td align=right>4</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>9</td>
  <td align=right>97</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>-9</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.7142857<span style='display:none'>142857143</span></td>
  <td>0.7142857<span style='display:none'>142857143</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.7142857142857143</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>1000140</td>
  <td>hbiarge/Ex<span style='display:none'>periments</span></td>
  <td>https://git<span style='display:none'>hub.com/hbiarge/Experiments/commit/f826537c9de7ed4a0b82e27421828e1f38eac610</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Messaging/Rebus/Exte<span
  style='display:none'>rnal/Acheve.External.Images/Acheve.External.Images.csproj</span></td>
  <td>net5.0</td>
  <td align=right>6</td>
  <td align=right>83</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>97</td>
  <td align=right>2</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>9</td>
  <td align=right>97</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>-9</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.7142857<span style='display:none'>142857143</span></td>
  <td>0.7142857<span style='display:none'>142857143</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.7142857142857143</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>1000141</td>
  <td>hbiarge/Ex<span style='display:none'>periments</span></td>
  <td>https://git<span style='display:none'>hub.com/hbiarge/Experiments/commit/f826537c9de7ed4a0b82e27421828e1f38eac610</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Messaging/Rebus/Exte<span
  style='display:none'>rnal/Acheve.External.Notifications/Acheve.External.Notifications.csproj</span></td>
  <td>net5.0</td>
  <td align=right>6</td>
  <td align=right>83</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>97</td>
  <td align=right>2</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>9</td>
  <td align=right>97</td>
  <td align=right>2</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>-9</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.7142857<span style='display:none'>142857143</span></td>
  <td>0.7142857<span style='display:none'>142857143</span></td>
  <td colspan=2 style='mso-ignore:colspan'>0.7142857142857143</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>1000144</td>
  <td>flyingpiano<span style='display:none'>man/TorrentGrease</span></td>
  <td>https://git<span style='display:none'>hub.com/flyingpianoman/TorrentGrease/commit/f77ed49be04d149fc30870620db41dc913265dfe</span></td>
  <td colspan=2 style='mso-ignore:colspan'>TorrentGrease.Server/<span
  style='display:none'>TorrentGrease.Server.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>6</td>
  <td align=right>25</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>23</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>5</td>
  <td align=right>23</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>-5</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>1.0</td>
  <td>1.0</td>
  <td>0.6</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>1000145</td>
  <td>awaisa/AK</td>
  <td>https://git<span style='display:none'>hub.com/awaisa/AK/commit/4f2b429dd7c299c3d7e0fbf6888935eb1ea44c5a</span></td>
  <td colspan=2 style='mso-ignore:colspan'>ak/WebApi/WebApiCo<span
  style='display:none'>re.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp2.0</span></td>
  <td align=right>49</td>
  <td align=right>160</td>
  <td align=right>58</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>155</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>29</td>
  <td align=right>24</td>
  <td align=right>36</td>
  <td align=right>158</td>
  <td align=right>0</td>
  <td align=right>8</td>
  <td align=right>0</td>
  <td align=right>29</td>
  <td align=right>29</td>
  <td align=right>-36</td>
  <td align=right>3</td>
  <td align=right>-4</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.7307692<span style='display:none'>307692307</span></td>
  <td>0.5517241<span style='display:none'>379310345</span></td>
  <td colspan=3 style='mso-ignore:colspan'>0.45161290322580644</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>1000147</td>
  <td>dr1rrb/sma<span style='display:none'>rthome.net</span></td>
  <td>https://git<span style='display:none'>hub.com/dr1rrb/smarthome.net/commit/943a70c58726bf466c3e6e942be52bbd1464e115</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/SmartHomeDotNet<span
  style='display:none'>.Package/SmartHomeDotNet.Package.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>6</td>
  <td align=right>24</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>38</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>5</td>
  <td align=right>6</td>
  <td align=right>35</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>5</td>
  <td align=right>-6</td>
  <td align=right>-3</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>1.0</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>1000149</td>
  <td>dr1rrb/sma<span style='display:none'>rthome.net</span></td>
  <td>https://git<span style='display:none'>hub.com/dr1rrb/smarthome.net/commit/646232e0a1c757b89a40c7ed25b9a54ee929506f</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/SmartHomeDotNet<span
  style='display:none'>.Package/SmartHomeDotNet.Package.csproj</span></td>
  <td>.NETStanda<span style='display:none'>rd2.0</span></td>
  <td align=right>6</td>
  <td align=right>24</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>38</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>5</td>
  <td align=right>6</td>
  <td align=right>35</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>5</td>
  <td align=right>-6</td>
  <td align=right>-3</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>1.0</td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>1000152</td>
  <td>jernejk/EfC<span style='display:none'>oreSamples.Logging</span></td>
  <td>https://git<span style='display:none'>hub.com/jernejk/EfCoreSamples.Logging/commit/bfdaf92d4a9576f3ec42995ee6a851dea55669f6</span></td>
  <td colspan=2 style='mso-ignore:colspan'>EfCoreSamples.Loggin<span
  style='display:none'>g.Web/EfCoreSamples.Logging.Web.csproj</span></td>
  <td>net5.0</td>
  <td align=right>13</td>
  <td align=right>75</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>130</td>
  <td align=right>2</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>12</td>
  <td align=right>22</td>
  <td align=right>135</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>21</td>
  <td align=right>-22</td>
  <td align=right>5</td>
  <td align=right>-5</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.5</td>
  <td>0.375</td>
  <td>0.375</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>1000153</td>
  <td>jernejk/EfC<span style='display:none'>oreSamples.Logging</span></td>
  <td>https://git<span style='display:none'>hub.com/jernejk/EfCoreSamples.Logging/commit/1fa9b4196ee2d0ad59fcaba6f4b224685ffba087</span></td>
  <td colspan=2 style='mso-ignore:colspan'>EfCoreSamples.Loggin<span
  style='display:none'>g.Web/EfCoreSamples.Logging.Web.csproj</span></td>
  <td>net5.0</td>
  <td align=right>13</td>
  <td align=right>75</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>130</td>
  <td align=right>4</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>12</td>
  <td align=right>22</td>
  <td align=right>135</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>21</td>
  <td align=right>-22</td>
  <td align=right>5</td>
  <td align=right>-5</td>
  <td align=right>0</td>
  <td align=right>9</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.5</td>
  <td>0.375</td>
  <td>0.375</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>1000154</td>
  <td>ztytotoro/<span style='display:none'>Blog.Service</span></td>
  <td>https://git<span style='display:none'>hub.com/ztytotoro/Blog.Service/commit/986442695af6e0a74fd74134955a472dc5e19657</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Blog.Service/Blog.Servi<span
  style='display:none'>ce.csproj</span></td>
  <td>net5.0</td>
  <td align=right>7</td>
  <td align=right>119</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>101</td>
  <td align=right>6</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>7</td>
  <td align=right>15</td>
  <td align=right>137</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>14</td>
  <td align=right>-15</td>
  <td align=right>36</td>
  <td align=right>-1</td>
  <td align=right>-1</td>
  <td align=right>7</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.4285714<span style='display:none'>2857142855</span></td>
  <td>0.4285714<span style='display:none'>2857142855</span></td>
  <td colspan=3 style='mso-ignore:colspan'>0.17647058823529413</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>1000155</td>
  <td>matteogar<span style='display:none'>ato/HellsGate</span></td>
  <td>https://git<span style='display:none'>hub.com/matteogarato/HellsGate/commit/94ae32d5cf86a2fb60eb8a36f1f77621201cac38</span></td>
  <td colspan=2 style='mso-ignore:colspan'>HellsGate.MVC/HellsG<span
  style='display:none'>ate.MVC.csproj</span></td>
  <td>net5.0</td>
  <td align=right>8</td>
  <td align=right>137</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>146</td>
  <td align=right>10</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>7</td>
  <td align=right>8</td>
  <td align=right>146</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>8</td>
  <td align=right>-8</td>
  <td align=right>0</td>
  <td align=right>-1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>1.0</td>
  <td>1.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.5555555555555556</td>
  <td></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>1000159</td>
  <td>Christophe<span style='display:none'>r-Shi/Chris.Personnel.Management</span></td>
  <td>https://git<span style='display:none'>hub.com/Christopher-Shi/Chris.Personnel.Management/commit/35fd5f86c0d3c8b65a7c146ed2a40e3eed7d5165</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Back-end-code/Chris.P<span
  style='display:none'>ersonnel.Management.API/Chris.Personnel.Management.API.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>9</td>
  <td align=right>101</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>120</td>
  <td align=right>4</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>10</td>
  <td align=right>107</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>-10</td>
  <td align=right>-13</td>
  <td align=right>-2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.625</td>
  <td>0.625</td>
  <td colspan=3 style='mso-ignore:colspan'>0.18181818181818182</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>1000161</td>
  <td>attuo/My<span style='display:none'>WebAPITemplate</span></td>
  <td>https://git<span style='display:none'>hub.com/attuo/MyWebAPITemplate/commit/121a6fe800313ddb6a090f20c70cfae87e2bc87b</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/Web/Web.csproj</td>
  <td>net5.0</td>
  <td align=right>12</td>
  <td align=right>222</td>
  <td align=right>2</td>
  <td align=right>3</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>217</td>
  <td align=right>4</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>10</td>
  <td align=right>18</td>
  <td align=right>191</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>11</td>
  <td align=right>-18</td>
  <td align=right>-26</td>
  <td align=right>-1</td>
  <td align=right>-4</td>
  <td align=right>1</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.3571428<span style='display:none'>5714285715</span></td>
  <td>0.3571428<span style='display:none'>5714285715</span></td>
  <td colspan=3 style='mso-ignore:colspan'>0.26666666666666666</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>1000166</td>
  <td>daxnet/aba<span style='display:none'>cuza</span></td>
  <td>https://git<span style='display:none'>hub.com/daxnet/abacuza/commit/b0835392a2c65ea95793e23bc6ebb6a872383932</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/services/jobs/Abac<span
  style='display:none'>uza.Jobs.ApiService/Abacuza.Jobs.ApiService.csproj</span></td>
  <td>net5.0</td>
  <td align=right>10</td>
  <td align=right>142</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>110</td>
  <td align=right>4</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>10</td>
  <td align=right>14</td>
  <td align=right>113</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>11</td>
  <td align=right>-14</td>
  <td align=right>3</td>
  <td align=right>-1</td>
  <td align=right>-2</td>
  <td align=right>1</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.5833333<span style='display:none'>333333334</span></td>
  <td>0.4615384<span style='display:none'>6153846156</span></td>
  <td colspan=3 style='mso-ignore:colspan'>0.46153846153846156</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>1000168</td>
  <td>arditmezini<span style='display:none'>/api-core</span></td>
  <td>https://git<span style='display:none'>hub.com/arditmezini/api-core/commit/b465385d1e206966c37f806862073263fbe75fb5</span></td>
  <td colspan=2 style='mso-ignore:colspan'>AspNetCoreApi.Api/As<span
  style='display:none'>pNetCoreApi.Api.csproj</span></td>
  <td>net5.0</td>
  <td align=right>25</td>
  <td align=right>202</td>
  <td align=right>2</td>
  <td align=right>1</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>188</td>
  <td align=right>2</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>20</td>
  <td align=right>32</td>
  <td align=right>186</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>0</td>
  <td align=right>4</td>
  <td align=right>22</td>
  <td align=right>-32</td>
  <td align=right>-2</td>
  <td align=right>-4</td>
  <td align=right>-2</td>
  <td align=right>2</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.6521739<span style='display:none'>130434783</span></td>
  <td>0.6521739<span style='display:none'>130434783</span></td>
  <td colspan=3 style='mso-ignore:colspan'>0.35714285714285715</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>1000169</td>
  <td>shawnwild<span style='display:none'>ermuth/WilderBlog</span></td>
  <td>https://git<span style='display:none'>hub.com/shawnwildermuth/WilderBlog/commit/9e828ffdc6e04c72a9a09253b738f83ad33b4a1d</span></td>
  <td colspan=2 style='mso-ignore:colspan'>src/WilderBlog/Wilder<span
  style='display:none'>Blog.csproj</span></td>
  <td>net5.0</td>
  <td align=right>14</td>
  <td align=right>176</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>159</td>
  <td align=right>4</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>7</td>
  <td align=right>14</td>
  <td align=right>27</td>
  <td align=right>160</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>23</td>
  <td align=right>-27</td>
  <td align=right>1</td>
  <td align=right>-3</td>
  <td align=right>-4</td>
  <td align=right>9</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.4</td>
  <td>0.2962962<span style='display:none'>962962963</span></td>
  <td>0.25</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>1000174</td>
  <td>eventflow/<span style='display:none'>EventFlow</span></td>
  <td>https://git<span style='display:none'>hub.com/eventflow/EventFlow/commit/b1880a2a303362fa44b580a4a41e6e2368312506</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Source/EventFlow.Owi<span
  style='display:none'>n.Tests/EventFlow.Owin.Tests.csproj</span></td>
  <td>.NETFrame<span style='display:none'>work4.7.2</span></td>
  <td align=right>6</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>5</td>
  <td align=right>6</td>
  <td align=right>6</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>3</td>
  <td align=right>-6</td>
  <td align=right>0</td>
  <td align=right>-2</td>
  <td align=right>-2</td>
  <td align=right>-2</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.75</td>
  <td>0.75</td>
  <td>0.75</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>1000177</td>
  <td>yotkoKanc<span style='display:none'>hev/LetsSport</span></td>
  <td>https://git<span style='display:none'>hub.com/yotkoKanchev/LetsSport/commit/9a6c034f48350798b66878017a821291ba08f045</span></td>
  <td colspan=2 style='mso-ignore:colspan'>Web/LetsSport.Web/L<span
  style='display:none'>etsSport.Web.csproj</span></td>
  <td>net5.0</td>
  <td align=right>15</td>
  <td align=right>152</td>
  <td align=right>2</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>165</td>
  <td align=right>8</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>14</td>
  <td align=right>26</td>
  <td align=right>184</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>20</td>
  <td align=right>-26</td>
  <td align=right>19</td>
  <td align=right>-3</td>
  <td align=right>-1</td>
  <td align=right>6</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.45</td>
  <td>0.45</td>
  <td colspan=3 style='mso-ignore:colspan'>0.38095238095238093</td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>1000178</td>
  <td>dzimchuk/<span style='display:none'>book-fast-docker</span></td>
  <td>https://git<span style='display:none'>hub.com/dzimchuk/book-fast-docker/commit/b379091a244426816bd6241b39cc1cbed3f57d77</span></td>
  <td colspan=2 style='mso-ignore:colspan'>BookFast.Web/BookFa<span
  style='display:none'>st.Web.csproj</span></td>
  <td>net5.0</td>
  <td align=right>6</td>
  <td align=right>152</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>184</td>
  <td align=right>4</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>10</td>
  <td align=right>137</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>9</td>
  <td align=right>-10</td>
  <td align=right>-47</td>
  <td align=right>-1</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.8333333<span style='display:none'>333333334</span></td>
  <td>0.5714285<span style='display:none'>714285714</span></td>
  <td>0.375</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>1000179</td>
  <td>dzimchuk/<span style='display:none'>book-fast-docker</span></td>
  <td>https://git<span style='display:none'>hub.com/dzimchuk/book-fast-docker/commit/c359866d3efffde9adedc5dd2f41db3b1cb4e8aa</span></td>
  <td colspan=2 style='mso-ignore:colspan'>BookFast.Web/BookFa<span
  style='display:none'>st.Web.csproj</span></td>
  <td>.NETCoreA<span style='display:none'>pp3.1</span></td>
  <td align=right>6</td>
  <td align=right>152</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>179</td>
  <td align=right>2</td>
  <td align=right>1</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>5</td>
  <td align=right>10</td>
  <td align=right>137</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>1</td>
  <td align=right>9</td>
  <td align=right>-10</td>
  <td align=right>-42</td>
  <td align=right>-1</td>
  <td align=right>1</td>
  <td align=right>4</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>0.8333333<span style='display:none'>333333334</span></td>
  <td>0.5714285<span style='display:none'>714285714</span></td>
  <td>0.375</td>
  <td colspan=2 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=19 style='height:14.25pt'>
  <td height=19 align=right style='height:14.25pt'>1000186</td>
  <td>I-Synergy/I-<span style='display:none'>Synergy.Framework</span></td>
  <td>https://git<span style='display:none'>hub.com/I-Synergy/I-Synergy.Framework/commit/38419792134ba7ae6a0a43e4c5eceb4e97cc21ed</span></td>
  <td colspan=2 style='mso-ignore:colspan'>samples/ISynergy.Fra<span
  style='display:none'>mework.UI.Sample/ISynergy.Framework.UI.Sample.Skia.Gtk/ISynergy.Framework.UI.Sample.Skia.Gtk.csproj→samples/ISynergy.Framework.UI/Sample.Skia.Gtk/Sample.Skia.Gtk.csproj</span></td>
  <td>net5.0</td>
  <td align=right>5</td>
  <td align=right>71</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>70</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>4</td>
  <td align=right>70</td>
  <td align=right>0</td>
  <td align=right>2</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td align=right>3</td>
  <td align=right>-4</td>
  <td align=right>0</td>
  <td align=right>-3</td>
  <td align=right>0</td>
  <td align=right>0</td>
  <td>-1-1-0.02-1<span style='display:none'>-0.1-1</span></td>
  <td>3.0</td>
  <td>3.0</td>
  <td colspan=2 style='mso-ignore:colspan'>0.3333333333333333</td>
  <td></td>
 </tr>
 <![if supportMisalignedColumns]>
 <tr height=0 style='display:none'>
  <td width=68 style='width:51pt'></td>
  <td width=68 style='width:51pt'></td>
  <td width=68 style='width:51pt'></td>
  <td width=68 style='width:51pt'></td>
  <td width=68 style='width:51pt'></td>
  <td width=68 style='width:51pt'></td>
  <td width=68 style='width:51pt'></td>
  <td width=68 style='width:51pt'></td>
  <td width=68 style='width:51pt'></td>
  <td width=68 style='width:51pt'></td>
  <td width=68 style='width:51pt'></td>
  <td width=68 style='width:51pt'></td>
  <td width=68 style='width:51pt'></td>
  <td width=68 style='width:51pt'></td>
  <td width=68 style='width:51pt'></td>
  <td width=68 style='width:51pt'></td>
  <td width=68 style='width:51pt'></td>
  <td width=68 style='width:51pt'></td>
  <td width=68 style='width:51pt'></td>
  <td width=68 style='width:51pt'></td>
  <td width=68 style='width:51pt'></td>
  <td width=68 style='width:51pt'></td>
  <td width=68 style='width:51pt'></td>
  <td width=68 style='width:51pt'></td>
  <td width=68 style='width:51pt'></td>
  <td width=68 style='width:51pt'></td>
  <td width=68 style='width:51pt'></td>
  <td width=68 style='width:51pt'></td>
  <td width=68 style='width:51pt'></td>
  <td width=68 style='width:51pt'></td>
  <td width=68 style='width:51pt'></td>
  <td width=68 style='width:51pt'></td>
  <td width=68 style='width:51pt'></td>
  <td width=68 style='width:51pt'></td>
  <td width=68 style='width:51pt'></td>
  <td width=68 style='width:51pt'></td>
  <td width=68 style='width:51pt'></td>
  <td width=68 style='width:51pt'></td>
  <td width=68 style='width:51pt'></td>
 </tr>
 </tbody></table>
### USER STUDY DATASET

<a href="https://github.com/nufix-dependency-maze/nufix/blob/gh-pages/A Survey for dependency issue patches.zip?raw=true">A Survey for dependency issue patches.zip</a>
