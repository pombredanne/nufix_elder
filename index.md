
<section class="page-header">
    <h1 class="project-name">Sensor</h1>
    <h2 class="project-tagline">This is the project containing information related to research project Sensor</h2>
    <a href="https://github.com/SensorDC/Sensor" class="btn">View on GitHub</a>
</section>

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
<tr >
  <td>id</td>
  <td>repository_full_name</td>
  <td>html_url</td>
  <td>title_info</td>
  <td>commit_date</td>
  <td>targetFramework</td>
  <td>directly_dependencies_count</td>
  <td>total_dep_count</td>
  <td>NU1605_count</td>
  <td>NU1107_count</td>
  <td>NU1202_count</td>
  <td>NU1608_count</td>
  <td>NU1103_count</td>
  <td>NU1701_count</td>
  <td>developer_directly_dependencies_count</td>
  <td>developer_total_dep_count</td>
  <td>developer_NU1608_count</td>
  <td>developer_NU1103_count</td>
  <td>developer_NU1701_count</td>
  <td>developer_major_count</td>
  <td>developer_change_directly_count</td>
  <td>SAT_directly_dependencies_count</td>
  <td>SAT_total_dep_count</td>
  <td>SAT_NU1608_count</td>
  <td>SAT_NU1103_count</td>
  <td>SAT_NU1701_count</td>
  <td>SAT_major_count</td>
  <td>SAT_change_directly_count</td>
  <td>difference_value_directly_dependencies_count</td>
  <td>difference_value_total_dep_count</td>
  <td>difference_value_warning_count</td>
  <td>difference_value_major_count</td>
  <td>difference_value_change_directly_count</td>
  <td >same_packageName_proportion</td>
  <td>same_packageMajorVersion_proportion</td>
  <td>same_dependencies_proportion</td>
 </tr>
 <tr >
  <td >9014</td>
  <td>arnoldasgudas/Hangfire.MySqlStorage</td>
  <td>https://github.com/arnoldasgudas/Hangfire.MySqlStorage/commit/a07d9d5273dfb87a2631c73b34658a87bfc43145</td>
  <td >Hangfire.MySql.Tests/Hangfire.MySql.Tests.csproj</td>
  <td>.NETFramework4.5</td>
  <td >8</td>
  <td >9</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >9</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >1</td>
  <td >7</td>
  <td >7</td>
  <td >8</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >-7</td>
  <td >-1</td>
  <td >-4</td>
  <td >-1</td>
  <td >-3</td>
  <td >0.57 </td>
  <td >0.57 </td>
  <td >0.38 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9017</td>
  <td>SharebookBR/sharebook-backend</td>
  <td>https://github.com/SharebookBR/sharebook-backend/commit/9b6e87d57feb5e6d0bfda6323a7f9cd7a3b2be21</td>
  <td >ShareBook/ShareBook.
  Tests.BDD/ShareBook.Tests.BDD.csproj</td>
  <td>net5.0</td>
  <td >8</td>
  <td >78</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >45</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >7</td>
  <td >7</td>
  <td >73</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >4</td>
  <td >-7</td>
  <td >28</td>
  <td >-1</td>
  <td >0</td>
  <td >-3</td>
  <td >0.57 </td>
  <td >0.38 </td>
  <td >0.38 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9025</td>
  <td>threenine/swcApi</td>
  <td>https://github.com/threenine/swcApi/commit/48026b0cfd2ced740afad4cb803caa183320cf94</td>
  <td >src/Api.Database/Api.
  Database.csproj</td>
  <td>.NETStandard2.0</td>
  <td >6</td>
  <td >64</td>
  <td >6</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >74</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >5</td>
  <td >5</td>
  <td >40</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >4</td>
  <td >-5</td>
  <td >-34</td>
  <td >0</td>
  <td >0</td>
  <td >-1</td>
  <td >0.80 </td>
  <td >0.80 </td>
  <td >0.29 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9030</td>
  <td>R2D221/WebView2.DOM</td>
  <td>https://github.com/R2D221/WebView2.DOM/commit/5ba200267beb7822ad86d03267de4065e0db50cd</td>
  <td >WebView2.DOM/Web
  View2.DOM.csproj</td>
  <td>net5.0</td>
  <td >7</td>
  <td >8</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >7</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >2</td>
  <td >5</td>
  <td >7</td>
  <td >7</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >-7</td>
  <td >0</td>
  <td >-1</td>
  <td >-2</td>
  <td >-2</td>
  <td >0.33 </td>
  <td >0.33 </td>
  <td >0.33 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9031</td>
  <td>TodorStamenov/GameBox</td>
  <td>https://github.com/TodorStamenov/GameBox/commit/a738cffa6b9e1a22927b7c7b9f52380646cbd536</td>
  <td >Server/GameBox.Sche
  duler/GameBox.Scheduler.csproj</td>
  <td>net5.0</td>
  <td >5</td>
  <td >36</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >46</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >5</td>
  <td >37</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >-5</td>
  <td >-9</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0.80 </td>
  <td >0.80 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9039</td>
  <td>logcorner/LogCorner.EduSync.Speech.Command</td>
  <td>https://github.com/logcorner/LogCorner.EduSync.Speech.Command/commit/d676918357650f9e3b8d3294cd220f38db55bf22</td>
  <td >src/LogCorner.EduSync
  .Speech/LogCorner.EduSync.Speech.Presentation/LogCorner.EduSync.Speech.Presentation.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >5</td>
  <td >94</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >3</td>
  <td >3</td>
  <td >4</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >3</td>
  <td >-4</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9042</td>
  <td>enisn/AutoFilterer</td>
  <td>https://github.com/enisn/AutoFilterer/commit/a97399a53a06888dcd4d9d151f450b15653c2bd0</td>
  <td >sandbox/WebApplicati
  on.API/WebApplication.API.csproj</td>
  <td>net5.0</td>
  <td >5</td>
  <td >38</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >37</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >5</td>
  <td >37</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >-5</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0.75 </td>
  <td >0.75 </td>
  <td >0.40 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9043</td>
  <td>rockfordlhotka/Cloud-Native-HOL</td>
  <td>https://github.com/rockfordlhotka/Cloud-Native-HOL/commit/4c655ccf40c8932a1ab74ac8e65ca8d80c54bfe8</td>
  <td >src/Lab03/End/BreadS
  ervice/BreadService.csproj</td>
  <td>.NETCoreApp3.0</td>
  <td >5</td>
  <td >75</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >24</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >4</td>
  <td >24</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >-4</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.33 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9049</td>
  <td>signumsoftware/southwind</td>
  <td>https://github.com/signumsoftware/southwind/commit/db5736eff63bd240d78f27a6db71ab693c5903f8</td>
  <td >Southwind.React/Sout
  hwind.React.csproj</td>
  <td>net5.0</td>
  <td >6</td>
  <td >11</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >1</td>
  <td >0</td>
  <td >10</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >5</td>
  <td >10</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >-5</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >-1</td>
  <td >0.67 </td>
  <td >0.67 </td>
  <td >0.67 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9067</td>
  <td>pekkah/tanka-graphql-samples</td>
  <td>https://github.com/pekkah/tanka-graphql-samples/commit/20d0856841f0010b7a88051c2693c53335dfbdea</td>
  <td >src/Host/Host.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >8</td>
  <td >84</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >87</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >7</td>
  <td >9</td>
  <td >84</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >6</td>
  <td >-9</td>
  <td >-3</td>
  <td >-2</td>
  <td >0</td>
  <td >-1</td>
  <td >0.44 </td>
  <td >0.44 </td>
  <td >0.18 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9071</td>
  <td>ismaelhamed/akka-cluster-management</td>
  <td>https://github.com/ismaelhamed/akka-cluster-management/commit/fa190f5c13008ec2b54693c37c683c73ae02b8ad</td>
  <td >src/Akka.Cluster.Mana
  gement/Akka.Cluster.Management.csproj</td>
  <td>.NETStandard2.0</td>
  <td >6</td>
  <td >109</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >119</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >6</td>
  <td >119</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >-6</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0.80 </td>
  <td >0.80 </td>
  <td >0.13 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9078</td>
  <td>ysmoradi/BitSampleApp</td>
  <td>https://github.com/ysmoradi/BitSampleApp/commit/6e89f190d0421149f36e8ea0d8cc2ab70764e901</td>
  <td >SampleApp/SampleAp
  p.csproj</td>
  <td>net5.0</td>
  <td >8</td>
  <td >162</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >179</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >6</td>
  <td >8</td>
  <td >182</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >5</td>
  <td >-8</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >-1</td>
  <td >0.57 </td>
  <td >0.57 </td>
  <td >0.38 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9079</td>
  <td>ysmoradi/BitSampleApp</td>
  <td>https://github.com/ysmoradi/BitSampleApp/commit/4d9891d0d99571a64c9a26e8f927643da6b821bf</td>
  <td >SampleApp/SampleAp
  p.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >11</td>
  <td >217</td>
  <td >0</td>
  <td >1</td>
  <td >6</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >51</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >8</td>
  <td >124</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >7</td>
  <td >-8</td>
  <td >73</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0.86 </td>
  <td >0.86 </td>
  <td >0.63 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9081</td>
  <td>net-daemon/net-hassclient</td>
  <td>https://github.com/net-daemon/net-hassclient/commit/0bf4f7dee4b766e81f7059598d05794f235497b6</td>
  <td >tests/HassClient.Unit.T
  ests/HassClient.Unit.Tests.csproj</td>
  <td>net5.0</td>
  <td >8</td>
  <td >47</td>
  <td >2</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >81</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >4</td>
  <td >9</td>
  <td >81</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >-9</td>
  <td >0</td>
  <td >0</td>
  <td >-2</td>
  <td >1</td>
  <td >0.50 </td>
  <td >0.50 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9085</td>
  <td>ricardocmartin/3d-social-backend</td>
  <td>https://github.com/ricardocmartin/3d-social-backend/commit/ec478ff4cc2cc298d470170cd7ae4e9b35aed4b8</td>
  <td >3dSocial.Api/3dSocial.
  Api.Test/3dSocial.Api.Test.csproj</td>
  <td>.NETCoreApp3.0</td>
  <td >5</td>
  <td >94</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >3</td>
  <td >2</td>
  <td >0</td>
  <td >43</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >4</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >3</td>
  <td >-4</td>
  <td >-39</td>
  <td >-3</td>
  <td >1</td>
  <td >-1</td>
  <td >0.75 </td>
  <td >0.40 </td>
  <td >0.40 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9086</td>
  <td>Nedevski/PanasonicACRemote.VoiceControlLambda</td>
  <td>https://github.com/Nedevski/PanasonicACRemote.VoiceControlLambda/commit/1e67a2b059db347ce24671af3c4e17397e2e4e17</td>
  <td >PanasonicACVoiceRem
  ote/PanasonicACVoiceRemote.csproj</td>
  <td>.NETCoreApp2.1</td>
  <td >5</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >41</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >4</td>
  <td >41</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >-4</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >-1</td>
  <td >0.67 </td>
  <td >0.67 </td>
  <td >0.67 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9099</td>
  <td>SkillsFundingAgency/dss-changefeedsqlprocessor</td>
  <td>https://github.com/SkillsFundingAgency/dss-changefeedsqlprocessor/commit/9eb6b51b3eecc7fa83c5dd8bbda746fda56d585b</td>
  <td >NCS.DSS.ChangeFeedS
  qlProcessor/NCS.DSS.ChangeFeedSqlProcessor.csproj</td>
  <td>.NETStandard2.0</td>
  <td >8</td>
  <td >143</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >146</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >8</td>
  <td >141</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >-8</td>
  <td >-5</td>
  <td >-1</td>
  <td >0</td>
  <td >0</td>
  <td >0.71 </td>
  <td >0.71 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9100</td>
  <td>latinonetonline/LatinoNETOnline.App</td>
  <td>https://github.com/latinonetonline/LatinoNETOnline.App/commit/082804a120ca6c3a4f1e3c87e82f121263f68349</td>
  <td >LatinoNETOnline.App/
  Server/LatinoNETOnline.App.Server.csproj</td>
  <td>net5.0</td>
  <td >6</td>
  <td >13</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >11</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >2</td>
  <td >5</td>
  <td >5</td>
  <td >11</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >4</td>
  <td >-5</td>
  <td >0</td>
  <td >-2</td>
  <td >-1</td>
  <td >-1</td>
  <td >0.80 </td>
  <td >0.80 </td>
  <td >0.80 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9101</td>
  <td>latinonetonline/LatinoNETOnline.App</td>
  <td>https://github.com/latinonetonline/LatinoNETOnline.App/commit/fcb560e7ab085e73eae9d1e773449c4fbe642d75</td>
  <td >LatinoNETOnline.App/
  Server/LatinoNETOnline.App.Server.csproj</td>
  <td>net5.0</td>
  <td >6</td>
  <td >13</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >11</td>
  <td >0</td>
  <td >2</td>
  <td >1</td>
  <td >2</td>
  <td >5</td>
  <td >5</td>
  <td >11</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >4</td>
  <td >-5</td>
  <td >0</td>
  <td >-2</td>
  <td >-1</td>
  <td >-1</td>
  <td >0.80 </td>
  <td >0.80 </td>
  <td >0.80 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9105</td>
  <td>pact-foundation/pact-net</td>
  <td>https://github.com/pact-foundation/pact-net/commit/130d8b97a4aa28dd2b9361e22e51d836005ea825</td>
  <td >Samples/EventApi/Con
  sumer.Tests/Consumer.Tests.csproj</td>
  <td>.NETFramework4.6</td>
  <td >6</td>
  <td >6</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >6</td>
  <td >6</td>
  <td >6</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >-6</td>
  <td >0</td>
  <td >-2</td>
  <td >-1</td>
  <td >-1</td>
  <td >0.83 </td>
  <td >0.83 </td>
  <td >0.83 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9109</td>
  <td>arcus-azure/arcus.eventgrid.proxy</td>
  <td>https://github.com/arcus-azure/arcus.eventgrid.proxy/commit/637fbcac8afe933f0be934f001b65a53546091af</td>
  <td >src/Arcus.EventGrid.Pr
  oxy.Api/Arcus.EventGrid.Proxy.Api.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >6</td>
  <td >119</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >2</td>
  <td >0</td>
  <td >102</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >4</td>
  <td >4</td>
  <td >8</td>
  <td >115</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >5</td>
  <td >-8</td>
  <td >13</td>
  <td >-1</td>
  <td >-3</td>
  <td >1</td>
  <td >0.29 </td>
  <td >0.00 </td>
  <td >0.00 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9122</td>
  <td>Fresa/Port</td>
  <td>https://github.com/Fresa/Port/commit/cf9af696b854d7f8ee8fa13ff4e158ee6fb67f03</td>
  <td >tests/Kubernetes.Test.
  API.Server/Kubernetes.Test.API.Server.csproj</td>
  <td>net5.0</td>
  <td >6</td>
  <td >69</td>
  <td >1</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >64</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >4</td>
  <td >7</td>
  <td >64</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >6</td>
  <td >-7</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0.67 </td>
  <td >0.67 </td>
  <td >0.67 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9123</td>
  <td>Fresa/Port</td>
  <td>https://github.com/Fresa/Port/commit/cf9af696b854d7f8ee8fa13ff4e158ee6fb67f03</td>
  <td >tests/Port.Server.Integ
  rationTests/Port.Server.IntegrationTests.csproj</td>
  <td>net5.0</td>
  <td >11</td>
  <td >96</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >87</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >5</td>
  <td >14</td>
  <td >97</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >6</td>
  <td >-14</td>
  <td >10</td>
  <td >0</td>
  <td >-1</td>
  <td >1</td>
  <td >0.38 </td>
  <td >0.38 </td>
  <td >0.38 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9126</td>
  <td>ops-ai/BeyondAuth</td>
  <td>https://github.com/ops-ai/BeyondAuth/commit/6a5de6939f7bcc586d214994503deaa60c78ea4d</td>
  <td >src/Bridges/DiameterS
  erver/DiameterServer.csproj</td>
  <td>net5.0</td>
  <td >6</td>
  <td >8</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >74</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >5</td>
  <td >5</td>
  <td >29</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >5</td>
  <td >-5</td>
  <td >-45</td>
  <td >-1</td>
  <td >0</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.43 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9127</td>
  <td>ops-ai/BeyondAuth</td>
  <td>https://github.com/ops-ai/BeyondAuth/commit/6a5de6939f7bcc586d214994503deaa60c78ea4d</td>
  <td >src/Bridges/RadiusServ
  er/RadiusServer.csproj</td>
  <td>net5.0</td>
  <td >7</td>
  <td >30</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >28</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >5</td>
  <td >7</td>
  <td >30</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >6</td>
  <td >-7</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0.83 </td>
  <td >0.83 </td>
  <td >0.83 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9142</td>
  <td>jamerst/OpenLD</td>
  <td>https://github.com/jamerst/OpenLD/commit/01d161808e9476ba6b7f2a120035e504acfeee5c</td>
  <td >openld.Tests/openld.T
  ests.csproj</td>
  <td>net5.0</td>
  <td >12</td>
  <td >112</td>
  <td >2</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >114</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >11</td>
  <td >11</td>
  <td >107</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >8</td>
  <td >-11</td>
  <td >-7</td>
  <td >0</td>
  <td >0</td>
  <td >-3</td>
  <td >0.73 </td>
  <td >0.46 </td>
  <td >0.46 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9148</td>
  <td>dr1rrb/smarthome.net</td>
  <td>https://github.com/dr1rrb/smarthome.net/commit/943a70c58726bf466c3e6e942be52bbd1464e115</td>
  <td >src/SmartHomeDotNet
  Host/SmartHomeDotNetHost.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >11</td>
  <td >56</td>
  <td >6</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >46</td>
  <td >0</td>
  <td >2</td>
  <td >2</td>
  <td >3</td>
  <td >10</td>
  <td >10</td>
  <td >50</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >8</td>
  <td >-10</td>
  <td >4</td>
  <td >-2</td>
  <td >0</td>
  <td >-2</td>
  <td >0.80 </td>
  <td >0.64 </td>
  <td >0.64 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9150</td>
  <td>dr1rrb/smarthome.net</td>
  <td>https://github.com/dr1rrb/smarthome.net/commit/646232e0a1c757b89a40c7ed25b9a54ee929506f</td>
  <td >src/SmartHomeDotNet
  Host/SmartHomeDotNetHost.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >11</td>
  <td >56</td>
  <td >6</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >46</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >3</td>
  <td >10</td>
  <td >10</td>
  <td >50</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >8</td>
  <td >-10</td>
  <td >4</td>
  <td >-2</td>
  <td >0</td>
  <td >-2</td>
  <td >0.80 </td>
  <td >0.64 </td>
  <td >0.64 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9151</td>
  <td>stensolino/PersonalAccounting</td>
  <td>https://github.com/stensolino/PersonalAccounting/commit/68b3e17c772e151314ab8552871720d99cdd021f</td>
  <td >PersonalAccounting/P
  ersonalAccounting.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >6</td>
  <td >35</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >35</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >6</td>
  <td >35</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >-6</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0.83 </td>
  <td >0.83 </td>
  <td >0.00 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9163</td>
  <td>Delirios/TaxiService</td>
  <td>https://github.com/Delirios/TaxiService/commit/d33107c5ba2806a65a41ab8ec534c03676f6f113</td>
  <td >TaxiService.News/Taxi
  Service.News.csproj</td>
  <td>net5.0</td>
  <td >5</td>
  <td >105</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >104</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >4</td>
  <td >104</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >-4</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.33 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9165</td>
  <td>daxnet/abacuza</td>
  <td>https://github.com/daxnet/abacuza/commit/b0835392a2c65ea95793e23bc6ebb6a872383932</td>
  <td >src/services/clusters/A
  bacuza.Clusters.ApiService/Abacuza.Clusters.ApiService.csproj</td>
  <td>net5.0</td>
  <td >7</td>
  <td >35</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >1</td>
  <td >0</td>
  <td >31</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >7</td>
  <td >34</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >-7</td>
  <td >3</td>
  <td >-1</td>
  <td >0</td>
  <td >0</td>
  <td >0.60 </td>
  <td >0.60 </td>
  <td >0.33 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9167</td>
  <td>daxnet/abacuza</td>
  <td>https://github.com/daxnet/abacuza/commit/b0835392a2c65ea95793e23bc6ebb6a872383932</td>
  <td >src/services/projects/A
  bacuza.Projects.ApiService/Abacuza.Projects.ApiService.csproj</td>
  <td>net5.0</td>
  <td >5</td>
  <td >31</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >30</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >4</td>
  <td >4</td>
  <td >30</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >-4</td>
  <td >0</td>
  <td >0</td>
  <td >-1</td>
  <td >-2</td>
  <td >0.50 </td>
  <td >0.50 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9170</td>
  <td>pact-foundation/pact-net</td>
  <td>https://github.com/pact-foundation/pact-net/commit/470f7020d763905c85816167ef21466fc46ced74</td>
  <td >Samples/EventApi/Con
  sumer.Tests/Consumer.Tests.csproj</td>
  <td>.NETStandard2.0</td>
  <td >5</td>
  <td >77</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >6</td>
  <td >6</td>
  <td >78</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >-6</td>
  <td >72</td>
  <td >-2</td>
  <td >-1</td>
  <td >-1</td>
  <td >0.83 </td>
  <td >0.83 </td>
  <td >0.83 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9175</td>
  <td>MicrosoftLearning/AI-100-Design-Implement-Azure-AISol</td>
  <td>https://github.com/MicrosoftLearning/AI-100-Design-Implement-Azure-AISol/commit/14cbd42faef0637fefc4a2acc0e2cba81715c334</td>
  <td >Lab3-Basic_Filter_Bot/
  code/Finished/PictureBot/PictureBot.csproj</td>
  <td>.NETCoreApp2.1</td>
  <td >7</td>
  <td >91</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >79</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >5</td>
  <td >6</td>
  <td >126</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >-6</td>
  <td >47</td>
  <td >0</td>
  <td >-1</td>
  <td >-2</td>
  <td >0.60 </td>
  <td >0.60 </td>
  <td >0.33 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9176</td>
  <td>JuergenGutsch/graphql-aspnetcore</td>
  <td>https://github.com/JuergenGutsch/graphql-aspnetcore/commit/3ce31196e0a691c66156248c57a861bf4db48430</td>
  <td >GraphQl.AspNetCore/
  GraphQl.AspNetCore.csproj</td>
  <td>.NETStandard2.0</td>
  <td >6</td>
  <td >86</td>
  <td >2</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >189</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >5</td>
  <td >7</td>
  <td >129</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >6</td>
  <td >-7</td>
  <td >-60</td>
  <td >0</td>
  <td >-1</td>
  <td >1</td>
  <td >0.57 </td>
  <td >0.38 </td>
  <td >0.38 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9180</td>
  <td>revaturexyz/housingxyz</td>
  <td>https://github.com/revaturexyz/housingxyz/commit/ec81ef6623c39fce35f74bc0d6354ca9d5149f5b</td>
  <td >account/src/Revature.
  Account.Tests/Revature.Account.Tests.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >7</td>
  <td >58</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >97</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >6</td>
  <td >93</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >4</td>
  <td >-6</td>
  <td >-4</td>
  <td >-1</td>
  <td >2</td>
  <td >0</td>
  <td >0.60 </td>
  <td >0.60 </td>
  <td >0.60 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9181</td>
  <td>revaturexyz/housingxyz</td>
  <td>https://github.com/revaturexyz/housingxyz/commit/82041eede0256cdf326e1084fa4a85287126eb0e</td>
  <td >account/src/Revature.
  Account.Tests/Revature.Account.Tests.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >7</td>
  <td >58</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >97</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >6</td>
  <td >93</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >4</td>
  <td >-6</td>
  <td >-4</td>
  <td >-1</td>
  <td >2</td>
  <td >0</td>
  <td >0.60 </td>
  <td >0.60 </td>
  <td >0.60 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9187</td>
  <td>hsourcer/hsourcer-backend</td>
  <td>https://github.com/hsourcer/hsourcer-backend/commit/b890e24eef5bafd86c6472c0d6bc26e36c8875a3</td>
  <td >HsourcerXUnitTest/Hs
  ourcerXUnitTest.csproj</td>
  <td>.NETCoreApp2.2</td>
  <td >6</td>
  <td >95</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >78</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >5</td>
  <td >71</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >4</td>
  <td >-5</td>
  <td >-7</td>
  <td >-3</td>
  <td >1</td>
  <td >-1</td>
  <td >0.80 </td>
  <td >0.50 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9188</td>
  <td>phongnguyend/Practical.CleanArchitecture</td>
  <td>https://github.com/phongnguyend/Practical.CleanArchitecture/commit/202604d7a6c3817966e3988634398697ff1cb3f5</td>
  <td >src/Microservices/Serv
  ices.Storage/ClassifiedAds.Services.Storage.Api/ClassifiedAds.Services.Storage.Api.csproj</td>
  <td>net5.0</td>
  <td >442</td>
  <td >55</td>
  <td >28</td>
  <td >2</td>
  <td >4</td>
  <td >2</td>
  <td >16</td>
  <td >0</td>
  <td >13</td>
  <td >83</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >95</td>
  <td >8</td>
  <td >12</td>
  <td >85</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >46</td>
  <td >9</td>
  <td >0</td>
  <td >2</td>
  <td >-1</td>
  <td >-49</td>
  <td >1</td>
  <td >1.08 </td>
  <td >0.67 </td>
  <td >0.39 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9189</td>
  <td>MichaCo/AspNetCore.Services</td>
  <td>https://github.com/MichaCo/AspNetCore.Services/commit/333cb490f2ec922b3d70de3592946ca8ee62cc9d</td>
  <td >ConsulExample/src/ser
  vices/DataService/DataService.csproj</td>
  <td>.NETCoreApp2.0</td>
  <td >264</td>
  <td >175</td>
  <td >60</td>
  <td >2</td>
  <td >3</td>
  <td >4</td>
  <td >18</td>
  <td >0</td>
  <td >9</td>
  <td >175</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >8</td>
  <td >5</td>
  <td >8</td>
  <td >172</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >5</td>
  <td >0</td>
  <td >-3</td>
  <td >-2</td>
  <td >-5</td>
  <td >0</td>
  <td >1.13 </td>
  <td >0.89 </td>
  <td >0.42 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9190</td>
  <td>JonPSmith/EfCoreinAction-SecondEdition</td>
  <td>https://github.com/JonPSmith/EfCoreinAction-SecondEdition/commit/e8baacf0651b3797175858d588e95b699900df5a</td>
  <td >BookApp/BookApp.csp
  roj</td>
  <td>net5.0</td>
  <td >272</td>
  <td >99</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >2</td>
  <td >3</td>
  <td >0</td>
  <td >6</td>
  <td >137</td>
  <td >2</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >5</td>
  <td >137</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >-3</td>
  <td >0</td>
  <td >1</td>
  <td >0.83 </td>
  <td >0.83 </td>
  <td >0.38 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9191</td>
  <td>theolivenbaum/h5</td>
  <td>https://github.com/theolivenbaum/h5/commit/49ad367527f5a82d9db8fea851704ae91b77e14b</td>
  <td >H5/Compiler/Compiler
  .Service/H5.Compiler.Service.csproj</td>
  <td>.NETStandard2.1</td>
  <td >858</td>
  <td >140</td>
  <td >8</td>
  <td >2</td>
  <td >11</td>
  <td >2</td>
  <td >4</td>
  <td >0</td>
  <td >27</td>
  <td >140</td>
  <td >2</td>
  <td >1</td>
  <td >0</td>
  <td >3</td>
  <td >15</td>
  <td >27</td>
  <td >129</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >13</td>
  <td >0</td>
  <td >-11</td>
  <td >-1</td>
  <td >-3</td>
  <td >-2</td>
  <td >0.93 </td>
  <td >0.86 </td>
  <td >0.86 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9192</td>
  <td>Djohnnie/MijnSauna</td>
  <td>https://github.com/Djohnnie/MijnSauna/commit/afb175f255c45830a15fe43d4c1d7ccbce1b9f8a</td>
  <td >src/MijnSauna.Fronten
  d.Phone/MijnSauna.Frontend.Phone/MijnSauna.Frontend.Phone.csproj</td>
  <td>.NETStandard2.0</td>
  <td >272</td>
  <td >79</td>
  <td >39</td>
  <td >2</td>
  <td >6</td>
  <td >2</td>
  <td >14</td>
  <td >0</td>
  <td >8</td>
  <td >32</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >6</td>
  <td >8</td>
  <td >78</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >46</td>
  <td >0</td>
  <td >-4</td>
  <td >0</td>
  <td >0.71 </td>
  <td >0.50 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9193</td>
  <td>EvolutionPlugins/Dummy</td>
  <td>https://github.com/EvolutionPlugins/Dummy/commit/a2866da31ce9c9609313cbbc9defcc1d7acadf84</td>
  <td >Dummy/Dummy.csproj</td>
  <td>.NETFramework4.6.1</td>
  <td >153</td>
  <td >139</td>
  <td >3</td>
  <td >2</td>
  <td >0</td>
  <td >2</td>
  <td >2</td>
  <td >0</td>
  <td >9</td>
  <td >134</td>
  <td >2</td>
  <td >1</td>
  <td >1</td>
  <td >3</td>
  <td >6</td>
  <td >7</td>
  <td >132</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >-2</td>
  <td >-1</td>
  <td >-3</td>
  <td >-1</td>
  <td >1.00 </td>
  <td >0.78 </td>
  <td >0.78 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9194</td>
  <td>by-pinja/pdf-storage</td>
  <td>https://github.com/by-pinja/pdf-storage/commit/7252bed70c7b3b2d2bddf6a50e6cd50abf16b34b</td>
  <td >Pdf.Storage.csproj</td>
  <td>.NETCoreApp2.2</td>
  <td >647</td>
  <td >319</td>
  <td >14</td>
  <td >2</td>
  <td >24</td>
  <td >4</td>
  <td >104</td>
  <td >0</td>
  <td >20</td>
  <td >307</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >131</td>
  <td >8</td>
  <td >20</td>
  <td >303</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >117</td>
  <td >12</td>
  <td >0</td>
  <td >-4</td>
  <td >0</td>
  <td >-14</td>
  <td >4</td>
  <td >1.00 </td>
  <td >0.90 </td>
  <td >0.43 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9195</td>
  <td>Q42/DynamicDataCMS</td>
  <td>https://github.com/Q42/DynamicDataCMS/commit/35fb66f8455a31e1a982b290209b3feed68b5ecc</td>
  <td >src/QMS.Core.Services
  /QMS.Core.Services.csproj</td>
  <td>.NETStandard2.1</td>
  <td >299</td>
  <td >90</td>
  <td >0</td>
  <td >2</td>
  <td >3</td>
  <td >2</td>
  <td >4</td>
  <td >0</td>
  <td >9</td>
  <td >65</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >5</td>
  <td >8</td>
  <td >94</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >7</td>
  <td >0</td>
  <td >29</td>
  <td >0</td>
  <td >-3</td>
  <td >2</td>
  <td >0.89 </td>
  <td >0.55 </td>
  <td >0.21 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9196</td>
  <td>govau/digitalmarketplace</td>
  <td>https://github.com/govau/digitalmarketplace/commit/ea3648dccc2ccce1aba8b24bf14a49627cb1cc7f</td>
  <td >subscribers/email.logg
  er/worker/worker.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >849</td>
  <td >113</td>
  <td >8</td>
  <td >2</td>
  <td >9</td>
  <td >2</td>
  <td >10</td>
  <td >0</td>
  <td >21</td>
  <td >55</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >10</td>
  <td >13</td>
  <td >21</td>
  <td >57</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >12</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >-7</td>
  <td >-1</td>
  <td >0.91 </td>
  <td >0.68 </td>
  <td >0.62 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9197</td>
  <td>jcapellman/DMTP</td>
  <td>https://github.com/jcapellman/DMTP/commit/b05340ad53379623b53710e1ef3566d8fc51a28e</td>
  <td >src/DMTP.REST/DMTP.
  REST.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >700</td>
  <td >182</td>
  <td >28</td>
  <td >2</td>
  <td >3</td>
  <td >2</td>
  <td >14</td>
  <td >0</td>
  <td >17</td>
  <td >181</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >88</td>
  <td >4</td>
  <td >16</td>
  <td >181</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >44</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >-1</td>
  <td >-44</td>
  <td >0</td>
  <td >1.06 </td>
  <td >0.83 </td>
  <td >0.65 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9198</td>
  <td>LykkeCity/Lykke.Service.HftInternalService</td>
  <td>https://github.com/LykkeCity/Lykke.Service.HftInternalService/commit/63c1a10a7bb63b4d0c4c51379c6d851da8a992c2</td>
  <td >src/Lykke.Service.HftIn
  ternalService.Services/Lykke.Service.HftInternalService.Services.csproj</td>
  <td>.NETCoreApp2.1</td>
  <td >135</td>
  <td >338</td>
  <td >0</td>
  <td >3</td>
  <td >1</td>
  <td >2</td>
  <td >1</td>
  <td >0</td>
  <td >7</td>
  <td >297</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >2</td>
  <td >4</td>
  <td >6</td>
  <td >329</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >32</td>
  <td >-1</td>
  <td >-2</td>
  <td >2</td>
  <td >0.86 </td>
  <td >0.86 </td>
  <td >0.44 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9199</td>
  <td>LykkeCity/Lykke.Service.HftInternalService</td>
  <td>https://github.com/LykkeCity/Lykke.Service.HftInternalService/commit/57b7bdc1ab6bf3c0e3e9f3e96178e60a55a99dc7</td>
  <td >src/Lykke.Service.HftIn
  ternalService.Services/Lykke.Service.HftInternalService.Services.csproj</td>
  <td>.NETCoreApp2.1</td>
  <td >135</td>
  <td >338</td>
  <td >0</td>
  <td >3</td>
  <td >1</td>
  <td >2</td>
  <td >1</td>
  <td >0</td>
  <td >7</td>
  <td >297</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >2</td>
  <td >4</td>
  <td >6</td>
  <td >329</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >32</td>
  <td >-1</td>
  <td >-2</td>
  <td >2</td>
  <td >0.86 </td>
  <td >0.86 </td>
  <td >0.44 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9200</td>
  <td>matand/bankor</td>
  <td>https://github.com/matand/bankor/commit/82605778955c716a7d92f2dde267a936e0b2a988</td>
  <td >src/Bancor.Api/Bancor
  .Api.csproj</td>
  <td>.NETCoreApp3.0</td>
  <td >326</td>
  <td >264</td>
  <td >8</td>
  <td >5</td>
  <td >3</td>
  <td >2</td>
  <td >4</td>
  <td >0</td>
  <td >8</td>
  <td >124</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >4</td>
  <td >8</td>
  <td >7</td>
  <td >121</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >7</td>
  <td >0</td>
  <td >-3</td>
  <td >-1</td>
  <td >-1</td>
  <td >-1</td>
  <td >0.88 </td>
  <td >0.67 </td>
  <td >0.67 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9201</td>
  <td>aiba1805/TaskTrackingSystem</td>
  <td>https://github.com/tsukidaime/TaskTrackingSystem/commit/2856879ba01f77b2558e9eef4c7bb93ca34c0718</td>
  <td >TTS.Web/TTS.Web.csp
  roj</td>
  <td>.NETCoreApp3.0</td>
  <td >655</td>
  <td >129</td>
  <td >1</td>
  <td >2</td>
  <td >0</td>
  <td >2</td>
  <td >2</td>
  <td >0</td>
  <td >15</td>
  <td >130</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >3</td>
  <td >14</td>
  <td >13</td>
  <td >127</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >7</td>
  <td >0</td>
  <td >-3</td>
  <td >0</td>
  <td >-2</td>
  <td >-7</td>
  <td >0.87 </td>
  <td >0.87 </td>
  <td >0.75 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9202</td>
  <td>guigomesa/ScrapyTibiaCSharp</td>
  <td>https://github.com/guigomesa/ScrapyTibiaCSharp/commit/b7f6c6908b7faca54f6e9f1269f88424a6ca41ba</td>
  <td >TibiaApi/TibiaApi.Web
  .csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >762</td>
  <td >294</td>
  <td >2</td>
  <td >2</td>
  <td >0</td>
  <td >2</td>
  <td >4</td>
  <td >0</td>
  <td >19</td>
  <td >327</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >10</td>
  <td >18</td>
  <td >326</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >10</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >0.95 </td>
  <td >0.85 </td>
  <td >0.48 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9203</td>
  <td>JanKnipp/Template_NET_5_WORKER</td>
  <td>https://github.com/JanKnipp/Template_NET_5_WORKER/commit/b05d6a11b72283444cbb916bf86852e307253297</td>
  <td >src/Template_NET_CO
  RE_3_WORKER.CoreService/Template_NET_CORE_3_WORKER.CoreService.csproj��src/Template_NET_5_WORKER.CoreService/Template_NET_5_WORKER.CoreService.csproj</td>
  <td>net5.0</td>
  <td >1348</td>
  <td >174</td>
  <td >33</td>
  <td >2</td>
  <td >16</td>
  <td >2</td>
  <td >15</td>
  <td >0</td>
  <td >38</td>
  <td >104</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >17</td>
  <td >24</td>
  <td >37</td>
  <td >168</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >13</td>
  <td >23</td>
  <td >0</td>
  <td >64</td>
  <td >-1</td>
  <td >-4</td>
  <td >-1</td>
  <td >1.03 </td>
  <td >0.97 </td>
  <td >0.63 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9204</td>
  <td>mp1011/JiraGraphThing</td>
  <td>https://github.com/mp1011/JiraGraphThing/commit/50b8349a2f1a136672fcf62c05c66178b78f976c</td>
  <td >JiraDataLayer/JiraData
  Layer.csproj</td>
  <td>.NETStandard2.0</td>
  <td >276</td>
  <td >57</td>
  <td >4</td>
  <td >1</td>
  <td >0</td>
  <td >2</td>
  <td >3</td>
  <td >0</td>
  <td >10</td>
  <td >32</td>
  <td >0</td>
  <td >1</td>
  <td >1</td>
  <td >3</td>
  <td >6</td>
  <td >9</td>
  <td >45</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >4</td>
  <td >0</td>
  <td >13</td>
  <td >-1</td>
  <td >-2</td>
  <td >-2</td>
  <td >0.90 </td>
  <td >0.90 </td>
  <td >0.90 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9205</td>
  <td>Maarten88/rrod</td>
  <td>https://github.com/Maarten88/rrod/commit/478759819ce2d44ec321064aa777fdc7908719be</td>
  <td >src/Webapp/Webapp.
  csproj</td>
  <td>.NETCoreApp2.1</td>
  <td >309</td>
  <td >269</td>
  <td >1</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >8</td>
  <td >331</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >5</td>
  <td >8</td>
  <td >333</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >5</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.60 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9206</td>
  <td>dotnet-presentations/aspnetcore-app-workshop</td>
  <td>https://github.com/dotnet-presentations/aspnetcore-app-workshop/commit/ce5bf9d06acf04aba73656a9c8c5462c487737c3</td>
  <td >save-points/6-Deploy
  ment-docker/ConferencePlanner/BackEnd/BackEnd.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >427</td>
  <td >124</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >7</td>
  <td >134</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >7</td>
  <td >7</td>
  <td >134</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >-1</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.17 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9207</td>
  <td>dotnet-presentations/aspnetcore-app-workshop</td>
  <td>https://github.com/dotnet-presentations/aspnetcore-app-workshop/commit/ce5bf9d06acf04aba73656a9c8c5462c487737c3</td>
  <td >save-points/6-Deploy
  ment-docker/ConferencePlanner/FrontEnd/FrontEnd.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >485</td>
  <td >116</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >8</td>
  <td >94</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >7</td>
  <td >8</td>
  <td >94</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >7</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.23 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9208</td>
  <td>phongnguyend/Practical.CleanArchitecture</td>
  <td>https://github.com/phongnguyend/Practical.CleanArchitecture/commit/202604d7a6c3817966e3988634398697ff1cb3f5</td>
  <td >src/Microservices/Com
  mon/ClassifiedAds.Infrastructure/ClassifiedAds.Infrastructure.csproj</td>
  <td>net5.0</td>
  <td >1660</td>
  <td >271</td>
  <td >18</td>
  <td >0</td>
  <td >13</td>
  <td >0</td>
  <td >10</td>
  <td >0</td>
  <td >46</td>
  <td >290</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >10</td>
  <td >37</td>
  <td >46</td>
  <td >279</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >34</td>
  <td >0</td>
  <td >-11</td>
  <td >0</td>
  <td >-7</td>
  <td >-3</td>
  <td >1.00 </td>
  <td >0.77 </td>
  <td >0.61 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9209</td>
  <td>phongnguyend/Practical.CleanArchitecture</td>
  <td>https://github.com/phongnguyend/Practical.CleanArchitecture/commit/202604d7a6c3817966e3988634398697ff1cb3f5</td>
  <td >src/ModularMonolith/
  ClassifiedAds.Infrastructure/ClassifiedAds.Infrastructure.csproj</td>
  <td>net5.0</td>
  <td >1610</td>
  <td >267</td>
  <td >18</td>
  <td >0</td>
  <td >12</td>
  <td >0</td>
  <td >9</td>
  <td >0</td>
  <td >46</td>
  <td >290</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >10</td>
  <td >38</td>
  <td >46</td>
  <td >279</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >34</td>
  <td >0</td>
  <td >-11</td>
  <td >0</td>
  <td >-7</td>
  <td >-4</td>
  <td >1.00 </td>
  <td >0.77 </td>
  <td >0.61 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9210</td>
  <td>phongnguyend/Practical.CleanArchitecture</td>
  <td>https://github.com/phongnguyend/Practical.CleanArchitecture/commit/42f0e227185092642a1ccedb7e9c4df952d3eb37</td>
  <td >src/Monolith/Classifie
  dAds.BlazorServerSide/ClassifiedAds.BlazorServerSide.csproj</td>
  <td>net5.0</td>
  <td >310</td>
  <td >132</td>
  <td >2</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >5</td>
  <td >132</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >3</td>
  <td >5</td>
  <td >132</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.43 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9211</td>
  <td>phongnguyend/Practical.CleanArchitecture</td>
  <td>https://github.com/phongnguyend/Practical.CleanArchitecture/commit/42f0e227185092642a1ccedb7e9c4df952d3eb37</td>
  <td >src/Monolith/Classifie
  dAds.Infrastructure/ClassifiedAds.Infrastructure.csproj</td>
  <td>net5.0</td>
  <td >1690</td>
  <td >271</td>
  <td >18</td>
  <td >0</td>
  <td >13</td>
  <td >0</td>
  <td >9</td>
  <td >0</td>
  <td >46</td>
  <td >290</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >10</td>
  <td >38</td>
  <td >46</td>
  <td >279</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >34</td>
  <td >0</td>
  <td >-11</td>
  <td >0</td>
  <td >-7</td>
  <td >-4</td>
  <td >1.00 </td>
  <td >0.77 </td>
  <td >0.61 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9212</td>
  <td>asc-lab/dotnetcore-microservices-poc</td>
  <td>https://github.com/asc-lab/dotnetcore-microservices-poc/commit/268f768d2ad043275f04ac59f907c37d0eb03bd4</td>
  <td >PricingService/PricingS
  ervice.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >373</td>
  <td >129</td>
  <td >1</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >9</td>
  <td >132</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >3</td>
  <td >8</td>
  <td >9</td>
  <td >128</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >6</td>
  <td >0</td>
  <td >-4</td>
  <td >0</td>
  <td >-2</td>
  <td >-2</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9213</td>
  <td>asc-lab/dotnetcore-microservices-poc</td>
  <td>https://github.com/asc-lab/dotnetcore-microservices-poc/commit/07960a3d26dbf92e19b2c2d6dc60fba416384044</td>
  <td >PricingService/PricingS
  ervice.csproj</td>
  <td>.NETCoreApp3.0</td>
  <td >358</td>
  <td >278</td>
  <td >1</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >9</td>
  <td >128</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >3</td>
  <td >8</td>
  <td >9</td>
  <td >128</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >7</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >-1</td>
  <td >-1</td>
  <td >0.88 </td>
  <td >0.67 </td>
  <td >0.67 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9214</td>
  <td>SharebookBR/sharebook-backend</td>
  <td>https://github.com/SharebookBR/sharebook-backend/commit/9b6e87d57feb5e6d0bfda6323a7f9cd7a3b2be21</td>
  <td >ShareBook/ShareBook.
  Api/ShareBook.Api.csproj</td>
  <td>net5.0</td>
  <td >781</td>
  <td >241</td>
  <td >1</td>
  <td >0</td>
  <td >2</td>
  <td >4</td>
  <td >2</td>
  <td >0</td>
  <td >19</td>
  <td >231</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >11</td>
  <td >19</td>
  <td >209</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >5</td>
  <td >0</td>
  <td >-22</td>
  <td >-1</td>
  <td >-5</td>
  <td >-6</td>
  <td >1.00 </td>
  <td >0.65 </td>
  <td >0.65 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9215</td>
  <td>SharebookBR/sharebook-backend</td>
  <td>https://github.com/SharebookBR/sharebook-backend/commit/9b6e87d57feb5e6d0bfda6323a7f9cd7a3b2be21</td>
  <td >ShareBook/ShareBook.
  Service/ShareBook.Service.csproj</td>
  <td>net5.0</td>
  <td >176</td>
  <td >98</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >6</td>
  <td >32</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >5</td>
  <td >6</td>
  <td >110</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >5</td>
  <td >0</td>
  <td >78</td>
  <td >0</td>
  <td >-2</td>
  <td >0</td>
  <td >1.00 </td>
  <td >0.50 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9216</td>
  <td>damienbod/AspNetCoreWindowsAuth</td>
  <td>https://github.com/damienbod/AspNetCoreWindowsAuth/commit/af171de45b0f700182235ed6abe1c996ced443f9</td>
  <td >StsServer/StsServer.cs
  proj</td>
  <td>net5.0</td>
  <td >752</td>
  <td >145</td>
  <td >11</td>
  <td >0</td>
  <td >8</td>
  <td >0</td>
  <td >8</td>
  <td >0</td>
  <td >18</td>
  <td >155</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >12</td>
  <td >14</td>
  <td >18</td>
  <td >155</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >8</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >-6</td>
  <td >-6</td>
  <td >1.00 </td>
  <td >0.50 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9217</td>
  <td>damienbod/AspNetCoreWindowsAuth</td>
  <td>https://github.com/damienbod/AspNetCoreWindowsAuth/commit/fc7caf370af8d2070fb73d266771b8d4f2c7b8a8</td>
  <td >StsServer/StsServer.cs
  proj</td>
  <td>.NETCoreApp3.1</td>
  <td >752</td>
  <td >148</td>
  <td >11</td>
  <td >0</td>
  <td >8</td>
  <td >0</td>
  <td >8</td>
  <td >0</td>
  <td >18</td>
  <td >155</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >8</td>
  <td >16</td>
  <td >18</td>
  <td >155</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >7</td>
  <td >16</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >1.00 </td>
  <td >0.88 </td>
  <td >0.78 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9218</td>
  <td>damienbod/AspNetCoreWindowsAuth</td>
  <td>https://github.com/damienbod/AspNetCoreWindowsAuth/commit/0f05e99a58771118fd4ac629f681b86649c96c94</td>
  <td >StsServer/StsServer.cs
  proj</td>
  <td>.NETCoreApp3.1</td>
  <td >752</td>
  <td >148</td>
  <td >11</td>
  <td >0</td>
  <td >8</td>
  <td >0</td>
  <td >8</td>
  <td >0</td>
  <td >18</td>
  <td >155</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >8</td>
  <td >16</td>
  <td >18</td>
  <td >155</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >7</td>
  <td >16</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >1.00 </td>
  <td >0.88 </td>
  <td >0.78 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9219</td>
  <td>AutomateThePlanet/Meissa</td>
  <td>https://github.com/AutomateThePlanet/Meissa/commit/427e3761b95a5a0f7aa472dbd194d9f35101520f</td>
  <td >Meissa/Meissa.csproj</td>
  <td>.NETCoreApp2.1</td>
  <td >450</td>
  <td >61</td>
  <td >4</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >7</td>
  <td >0</td>
  <td >12</td>
  <td >62</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >12</td>
  <td >12</td>
  <td >92</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >11</td>
  <td >0</td>
  <td >30</td>
  <td >0</td>
  <td >-2</td>
  <td >-1</td>
  <td >1.00 </td>
  <td >0.71 </td>
  <td >0.71 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9220</td>
  <td>SlalomBuild/blackslope.net</td>
  <td>https://github.com/SlalomBuild/blackslope.net/commit/8552b30589b9ba57e05ec80b67f6b2c2350912aa</td>
  <td >src/BlackSlope.Api/Bla
  ckSlope.Api.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >327</td>
  <td >94</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >6</td>
  <td >43</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >4</td>
  <td >6</td>
  <td >33</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >-10</td>
  <td >0</td>
  <td >-1</td>
  <td >1</td>
  <td >1.00 </td>
  <td >0.71 </td>
  <td >0.20 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9221</td>
  <td>sphildreth/roadie</td>
  <td>https://github.com/sphildreth/roadie/commit/2e0759ab2122ec4fdef7c7d107544b64f62b4f70</td>
  <td >Roadie.Api/Roadie.Api
  .csproj</td>
  <td>net5.0</td>
  <td >952</td>
  <td >111</td>
  <td >5</td>
  <td >0</td>
  <td >11</td>
  <td >0</td>
  <td >7</td>
  <td >0</td>
  <td >23</td>
  <td >161</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >12</td>
  <td >18</td>
  <td >23</td>
  <td >177</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >14</td>
  <td >0</td>
  <td >16</td>
  <td >0</td>
  <td >-8</td>
  <td >-4</td>
  <td >1.00 </td>
  <td >0.59 </td>
  <td >0.53 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9222</td>
  <td>rzander/jaindb</td>
  <td>https://github.com/rzander/jaindb/commit/efc4593fece4f5b68fbf0c42a51d3493cf06de9a</td>
  <td >source/Plugin_AzureBl
  ob/Plugin_AzureBlob.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >118</td>
  <td >13</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >8</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >4</td>
  <td >5</td>
  <td >8</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0.80 </td>
  <td >0.80 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9223</td>
  <td>rzander/jaindb</td>
  <td>https://github.com/rzander/jaindb/commit/efc4593fece4f5b68fbf0c42a51d3493cf06de9a</td>
  <td >source/Plugin_Cosmos
  DB/Plugin_CosmosDB.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >120</td>
  <td >6</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >54</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >4</td>
  <td >5</td>
  <td >54</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0.80 </td>
  <td >0.80 </td>
  <td >0.80 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9224</td>
  <td>rzander/jaindb</td>
  <td>https://github.com/rzander/jaindb/commit/efc4593fece4f5b68fbf0c42a51d3493cf06de9a</td>
  <td >source/Plugin_Memor
  yCache/Plugin_MemoryCache.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >124</td>
  <td >6</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >5</td>
  <td >73</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >4</td>
  <td >5</td>
  <td >74</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >5</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >-1</td>
  <td >1</td>
  <td >0.80 </td>
  <td >0.50 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9225</td>
  <td>rzander/jaindb</td>
  <td>https://github.com/rzander/jaindb/commit/efc4593fece4f5b68fbf0c42a51d3493cf06de9a</td>
  <td >source/Plugin_Redis/Pl
  ugin_Redis.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >110</td>
  <td >6</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >78</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >2</td>
  <td >4</td>
  <td >5</td>
  <td >78</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0.80 </td>
  <td >0.80 </td>
  <td >0.80 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9226</td>
  <td>rzander/jaindb</td>
  <td>https://github.com/rzander/jaindb/commit/efc4593fece4f5b68fbf0c42a51d3493cf06de9a</td>
  <td >source/Plugin_Rethink
  DB/Plugin_RethinkDB.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >107</td>
  <td >6</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >5</td>
  <td >79</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >4</td>
  <td >5</td>
  <td >69</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >5</td>
  <td >0</td>
  <td >-10</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0.80 </td>
  <td >0.80 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9227</td>
  <td>rzander/jaindb</td>
  <td>https://github.com/rzander/jaindb/commit/efc4593fece4f5b68fbf0c42a51d3493cf06de9a</td>
  <td >source/Plugin_SQLCac
  he/Plugin_SQLCache.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >157</td>
  <td >7</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >6</td>
  <td >78</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >5</td>
  <td >6</td>
  <td >32</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >6</td>
  <td >0</td>
  <td >-46</td>
  <td >0</td>
  <td >-1</td>
  <td >1</td>
  <td >0.83 </td>
  <td >0.57 </td>
  <td >0.57 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9228</td>
  <td>rzander/jaindb</td>
  <td>https://github.com/rzander/jaindb/commit/e8218c30b57f0a072b82cdc402cca434fb3596fe</td>
  <td >source/Plugin_AzureBl
  ob/Plugin_AzureBlob.csproj</td>
  <td>.NETCoreApp2.2</td>
  <td >117</td>
  <td >13</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >8</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >5</td>
  <td >5</td>
  <td >7</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >5</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.67 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9229</td>
  <td>rzander/jaindb</td>
  <td>https://github.com/rzander/jaindb/commit/e8218c30b57f0a072b82cdc402cca434fb3596fe</td>
  <td >source/Plugin_Cosmos
  DB/Plugin_CosmosDB.csproj</td>
  <td>.NETCoreApp2.2</td>
  <td >120</td>
  <td >87</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >53</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >5</td>
  <td >5</td>
  <td >53</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9230</td>
  <td>rzander/jaindb</td>
  <td>https://github.com/rzander/jaindb/commit/e8218c30b57f0a072b82cdc402cca434fb3596fe</td>
  <td >source/Plugin_Memor
  yCache/Plugin_MemoryCache.csproj</td>
  <td>.NETCoreApp2.2</td>
  <td >124</td>
  <td >6</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >5</td>
  <td >75</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >5</td>
  <td >5</td>
  <td >73</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >5</td>
  <td >0</td>
  <td >-2</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.67 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9231</td>
  <td>rzander/jaindb</td>
  <td>https://github.com/rzander/jaindb/commit/e8218c30b57f0a072b82cdc402cca434fb3596fe</td>
  <td >source/Plugin_Redis/Pl
  ugin_Redis.csproj</td>
  <td>.NETCoreApp2.2</td>
  <td >110</td>
  <td >6</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >67</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >5</td>
  <td >5</td>
  <td >77</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >5</td>
  <td >0</td>
  <td >10</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.67 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9232</td>
  <td>rzander/jaindb</td>
  <td>https://github.com/rzander/jaindb/commit/e8218c30b57f0a072b82cdc402cca434fb3596fe</td>
  <td >source/Plugin_Rethink
  DB/Plugin_RethinkDB.csproj</td>
  <td>.NETCoreApp2.2</td>
  <td >106</td>
  <td >6</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >5</td>
  <td >69</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >5</td>
  <td >5</td>
  <td >68</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >5</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.67 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9233</td>
  <td>rzander/jaindb</td>
  <td>https://github.com/rzander/jaindb/commit/e8218c30b57f0a072b82cdc402cca434fb3596fe</td>
  <td >source/Plugin_SQLCac
  he/Plugin_SQLCache.csproj</td>
  <td>.NETCoreApp2.2</td>
  <td >127</td>
  <td >6</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >6</td>
  <td >81</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >6</td>
  <td >6</td>
  <td >33</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >6</td>
  <td >0</td>
  <td >-48</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9234</td>
  <td>PiranhaCMS/piranha.core.templates</td>
  <td>https://github.com/PiranhaCMS/piranha.core.templates/commit/be8c3fd921595cc6a14e4a6c4dd2199d72d01874</td>
  <td >src/web/mvc/MvcWeb
  .csproj</td>
  <td>net5.0</td>
  <td >632</td>
  <td >111</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >16</td>
  <td >0</td>
  <td >16</td>
  <td >111</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >16</td>
  <td >16</td>
  <td >111</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >16</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9235</td>
  <td>PiranhaCMS/piranha.core.templates</td>
  <td>https://github.com/PiranhaCMS/piranha.core.templates/commit/be8c3fd921595cc6a14e4a6c4dd2199d72d01874</td>
  <td >src/web/razor/RazorW
  eb.csproj</td>
  <td>net5.0</td>
  <td >632</td>
  <td >111</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >16</td>
  <td >0</td>
  <td >16</td>
  <td >111</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >16</td>
  <td >16</td>
  <td >111</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >16</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9236</td>
  <td>dennisdoomen/EffectiveTddDemo</td>
  <td>https://github.com/dennisdoomen/EffectiveTddDemo/commit/6ef172c78ab08ca915cf45c944838acdc3639ce1</td>
  <td >Tests/DocumentMana
  gement.Specs/DocumentManagement.Specs.csproj</td>
  <td>.NETCoreApp2.2</td>
  <td >340</td>
  <td >105</td>
  <td >2</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >12</td>
  <td >105</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >9</td>
  <td >12</td>
  <td >105</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >-1</td>
  <td >-4</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9237</td>
  <td>adamradocz/boinc-manager</td>
  <td>https://github.com/adamradocz/boinc-manager/commit/a35470012d244a2f9d8dd2ef41559aa3750de218</td>
  <td >BoincManagerWeb/Bo
  incManagerWeb.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >681</td>
  <td >122</td>
  <td >2</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >8</td>
  <td >0</td>
  <td >11</td>
  <td >148</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >10</td>
  <td >11</td>
  <td >146</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >8</td>
  <td >0</td>
  <td >-2</td>
  <td >0</td>
  <td >-3</td>
  <td >-2</td>
  <td >0.80 </td>
  <td >0.64 </td>
  <td >0.64 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9238</td>
  <td>thanhxuanhd/BlogSimpleAPI</td>
  <td>https://github.com/thanhxuanhd/BlogSimpleAPI/commit/dcd2f6da7e0d20cdc80440082a8004dc643af31d</td>
  <td >Blog.WebApi/Blog.We
  bApi.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >888</td>
  <td >169</td>
  <td >3</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >8</td>
  <td >0</td>
  <td >18</td>
  <td >168</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >13</td>
  <td >18</td>
  <td >168</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >11</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >-2</td>
  <td >-2</td>
  <td >1.00 </td>
  <td >0.80 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9239</td>
  <td>niaher/uimf-app</td>
  <td>https://github.com/niaher/uimf-app/commit/eba305f738df7ba4af0e86a63fc44b623b6f2837</td>
  <td >UimfApp.Infrastructur
  e/UimfApp.Infrastructure.csproj</td>
  <td>net5.0</td>
  <td >508</td>
  <td >157</td>
  <td >4</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >8</td>
  <td >0</td>
  <td >10</td>
  <td >104</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >9</td>
  <td >10</td>
  <td >83</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >9</td>
  <td >0</td>
  <td >-21</td>
  <td >0</td>
  <td >-6</td>
  <td >0</td>
  <td >1.00 </td>
  <td >0.25 </td>
  <td >0.25 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9240</td>
  <td>viniciusduartereis/Corporate-Chat</td>
  <td>https://github.com/viniciusduartereis/Corporate-Chat/commit/062130e570d21395ce2c5fe933e4f9ab9bc5b608</td>
  <td >src/Corporate.Chat.API
  /Corporate.Chat.API.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >1038</td>
  <td >305</td>
  <td >11</td>
  <td >2</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >21</td>
  <td >308</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >11</td>
  <td >21</td>
  <td >295</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >10</td>
  <td >0</td>
  <td >-13</td>
  <td >0</td>
  <td >-2</td>
  <td >-1</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.91 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9241</td>
  <td>viniciusduartereis/Corporate-Chat</td>
  <td>https://github.com/viniciusduartereis/Corporate-Chat/commit/3e8c2e534c1ad0aebe2543dbe33b2642c123a22b</td>
  <td >src/Corporate.Chat.API
  /Corporate.Chat.API.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >1038</td>
  <td >305</td>
  <td >11</td>
  <td >2</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >21</td>
  <td >308</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >3</td>
  <td >11</td>
  <td >21</td>
  <td >295</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >10</td>
  <td >0</td>
  <td >-13</td>
  <td >0</td>
  <td >-2</td>
  <td >-1</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.91 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9242</td>
  <td>zhangchaoza/corert-samples</td>
  <td>https://github.com/zhangchaoza/corert-samples/commit/f74c71e0eb92f3f9785a4c89d41ce79628e72d47</td>
  <td >CommandLineUtilsDe
  mo/AdvancedAttributesCoreRTDemo/AdvancedAttributesCoreRTDemo.csproj</td>
  <td>net5.0</td>
  <td >483</td>
  <td >8</td>
  <td >2</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >7</td>
  <td >0</td>
  <td >7</td>
  <td >17</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >8</td>
  <td >7</td>
  <td >7</td>
  <td >73</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >6</td>
  <td >0</td>
  <td >56</td>
  <td >0</td>
  <td >-6</td>
  <td >-1</td>
  <td >1.00 </td>
  <td >0.08 </td>
  <td >0.08 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9243</td>
  <td>innvistech/dotnetcore-microservices-poc</td>
  <td>https://github.com/innvistech/dotnetcore-microservices-poc/commit/268f768d2ad043275f04ac59f907c37d0eb03bd4</td>
  <td >PricingService/PricingS
  ervice.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >373</td>
  <td >129</td>
  <td >1</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >9</td>
  <td >132</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >8</td>
  <td >9</td>
  <td >128</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >6</td>
  <td >0</td>
  <td >-4</td>
  <td >0</td>
  <td >-2</td>
  <td >-2</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9244</td>
  <td>innvistech/dotnetcore-microservices-poc</td>
  <td>https://github.com/innvistech/dotnetcore-microservices-poc/commit/07960a3d26dbf92e19b2c2d6dc60fba416384044</td>
  <td >PricingService/PricingS
  ervice.csproj</td>
  <td>.NETCoreApp3.0</td>
  <td >358</td>
  <td >278</td>
  <td >1</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >9</td>
  <td >128</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >8</td>
  <td >9</td>
  <td >128</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >7</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >-1</td>
  <td >-1</td>
  <td >0.88 </td>
  <td >0.67 </td>
  <td >0.67 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9245</td>
  <td>CharlesRea/clud</td>
  <td>https://github.com/CharlesRea/clud/commit/9d42def2d09d143a150e110085a26d3649865f50</td>
  <td >src/Api/Api.csproj</td>
  <td>net5.0</td>
  <td >354</td>
  <td >107</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >9</td>
  <td >122</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >8</td>
  <td >9</td>
  <td >113</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >-9</td>
  <td >0</td>
  <td >-3</td>
  <td >-4</td>
  <td >1.00 </td>
  <td >0.64 </td>
  <td >0.64 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9246</td>
  <td>FightCore/Backend</td>
  <td>https://github.com/FightCore/Backend/commit/0a644dd3588f8543bb56882007d23dfecc19369a</td>
  <td >FightCore.Backend/Fig
  htCore.Backend/FightCore.Backend.csproj</td>
  <td>net5.0</td>
  <td >821</td>
  <td >180</td>
  <td >4</td>
  <td >0</td>
  <td >9</td>
  <td >0</td>
  <td >10</td>
  <td >0</td>
  <td >19</td>
  <td >177</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >10</td>
  <td >17</td>
  <td >19</td>
  <td >177</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >13</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >-5</td>
  <td >-4</td>
  <td >0.67 </td>
  <td >0.50 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9247</td>
  <td>DiyazY/service-log</td>
  <td>https://github.com/DiyazY/service-log/commit/dbec477fde310985f42169d82bfc6a22e9d3d9b7</td>
  <td >sl.web/sl.web.csproj</td>
  <td>net5.0</td>
  <td >244</td>
  <td >106</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >4</td>
  <td >54</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >4</td>
  <td >4</td>
  <td >111</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >57</td>
  <td >0</td>
  <td >-3</td>
  <td >-2</td>
  <td >1.00 </td>
  <td >0.14 </td>
  <td >0.14 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9248</td>
  <td>ops-ai/BeyondAuth</td>
  <td>https://github.com/ops-ai/BeyondAuth/commit/6a5de6939f7bcc586d214994503deaa60c78ea4d</td>
  <td >src/AuditServer/AuditS
  erver.csproj</td>
  <td>net5.0</td>
  <td >642</td>
  <td >210</td>
  <td >2</td>
  <td >0</td>
  <td >8</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >17</td>
  <td >214</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >14</td>
  <td >17</td>
  <td >193</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >11</td>
  <td >0</td>
  <td >-21</td>
  <td >0</td>
  <td >-5</td>
  <td >-3</td>
  <td >1.00 </td>
  <td >0.55 </td>
  <td >0.31 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9249</td>
  <td>MattRyder/LifeCMS</td>
  <td>https://github.com/MattRyder/LifeCMS/commit/877a4ef726f7105b2748d8678e71570d2898b913</td>
  <td >src/Services/ContentCr
  eation/ContentCreation.API/ContentCreation.API.csproj</td>
  <td>net5.0</td>
  <td >573</td>
  <td >156</td>
  <td >3</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >16</td>
  <td >110</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >11</td>
  <td >16</td>
  <td >160</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >11</td>
  <td >0</td>
  <td >50</td>
  <td >0</td>
  <td >-4</td>
  <td >0</td>
  <td >1.00 </td>
  <td >0.60 </td>
  <td >0.52 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9250</td>
  <td>nojkhieppso/dotnetcore-microservices</td>
  <td>https://github.com/nojkhieppso/dotnetcore-microservices/commit/268f768d2ad043275f04ac59f907c37d0eb03bd4</td>
  <td >PricingService/PricingS
  ervice.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >373</td>
  <td >129</td>
  <td >1</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >9</td>
  <td >132</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >8</td>
  <td >9</td>
  <td >128</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >6</td>
  <td >0</td>
  <td >-4</td>
  <td >0</td>
  <td >-2</td>
  <td >-2</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9251</td>
  <td>nojkhieppso/dotnetcore-microservices</td>
  <td>https://github.com/nojkhieppso/dotnetcore-microservices/commit/07960a3d26dbf92e19b2c2d6dc60fba416384044</td>
  <td >PricingService/PricingS
  ervice.csproj</td>
  <td>.NETCoreApp3.0</td>
  <td >358</td>
  <td >278</td>
  <td >1</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >9</td>
  <td >128</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >8</td>
  <td >9</td>
  <td >128</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >7</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >-1</td>
  <td >-1</td>
  <td >0.88 </td>
  <td >0.67 </td>
  <td >0.67 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9252</td>
  <td>LykkeCity/Lykke.Service.HftInternalService</td>
  <td>https://github.com/LykkeCity/Lykke.Service.HftInternalService/commit/63c1a10a7bb63b4d0c4c51379c6d851da8a992c2</td>
  <td >src/Lykke.Service.HftIn
  ternalService/Lykke.Service.HftInternalService.csproj</td>
  <td>.NETCoreApp2.1</td>
  <td >561</td>
  <td >239</td>
  <td >4</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >17</td>
  <td >188</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >13</td>
  <td >17</td>
  <td >186</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >12</td>
  <td >0</td>
  <td >-2</td>
  <td >0</td>
  <td >-2</td>
  <td >-1</td>
  <td >0.92 </td>
  <td >0.67 </td>
  <td >0.67 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9253</td>
  <td>LykkeCity/Lykke.Service.HftInternalService</td>
  <td>https://github.com/LykkeCity/Lykke.Service.HftInternalService/commit/57b7bdc1ab6bf3c0e3e9f3e96178e60a55a99dc7</td>
  <td >src/Lykke.Service.HftIn
  ternalService/Lykke.Service.HftInternalService.csproj</td>
  <td>.NETCoreApp2.1</td>
  <td >561</td>
  <td >239</td>
  <td >4</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >17</td>
  <td >188</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >13</td>
  <td >17</td>
  <td >186</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >12</td>
  <td >0</td>
  <td >-2</td>
  <td >0</td>
  <td >-2</td>
  <td >-1</td>
  <td >0.92 </td>
  <td >0.67 </td>
  <td >0.67 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9254</td>
  <td>equinor/procosys-library-api</td>
  <td>https://github.com/equinor/procosys-library-api/commit/89874e14c935fe47918674352097f1d7d512aa1d</td>
  <td >src/Equinor.Procosys.Li
  brary.WebApi/Equinor.Procosys.Library.WebApi.csproj</td>
  <td>net5.0</td>
  <td >829</td>
  <td >113</td>
  <td >4</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >17</td>
  <td >174</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >7</td>
  <td >11</td>
  <td >17</td>
  <td >161</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >10</td>
  <td >0</td>
  <td >-13</td>
  <td >0</td>
  <td >-5</td>
  <td >-1</td>
  <td >1.00 </td>
  <td >0.79 </td>
  <td >0.79 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9255</td>
  <td>ElizaReiGWCD/cutie-bot</td>
  <td>https://github.com/ElizaReiGWCD/cutie-bot/commit/6bfb79650d89d6e59abd76b886645ecb6db93826</td>
  <td >src/discordbot/discord
  bot.csproj</td>
  <td>net5.0</td>
  <td >257</td>
  <td >267</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >9</td>
  <td >266</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >6</td>
  <td >9</td>
  <td >267</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >1.00 </td>
  <td >0.71 </td>
  <td >0.71 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9256</td>
  <td>ttu/dotnet-fake-json-server</td>
  <td>https://github.com/ttu/dotnet-fake-json-server/commit/077ce5d556fcef3c355c3adeb1704d9ebb93d817</td>
  <td >FakeServer/FakeServer
  .csproj</td>
  <td>.NETCoreApp2.1</td>
  <td >634</td>
  <td >226</td>
  <td >8</td>
  <td >0</td>
  <td >7</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >17</td>
  <td >233</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >16</td>
  <td >17</td>
  <td >215</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >10</td>
  <td >0</td>
  <td >-18</td>
  <td >0</td>
  <td >-2</td>
  <td >-6</td>
  <td >1.00 </td>
  <td >0.89 </td>
  <td >0.62 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9257</td>
  <td>luoyunchong/lin-cms-dotnetcore</td>
  <td>https://github.com/luoyunchong/lin-cms-dotnetcore/commit/3caa119ea496db6d736f2f16c4d1aade95daf0f2</td>
  <td >src/LinCms.Web/LinC
  ms.Web.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >901</td>
  <td >182</td>
  <td >15</td>
  <td >0</td>
  <td >11</td>
  <td >0</td>
  <td >10</td>
  <td >0</td>
  <td >24</td>
  <td >207</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >7</td>
  <td >17</td>
  <td >24</td>
  <td >171</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >17</td>
  <td >0</td>
  <td >-36</td>
  <td >0</td>
  <td >-4</td>
  <td >0</td>
  <td >1.00 </td>
  <td >0.85 </td>
  <td >0.78 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9258</td>
  <td>chayxana/Restaurant-App</td>
  <td>https://github.com/chayxana/Restaurant-App/commit/43ae499d618e5887781054fed4530ca91b03b811</td>
  <td >src/backend/services/
  menu.api/Menu.API/Menu.API.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >553</td>
  <td >90</td>
  <td >1</td>
  <td >0</td>
  <td >8</td>
  <td >0</td>
  <td >7</td>
  <td >0</td>
  <td >16</td>
  <td >106</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >8</td>
  <td >13</td>
  <td >16</td>
  <td >131</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >14</td>
  <td >0</td>
  <td >25</td>
  <td >0</td>
  <td >-6</td>
  <td >1</td>
  <td >1.00 </td>
  <td >0.68 </td>
  <td >0.33 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9259</td>
  <td>asc-lab/dotnetcore-microservices-poc</td>
  <td>https://github.com/asc-lab/dotnetcore-microservices-poc/commit/f58f7714fffce0c9de6ea6926e67989f1c18ae88</td>
  <td >PricingService/PricingS
  ervice.csproj</td>
  <td>.NETCoreApp3.0</td>
  <td >358</td>
  <td >278</td>
  <td >1</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >9</td>
  <td >128</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >8</td>
  <td >9</td>
  <td >128</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >7</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >-1</td>
  <td >-1</td>
  <td >0.88 </td>
  <td >0.67 </td>
  <td >0.67 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9260</td>
  <td>igritco/CleanArchitecture</td>
  <td>https://github.com/igritco/CleanArchitecture/commit/626a7fbd977ed31d1da84d0c1643250460156336</td>
  <td >ToDoApp/Presentation
  /ToDoApp.Server/ToDoApp.Server.csproj</td>
  <td>net5.0</td>
  <td >495</td>
  <td >147</td>
  <td >1</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >7</td>
  <td >118</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >6</td>
  <td >7</td>
  <td >147</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >4</td>
  <td >0</td>
  <td >29</td>
  <td >0</td>
  <td >-2</td>
  <td >-2</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9261</td>
  <td>Oragon/Oragon.Contexts</td>
  <td>https://github.com/Oragon/Oragon.Contexts/commit/a209b5bdcafbcaf74db4a6379eb94c2c5b3e9cc7</td>
  <td >tests/Oragon.Context.
  Tests/Oragon.Context.Tests.csproj</td>
  <td>.NETCoreApp2.2</td>
  <td >294</td>
  <td >110</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >12</td>
  <td >132</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >10</td>
  <td >12</td>
  <td >123</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >9</td>
  <td >0</td>
  <td >-9</td>
  <td >0</td>
  <td >-1</td>
  <td >-1</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.71 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9262</td>
  <td>zunath/SWLOR_Website</td>
  <td>https://github.com/zunath/SWLOR_Website/commit/4fb3c7471ddf3c8c0a545badb78abaab4d07f72f</td>
  <td >SWLOR.Web/SWLOR.
  Web.csproj</td>
  <td>.NETCoreApp2.1</td>
  <td >253</td>
  <td >149</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >5</td>
  <td >151</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >5</td>
  <td >145</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >-6</td>
  <td >0</td>
  <td >0</td>
  <td >-1</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.67 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9263</td>
  <td>TomaT3/SpiritSpender</td>
  <td>https://github.com/TomaT3/SpiritSpender/commit/ec06c5d3aec22f69cf8930b3115fd5a6b0134b8c</td>
  <td >SpiritSpenderServer/sr
  c/SpiritSpenderServer/SpiritSpenderServer.csproj</td>
  <td>net5.0</td>
  <td >489</td>
  <td >166</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >12</td>
  <td >143</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >10</td>
  <td >12</td>
  <td >147</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >9</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >-2</td>
  <td >-1</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9264</td>
  <td>TomaT3/SpiritSpender</td>
  <td>https://github.com/TomaT3/SpiritSpender/commit/d0f08fb1e21a4e311b3e16a2599c81ee6136874c</td>
  <td >SpiritSpenderServer/sr
  c/SpiritSpenderServer/SpiritSpenderServer.csproj</td>
  <td>net5.0</td>
  <td >489</td>
  <td >166</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >12</td>
  <td >143</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >10</td>
  <td >12</td>
  <td >147</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >9</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >-2</td>
  <td >-1</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9265</td>
  <td>hiarcdb/hiarc</td>
  <td>https://github.com/hiarcdb/hiarc/commit/d7ab5b3778e75fa591c30eceab6cd35465acaab3</td>
  <td >HiarcCore/HiarcCore.cs
  proj</td>
  <td>.NETCoreApp3.1</td>
  <td >389</td>
  <td >61</td>
  <td >1</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >11</td>
  <td >111</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >8</td>
  <td >11</td>
  <td >107</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >10</td>
  <td >0</td>
  <td >-4</td>
  <td >0</td>
  <td >-1</td>
  <td >2</td>
  <td >1.00 </td>
  <td >0.83 </td>
  <td >0.29 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9266</td>
  <td>hiarcdb/hiarc</td>
  <td>https://github.com/hiarcdb/hiarc/commit/cbdcdf0b0f873ad8cdd6518687492985b9fd54a8</td>
  <td >HiarcCore/HiarcCore.cs
  proj</td>
  <td>.NETCoreApp3.1</td>
  <td >389</td>
  <td >61</td>
  <td >1</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >11</td>
  <td >111</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >8</td>
  <td >11</td>
  <td >107</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >10</td>
  <td >0</td>
  <td >-4</td>
  <td >0</td>
  <td >-1</td>
  <td >2</td>
  <td >1.00 </td>
  <td >0.83 </td>
  <td >0.29 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9267</td>
  <td>Azure-Samples/Commercial-Marketplace-SaaS-Manual-On-Boarding</td>
  <td>https://github.com/microsoft/Commercial-Marketplace-SaaS-Manual-On-Boarding/commit/723e2b484239ea902a4ecfbc56de52ab90e514a6</td>
  <td >src/CommandCenter/C
  ommandCenter.csproj</td>
  <td>net5.0</td>
  <td >695</td>
  <td >205</td>
  <td >10</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >16</td>
  <td >193</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >9</td>
  <td >16</td>
  <td >182</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >7</td>
  <td >0</td>
  <td >-11</td>
  <td >0</td>
  <td >-3</td>
  <td >-2</td>
  <td >1.00 </td>
  <td >0.68 </td>
  <td >0.52 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9268</td>
  <td>innvistech/dotnetcore-microservices-poc</td>
  <td>https://github.com/innvistech/dotnetcore-microservices-poc/commit/f58f7714fffce0c9de6ea6926e67989f1c18ae88</td>
  <td >PricingService/PricingS
  ervice.csproj</td>
  <td>.NETCoreApp3.0</td>
  <td >358</td>
  <td >278</td>
  <td >1</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >9</td>
  <td >128</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >8</td>
  <td >9</td>
  <td >128</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >7</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >-1</td>
  <td >-1</td>
  <td >0.88 </td>
  <td >0.67 </td>
  <td >0.67 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9269</td>
  <td>brettm42/HistoCoin</td>
  <td>https://github.com/brettm42/HistoCoin/commit/23f72b56e1d80446b99d4b317e36d81b42dfc262</td>
  <td >HistoCoin.csproj</td>
  <td>.NETCoreApp2.1</td>
  <td >195</td>
  <td >280</td>
  <td >2</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >6</td>
  <td >251</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >5</td>
  <td >6</td>
  <td >248</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >5</td>
  <td >0</td>
  <td >-3</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.33 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9270</td>
  <td>matheusrmartinez/api-datadriven-efcore3</td>
  <td>https://github.com/matheusrmartinez/api-datadriven-efcore3/commit/8f6337ad10e0a75bfb428ef2c98a1dcb654b5411</td>
  <td >Shop.csproj</td>
  <td>.NETCoreApp3.0</td>
  <td >274</td>
  <td >76</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >5</td>
  <td >61</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >1</td>
  <td >5</td>
  <td >61</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >-1</td>
  <td >2</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.43 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9271</td>
  <td>nojkhieppso/dotnetcore-microservices</td>
  <td>https://github.com/nojkhieppso/dotnetcore-microservices/commit/f58f7714fffce0c9de6ea6926e67989f1c18ae88</td>
  <td >PricingService/PricingS
  ervice.csproj</td>
  <td>.NETCoreApp3.0</td>
  <td >358</td>
  <td >278</td>
  <td >1</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >9</td>
  <td >128</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >8</td>
  <td >9</td>
  <td >128</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >7</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >-1</td>
  <td >-1</td>
  <td >0.88 </td>
  <td >0.67 </td>
  <td >0.67 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9272</td>
  <td>kinderbueno360/SollariExchangeMoney</td>
  <td>https://github.com/kinderbueno360/SollariExchangeMoney/commit/341536e1d4508cbdc0c1a7929b30f86d2adaeb86</td>
  <td >solari.wallet/solari.wal
  let.csproj</td>
  <td>net5.0</td>
  <td >271</td>
  <td >120</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >5</td>
  <td >119</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >2</td>
  <td >5</td>
  <td >114</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >-5</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9273</td>
  <td>DominikStiller/Vertretungsplan</td>
  <td>https://github.com/DominikStiller/Vertretungsplan/commit/9d11c50dcb35a3a0f181e632830b9cc4f394b04e</td>
  <td >Web/Web.csproj</td>
  <td>.NETCoreApp2.1</td>
  <td >195</td>
  <td >85</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >5</td>
  <td >94</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >4</td>
  <td >5</td>
  <td >43</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >-51</td>
  <td >0</td>
  <td >-3</td>
  <td >-3</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9274</td>
  <td>microsoft/data-accelerator</td>
  <td>https://github.com/microsoft/data-accelerator/commit/e4d6d23bd02cb0737b9edd2b78b8c5f4c0fd8d2e</td>
  <td >Services/DataX.Utilitie
  s/DataX.Utilities.CosmosDB/DataX.Utilities.CosmosDB.csproj</td>
  <td>.NETCoreApp2.2</td>
  <td >180</td>
  <td >90</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >74</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >5</td>
  <td >74</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0.75 </td>
  <td >0.75 </td>
  <td >0.75 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9275</td>
  <td>OData/RESTier</td>
  <td>https://github.com/OData/RESTier/commit/db849518e060f4aea000cb6f82ddbb0178847db9</td>
  <td >src/Microsoft.Restier.T
  ests.AspNet/Microsoft.Restier.Tests.AspNet.csproj</td>
  <td>.NETFramework4.7.2</td>
  <td >198</td>
  <td >16</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >5</td>
  <td >6</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >3</td>
  <td >5</td>
  <td >6</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.67 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9276</td>
  <td>OData/RESTier</td>
  <td>https://github.com/OData/RESTier/commit/db849518e060f4aea000cb6f82ddbb0178847db9</td>
  <td >src/Microsoft.Restier.T
  ests.Core/Microsoft.Restier.Tests.Core.csproj</td>
  <td>.NETFramework4.7.2</td>
  <td >197</td>
  <td >15</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >4</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >2</td>
  <td >4</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >-1</td>
  <td >1</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.60 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9277</td>
  <td>KirillOsenkov/SourceBrowser</td>
  <td>https://github.com/KirillOsenkov/SourceBrowser/commit/3d60ce2e5dc706702080fb4f46b0dbc6f0a2b788</td>
  <td >src/HtmlGenerator.Tes
  ts/HtmlGenerator.Tests.csproj</td>
  <td>.NETFramework4.7.2</td>
  <td >140</td>
  <td >7</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >8</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >5</td>
  <td >5</td>
  <td >8</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >-2</td>
  <td >-1</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.67 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9278</td>
  <td>danielgerlag/workflow-core</td>
  <td>https://github.com/danielgerlag/workflow-core/commit/19f90efafa6da0a382901d2da790c7c09413835f</td>
  <td >src/samples/Workflow
  Core.Sample04/WorkflowCore.Sample04.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >195</td>
  <td >25</td>
  <td >2</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >5</td>
  <td >28</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >5</td>
  <td >5</td>
  <td >84</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >5</td>
  <td >0</td>
  <td >56</td>
  <td >0</td>
  <td >-2</td>
  <td >0</td>
  <td >1.00 </td>
  <td >0.43 </td>
  <td >0.43 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9279</td>
  <td>danielgerlag/workflow-core</td>
  <td>https://github.com/danielgerlag/workflow-core/commit/fcb14346397a56dee53647370281550e9fd95cc9</td>
  <td >src/providers/Workflo
  wCore.Providers.AWS/WorkflowCore.Providers.AWS.csproj</td>
  <td>.NETStandard2.0</td>
  <td >159</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >5</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >4</td>
  <td >5</td>
  <td >67</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >62</td>
  <td >0</td>
  <td >-1</td>
  <td >1</td>
  <td >0.80 </td>
  <td >0.50 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9280</td>
  <td>danielgerlag/workflow-core</td>
  <td>https://github.com/danielgerlag/workflow-core/commit/fcb14346397a56dee53647370281550e9fd95cc9</td>
  <td >src/samples/Workflow
  Core.Sample04/WorkflowCore.Sample04.csproj</td>
  <td>.NETCoreApp3.0</td>
  <td >195</td>
  <td >27</td>
  <td >2</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >5</td>
  <td >27</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >5</td>
  <td >5</td>
  <td >83</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >5</td>
  <td >0</td>
  <td >56</td>
  <td >0</td>
  <td >-2</td>
  <td >0</td>
  <td >1.00 </td>
  <td >0.43 </td>
  <td >0.43 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9281</td>
  <td>danielgerlag/workflow-core</td>
  <td>https://github.com/danielgerlag/workflow-core/commit/a96d7f618aac823b99a094aaf37102827449d187</td>
  <td >src/providers/Workflo
  wCore.Providers.AWS/WorkflowCore.Providers.AWS.csproj</td>
  <td>.NETStandard2.0</td>
  <td >159</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >5</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >4</td>
  <td >5</td>
  <td >67</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >62</td>
  <td >0</td>
  <td >-1</td>
  <td >1</td>
  <td >0.80 </td>
  <td >0.50 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9282</td>
  <td>danielgerlag/workflow-core</td>
  <td>https://github.com/danielgerlag/workflow-core/commit/a96d7f618aac823b99a094aaf37102827449d187</td>
  <td >src/samples/Workflow
  Core.Sample04/WorkflowCore.Sample04.csproj</td>
  <td>.NETCoreApp3.0</td>
  <td >195</td>
  <td >27</td>
  <td >2</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >5</td>
  <td >27</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >5</td>
  <td >5</td>
  <td >83</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >5</td>
  <td >0</td>
  <td >56</td>
  <td >0</td>
  <td >-2</td>
  <td >0</td>
  <td >1.00 </td>
  <td >0.43 </td>
  <td >0.43 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9283</td>
  <td>danielgerlag/workflow-core</td>
  <td>https://github.com/danielgerlag/workflow-core/commit/73b098e115c499ee804197f3c25ab81007066fa5</td>
  <td >src/providers/Workflo
  wCore.Providers.AWS/WorkflowCore.Providers.AWS.csproj</td>
  <td>.NETStandard2.0</td>
  <td >159</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >5</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >4</td>
  <td >5</td>
  <td >67</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >62</td>
  <td >0</td>
  <td >-1</td>
  <td >1</td>
  <td >0.80 </td>
  <td >0.50 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9284</td>
  <td>danielgerlag/workflow-core</td>
  <td>https://github.com/danielgerlag/workflow-core/commit/73b098e115c499ee804197f3c25ab81007066fa5</td>
  <td >src/samples/Workflow
  Core.Sample04/WorkflowCore.Sample04.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >195</td>
  <td >25</td>
  <td >2</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >5</td>
  <td >28</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >5</td>
  <td >5</td>
  <td >84</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >5</td>
  <td >0</td>
  <td >56</td>
  <td >0</td>
  <td >-2</td>
  <td >0</td>
  <td >1.00 </td>
  <td >0.43 </td>
  <td >0.43 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9285</td>
  <td>danielgerlag/workflow-core</td>
  <td>https://github.com/danielgerlag/workflow-core/commit/b1a0f42da4e7ff6894425de2acbd9e2fd6d9f299</td>
  <td >src/providers/Workflo
  wCore.Providers.AWS/WorkflowCore.Providers.AWS.csproj</td>
  <td>.NETStandard2.0</td>
  <td >159</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >5</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >4</td>
  <td >5</td>
  <td >67</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >62</td>
  <td >0</td>
  <td >-1</td>
  <td >1</td>
  <td >0.80 </td>
  <td >0.50 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9286</td>
  <td>danielgerlag/workflow-core</td>
  <td>https://github.com/danielgerlag/workflow-core/commit/b1a0f42da4e7ff6894425de2acbd9e2fd6d9f299</td>
  <td >src/samples/Workflow
  Core.Sample04/WorkflowCore.Sample04.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >195</td>
  <td >25</td>
  <td >2</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >5</td>
  <td >28</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >5</td>
  <td >5</td>
  <td >84</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >5</td>
  <td >0</td>
  <td >56</td>
  <td >0</td>
  <td >-2</td>
  <td >0</td>
  <td >1.00 </td>
  <td >0.43 </td>
  <td >0.43 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9287</td>
  <td>aws/aws-logging-dotnet</td>
  <td>https://github.com/aws/aws-logging-dotnet/commit/17af19a7d9c490697b60f1c9f68b84f7366ea753</td>
  <td >test/AWS.Logger.AspN
  etCore.Tests/AWS.Logger.AspNetCore.Tests.csproj</td>
  <td>.NETCoreApp2.0</td>
  <td >558</td>
  <td >110</td>
  <td >4</td>
  <td >0</td>
  <td >7</td>
  <td >0</td>
  <td >7</td>
  <td >0</td>
  <td >12</td>
  <td >57</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >8</td>
  <td >10</td>
  <td >12</td>
  <td >126</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >12</td>
  <td >0</td>
  <td >69</td>
  <td >0</td>
  <td >-8</td>
  <td >2</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.71 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9288</td>
  <td>cmendible/dotnetcore.samples</td>
  <td>https://github.com/cmendible/dotnetcore.samples/commit/fd0a7e5388f3aee5c35baf62143b1995cb156d98</td>
  <td >cloud.design.patterns/
  health.endpoint.monitor/health.endpoint.monitor.csproj</td>
  <td>.NETCoreApp3.0</td>
  <td >1147</td>
  <td >212</td>
  <td >6</td>
  <td >0</td>
  <td >8</td>
  <td >0</td>
  <td >12</td>
  <td >0</td>
  <td >21</td>
  <td >175</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >18</td>
  <td >21</td>
  <td >177</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >19</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >-4</td>
  <td >1</td>
  <td >1.00 </td>
  <td >0.75 </td>
  <td >0.27 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9289</td>
  <td>bizanc/Bizanc.io.Core</td>
  <td>https://github.com/bizanc/Bizanc.io.Core/commit/f04b0a69e0dcf59e47691626146a32d24957c362</td>
  <td >Bizanc.io.Matching.Or
  acle/Bizanc.io.Matching.Oracle.csproj</td>
  <td>.NETCoreApp3.0</td>
  <td >233</td>
  <td >7</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >7</td>
  <td >95</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >6</td>
  <td >7</td>
  <td >94</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >6</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1.00 </td>
  <td >0.75 </td>
  <td >0.40 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9290</td>
  <td>NTumbleBit/NTumbleBit</td>
  <td>https://github.com/NTumbleBit/NTumbleBit/commit/7e283ac6d599c7bc8a06e207b3f764b495d39b2e</td>
  <td >NTumbleBit/NTumble
  Bit.csproj</td>
  <td>.NETCoreApp2.1</td>
  <td >118</td>
  <td >263</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >269</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >3</td>
  <td >5</td>
  <td >248</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >3</td>
  <td >0</td>
  <td >-21</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.43 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9291</td>
  <td>rzander/ruckzuck</td>
  <td>https://github.com/rzander/ruckzuck/commit/c69e61ce5852a88ebed0909de717063ecd6e763d</td>
  <td >RZ.Server/RZ.Plugin.So
  ftware.Azure/RZ.Plugin.Software.Azure.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >146</td>
  <td >8</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >5</td>
  <td >78</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >5</td>
  <td >5</td>
  <td >80</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >5</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >1.00 </td>
  <td >0.67 </td>
  <td >0.67 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9292</td>
  <td>rzander/ruckzuck</td>
  <td>https://github.com/rzander/ruckzuck/commit/c69e61ce5852a88ebed0909de717063ecd6e763d</td>
  <td >RZ.Server/RZ.Plugin.So
  ftware.Proxy/RZ.Plugin.Software.Proxy.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >146</td>
  <td >8</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >5</td>
  <td >78</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >5</td>
  <td >5</td>
  <td >80</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >5</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >1.00 </td>
  <td >0.67 </td>
  <td >0.67 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9293</td>
  <td>damienbod/AspNetCoreWindowsAuth</td>
  <td>https://github.com/damienbod/AspNetCoreWindowsAuth/commit/10077a81ce84bed80f1fc218da799f01f9567116</td>
  <td >WebApi/WebApi.cspro
  j</td>
  <td>net5.0</td>
  <td >466</td>
  <td >43</td>
  <td >10</td>
  <td >0</td>
  <td >7</td>
  <td >0</td>
  <td >7</td>
  <td >0</td>
  <td >11</td>
  <td >138</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >7</td>
  <td >11</td>
  <td >124</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >8</td>
  <td >0</td>
  <td >-14</td>
  <td >0</td>
  <td >-1</td>
  <td >1</td>
  <td >0.88 </td>
  <td >0.50 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9294</td>
  <td>damienbod/AspNetCoreWindowsAuth</td>
  <td>https://github.com/damienbod/AspNetCoreWindowsAuth/commit/fc7caf370af8d2070fb73d266771b8d4f2c7b8a8</td>
  <td >WebApi/WebApi.cspro
  j</td>
  <td>.NETCoreApp3.1</td>
  <td >470</td>
  <td >68</td>
  <td >10</td>
  <td >0</td>
  <td >7</td>
  <td >0</td>
  <td >8</td>
  <td >0</td>
  <td >11</td>
  <td >139</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >7</td>
  <td >11</td>
  <td >11</td>
  <td >124</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >11</td>
  <td >0</td>
  <td >-15</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >1.00 </td>
  <td >0.83 </td>
  <td >0.57 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9295</td>
  <td>Byndyusoft/Byndyusoft.Dotnet.Core.Infrastructure</td>
  <td>https://github.com/Byndyusoft/Byndyusoft.Dotnet.Core.Infrastructure/commit/7de6ed32ac5fd8dcb5e2fbfd080e282deb243676</td>
  <td >src/Jobs/Consumer/Co
  nsumer.csproj</td>
  <td>.NETCoreApp2.1</td>
  <td >674</td>
  <td >111</td>
  <td >0</td>
  <td >0</td>
  <td >13</td>
  <td >0</td>
  <td >11</td>
  <td >0</td>
  <td >16</td>
  <td >122</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >9</td>
  <td >13</td>
  <td >16</td>
  <td >60</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >14</td>
  <td >0</td>
  <td >-62</td>
  <td >0</td>
  <td >-8</td>
  <td >1</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.60 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9296</td>
  <td>Byndyusoft/Byndyusoft.Dotnet.Core.Infrastructure</td>
  <td>https://github.com/Byndyusoft/Byndyusoft.Dotnet.Core.Infrastructure/commit/7de6ed32ac5fd8dcb5e2fbfd080e282deb243676</td>
  <td >src/Web.Application/
  Web.Application.csproj</td>
  <td>.NETCoreApp2.1</td>
  <td >578</td>
  <td >210</td>
  <td >5</td>
  <td >0</td>
  <td >12</td>
  <td >0</td>
  <td >10</td>
  <td >0</td>
  <td >17</td>
  <td >213</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >11</td>
  <td >17</td>
  <td >212</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >13</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >-1</td>
  <td >2</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.42 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9297</td>
  <td>shawnwildermuth/MetaWeblog</td>
  <td>https://github.com/shawnwildermuth/MetaWeblog/commit/9c9040ea2238512a756e3159c183f117fea90d97</td>
  <td >src/WilderMinds.Meta
  Weblog.Tests/WilderMinds.MetaWeblog.Tests.csproj</td>
  <td>.NETCoreApp2.0</td>
  <td >174</td>
  <td >111</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >5</td>
  <td >103</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >5</td>
  <td >103</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9298</td>
  <td>shawnwildermuth/MetaWeblog</td>
  <td>https://github.com/shawnwildermuth/MetaWeblog/commit/263517ab080e2672922bc8c1bdbe9d6146c889fb</td>
  <td >src/WilderMinds.Meta
  Weblog.Tests/WilderMinds.MetaWeblog.Tests.csproj</td>
  <td>.NETCoreApp2.0</td>
  <td >174</td>
  <td >111</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >5</td>
  <td >103</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >5</td>
  <td >103</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9299</td>
  <td>thinkabouthub/Configuration.EntityFramework</td>
  <td>https://github.com/thinkabouthub/Configuration.EntityFramework/commit/8faabbfa9d40f1b24b57ec64e9d0ce73e7243120</td>
  <td >src/Configuration.Entit
  yFramework.Localization/Configuration.EntityFramework.Localization.csproj</td>
  <td>.NETStandard1.6</td>
  <td >321</td>
  <td >113</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >7</td>
  <td >124</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >6</td>
  <td >7</td>
  <td >124</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.40 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9300</td>
  <td>wwwlicious/servicestack-authentication-identityserver</td>
  <td>https://github.com/wwwlicious/servicestack-authentication-identityserver/commit/2dcc7b5e0a5750b0229bdfdc4ec957e34c5dc650</td>
  <td >src/test/IdentityServer
  3.Contrib.ServiceStack.Tests/IdentityServer3.Contrib.ServiceStack.Tests.csproj</td>
  <td>.NETFramework4.6.2</td>
  <td >125</td>
  <td >7</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >8</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >3</td>
  <td >5</td>
  <td >7</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >-2</td>
  <td >0</td>
  <td >1.00 </td>
  <td >0.67 </td>
  <td >0.67 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9301</td>
  <td>microsoft/SPP_Public</td>
  <td>https://github.com/microsoft/SPP_Public/commit/37502f137a8985d61f5da4147d0003f80db208ed</td>
  <td >src/api/Web/TPP.Web.
  Api/TPP.Api.csproj</td>
  <td>.NETCoreApp1.1</td>
  <td >939</td>
  <td >229</td>
  <td >2</td>
  <td >0</td>
  <td >8</td>
  <td >0</td>
  <td >8</td>
  <td >0</td>
  <td >22</td>
  <td >228</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >14</td>
  <td >22</td>
  <td >230</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >13</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >-3</td>
  <td >-1</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.69 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9302</td>
  <td>theolivenbaum/h5</td>
  <td>https://github.com/theolivenbaum/h5/commit/49ad367527f5a82d9db8fea851704ae91b77e14b</td>
  <td >H5/Compiler/Translato
  r/H5.Translator.csproj</td>
  <td>.NETStandard2.1</td>
  <td >844</td>
  <td >101</td>
  <td >8</td>
  <td >0</td>
  <td >12</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >24</td>
  <td >83</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >13</td>
  <td >25</td>
  <td >116</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >12</td>
  <td >0</td>
  <td >33</td>
  <td >0</td>
  <td >-3</td>
  <td >-1</td>
  <td >0.96 </td>
  <td >0.81 </td>
  <td >0.81 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9303</td>
  <td>CadyIO/hangfire-ravendb</td>
  <td>https://github.com/CadyIO/hangfire-ravendb/commit/f19f1c17b37818656a704fcfdff262f7c6204322</td>
  <td >src/Hangfire.Raven.Tes
  ts/Hangfire.Raven.Tests.csproj</td>
  <td>.NETStandard2.0</td>
  <td >170</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >4</td>
  <td >71</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >4</td>
  <td >4</td>
  <td >71</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.60 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9304</td>
  <td>TechSmith/hyde</td>
  <td>https://github.com/TechSmith/hyde/commit/7cb23c3fa6de37300b3675d46c3a4f9916883ade</td>
  <td >src/Hyde.IntegrationTe
  st/Hyde.IntegrationTest.csproj</td>
  <td>.NETCoreApp1.0</td>
  <td >264</td>
  <td >7</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >7</td>
  <td >92</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >7</td>
  <td >7</td>
  <td >68</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >7</td>
  <td >0</td>
  <td >-24</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9305</td>
  <td>TechSmith/hyde</td>
  <td>https://github.com/TechSmith/hyde/commit/7cb23c3fa6de37300b3675d46c3a4f9916883ade</td>
  <td >src/Hyde.Test/Hyde.Te
  st.csproj</td>
  <td>.NETCoreApp1.0</td>
  <td >173</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >5</td>
  <td >52</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >5</td>
  <td >52</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9306</td>
  <td>ProjectIxian/Spixi</td>
  <td>https://github.com/ProjectIxian/Spixi/commit/2133cc584eb8683fb783b9f16c48b5ffba66a89c</td>
  <td >SPIXI/SPIXI/SPIXI.csproj</td>
  <td>.NETStandard2.0</td>
  <td >221</td>
  <td >70</td>
  <td >2</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >69</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >6</td>
  <td >69</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0.50 </td>
  <td >0.50 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9307</td>
  <td>JudahGabriel/RavenDB.StructuredLog</td>
  <td>https://github.com/JudahGabriel/RavenDB.StructuredLog/commit/c873b32f7a3e425771aab525d8d86034cf627df3</td>
  <td >RavenDB.StructuredLo
  g/RavenDB.StructuredLog.csproj</td>
  <td>.NETStandard2.0</td>
  <td >240</td>
  <td >6</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >6</td>
  <td >66</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >6</td>
  <td >6</td>
  <td >73</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >6</td>
  <td >0</td>
  <td >7</td>
  <td >0</td>
  <td >-4</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9308</td>
  <td>rolfwessels/Command.Bot</td>
  <td>https://github.com/rolfwessels/Command.Bot/commit/30acb58d7dcdf3c8a0caaa1ddd3dfa0f2c1191bd</td>
  <td >src/Command.Bot.Con
  sole/Command.Bot.Console.csproj</td>
  <td>.NETFramework4.6.1</td>
  <td >162</td>
  <td >9</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >8</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >2</td>
  <td >6</td>
  <td >8</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >-1</td>
  <td >2</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.71 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9309</td>
  <td>dapplo/Dapplo.Dopy</td>
  <td>https://github.com/dapplo/Dapplo.Dopy/commit/1581c88ba420b1658da4e0ec62a2a33532954f55</td>
  <td >src/Dapplo.Dopy/Dapp
  lo.Dopy.csproj</td>
  <td>net5.0</td>
  <td >145</td>
  <td >29</td>
  <td >2</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >33</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >5</td>
  <td >33</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0.75 </td>
  <td >0.75 </td>
  <td >0.75 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9310</td>
  <td>coderrio/Coderr.Client.WinForms</td>
  <td>https://github.com/coderrio/Coderr.Client.WinForms/commit/ea5c0487ab8a51a32ffc8a41ad80f1aad4809a99</td>
  <td >src/Coderr.Client.WinF
  orms.Tests/Coderr.Client.WinForms.Tests.csproj</td>
  <td>.NETFramework4.6.1</td>
  <td >149</td>
  <td >7</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >7</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >6</td>
  <td >7</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0.50 </td>
  <td >0.50 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9311</td>
  <td>mscheetz/KuCoinApi.Net</td>
  <td>https://github.com/mscheetz/KuCoinApi.Net/commit/56121142fe87e5bf36c3ba03dca063450c6bc10e</td>
  <td >KuCoinApi.NetCore/Ku
  CoinApi.NetCore/KuCoinApi.NetCore.csproj</td>
  <td>.NETStandard2.0</td>
  <td >143</td>
  <td >6</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >4</td>
  <td >5</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >0.60 </td>
  <td >0.60 </td>
  <td >0.60 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9312</td>
  <td>ThomasZeman/KnxNetCore</td>
  <td>https://github.com/ThomasZeman/KnxNetCore/commit/4501fcc9c194fad2fbfa4ad840d295ee7aa467a4</td>
  <td >KnxNetCore.UnitTests/
  KnxNetCore.UnitTests.csproj</td>
  <td>.NETStandard2.0</td>
  <td >168</td>
  <td >67</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >4</td>
  <td >66</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >2</td>
  <td >4</td>
  <td >66</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0.67 </td>
  <td >0.67 </td>
  <td >0.67 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9313</td>
  <td>BK-Soft/Benchmark.netCoreMappers</td>
  <td>https://github.com/BK-Soft/Benchmark.netCoreMappers/commit/427c6689be70f49ffa8849ceed50a6457bedd95a</td>
  <td >ObjectsMapperBench
  mark/ObjectsMapperBenchmark.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >175</td>
  <td >81</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >7</td>
  <td >90</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >4</td>
  <td >7</td>
  <td >91</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >-2</td>
  <td >1</td>
  <td >1.00 </td>
  <td >0.56 </td>
  <td >0.56 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9314</td>
  <td>mscheetz/CoinbaseProApi.NetCore</td>
  <td>https://github.com/mscheetz/CoinbaseProApi.NetCore/commit/824ebaaf9797b1209b5127c36e17178fe920d423</td>
  <td >CoinbaseProApi.NetCo
  re/CoinbaseProApi.NetCore/CoinbaseProApi.NetCore.csproj</td>
  <td>.NETStandard2.0</td>
  <td >143</td>
  <td >6</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >4</td>
  <td >5</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >0.60 </td>
  <td >0.60 </td>
  <td >0.60 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9315</td>
  <td>rhythminme/splunk.metrics</td>
  <td>https://github.com/rhythminme/splunk.metrics/commit/faef6f61dc325b089372f73c95580bc551ed6ade</td>
  <td >tests/Splunk.Metrics.
  WebApi.Tests/Splunk.Metrics.WebApi.Tests.csproj</td>
  <td>.NETFramework4.7.2</td>
  <td >206</td>
  <td >8</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >7</td>
  <td >8</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >7</td>
  <td >8</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.75 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9316</td>
  <td>rhythminme/splunk.metrics</td>
  <td>https://github.com/rhythminme/splunk.metrics/commit/eb78bc4f2942bd5ab5f764e1d22492f083a1d0a8</td>
  <td >tests/Splunk.Metrics.
  WebApi.Tests/Splunk.Metrics.WebApi.Tests.csproj</td>
  <td>.NETFramework4.7.2</td>
  <td >206</td>
  <td >8</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >7</td>
  <td >8</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >7</td>
  <td >8</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.75 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9317</td>
  <td>terrajobst/sourcebrowser</td>
  <td>https://github.com/terrajobst/sourcebrowser/commit/3d60ce2e5dc706702080fb4f46b0dbc6f0a2b788</td>
  <td >src/HtmlGenerator.Tes
  ts/HtmlGenerator.Tests.csproj</td>
  <td>.NETFramework4.7.2</td>
  <td >140</td>
  <td >7</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >8</td>
  <td >2</td>
  <td >0</td>
  <td >2</td>
  <td >3</td>
  <td >5</td>
  <td >5</td>
  <td >8</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >-2</td>
  <td >-1</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.67 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9318</td>
  <td>WarBorg/RATBVFormsPrism</td>
  <td>https://github.com/WarBorg/RATBVFormsPrism/commit/b8320b7a456c5a680641f501653d7e99c0896ba7</td>
  <td >RATBVFormsPrism/RA
  TBVFormsPrism/RATBVFormsPrism.csproj</td>
  <td>.NETStandard2.0</td>
  <td >213</td>
  <td >12</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >5</td>
  <td >70</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >4</td>
  <td >5</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >4</td>
  <td >0</td>
  <td >-65</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.67 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9319</td>
  <td>govau/digitalmarketplace</td>
  <td>https://github.com/govau/digitalmarketplace/commit/ea3648dccc2ccce1aba8b24bf14a49627cb1cc7f</td>
  <td >subscribers/logs/work
  er.tests/logger.tests.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >237</td>
  <td >122</td>
  <td >2</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >8</td>
  <td >115</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >3</td>
  <td >8</td>
  <td >124</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >4</td>
  <td >0</td>
  <td >9</td>
  <td >0</td>
  <td >-1</td>
  <td >1</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.60 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9320</td>
  <td>govau/digitalmarketplace</td>
  <td>https://github.com/govau/digitalmarketplace/commit/ea3648dccc2ccce1aba8b24bf14a49627cb1cc7f</td>
  <td >subscribers/logs/work
  er/worker.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >706</td>
  <td >108</td>
  <td >9</td>
  <td >0</td>
  <td >10</td>
  <td >0</td>
  <td >10</td>
  <td >0</td>
  <td >20</td>
  <td >54</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >9</td>
  <td >17</td>
  <td >21</td>
  <td >57</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >16</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >-6</td>
  <td >-1</td>
  <td >0.95 </td>
  <td >0.71 </td>
  <td >0.64 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9321</td>
  <td>govau/digitalmarketplace</td>
  <td>https://github.com/govau/digitalmarketplace/commit/ea3648dccc2ccce1aba8b24bf14a49627cb1cc7f</td>
  <td >subscribers/slack/work
  er/worker.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >631</td>
  <td >96</td>
  <td >7</td>
  <td >0</td>
  <td >9</td>
  <td >0</td>
  <td >9</td>
  <td >0</td>
  <td >20</td>
  <td >64</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >10</td>
  <td >16</td>
  <td >21</td>
  <td >57</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >16</td>
  <td >0</td>
  <td >-7</td>
  <td >0</td>
  <td >-7</td>
  <td >0</td>
  <td >0.95 </td>
  <td >0.71 </td>
  <td >0.64 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9322</td>
  <td>nuthrash/Minax</td>
  <td>https://github.com/nuthrash/Minax/commit/81c27f89c93436da0cecd0efe0218f5c3306a7c4</td>
  <td >MinaxWebTranslator/
  MinaxWebTranslator/MinaxWebTranslator.csproj</td>
  <td>.NETStandard2.0</td>
  <td >249</td>
  <td >12</td>
  <td >2</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >8</td>
  <td >12</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >4</td>
  <td >7</td>
  <td >12</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >1.14 </td>
  <td >1.14 </td>
  <td >0.67 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9323</td>
  <td>rolfwessels/CoreDocker</td>
  <td>https://github.com/rolfwessels/CoreDocker/commit/6d8619389ce97589db895a516ed1a1a5090666ae</td>
  <td >src/CoreDocker.Api/Co
  reDocker.Api.csproj</td>
  <td>.NETCoreApp2.0</td>
  <td >617</td>
  <td >163</td>
  <td >4</td>
  <td >0</td>
  <td >11</td>
  <td >0</td>
  <td >11</td>
  <td >0</td>
  <td >13</td>
  <td >163</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >7</td>
  <td >10</td>
  <td >13</td>
  <td >165</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >11</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >-7</td>
  <td >1</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.86 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9324</td>
  <td>SiroccoHub/OneWorldDbClient</td>
  <td>https://github.com/SiroccoHub/OneWorldDbClient/commit/0fa05658438867e0b30246e5a4b8d51e48c154c2</td>
  <td >src/OneWorldDbClient
  .SampleWeb/OneWorldDbClient.SampleWeb.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >418</td>
  <td >7</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >6</td>
  <td >37</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >6</td>
  <td >6</td>
  <td >36</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >1.00 </td>
  <td >0.71 </td>
  <td >0.71 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9325</td>
  <td>awaisa/AK</td>
  <td>https://github.com/awaisa/AK/commit/4f2b429dd7c299c3d7e0fbf6888935eb1ea44c5a</td>
  <td >ak/BusinessCore/Busin
  essCore.csproj</td>
  <td>.NETCoreApp2.0</td>
  <td >221</td>
  <td >105</td>
  <td >2</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >4</td>
  <td >33</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >4</td>
  <td >4</td>
  <td >86</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >53</td>
  <td >0</td>
  <td >-4</td>
  <td >0</td>
  <td >1.00 </td>
  <td >0.33 </td>
  <td >0.33 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9326</td>
  <td>awaisa/AK</td>
  <td>https://github.com/awaisa/AK/commit/4f2b429dd7c299c3d7e0fbf6888935eb1ea44c5a</td>
  <td >ak/WebApi/WebApiCo
  re.csproj</td>
  <td>.NETCoreApp2.0</td>
  <td >2326</td>
  <td >160</td>
  <td >60</td>
  <td >0</td>
  <td >8</td>
  <td >0</td>
  <td >8</td>
  <td >0</td>
  <td >26</td>
  <td >190</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >30</td>
  <td >21</td>
  <td >26</td>
  <td >224</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >17</td>
  <td >6</td>
  <td >0</td>
  <td >34</td>
  <td >0</td>
  <td >-13</td>
  <td >-15</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.93 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9327</td>
  <td>CityOfPhiladelphia/DPD-DocumentAPI</td>
  <td>https://github.com/CityOfPhiladelphia/DPD-DocumentAPI/commit/3a96849fa93b9a4e787873a4ea2f2bc32bd3ebbe</td>
  <td >DocumentAPI/Docume
  ntAPI.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >363</td>
  <td >122</td>
  <td >2</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >7</td>
  <td >121</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >1</td>
  <td >2</td>
  <td >7</td>
  <td >121</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >-1</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9328</td>
  <td>CityOfPhiladelphia/DPD-DocumentAPI</td>
  <td>https://github.com/CityOfPhiladelphia/DPD-DocumentAPI/commit/4332c35b9c2118568f3245e09837a9b92faa31fb</td>
  <td >DocumentAPI/Docume
  ntAPI.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >363</td>
  <td >122</td>
  <td >2</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >1</td>
  <td >2</td>
  <td >7</td>
  <td >121</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >2</td>
  <td >7</td>
  <td >121</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >-1</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9329</td>
  <td>kvantetore/tandembooking</td>
  <td>https://github.com/kvantetore/tandembooking/commit/d2baee28fa467c3b202dd6fd261bcfd7a6934184</td>
  <td >src/src.csproj</td>
  <td>.NETCoreApp1.1</td>
  <td >979</td>
  <td >228</td>
  <td >3</td>
  <td >0</td>
  <td >11</td>
  <td >0</td>
  <td >10</td>
  <td >0</td>
  <td >22</td>
  <td >217</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >3</td>
  <td >16</td>
  <td >22</td>
  <td >219</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >19</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >-3</td>
  <td >3</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.52 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9330</td>
  <td>xerris/Xerris.DotNet.Core.Aws</td>
  <td>https://github.com/xerris/Xerris.DotNet.Core.Aws/commit/02a700e28ea1eac673b09d229d8bb788c0088e2b</td>
  <td >test/Xerris.DotNet.Cor
  e.Aws.Test/Xerris.DotNet.Core.Aws.Test.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >233</td>
  <td >49</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >8</td>
  <td >68</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >5</td>
  <td >9</td>
  <td >82</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >14</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >0.89 </td>
  <td >0.89 </td>
  <td >0.70 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9331</td>
  <td>djpnewton/xchwallet</td>
  <td>https://github.com/djpnewton/xchwallet/commit/59637088a411950fd065047a009516765b01f983</td>
  <td >test/test.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >169</td>
  <td >79</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >5</td>
  <td >86</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >2</td>
  <td >5</td>
  <td >82</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >-4</td>
  <td >0</td>
  <td >-2</td>
  <td >2</td>
  <td >1.00 </td>
  <td >0.43 </td>
  <td >0.25 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9332</td>
  <td>microsoft/data-accelerator</td>
  <td>https://github.com/microsoft/data-accelerator/commit/630fa78263a37ba1598dba002ddc2389301b1d1b</td>
  <td >Services/DataX.Utilitie
  s/DataX.Utilities.CosmosDB/DataX.Utilities.CosmosDB.csproj</td>
  <td>.NETCoreApp2.2</td>
  <td >180</td>
  <td >90</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >74</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >5</td>
  <td >74</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0.75 </td>
  <td >0.75 </td>
  <td >0.75 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9333</td>
  <td>JonPSmith/EfCore.GenericServices</td>
  <td>https://github.com/JonPSmith/EfCore.GenericServices/commit/087cd42b7f7a42b252d046494c02b17308d8885c</td>
  <td >Benchmarking/Bench
  marking.csproj</td>
  <td>net5.0</td>
  <td >179</td>
  <td >132</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >156</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >2</td>
  <td >6</td>
  <td >140</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >2</td>
  <td >0</td>
  <td >-16</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9334</td>
  <td>quartznet/quartznet</td>
  <td>https://github.com/quartznet/quartznet/commit/a22915a9abac1568accb93eb24b4cce5331c8249</td>
  <td >src/Quartz.Examples.A
  spNetCore/Quartz.Examples.AspNetCore.csproj</td>
  <td>net5.0</td>
  <td >291</td>
  <td >120</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >6</td>
  <td >125</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >4</td>
  <td >6</td>
  <td >125</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >1.00 </td>
  <td >0.60 </td>
  <td >0.60 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9335</td>
  <td>danielgerlag/workflow-core</td>
  <td>https://github.com/danielgerlag/workflow-core/commit/0f570816758dc62a3f3eab77ab1a56eff03b35b1</td>
  <td >src/samples/Workflow
  Core.Sample04/WorkflowCore.Sample04.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >195</td>
  <td >25</td>
  <td >2</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >5</td>
  <td >28</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >5</td>
  <td >5</td>
  <td >84</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >5</td>
  <td >0</td>
  <td >56</td>
  <td >0</td>
  <td >-2</td>
  <td >0</td>
  <td >1.00 </td>
  <td >0.43 </td>
  <td >0.25 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9336</td>
  <td>danielgerlag/workflow-core</td>
  <td>https://github.com/danielgerlag/workflow-core/commit/68a38035c210423fbd6c9f93d3cb34ce53c97943</td>
  <td >src/samples/Workflow
  Core.Sample04/WorkflowCore.Sample04.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >195</td>
  <td >25</td>
  <td >2</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >4</td>
  <td >2</td>
  <td >5</td>
  <td >28</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >5</td>
  <td >5</td>
  <td >84</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >5</td>
  <td >0</td>
  <td >56</td>
  <td >0</td>
  <td >-2</td>
  <td >0</td>
  <td >1.00 </td>
  <td >0.43 </td>
  <td >0.25 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9337</td>
  <td>danielgerlag/workflow-core</td>
  <td>https://github.com/danielgerlag/workflow-core/commit/cf2f3ed803f004903456601d9c4a49c9900e3f85</td>
  <td >src/samples/Workflow
  Core.Sample04/WorkflowCore.Sample04.csproj</td>
  <td>.NETCoreApp3.0</td>
  <td >195</td>
  <td >22</td>
  <td >2</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >5</td>
  <td >27</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >5</td>
  <td >5</td>
  <td >83</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >5</td>
  <td >0</td>
  <td >56</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >1.00 </td>
  <td >0.25 </td>
  <td >0.25 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9338</td>
  <td>danielgerlag/workflow-core</td>
  <td>https://github.com/danielgerlag/workflow-core/commit/647d9b8dfbd8cbd14a3dce02c9358a0bf8efe502</td>
  <td >src/samples/Workflow
  Core.Sample04/WorkflowCore.Sample04.csproj</td>
  <td>.NETCoreApp3.0</td>
  <td >195</td>
  <td >22</td>
  <td >2</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >5</td>
  <td >27</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >5</td>
  <td >5</td>
  <td >83</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >5</td>
  <td >0</td>
  <td >56</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >1.00 </td>
  <td >0.25 </td>
  <td >0.25 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9339</td>
  <td>danielgerlag/workflow-core</td>
  <td>https://github.com/danielgerlag/workflow-core/commit/d28b54e02b85abca0c628443b61abd005e5605ae</td>
  <td >src/samples/Workflow
  Core.Sample04/WorkflowCore.Sample04.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >195</td>
  <td >25</td>
  <td >2</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >5</td>
  <td >28</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >5</td>
  <td >5</td>
  <td >84</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >5</td>
  <td >0</td>
  <td >56</td>
  <td >0</td>
  <td >-2</td>
  <td >0</td>
  <td >1.00 </td>
  <td >0.43 </td>
  <td >0.25 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9340</td>
  <td>danielgerlag/workflow-core</td>
  <td>https://github.com/danielgerlag/workflow-core/commit/d7b3c65028f5badadccca8dfcdb683c0fa13d664</td>
  <td >src/samples/Workflow
  Core.Sample04/WorkflowCore.Sample04.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >195</td>
  <td >25</td>
  <td >2</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >5</td>
  <td >28</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >5</td>
  <td >5</td>
  <td >84</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >5</td>
  <td >0</td>
  <td >56</td>
  <td >0</td>
  <td >-2</td>
  <td >0</td>
  <td >1.00 </td>
  <td >0.43 </td>
  <td >0.25 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9341</td>
  <td>Accelerider/Accelerider.Windows</td>
  <td>https://github.com/Accelerider/Accelerider.Windows/commit/a83a3c8413a5e8c518ddf8c3cf32579c6aefff06</td>
  <td >Source/Accelerider.Wi
  ndows.Infrastructure.UI/Accelerider.Windows.Infrastructure.UI.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >279</td>
  <td >79</td>
  <td >2</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >10</td>
  <td >76</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >8</td>
  <td >9</td>
  <td >10</td>
  <td >80</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >9</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >-3</td>
  <td >0</td>
  <td >1.00 </td>
  <td >0.82 </td>
  <td >0.67 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9342</td>
  <td>Accelerider/Accelerider.Windows</td>
  <td>https://github.com/Accelerider/Accelerider.Windows/commit/a83a3c8413a5e8c518ddf8c3cf32579c6aefff06</td>
  <td >Source/Accelerider.Wi
  ndows.InfrastructureTests/Accelerider.Windows.InfrastructureTests.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >195</td>
  <td >97</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >45</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >3</td>
  <td >5</td>
  <td >77</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >1</td>
  <td >0</td>
  <td >32</td>
  <td >0</td>
  <td >0</td>
  <td >-2</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9343</td>
  <td>Accelerider/Accelerider.Windows</td>
  <td>https://github.com/Accelerider/Accelerider.Windows/commit/a83a3c8413a5e8c518ddf8c3cf32579c6aefff06</td>
  <td >Source/Accelerider.Wi
  ndows.Modules.NetDisk/Accelerider.Windows.Modules.NetDisk.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >302</td>
  <td >79</td>
  <td >2</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >10</td>
  <td >21</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >8</td>
  <td >10</td>
  <td >79</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >8</td>
  <td >0</td>
  <td >58</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >1.00 </td>
  <td >0.82 </td>
  <td >0.54 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9344</td>
  <td>Accelerider/Accelerider.Windows</td>
  <td>https://github.com/Accelerider/Accelerider.Windows/commit/a83a3c8413a5e8c518ddf8c3cf32579c6aefff06</td>
  <td >Source/Accelerider.Wi
  ndows/Accelerider.Windows.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >260</td>
  <td >77</td>
  <td >2</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >8</td>
  <td >15</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >5</td>
  <td >8</td>
  <td >77</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >6</td>
  <td >0</td>
  <td >62</td>
  <td >0</td>
  <td >-1</td>
  <td >1</td>
  <td >1.00 </td>
  <td >0.78 </td>
  <td >0.60 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9345</td>
  <td>linys2333/Lys.NetCore</td>
  <td>https://github.com/linys2333/Lys.NetCore/commit/8b6f60da2a33f2248f605f6cec9981bf38578552</td>
  <td >MyWebAPI/Host/Host.
  csproj</td>
  <td>.NETCoreApp2.1</td>
  <td >416</td>
  <td >279</td>
  <td >2</td>
  <td >0</td>
  <td >8</td>
  <td >0</td>
  <td >9</td>
  <td >0</td>
  <td >11</td>
  <td >277</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >9</td>
  <td >11</td>
  <td >276</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >10</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >-3</td>
  <td >1</td>
  <td >1.00 </td>
  <td >0.69 </td>
  <td >0.57 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9346</td>
  <td>digipost/digipost-api-client-dotnet</td>
  <td>https://github.com/digipost/digipost-api-client-dotnet/commit/ae61e86d17b64e88621d0d4c7cba59ccf26d8145</td>
  <td >Digipost.Api.Client.Co
  mmon/Digipost.Api.Client.Common.csproj</td>
  <td>.NETStandard2.0</td>
  <td >203</td>
  <td >6</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >6</td>
  <td >28</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >4</td>
  <td >5</td>
  <td >6</td>
  <td >20</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >6</td>
  <td >0</td>
  <td >-8</td>
  <td >0</td>
  <td >-1</td>
  <td >1</td>
  <td >1.00 </td>
  <td >0.71 </td>
  <td >0.71 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9347</td>
  <td>digipost/digipost-api-client-dotnet</td>
  <td>https://github.com/digipost/digipost-api-client-dotnet/commit/ae61e86d17b64e88621d0d4c7cba59ccf26d8145</td>
  <td >Digipost.Api.Client.Con
  currencyTest/Digipost.Api.Client.ConcurrencyTest.csproj</td>
  <td>.NETStandard2.0</td>
  <td >151</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >14</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >2</td>
  <td >3</td>
  <td >14</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0.67 </td>
  <td >0.67 </td>
  <td >0.67 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9348</td>
  <td>digipost/digipost-api-client-dotnet</td>
  <td>https://github.com/digipost/digipost-api-client-dotnet/commit/ae61e86d17b64e88621d0d4c7cba59ccf26d8145</td>
  <td >Digipost.Api.Client/Dig
  ipost.Api.Client.csproj</td>
  <td>.NETStandard2.0</td>
  <td >412</td>
  <td >13</td>
  <td >0</td>
  <td >0</td>
  <td >12</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >11</td>
  <td >106</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >7</td>
  <td >10</td>
  <td >11</td>
  <td >99</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >11</td>
  <td >0</td>
  <td >-7</td>
  <td >0</td>
  <td >-2</td>
  <td >1</td>
  <td >0.91 </td>
  <td >0.50 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9349</td>
  <td>andrewBezerra/Xamarin_TODO</td>
  <td>https://github.com/andrewBezerra/Xamarin_TODO/commit/a92efbb40285f32f9c2379d104f565eaceec2a79</td>
  <td >Xamarin_TODO/Xamar
  in_TODO.csproj</td>
  <td>.NETStandard2.0</td>
  <td >268</td>
  <td >12</td>
  <td >2</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >17</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >5</td>
  <td >6</td>
  <td >11</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >-6</td>
  <td >0</td>
  <td >-2</td>
  <td >-2</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9350</td>
  <td>andrewBezerra/Xamarin_TODO</td>
  <td>https://github.com/andrewBezerra/Xamarin_TODO/commit/c4900de11c042d887402fb814686e95177bfbd42</td>
  <td >Xamarin_TODO/Xamar
  in_TODO.csproj</td>
  <td>.NETStandard2.1</td>
  <td >268</td>
  <td >12</td>
  <td >2</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >13</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >5</td>
  <td >6</td>
  <td >11</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >-2</td>
  <td >0</td>
  <td >-2</td>
  <td >-2</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9351</td>
  <td>amzn/ion-hash-dotnet</td>
  <td>https://github.com/amzn/ion-hash-dotnet/commit/883ea8ba96521cfe3017cd496d38121e75fe8844</td>
  <td >Amazon.IonHashDotne
  t.Tests/Amazon.IonHashDotnet.Tests.csproj</td>
  <td>.NETStandard2.0</td>
  <td >141</td>
  <td >10</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >9</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >3</td>
  <td >4</td>
  <td >9</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >-2</td>
  <td >0</td>
  <td >1.00 </td>
  <td >0.60 </td>
  <td >0.60 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9352</td>
  <td>ismaelhamed/akka-cluster-management</td>
  <td>https://github.com/ismaelhamed/akka-cluster-management/commit/7e86e1747ec6ca982ad2eabcfcc20def1bec9ebb</td>
  <td >src/Akka.Cluster.Mana
  gement/Akka.Cluster.Management.csproj</td>
  <td>.NETFramework4.7</td>
  <td >208</td>
  <td >73</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >5</td>
  <td >87</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >5</td>
  <td >86</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.43 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9353</td>
  <td>GeorgeLeithead/LiLo.Lite</td>
  <td>https://github.com/GeorgeLeithead/LiLo.Lite/commit/e5c0dd916515cf4f6f90daa43d72a24f00f5d22c</td>
  <td >Source/LiLo.Lite/LiLo.Li
  te/LiLo.Lite.csproj</td>
  <td>.NETStandard2.1</td>
  <td >383</td>
  <td >19</td>
  <td >1</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >10</td>
  <td >36</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >2</td>
  <td >10</td>
  <td >18</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >2</td>
  <td >0</td>
  <td >-18</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.82 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9354</td>
  <td>SnowSE/project_aspen</td>
  <td>https://github.com/SnowSE/project_aspen/commit/a2e7919e71e3c7d322833e7e30528d45e524de63</td>
  <td >src/aspen/aspen.api/a
  spen.api.csproj</td>
  <td>net5.0</td>
  <td >346</td>
  <td >56</td>
  <td >1</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >8</td>
  <td >54</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >2</td>
  <td >8</td>
  <td >60</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >-2</td>
  <td >2</td>
  <td >1.00 </td>
  <td >0.78 </td>
  <td >0.60 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9355</td>
  <td>onka13/dotnet-core-common</td>
  <td>https://github.com/onka13/dotnet-core-common/commit/34519c3bab2e0d597dd2dea8c039a9c1e7262474</td>
  <td >CoreCommon.Data.Ent
  ityFrameworkBase/CoreCommon.Data.EntityFrameworkBase.csproj</td>
  <td>.NETStandard2.0</td>
  <td >238</td>
  <td >72</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >101</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >4</td>
  <td >6</td>
  <td >96</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >-5</td>
  <td >0</td>
  <td >-4</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.20 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9356</td>
  <td>matand/bankor</td>
  <td>https://github.com/matand/bankor/commit/0c6ecfef9f5e82d86df2520dea3873ed4576c7ca</td>
  <td >src/Bancor.Api/Bancor
  .Api.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >293</td>
  <td >70</td>
  <td >8</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >7</td>
  <td >124</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >5</td>
  <td >7</td>
  <td >117</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >-7</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.75 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9357</td>
  <td>ncosentino/ProjectXyz</td>
  <td>https://github.com/ncosentino/ProjectXyz/commit/37095f676c6f072611a14677fd003c434e2577e3</td>
  <td >ProjectXyz.Framework.
  Tests/ProjectXyz.Framework.Tests.csproj</td>
  <td>.NETFramework4.8</td>
  <td >360</td>
  <td >13</td>
  <td >1</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >13</td>
  <td >13</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >13</td>
  <td >13</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >7</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0.86 </td>
  <td >0.86 </td>
  <td >0.86 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9358</td>
  <td>ApexPredator13/Nldb3</td>
  <td>https://github.com/ApexPredator13/Nldb3/commit/8004288c7d0f7f551c184ec6ad073e7c78ee1808</td>
  <td >tests/WebsiteTests/W
  ebsiteTests.csproj</td>
  <td>net5.0</td>
  <td >272</td>
  <td >92</td>
  <td >2</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >9</td>
  <td >84</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >7</td>
  <td >9</td>
  <td >82</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >-2</td>
  <td >0</td>
  <td >-1</td>
  <td >-2</td>
  <td >0.71 </td>
  <td >0.50 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9359</td>
  <td>guigomesa/ScrapyTibiaCSharp</td>
  <td>https://github.com/guigomesa/ScrapyTibiaCSharp/commit/b7f6c6908b7faca54f6e9f1269f88424a6ca41ba</td>
  <td >TibiaApi.Database/Tibi
  aApi.Database.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >402</td>
  <td >57</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >7</td>
  <td >97</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >4</td>
  <td >7</td>
  <td >97</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >-1</td>
  <td >-1</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.56 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9360</td>
  <td>xclemence/Dependencies.Viewer</td>
  <td>https://github.com/xclemence/Dependencies.Viewer/commit/250e2ad8976a6ec6205ef6aa96dcaf3e8acf1cd7</td>
  <td >src/Dependencies.Vie
  wer.Wpf.App/Dependencies.Viewer.Wpf.App.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >182</td>
  <td >7</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >13</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >3</td>
  <td >6</td>
  <td >68</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >55</td>
  <td >0</td>
  <td >-2</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.71 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9361</td>
  <td>xclemence/Dependencies.Viewer</td>
  <td>https://github.com/xclemence/Dependencies.Viewer/commit/250e2ad8976a6ec6205ef6aa96dcaf3e8acf1cd7</td>
  <td >src/Dependencies.Vie
  wer.Wpf.Controls/Dependencies.Viewer.Wpf.Controls.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >118</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >2</td>
  <td >4</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >-1</td>
  <td >-1</td>
  <td >0.50 </td>
  <td >0.50 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9362</td>
  <td>mattiasnordqvist/Galactic-Waste-Management</td>
  <td>https://github.com/mattiasnordqvist/Galactic-Waste-Management/commit/3d90c7032fde36f322fea3ae80e50a07b6fcc8bc</td>
  <td >GalacticWasteManage
  ment/GalacticWasteManagement.csproj</td>
  <td>.NETStandard2.0</td>
  <td >274</td>
  <td >89</td>
  <td >1</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >9</td>
  <td >46</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >7</td>
  <td >10</td>
  <td >45</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >-3</td>
  <td >-1</td>
  <td >0.90 </td>
  <td >0.90 </td>
  <td >0.73 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9363</td>
  <td>VPKSoft/amp</td>
  <td>https://github.com/VPKSoft/amp/commit/b443ff9c4553fdb85ee06fcc5933c636fad4c137</td>
  <td >amp/amp.csproj</td>
  <td>.NETFramework4.7.2</td>
  <td >806</td>
  <td >37</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >27</td>
  <td >36</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >27</td>
  <td >36</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.86 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9364</td>
  <td>blackducksoftware/blackduck-nuget-inspector</td>
  <td>https://github.com/blackducksoftware/blackduck-nuget-inspector/commit/be1b95247c1444c7585611223e60c9a7520b33d6</td>
  <td >BlackduckNugetInspec
  tor/BlackduckNugetInspector.csproj</td>
  <td>.NETCoreApp2.0</td>
  <td >181</td>
  <td >13</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >6</td>
  <td >86</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >5</td>
  <td >6</td>
  <td >102</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >16</td>
  <td >0</td>
  <td >-2</td>
  <td >1</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.71 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9365</td>
  <td>doghappy/HappyDog</td>
  <td>https://github.com/doghappy/HappyDog/commit/99c269133f93f97275225f9ea76dbea4a44052ee</td>
  <td >HappyDog.Console.Api
  /HappyDog.Console.Api.csproj</td>
  <td>net5.0</td>
  <td >247</td>
  <td >122</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >5</td>
  <td >132</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >4</td>
  <td >5</td>
  <td >130</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >-2</td>
  <td >0</td>
  <td >-1</td>
  <td >-1</td>
  <td >1.00 </td>
  <td >0.67 </td>
  <td >0.43 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9366</td>
  <td>doghappy/HappyDog</td>
  <td>https://github.com/doghappy/HappyDog/commit/99c269133f93f97275225f9ea76dbea4a44052ee</td>
  <td >HappyDog.WebUI/Hap
  pyDog.WebUI.csproj</td>
  <td>net5.0</td>
  <td >432</td>
  <td >159</td>
  <td >1</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >10</td>
  <td >158</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >8</td>
  <td >10</td>
  <td >153</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >7</td>
  <td >0</td>
  <td >-5</td>
  <td >0</td>
  <td >-1</td>
  <td >-1</td>
  <td >1.00 </td>
  <td >0.82 </td>
  <td >0.43 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9367</td>
  <td>mateanticevic/ProjectIvy.Api</td>
  <td>https://github.com/mateanticevic/ProjectIvy.Api/commit/c18daa8a0bc0b26025f56b35f9366be6bd21052f</td>
  <td >src/ProjectIvy.Api/Proj
  ectIvy.Api.csproj</td>
  <td>net5.0</td>
  <td >341</td>
  <td >105</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >6</td>
  <td >109</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >5</td>
  <td >6</td>
  <td >47</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >-62</td>
  <td >0</td>
  <td >-1</td>
  <td >-1</td>
  <td >1.00 </td>
  <td >0.71 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9368</td>
  <td>Everwealth/ETLBox</td>
  <td>https://github.com/Everwealth/ETLBox/commit/e52d15ae7309b5d2918c698049796f6d562f4650</td>
  <td >ETLBox/ETLBox.csproj</td>
  <td>.NETStandard2.0</td>
  <td >413</td>
  <td >13</td>
  <td >0</td>
  <td >0</td>
  <td >8</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >13</td>
  <td >119</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >11</td>
  <td >13</td>
  <td >95</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >10</td>
  <td >0</td>
  <td >-24</td>
  <td >0</td>
  <td >-1</td>
  <td >-1</td>
  <td >0.91 </td>
  <td >0.75 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9369</td>
  <td>Everwealth/ETLBox</td>
  <td>https://github.com/Everwealth/ETLBox/commit/fe3e81fea2b3ddec67eb49190a573aec22be3dbf</td>
  <td >ETLBox/ETLBox.csproj</td>
  <td>.NETStandard2.0</td>
  <td >413</td>
  <td >13</td>
  <td >0</td>
  <td >0</td>
  <td >8</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >13</td>
  <td >119</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >11</td>
  <td >13</td>
  <td >95</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >10</td>
  <td >0</td>
  <td >-24</td>
  <td >0</td>
  <td >-1</td>
  <td >-1</td>
  <td >0.91 </td>
  <td >0.75 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9370</td>
  <td>SimplerSoftware/IBM.IAM.AWS</td>
  <td>https://github.com/SimplerSoftware/IBM.IAM.AWS/commit/75fa7783e3cd2573a94e62294d13d2788271efdc</td>
  <td >IBM.IAM.AWS.Security
  Token/IBM.IAM.AWS.SecurityToken.csproj</td>
  <td>.NETStandard2.0</td>
  <td >217</td>
  <td >6</td>
  <td >2</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >5</td>
  <td >34</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >4</td>
  <td >6</td>
  <td >35</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >4</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0.60 </td>
  <td >0.60 </td>
  <td >0.60 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9371</td>
  <td>musgrosoft/OLD-v1-Health.API</td>
  <td>https://github.com/musgrosoft/OLD-v1-Health.API/commit/26a174623221cc7cafaba36c2aa9f4ffb1a31f42</td>
  <td >src/Repositories/Repos
  itories.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >255</td>
  <td >33</td>
  <td >2</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >7</td>
  <td >65</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >5</td>
  <td >7</td>
  <td >58</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >5</td>
  <td >0</td>
  <td >-7</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1.00 </td>
  <td >0.75 </td>
  <td >0.40 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9372</td>
  <td>pkozak2/Esp8266VueMeteoStation</td>
  <td>https://github.com/pkozak2/Esp8266VueMeteoStation/commit/902cc94be330c0b8cef4c3474ba230d69b6feb22</td>
  <td >ApiAndWeb/Esp8266V
  ueMeteo/Esp8266VueMeteo.csproj</td>
  <td>.NETCoreApp2.2</td>
  <td >313</td>
  <td >8</td>
  <td >0</td>
  <td >0</td>
  <td >7</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >178</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >5</td>
  <td >3</td>
  <td >26</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >-152</td>
  <td >0</td>
  <td >-5</td>
  <td >-3</td>
  <td >0.60 </td>
  <td >0.60 </td>
  <td >0.00 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9373</td>
  <td>rolfwessels/CoreDocker</td>
  <td>https://github.com/rolfwessels/CoreDocker/commit/39d24c9cde526d5195e464c982c8a1362c23cd6f</td>
  <td >src/CoreDocker.Api/Co
  reDocker.Api.csproj</td>
  <td>.NETCoreApp2.0</td>
  <td >617</td>
  <td >163</td>
  <td >4</td>
  <td >0</td>
  <td >11</td>
  <td >0</td>
  <td >11</td>
  <td >0</td>
  <td >13</td>
  <td >163</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >7</td>
  <td >10</td>
  <td >13</td>
  <td >165</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >11</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >-7</td>
  <td >1</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.86 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9374</td>
  <td>rolfwessels/CoreDocker</td>
  <td>https://github.com/rolfwessels/CoreDocker/commit/16c2907b44b9a95839a98b1940f4e0dd057139ad</td>
  <td >src/CoreDocker.Api/Co
  reDocker.Api.csproj</td>
  <td>.NETCoreApp2.0</td>
  <td >617</td>
  <td >163</td>
  <td >4</td>
  <td >0</td>
  <td >11</td>
  <td >0</td>
  <td >11</td>
  <td >0</td>
  <td >13</td>
  <td >163</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >7</td>
  <td >10</td>
  <td >13</td>
  <td >165</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >11</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >-7</td>
  <td >1</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.86 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9375</td>
  <td>countincognito/Zametek.Logging</td>
  <td>https://github.com/countincognito/Zametek.Logging/commit/832b29c744583f610533679e63f0824641170c57</td>
  <td >src/Zametek.Utility.Lo
  gging/Zametek.Utility.Logging.csproj</td>
  <td>.NETStandard1.4</td>
  <td >195</td>
  <td >34</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >6</td>
  <td >79</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >5</td>
  <td >6</td>
  <td >90</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >5</td>
  <td >0</td>
  <td >11</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >1.00 </td>
  <td >0.71 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9376</td>
  <td>d-avko/Vibechat.Core</td>
  <td>https://github.com/d-avko/Vibechat.Core/commit/3824a57b93dc6eedc1a1ba069c27005731da0849</td>
  <td >Vibechat.Web/Vibecha
  t.Web/Vibechat.Web.csproj</td>
  <td>.NETCoreApp2.2</td>
  <td >831</td>
  <td >100</td>
  <td >0</td>
  <td >0</td>
  <td >9</td>
  <td >0</td>
  <td >13</td>
  <td >0</td>
  <td >16</td>
  <td >143</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >9</td>
  <td >12</td>
  <td >12</td>
  <td >193</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >11</td>
  <td >0</td>
  <td >50</td>
  <td >0</td>
  <td >-9</td>
  <td >-1</td>
  <td >0.87 </td>
  <td >0.56 </td>
  <td >0.33 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9377</td>
  <td>coenm/VersionedPdfGenerator</td>
  <td>https://github.com/coenm/VersionedPdfGenerator/commit/a130ed3b7885226b05f2257e805f0a8b6e1315d2</td>
  <td >src/PdfGenerator/PdfG
  enerator.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >145</td>
  <td >5</td>
  <td >4</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >6</td>
  <td >67</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >4</td>
  <td >5</td>
  <td >67</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >1.00 </td>
  <td >0.60 </td>
  <td >0.60 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9378</td>
  <td>howesdomo/XamarinTestSolution</td>
  <td>https://github.com/howesdomo/XamarinTestSolution/commit/f56bb22477b296b2a0c80cb5085882b56193d310</td>
  <td >Client/Client/Client.csp
  roj</td>
  <td>.NETStandard2.1</td>
  <td >552</td>
  <td >18</td>
  <td >1</td>
  <td >0</td>
  <td >12</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >13</td>
  <td >45</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >9</td>
  <td >13</td>
  <td >23</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >9</td>
  <td >0</td>
  <td >-22</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.80 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9379</td>
  <td>nikkilocke/CodeFirstWebFramework</td>
  <td>https://github.com/nikkilocke/CodeFirstWebFramework/commit/819c528bb41740090fae4fc6813250fbc17c6fe1</td>
  <td >CodeFirstWebFramew
  ork.csproj</td>
  <td>.NETStandard2.0</td>
  <td >136</td>
  <td >76</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >76</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >6</td>
  <td >76</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0.50 </td>
  <td >0.50 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9380</td>
  <td>jthelin/HelloOwin</td>
  <td>https://github.com/jthelin/HelloOwin/commit/3a88e85e9f14b1f8ed101e6de28e38b4255715f5</td>
  <td >HelloOwinTests/Hello
  OwinTests.csproj</td>
  <td>.NETFramework4.7</td>
  <td >280</td>
  <td >11</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >10</td>
  <td >11</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >2</td>
  <td >10</td>
  <td >11</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >-1</td>
  <td >1</td>
  <td >1.00 </td>
  <td >0.82 </td>
  <td >0.67 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9381</td>
  <td>SoluiNet/SoluiNet.DevTools</td>
  <td>https://github.com/SoluiNet/SoluiNet.DevTools/commit/41ac48a607dfed0ca0f662e64ad36d36f9a804d2</td>
  <td >SoluiNet.DevTools.Cor
  e/SoluiNet.DevTools.Core.csproj</td>
  <td>.NETFramework4.7.2</td>
  <td >513</td>
  <td >23</td>
  <td >2</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >16</td>
  <td >56</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >16</td>
  <td >56</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.68 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9382</td>
  <td>pact-foundation/pact-net</td>
  <td>https://github.com/pact-foundation/pact-net/commit/130d8b97a4aa28dd2b9361e22e51d836005ea825</td>
  <td >Samples/EventApi/Con
  sumer.Tests/Consumer.Tests.csproj</td>
  <td>.NETFramework4.6</td>
  <td >182</td>
  <td >6</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >7</td>
  <td >7</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >6</td>
  <td >6</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0.60 </td>
  <td >0.60 </td>
  <td >0.60 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9383</td>
  <td>madslundt/NetCoreMicroservicesSample</td>
  <td>https://github.com/madslundt/NetCoreMicroservicesSample/commit/d078dae8578aa9b791d36465d798c7dd53a4e355</td>
  <td >Src/MessagesService/
  MessagesService/MessagesService.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >731</td>
  <td >120</td>
  <td >17</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >15</td>
  <td >116</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >14</td>
  <td >15</td>
  <td >119</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >11</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >-1</td>
  <td >-3</td>
  <td >1.00 </td>
  <td >0.88 </td>
  <td >0.58 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9384</td>
  <td>madslundt/NetCoreMicroservicesSample</td>
  <td>https://github.com/madslundt/NetCoreMicroservicesSample/commit/d078dae8578aa9b791d36465d798c7dd53a4e355</td>
  <td >Src/UsersService/Users
  Service/UsersService.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >924</td>
  <td >166</td>
  <td >18</td>
  <td >0</td>
  <td >7</td>
  <td >0</td>
  <td >10</td>
  <td >0</td>
  <td >19</td>
  <td >154</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >18</td>
  <td >19</td>
  <td >152</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >17</td>
  <td >0</td>
  <td >-2</td>
  <td >0</td>
  <td >-2</td>
  <td >-1</td>
  <td >1.00 </td>
  <td >0.90 </td>
  <td >0.46 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9385</td>
  <td>micro-elements/MicroElements.Swashbuckle.FluentValidation</td>
  <td>https://github.com/micro-elements/MicroElements.Swashbuckle.FluentValidation/commit/e000b3d21bf7bbd15c7e30da1df02495152db202</td>
  <td >samples/SampleWebA
  pi/SampleWebApi.csproj</td>
  <td>.NETCoreApp3.0</td>
  <td >190</td>
  <td >241</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >5</td>
  <td >272</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >5</td>
  <td >269</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >-3</td>
  <td >0</td>
  <td >0</td>
  <td >-1</td>
  <td >0.80 </td>
  <td >0.80 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9386</td>
  <td>bitfoundation/ToDoLine</td>
  <td>https://github.com/bitfoundation/ToDoLine/commit/f544da435035322ed631a3c9fe350a048bc20b79</td>
  <td >App/ToDoLineApp/To
  DoLineApp.csproj</td>
  <td>.NETStandard2.0</td>
  <td >386</td>
  <td >96</td>
  <td >4</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >11</td>
  <td >109</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >10</td>
  <td >11</td>
  <td >61</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >11</td>
  <td >0</td>
  <td >-48</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0.91 </td>
  <td >0.91 </td>
  <td >0.91 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9387</td>
  <td>ysmoradi/XamApp</td>
  <td>https://github.com/ysmoradi/XamApp/commit/e346f26aa84d1f5987e1142e0cd062f8f0530bd0</td>
  <td >src/XamApp/XamApp.
  csproj</td>
  <td>.NETStandard2.0</td>
  <td >369</td>
  <td >105</td>
  <td >5</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >11</td>
  <td >108</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >9</td>
  <td >11</td>
  <td >108</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >9</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0.80 </td>
  <td >0.64 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9388</td>
  <td>xerris/Xerris.DotNet.Core.Aws</td>
  <td>https://github.com/xerris/Xerris.DotNet.Core.Aws/commit/02a700e28ea1eac673b09d229d8bb788c0088e2b</td>
  <td >src/Xerris.DotNet.Core
  .Aws/Xerris.DotNet.Core.Aws.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >441</td>
  <td >91</td>
  <td >4</td>
  <td >0</td>
  <td >8</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >13</td>
  <td >91</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >9</td>
  <td >13</td>
  <td >91</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >8</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >-1</td>
  <td >-1</td>
  <td >0.89 </td>
  <td >0.89 </td>
  <td >0.70 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9389</td>
  <td>VirtoCommerce/vc-module-cart</td>
  <td>https://github.com/VirtoCommerce/vc-module-cart/commit/e6126d6c7ed0cef2731bb6536b8bad37e4dc2e7b</td>
  <td >src/VirtoCommerce.Ca
  rtModule.Data/VirtoCommerce.CartModule.Data.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >190</td>
  <td >192</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >6</td>
  <td >80</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >6</td>
  <td >6</td>
  <td >125</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >6</td>
  <td >0</td>
  <td >45</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1.00 </td>
  <td >0.50 </td>
  <td >0.33 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9390</td>
  <td>VirtoCommerce/vc-module-inventory</td>
  <td>https://github.com/VirtoCommerce/vc-module-inventory/commit/5639dae5c24d737f76f4a4f390b99762349d7f53</td>
  <td >src/VirtoCommerce.Inv
  entoryModule.Data/VirtoCommerce.InventoryModule.Data.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >299</td>
  <td >207</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >8</td>
  <td >163</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >8</td>
  <td >8</td>
  <td >126</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >8</td>
  <td >0</td>
  <td >-37</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1.00 </td>
  <td >0.60 </td>
  <td >0.60 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9391</td>
  <td>VirtoCommerce/vc-module-image-tools</td>
  <td>https://github.com/VirtoCommerce/vc-module-image-tools/commit/de7720a3e16b855c2912a38f5dfea20644a9b524</td>
  <td >src/VirtoCommerce.Im
  ageToolsModule.Data/VirtoCommerce.ImageToolsModule.Data.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >213</td>
  <td >195</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >5</td>
  <td >71</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >5</td>
  <td >5</td>
  <td >116</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >5</td>
  <td >0</td>
  <td >45</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.25 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9392</td>
  <td>VirtoCommerce/vc-module-store</td>
  <td>https://github.com/VirtoCommerce/vc-module-store/commit/e8145caab6adf6f7f8b2426670bc898ce2fc0a02</td>
  <td >src/VirtoCommerce.St
  oreModule.Data/VirtoCommerce.StoreModule.Data.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >308</td>
  <td >218</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >9</td>
  <td >203</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >8</td>
  <td >9</td>
  <td >183</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >9</td>
  <td >0</td>
  <td >-20</td>
  <td >0</td>
  <td >-1</td>
  <td >1</td>
  <td >0.89 </td>
  <td >0.55 </td>
  <td >0.55 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9393</td>
  <td>VirtoCommerce/vc-module-pricing</td>
  <td>https://github.com/VirtoCommerce/vc-module-pricing/commit/088d12cf6c08aa2dc168fed9099a0000b04cd394</td>
  <td >src/VirtoCommerce.Pri
  cingModule.Data/VirtoCommerce.PricingModule.Data.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >572</td>
  <td >234</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >10</td>
  <td >0</td>
  <td >14</td>
  <td >211</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >13</td>
  <td >14</td>
  <td >191</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >14</td>
  <td >0</td>
  <td >-20</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0.93 </td>
  <td >0.69 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9394</td>
  <td>MattRyder/LifeCMS</td>
  <td>https://github.com/MattRyder/LifeCMS/commit/877a4ef726f7105b2748d8678e71570d2898b913</td>
  <td >src/Services/ContentCr
  eation/ContentCreation.Infrastructure/ContentCreation.Infrastructure.csproj</td>
  <td>net5.0</td>
  <td >581</td>
  <td >132</td>
  <td >1</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >14</td>
  <td >155</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >11</td>
  <td >14</td>
  <td >160</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >10</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >-2</td>
  <td >-1</td>
  <td >1.00 </td>
  <td >0.87 </td>
  <td >0.65 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9395</td>
  <td>microsoft/TailwindTraders-Mobile</td>
  <td>https://github.com/microsoft/TailwindTraders-Mobile/commit/88d7671659be19e699b87347ea1fc17e41b2dff6</td>
  <td >Source/TailwindTrader
  s.Mobile/TailwindTraders.Mobile/TailwindTraders.Mobile.csproj</td>
  <td>.NETStandard2.0</td>
  <td >434</td>
  <td >16</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >13</td>
  <td >18</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >11</td>
  <td >13</td>
  <td >69</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >11</td>
  <td >0</td>
  <td >51</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.86 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9396</td>
  <td>RickStrahl/Westwind.Globalization</td>
  <td>https://github.com/RickStrahl/Westwind.Globalization/commit/554ff2592d66c7f5fa3547d9691202085b73ee2a</td>
  <td >src/NetCore/Westwind
  .Globalization.Test.NetCore/Westwind.Globalization.Test.NetCore.csproj</td>
  <td>.NETCoreApp2.0</td>
  <td >177</td>
  <td >93</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >7</td>
  <td >52</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >7</td>
  <td >7</td>
  <td >71</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >19</td>
  <td >0</td>
  <td >-3</td>
  <td >-2</td>
  <td >1.00 </td>
  <td >0.56 </td>
  <td >0.40 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9397</td>
  <td>daniellittledev/Enexure.MicroBus</td>
  <td>https://github.com/daniellittledev/Enexure.MicroBus/commit/18a42c4eae6bf53d6b74bd62b5580181499b5414</td>
  <td >src/Enexure.MicroBus.
  Saga.Autofac.Tests/Enexure.MicroBus.Saga.Autofac.Tests.csproj</td>
  <td>.NETCoreApp2.0</td>
  <td >151</td>
  <td >74</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >5</td>
  <td >73</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >5</td>
  <td >66</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >-7</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.43 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9398</td>
  <td>DynamicHands/NodaMoney</td>
  <td>https://github.com/DynamicHands/NodaMoney/commit/0cc1b64e32e64bd04a3d4d00ec046e3eeb5f5eed</td>
  <td >tests/NodaMoney.Seri
  alization.AspNet.Tests/NodaMoney.Serialization.AspNet.Tests.csproj</td>
  <td>.NETFramework4.5.2</td>
  <td >155</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >5</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >5</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >-1</td>
  <td >0.80 </td>
  <td >0.80 </td>
  <td >0.80 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9399</td>
  <td>DynamicHands/NodaMoney</td>
  <td>https://github.com/DynamicHands/NodaMoney/commit/0cc1b64e32e64bd04a3d4d00ec046e3eeb5f5eed</td>
  <td >tests/NodaMoney.Test
  s/NodaMoney.Tests.csproj</td>
  <td>.NETFramework4.6.2</td>
  <td >185</td>
  <td >6</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >6</td>
  <td >6</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >6</td>
  <td >6</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >-1</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9400</td>
  <td>NikolayIT/MusicX</td>
  <td>https://github.com/NikolayIT/MusicX/commit/89a68ffac5ca9a76efb594a14db03699cb9b7e05</td>
  <td >src/Tests/Sandbox/San
  dbox.csproj</td>
  <td>.NETCoreApp3.0</td>
  <td >262</td>
  <td >27</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >6</td>
  <td >84</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >6</td>
  <td >6</td>
  <td >83</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >1.00 </td>
  <td >0.71 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9401</td>
  <td>SharebookBR/sharebook-backend</td>
  <td>https://github.com/SharebookBR/sharebook-backend/commit/9b6e87d57feb5e6d0bfda6323a7f9cd7a3b2be21</td>
  <td >ShareBook/ShareBook.
  Tests.BDD/ShareBook.Tests.BDD.csproj</td>
  <td>net5.0</td>
  <td >210</td>
  <td >78</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >7</td>
  <td >45</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >7</td>
  <td >44</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >0</td>
  <td >-1</td>
  <td >0.83 </td>
  <td >0.83 </td>
  <td >0.83 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9402</td>
  <td>damienbod/AspNetCoreWindowsAuth</td>
  <td>https://github.com/damienbod/AspNetCoreWindowsAuth/commit/fc7caf370af8d2070fb73d266771b8d4f2c7b8a8</td>
  <td >MvcHybridClient/Mvc
  HybridClient.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >487</td>
  <td >56</td>
  <td >10</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >11</td>
  <td >82</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >10</td>
  <td >11</td>
  <td >87</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >8</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >-2</td>
  <td >0.80 </td>
  <td >0.80 </td>
  <td >0.80 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9403</td>
  <td>alanedwardes/Estranged.Lfs</td>
  <td>https://github.com/alanedwardes/Estranged.Lfs/commit/c429933cbda081d28b12c28fef1b88f33fc96319</td>
  <td >hosting/Estranged.Lfs.
  Hosting.Lambda/Estranged.Lfs.Hosting.Lambda.csproj</td>
  <td>.NETCoreApp2.1</td>
  <td >678</td>
  <td >168</td>
  <td >6</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >16</td>
  <td >125</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >12</td>
  <td >16</td>
  <td >16</td>
  <td >175</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >10</td>
  <td >16</td>
  <td >0</td>
  <td >50</td>
  <td >0</td>
  <td >-2</td>
  <td >0</td>
  <td >1.00 </td>
  <td >0.68 </td>
  <td >0.52 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9404</td>
  <td>dapplo/Dapplo.Jira</td>
  <td>https://github.com/dapplo/Dapplo.Jira/commit/bd18c9717aa57f68c93735d00c7869744aa346bf</td>
  <td >src/Dapplo.Jira.Tests/D
  applo.Jira.Tests.csproj</td>
  <td>.NETFramework4.7.1</td>
  <td >192</td>
  <td >26</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >7</td>
  <td >26</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >7</td>
  <td >24</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >-2</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9405</td>
  <td>Lakritzator/Pip</td>
  <td>https://github.com/Lakritzator/Pip/commit/9816801321f8aa128d8664f3d366a66935d8772f</td>
  <td >src/Pip/Pip.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >574</td>
  <td >47</td>
  <td >8</td>
  <td >0</td>
  <td >9</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >18</td>
  <td >48</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >18</td>
  <td >18</td>
  <td >49</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >15</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >-3</td>
  <td >0.83 </td>
  <td >0.74 </td>
  <td >0.57 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9406</td>
  <td>dapplo/Dapplo.Confluence</td>
  <td>https://github.com/dapplo/Dapplo.Confluence/commit/4804bc91e4eb8f1c2894a5ea5d12c3d38ff3bb02</td>
  <td >src/Dapplo.Confluence
  .Tests/Dapplo.Confluence.Tests.csproj</td>
  <td>.NETFramework4.7.1</td>
  <td >250</td>
  <td >28</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >9</td>
  <td >26</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >7</td>
  <td >9</td>
  <td >26</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >7</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.56 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9407</td>
  <td>easyquery/AspNetCoreSamples</td>
  <td>https://github.com/easyquery/DotNetSamples/commit/2aa7e142cc063dfdeadeeb1c2357b324c6d08dba</td>
  <td >AspNetCore/Razor-Mv
  c/Razor.AdvancedSearch/EqDemo.AspNetCoreRazor.AdvancedSearch.csproj</td>
  <td>net5.0</td>
  <td >485</td>
  <td >195</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >9</td>
  <td >202</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >9</td>
  <td >202</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >-1</td>
  <td >0.83 </td>
  <td >0.83 </td>
  <td >0.83 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9408</td>
  <td>easyquery/AspNetCoreSamples</td>
  <td>https://github.com/easyquery/DotNetSamples/commit/2aa7e142cc063dfdeadeeb1c2357b324c6d08dba</td>
  <td >AspNetCore/Razor-Mv
  c/RazorTypeScript.AdHocReporting/EqDemo.AspNetCoreRazorTypeScript.AdhocReporting.csproj</td>
  <td>net5.0</td>
  <td >500</td>
  <td >195</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >9</td>
  <td >202</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >9</td>
  <td >202</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >7</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0.86 </td>
  <td >0.86 </td>
  <td >0.63 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9409</td>
  <td>itinero/OpenLR</td>
  <td>https://github.com/itinero/OpenLR/commit/80e6ad22b00521daffe3b395e7b88ce26f55544c</td>
  <td >test/OpenLR.Test/Ope
  nLR.Test.csproj</td>
  <td>.NETFramework4.5.1</td>
  <td >118</td>
  <td >6</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >6</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >2</td>
  <td >5</td>
  <td >6</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >-1</td>
  <td >2</td>
  <td >1.00 </td>
  <td >0.67 </td>
  <td >0.67 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9410</td>
  <td>brminnick/XamarinIoTWorkshop</td>
  <td>https://github.com/brminnick/XamarinIoTWorkshop/commit/7e72e5644392540673be89dc653e153d9f657348</td>
  <td >Source/XamarinIoTWo
  rkshop/XamarinIoTWorkshop.csproj</td>
  <td>.NETStandard2.1</td>
  <td >370</td>
  <td >12</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >8</td>
  <td >41</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >8</td>
  <td >8</td>
  <td >43</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >-3</td>
  <td >-3</td>
  <td >1.00 </td>
  <td >0.78 </td>
  <td >0.78 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9411</td>
  <td>froko/SimpleDomain</td>
  <td>https://github.com/froko/SimpleDomain/commit/e53ea93a1bf85125c8804d704457dd4bc8400392</td>
  <td >src/SimpleDomain.MS
  MQ.Facts/SimpleDomain.MSMQ.Facts.csproj</td>
  <td>.NETFramework4.6.1</td>
  <td >165</td>
  <td >8</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >9</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >5</td>
  <td >6</td>
  <td >8</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >-1</td>
  <td >-1</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.71 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9412</td>
  <td>rookxx/StyleCopAnalyzers.CLI</td>
  <td>https://github.com/rookxx/StyleCopAnalyzers.CLI/commit/aa5986a48e6971613f48b823f4ab3856fe715377</td>
  <td >src/StyleCopAnalyzers.
  CLI.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >349</td>
  <td >71</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >9</td>
  <td >88</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >8</td>
  <td >9</td>
  <td >21</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >5</td>
  <td >0</td>
  <td >-67</td>
  <td >0</td>
  <td >-3</td>
  <td >-3</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9413</td>
  <td>rookxx/StyleCopAnalyzers.CLI</td>
  <td>https://github.com/rookxx/StyleCopAnalyzers.CLI/commit/2f27891270ff9ce757817d7d91a41c83166887c5</td>
  <td >src/StyleCopAnalyzers.
  CLI.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >349</td>
  <td >71</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >9</td>
  <td >88</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >8</td>
  <td >9</td>
  <td >21</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >5</td>
  <td >0</td>
  <td >-67</td>
  <td >0</td>
  <td >-3</td>
  <td >-3</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9414</td>
  <td>Azure/dedicated-hosts-manager</td>
  <td>https://github.com/Azure/dedicated-hosts-manager/commit/a08067e1d60bf95f9d252ca4b656ae1d34fb5299</td>
  <td >DedicatedHostsTests/
  DedicatedHostsManagerTests.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >137</td>
  <td >97</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >6</td>
  <td >78</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >6</td>
  <td >6</td>
  <td >93</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >15</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9415</td>
  <td>aws-quickstart/connect-integration-aspect-wfm</td>
  <td>https://github.com/aws-quickstart/connect-integration-aspect-wfm/commit/1eb29a7e876be6f2d2d6fc858e03552fe90f99b3</td>
  <td >functions/source/real-
  time-adherence/AspectKinesisLamda.Tests/AspectKinesisLamda.Tests.csproj</td>
  <td>.NETCoreApp2.1</td>
  <td >213</td>
  <td >70</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >8</td>
  <td >100</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >8</td>
  <td >8</td>
  <td >9</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >-91</td>
  <td >0</td>
  <td >-1</td>
  <td >-3</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.78 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9416</td>
  <td>aws-quickstart/connect-integration-aspect-wfm</td>
  <td>https://github.com/aws-quickstart/connect-integration-aspect-wfm/commit/1d49797b5c57e8393cdf6670db864126eec890f3</td>
  <td >functions/source/real-
  time-adherence/AspectKinesisLamda.Tests/AspectKinesisLamda.Tests.csproj</td>
  <td>.NETCoreApp2.1</td>
  <td >213</td>
  <td >70</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >8</td>
  <td >100</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >8</td>
  <td >8</td>
  <td >9</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >-91</td>
  <td >0</td>
  <td >-1</td>
  <td >-3</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.78 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9417</td>
  <td>Ontica/Empiria.Extensions</td>
  <td>https://github.com/Ontica/Empiria.Extensions/commit/79612b758a5eca3f7b931956c3b465e5e41bacaa</td>
  <td >Messaging.Tests/Empi
  ria.Messaging.Tests.csproj</td>
  <td>.NETFramework4.8</td>
  <td >299</td>
  <td >12</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >11</td>
  <td >12</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >11</td>
  <td >11</td>
  <td >12</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >8</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >-2</td>
  <td >-3</td>
  <td >0.73 </td>
  <td >0.58 </td>
  <td >0.58 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9418</td>
  <td>Ontica/Empiria.Extensions</td>
  <td>https://github.com/Ontica/Empiria.Extensions/commit/79612b758a5eca3f7b931956c3b465e5e41bacaa</td>
  <td >WebApi.Client.Tests/E
  mpiria.WebApi.Client.Tests.csproj</td>
  <td>.NETFramework4.8</td>
  <td >299</td>
  <td >12</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >11</td>
  <td >12</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >11</td>
  <td >11</td>
  <td >12</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >8</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >-2</td>
  <td >-3</td>
  <td >0.73 </td>
  <td >0.58 </td>
  <td >0.58 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9419</td>
  <td>punker76/Popcorn</td>
  <td>https://github.com/punker76/Popcorn/commit/f18f00a140ca145452fd92e2ad93796d06edbed6</td>
  <td >Popcorn/Popcorn.cspr
  oj</td>
  <td>.NETCoreApp3.1</td>
  <td >2309</td>
  <td >154</td>
  <td >0</td>
  <td >0</td>
  <td >20</td>
  <td >0</td>
  <td >8</td>
  <td >0</td>
  <td >73</td>
  <td >183</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >12</td>
  <td >50</td>
  <td >73</td>
  <td >188</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >9</td>
  <td >50</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >-3</td>
  <td >0</td>
  <td >1.00 </td>
  <td >0.97 </td>
  <td >0.76 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9420</td>
  <td>LBHackney-IT/document-api</td>
  <td>https://github.com/LBHackney-IT/document-api/commit/d3c8a31237cf16c9fc05b099a2f19f98feb3f684</td>
  <td >document-api.Tests/d
  ocument-api.Tests.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >193</td>
  <td >104</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >8</td>
  <td >36</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >6</td>
  <td >8</td>
  <td >72</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >6</td>
  <td >0</td>
  <td >36</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >1.00 </td>
  <td >0.50 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9421</td>
  <td>JustinWilkinson/Cryptonyms</td>
  <td>https://github.com/JustinWilkinson/Cryptonyms/commit/3682d340455adebf5e69114a96100db4cf798ce6</td>
  <td >Server/Cryptonyms.Ser
  ver.csproj</td>
  <td>net5.0</td>
  <td >363</td>
  <td >91</td>
  <td >1</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >10</td>
  <td >41</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >8</td>
  <td >10</td>
  <td >34</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >7</td>
  <td >0</td>
  <td >-7</td>
  <td >0</td>
  <td >0</td>
  <td >-1</td>
  <td >0.67 </td>
  <td >0.67 </td>
  <td >0.67 </td>
  <td ></td>
 </tr>
 <tr >
  <td >9422</td>
  <td>MechaDragonX/Majora</td>
  <td>https://github.com/MechaDragonX/Majora/commit/d9d1fb96d53a60c6bbc77edd6468bb6ecd10abc9</td>
  <td >Majora.Desktop/Major
  a.Desktop.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >225</td>
  <td >142</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >8</td>
  <td >45</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >5</td>
  <td >8</td>
  <td >45</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >6</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0.57 </td>
  <td >0.57 </td>
  <td >0.57 </td>
  <td ></td>
 </tr>
 <tr >
  <td >10001</td>
  <td>fals/cqrs-clean-eventual-consistency</td>
  <td>https://github.com/fals/cqrs-clean-eventual-consistency/commit/0869f8e40bace5492202bc2d819a00d1e1195487</td>
  <td >src/Ametista.Api/Amet
  ista.Api.csproj</td>
  <td>.NETCoreApp3.0</td>
  <td >8</td>
  <td >278</td>
  <td >4</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >40</td>
  <td >0</td>
  <td >4</td>
  <td >1</td>
  <td >6</td>
  <td >7</td>
  <td >15</td>
  <td >36</td>
  <td >0</td>
  <td >8</td>
  <td >0</td>
  <td >4</td>
  <td >14</td>
  <td >-15</td>
  <td >-4</td>
  <td >-4</td>
  <td >-2</td>
  <td >7</td>
  <td >0.86 </td>
  <td >0.44 </td>
  <td >0.44 </td>
  <td ></td>
 </tr>
 <tr >
  <td >10002</td>
  <td>robisim74/AngularSPAWebAPI</td>
  <td>https://github.com/robisim74/AngularSPAWebAPI/commit/8e50133188a894fdf744e5c636798e41d6a85c75</td>
  <td >src/AngularSPAWebAP
  I/AngularSPAWebAPI.csproj</td>
  <td>.NETCoreApp1.1</td>
  <td >24</td>
  <td >221</td>
  <td >6</td>
  <td >0</td>
  <td >10</td>
  <td >0</td>
  <td >2</td>
  <td >1</td>
  <td >0</td>
  <td >230</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >22</td>
  <td >26</td>
  <td >227</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >23</td>
  <td >-26</td>
  <td >-3</td>
  <td >-2</td>
  <td >0</td>
  <td >1</td>
  <td >0.91 </td>
  <td >0.91 </td>
  <td >0.57 </td>
  <td ></td>
 </tr>
 <tr >
  <td >10005</td>
  <td>dotnet-presentations/aspnetcore-app-workshop</td>
  <td>https://github.com/dotnet-presentations/aspnetcore-app-workshop/commit/ce5bf9d06acf04aba73656a9c8c5462c487737c3</td>
  <td >save-points/6-Deploy
  ment-docker/ConferencePlanner/FrontEnd/FrontEnd.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >9</td>
  <td >160</td>
  <td >0</td>
  <td >1</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >1</td>
  <td >0</td>
  <td >122</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >9</td>
  <td >15</td>
  <td >122</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >12</td>
  <td >-15</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >3</td>
  <td >0.46 </td>
  <td >0.46 </td>
  <td >0.46 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100010</td>
  <td>phongnguyend/Practical.CleanArchitecture</td>
  <td>https://github.com/phongnguyend/Practical.CleanArchitecture/commit/42f0e227185092642a1ccedb7e9c4df952d3eb37</td>
  <td >src/Monolith/Classifie
  dAds.Infrastructure/ClassifiedAds.Infrastructure.csproj</td>
  <td>net5.0</td>
  <td >46</td>
  <td >320</td>
  <td >18</td>
  <td >4</td>
  <td >13</td>
  <td >0</td>
  <td >9</td>
  <td >1</td>
  <td >0</td>
  <td >233</td>
  <td >2</td>
  <td >9</td>
  <td >2</td>
  <td >12</td>
  <td >45</td>
  <td >55</td>
  <td >202</td>
  <td >0</td>
  <td >8</td>
  <td >0</td>
  <td >11</td>
  <td >40</td>
  <td >-55</td>
  <td >-31</td>
  <td >-11</td>
  <td >-1</td>
  <td >-5</td>
  <td >0.71 </td>
  <td >0.67 </td>
  <td >0.43 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100012</td>
  <td>asadsahi/AspNetCoreSpa</td>
  <td>https://github.com/asadsahi/AspNetCoreSpa/commit/eebd2a84b06be339ead476dada31f41a05ff82e4</td>
  <td >src/Presentation/STS/S
  TS.csproj</td>
  <td>net5.0</td>
  <td >12</td>
  <td >151</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >1</td>
  <td >0</td>
  <td >139</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >2</td>
  <td >11</td>
  <td >21</td>
  <td >137</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >20</td>
  <td >-21</td>
  <td >-2</td>
  <td >-1</td>
  <td >-1</td>
  <td >9</td>
  <td >0.50 </td>
  <td >0.43 </td>
  <td >0.36 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100015</td>
  <td>nguyenquyhy/Flight-Tracker-StreamDeck</td>
  <td>https://github.com/nguyenquyhy/Flight-Tracker-StreamDeck/commit/c93be2864d62eab727caa0c5d04511fdffc39dba</td>
  <td >FlightStreamDeck.Add
  On/FlightStreamDeck.AddOn.csproj</td>
  <td>net5.0</td>
  <td >17</td>
  <td >59</td>
  <td >17</td>
  <td >0</td>
  <td >12</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >59</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >6</td>
  <td >15</td>
  <td >16</td>
  <td >60</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >6</td>
  <td >12</td>
  <td >-16</td>
  <td >1</td>
  <td >-5</td>
  <td >0</td>
  <td >-3</td>
  <td >1.00 </td>
  <td >0.71 </td>
  <td >0.71 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100018</td>
  <td>EasyAbp/Abp.SettingUi</td>
  <td>https://github.com/EasyAbp/Abp.SettingUi/commit/2cdea3214ffff1996cd17959d95a64614c381023</td>
  <td >sample/MyAbpApp/src
  /MyAbpApp.Web/MyAbpApp.Web.csproj</td>
  <td>net5.0</td>
  <td >15</td>
  <td >212</td>
  <td >2</td>
  <td >1</td>
  <td >3</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >233</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >3</td>
  <td >14</td>
  <td >17</td>
  <td >233</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >2</td>
  <td >11</td>
  <td >-17</td>
  <td >0</td>
  <td >-4</td>
  <td >-1</td>
  <td >-3</td>
  <td >0.60 </td>
  <td >0.41 </td>
  <td >0.14 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100019</td>
  <td>DavidCBerry13/FoodTruckNationApi</td>
  <td>https://github.com/DavidCBerry13/FoodTruckNationApi/commit/ebbc28c444e8f3a0a35d21238b2107de990a2539</td>
  <td >src/FoodTruckNationA
  pi.Tests.Integration/FoodTruckNationApi.Tests.Integration.csproj</td>
  <td>.NETCoreApp2.1</td>
  <td >7</td>
  <td >103</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >134</td>
  <td >0</td>
  <td >2</td>
  <td >2</td>
  <td >0</td>
  <td >6</td>
  <td >6</td>
  <td >72</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >4</td>
  <td >-6</td>
  <td >-62</td>
  <td >-2</td>
  <td >1</td>
  <td >-2</td>
  <td >0.80 </td>
  <td >0.50 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100020</td>
  <td>mhutch/MonoDevelop.MSBuildEditor</td>
  <td>https://github.com/mhutch/MonoDevelop.MSBuildEditor/commit/3b928ddb25f78649d891ac92c4eb6864ed1f5448</td>
  <td >MonoDevelop.MSBuild
  .Tests/MonoDevelop.MSBuild.Tests.csproj</td>
  <td>.NETFramework4.7.2</td>
  <td >8</td>
  <td >42</td>
  <td >2</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >40</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >4</td>
  <td >8</td>
  <td >11</td>
  <td >33</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >3</td>
  <td >10</td>
  <td >-11</td>
  <td >-7</td>
  <td >-2</td>
  <td >-1</td>
  <td >2</td>
  <td >0.78 </td>
  <td >0.78 </td>
  <td >0.60 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100021</td>
  <td>aspnetrun/run-aspnetcore-basics</td>
  <td>https://github.com/aspnetrun/run-aspnetcore-basics/commit/b26a8bdde3ed5962cc601f3a5f7ffd770b1b133f</td>
  <td >AspnetRunBasics/Aspn
  etRunBasics.csproj</td>
  <td>net5.0</td>
  <td >7</td>
  <td >115</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >104</td>
  <td >0</td>
  <td >1</td>
  <td >2</td>
  <td >2</td>
  <td >6</td>
  <td >15</td>
  <td >121</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >14</td>
  <td >-15</td>
  <td >17</td>
  <td >-1</td>
  <td >-1</td>
  <td >8</td>
  <td >0.36 </td>
  <td >0.27 </td>
  <td >0.12 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100022</td>
  <td>Azure-Samples/storage-blob-upload-from-webapp</td>
  <td>https://github.com/Azure-Samples/storage-blob-upload-from-webapp/commit/1130984c77a85b9cb5647e69ed384664a012e81b</td>
  <td >ImageResizeWebApp/I
  mageResizeWebApp/ImageResizeWebApp.csproj</td>
  <td>.NETCoreApp2.0</td>
  <td >12</td>
  <td >191</td>
  <td >3</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >209</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >6</td>
  <td >12</td>
  <td >150</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >6</td>
  <td >-12</td>
  <td >-59</td>
  <td >-1</td>
  <td >0</td>
  <td >0</td>
  <td >0.57 </td>
  <td >0.57 </td>
  <td >0.57 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100027</td>
  <td>Jaxelr/Nancy.Template.Webservice</td>
  <td>https://github.com/Jaxelr/Nancy.Template.Webservice/commit/ca1393b58c6d3107059eb28e2ffefe1b862e25d7</td>
  <td >Content/src/Nancy.Te
  mplate.WebService.csproj</td>
  <td>.NETCoreApp2.2</td>
  <td >13</td>
  <td >159</td>
  <td >4</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >3</td>
  <td >2</td>
  <td >0</td>
  <td >156</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >2</td>
  <td >7</td>
  <td >12</td>
  <td >156</td>
  <td >0</td>
  <td >2</td>
  <td >2</td>
  <td >2</td>
  <td >6</td>
  <td >-12</td>
  <td >0</td>
  <td >-3</td>
  <td >0</td>
  <td >-1</td>
  <td >1.20 </td>
  <td >1.20 </td>
  <td >0.83 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100032</td>
  <td>uvasoftware/scanii-dotnet</td>
  <td>https://github.com/uvasoftware/scanii-dotnet/commit/08249aca7da83bebde7d96cc809a1f68fb0c1ad4</td>
  <td >UvaSoftware.Scanii/Uv
  aSoftware.Scanii.csproj</td>
  <td>.NETStandard2.0</td>
  <td >5</td>
  <td >6</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >33</td>
  <td >0</td>
  <td >1</td>
  <td >2</td>
  <td >1</td>
  <td >2</td>
  <td >4</td>
  <td >4</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >3</td>
  <td >-4</td>
  <td >-29</td>
  <td >-1</td>
  <td >0</td>
  <td >1</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.33 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100034</td>
  <td>JerryBian/blog.laobian.me</td>
  <td>https://github.com/JerryBian/blog.laobian.me/commit/cd3d46471cc3f11cb3df7eec3287da145da50e1b</td>
  <td >src/share/Laobian.Shar
  e.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >10</td>
  <td >23</td>
  <td >2</td>
  <td >1</td>
  <td >5</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >90</td>
  <td >1</td>
  <td >4</td>
  <td >0</td>
  <td >3</td>
  <td >7</td>
  <td >10</td>
  <td >85</td>
  <td >0</td>
  <td >1</td>
  <td >2</td>
  <td >2</td>
  <td >4</td>
  <td >-10</td>
  <td >-5</td>
  <td >-5</td>
  <td >-1</td>
  <td >-3</td>
  <td >0.67 </td>
  <td >0.43 </td>
  <td >0.11 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100035</td>
  <td>ryanwersal/MorseL</td>
  <td>https://github.com/ryanwersal/MorseL/commit/c1a080e599ba2ffee550b64510c9f712285e57d6</td>
  <td >test/MorseL.Shared.Te
  sts/MorseL.Shared.Tests.csproj</td>
  <td>.NETStandard2.0</td>
  <td >9</td>
  <td >107</td>
  <td >3</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >3</td>
  <td >2</td>
  <td >0</td>
  <td >101</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >4</td>
  <td >8</td>
  <td >8</td>
  <td >101</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >3</td>
  <td >7</td>
  <td >-8</td>
  <td >0</td>
  <td >-3</td>
  <td >-1</td>
  <td >-1</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.56 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100037</td>
  <td>pluto-arch/dotnet-project-template</td>
  <td>https://github.com/pluto-arch/dotnet-project-template/commit/d7c860330c2e95d534a91d756e45760627d0c047</td>
  <td >template/content/src/
  PlutoNetCoreTemplate/PlutoNetCoreTemplate.csproj</td>
  <td>net5.0</td>
  <td >11</td>
  <td >142</td>
  <td >3</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >2</td>
  <td >2</td>
  <td >0</td>
  <td >126</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >2</td>
  <td >10</td>
  <td >19</td>
  <td >136</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >2</td>
  <td >18</td>
  <td >-19</td>
  <td >10</td>
  <td >-2</td>
  <td >0</td>
  <td >8</td>
  <td >0.50 </td>
  <td >0.42 </td>
  <td >0.23 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100038</td>
  <td>yanpitangui/netcore-api-boilerplate</td>
  <td>https://github.com/yanpitangui/dotnet-api-boilerplate/commit/1170fc6ba8a8999c4e57abc20e00ce79f950d794</td>
  <td >src/Boilerplate.Api/Boi
  lerplate.Api.csproj</td>
  <td>net5.0</td>
  <td >15</td>
  <td >149</td>
  <td >9</td>
  <td >1</td>
  <td >6</td>
  <td >0</td>
  <td >2</td>
  <td >2</td>
  <td >0</td>
  <td >125</td>
  <td >0</td>
  <td >2</td>
  <td >2</td>
  <td >4</td>
  <td >14</td>
  <td >25</td>
  <td >144</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >3</td>
  <td >23</td>
  <td >-25</td>
  <td >19</td>
  <td >-2</td>
  <td >-1</td>
  <td >9</td>
  <td >0.59 </td>
  <td >0.52 </td>
  <td >0.25 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100044</td>
  <td>theolivenbaum/h5</td>
  <td>https://github.com/theolivenbaum/h5/commit/49ad367527f5a82d9db8fea851704ae91b77e14b</td>
  <td >H5/Compiler/Compiler
  .Service/H5.Compiler.Service.csproj</td>
  <td>.NETStandard2.1</td>
  <td >26</td>
  <td >140</td>
  <td >8</td>
  <td >2</td>
  <td >11</td>
  <td >0</td>
  <td >11</td>
  <td >2</td>
  <td >0</td>
  <td >121</td>
  <td >0</td>
  <td >11</td>
  <td >0</td>
  <td >10</td>
  <td >25</td>
  <td >35</td>
  <td >129</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >4</td>
  <td >26</td>
  <td >-35</td>
  <td >8</td>
  <td >-11</td>
  <td >-6</td>
  <td >1</td>
  <td >0.62 </td>
  <td >0.62 </td>
  <td >0.38 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100045</td>
  <td>theolivenbaum/h5</td>
  <td>https://github.com/theolivenbaum/h5/commit/49ad367527f5a82d9db8fea851704ae91b77e14b</td>
  <td >H5/Compiler/Translato
  r/H5.Translator.csproj</td>
  <td>.NETStandard2.1</td>
  <td >26</td>
  <td >101</td>
  <td >8</td>
  <td >0</td>
  <td >12</td>
  <td >0</td>
  <td >9</td>
  <td >2</td>
  <td >0</td>
  <td >101</td>
  <td >0</td>
  <td >9</td>
  <td >0</td>
  <td >11</td>
  <td >24</td>
  <td >30</td>
  <td >105</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >5</td>
  <td >22</td>
  <td >-30</td>
  <td >4</td>
  <td >-9</td>
  <td >-6</td>
  <td >-2</td>
  <td >0.65 </td>
  <td >0.54 </td>
  <td >0.43 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100046</td>
  <td>AngleSharp/AngleSharp.Io</td>
  <td>https://github.com/AngleSharp/AngleSharp.Io/commit/2970ab158c0517cd32ef3a322265b1ef52a7bd12</td>
  <td >src/AngleSharp.Io.Test
  s/AngleSharp.Io.Tests.csproj</td>
  <td>.NETStandard2.0</td>
  <td >6</td>
  <td >6</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >7</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >4</td>
  <td >5</td>
  <td >66</td>
  <td >0</td>
  <td >1</td>
  <td >1</td>
  <td >1</td>
  <td >3</td>
  <td >-5</td>
  <td >59</td>
  <td >-1</td>
  <td >0</td>
  <td >-1</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100047</td>
  <td>trevoirwilliams/BookStore-API</td>
  <td>https://github.com/trevoirwilliams/BookStore-API-Blazor/commit/90d6e27be923550d6dc88db249eabb18e0ad3eae</td>
  <td >BookStore-API/BookSt
  ore-API.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >14</td>
  <td >116</td>
  <td >0</td>
  <td >1</td>
  <td >5</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >111</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >6</td>
  <td >11</td>
  <td >111</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >7</td>
  <td >-11</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >1</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.33 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100048</td>
  <td>CSA-OCP-GER/azure-developer-college</td>
  <td>https://github.com/CSA-OCP-GER/azure-developer-college/commit/0a7514418239addf4c753748dd446a4b7388c2c6</td>
  <td >day2/apps/dotnetcore
  /Scm.Resources/Adc.Scm.Resources.Api/Adc.Scm.Resources.Api.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >7</td>
  <td >101</td>
  <td >4</td>
  <td >1</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >94</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >4</td>
  <td >8</td>
  <td >90</td>
  <td >0</td>
  <td >2</td>
  <td >1</td>
  <td >1</td>
  <td >6</td>
  <td >-8</td>
  <td >-4</td>
  <td >-1</td>
  <td >0</td>
  <td >2</td>
  <td >0.60 </td>
  <td >0.60 </td>
  <td >0.60 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100050</td>
  <td>excubo-ag/Blazor.ScriptInjection</td>
  <td>https://github.com/excubo-ag/Blazor.ScriptInjection/commit/c7b410846fdd492704fdd033c78fe2fe64ebc592</td>
  <td >Tests_ScriptInjection/T
  ests_ScriptInjection.csproj</td>
  <td>net5.0</td>
  <td >9</td>
  <td >97</td>
  <td >4</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >111</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >3</td>
  <td >7</td>
  <td >14</td>
  <td >119</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >2</td>
  <td >11</td>
  <td >-14</td>
  <td >8</td>
  <td >-3</td>
  <td >-1</td>
  <td >4</td>
  <td >0.60 </td>
  <td >0.60 </td>
  <td >0.23 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100051</td>
  <td>Tentacule/PgsToSrt</td>
  <td>https://github.com/Tentacule/PgsToSrt/commit/08e6b3aba9074fde829ce864890855c506084f10</td>
  <td >PgsToSrt/PgsToSrt.cspr
  oj</td>
  <td>net5.0</td>
  <td >5</td>
  <td >32</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >17</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >1</td>
  <td >5</td>
  <td >5</td>
  <td >30</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >1</td>
  <td >5</td>
  <td >-5</td>
  <td >13</td>
  <td >-3</td>
  <td >0</td>
  <td >0</td>
  <td >2.50 </td>
  <td >2.50 </td>
  <td >2.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100052</td>
  <td>EasyAbp/Abp.AspNetCore.Mvc.UI.Theme.LYear</td>
  <td>https://github.com/EasyAbp/Abp.AspNetCore.Mvc.UI.Theme.LYear/commit/8a0c06eb2058ed2960f3a3bc0614c22178011b2d</td>
  <td >samples/LYearUiSampl
  e.Web/LYearUiSample.Web.csproj</td>
  <td>net5.0</td>
  <td >15</td>
  <td >211</td>
  <td >2</td>
  <td >1</td>
  <td >3</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >0</td>
  <td >212</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >4</td>
  <td >14</td>
  <td >17</td>
  <td >232</td>
  <td >0</td>
  <td >1</td>
  <td >2</td>
  <td >2</td>
  <td >13</td>
  <td >-17</td>
  <td >20</td>
  <td >-6</td>
  <td >-2</td>
  <td >-1</td>
  <td >0.73 </td>
  <td >0.53 </td>
  <td >0.18 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100058</td>
  <td>VolleyManagement/volley-management</td>
  <td>https://github.com/VolleyManagement/volley-management/commit/b89ae404596892c5c61f84727c16fad32221f5da</td>
  <td >src/Client/VolleyM.API
  /VolleyM.API.csproj</td>
  <td>net5.0</td>
  <td >20</td>
  <td >176</td>
  <td >6</td>
  <td >1</td>
  <td >6</td>
  <td >0</td>
  <td >8</td>
  <td >0</td>
  <td >0</td>
  <td >162</td>
  <td >0</td>
  <td >8</td>
  <td >0</td>
  <td >4</td>
  <td >17</td>
  <td >31</td>
  <td >171</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >4</td>
  <td >24</td>
  <td >-31</td>
  <td >9</td>
  <td >-8</td>
  <td >0</td>
  <td >7</td>
  <td >0.48 </td>
  <td >0.33 </td>
  <td >0.18 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100059</td>
  <td>Particular/NServiceBus.NHibernate</td>
  <td>https://github.com/Particular/NServiceBus.NHibernate/commit/14a10402953d63843d9949a0f12291dfd7fcb42b</td>
  <td >src/NServiceBus.NHibe
  rnate.AcceptanceTests-Oracle/NServiceBus.NHibernate.AcceptanceTests-Oracle.csproj</td>
  <td>.NETFramework4.7.2</td>
  <td >6</td>
  <td >24</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >24</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >6</td>
  <td >7</td>
  <td >24</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >7</td>
  <td >-7</td>
  <td >0</td>
  <td >-2</td>
  <td >0</td>
  <td >1</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.71 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100060</td>
  <td>bitfoundation/ToDoLine</td>
  <td>https://github.com/bitfoundation/ToDoLine/commit/f544da435035322ed631a3c9fe350a048bc20b79</td>
  <td >App/ToDoLineApp/To
  DoLineApp.csproj</td>
  <td>.NETStandard2.0</td>
  <td >12</td>
  <td >105</td>
  <td >4</td>
  <td >1</td>
  <td >5</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >119</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >4</td>
  <td >12</td>
  <td >16</td>
  <td >67</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >4</td>
  <td >16</td>
  <td >-16</td>
  <td >-52</td>
  <td >-1</td>
  <td >0</td>
  <td >4</td>
  <td >0.86 </td>
  <td >0.86 </td>
  <td >0.53 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100061</td>
  <td>bitfoundation/ToDoLine</td>
  <td>https://github.com/bitfoundation/ToDoLine/commit/f544da435035322ed631a3c9fe350a048bc20b79</td>
  <td >ToDoLine/ToDoLine.cs
  proj</td>
  <td>net5.0</td>
  <td >10</td>
  <td >165</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >203</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >2</td>
  <td >9</td>
  <td >10</td>
  <td >206</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >2</td>
  <td >7</td>
  <td >-10</td>
  <td >3</td>
  <td >-1</td>
  <td >0</td>
  <td >-2</td>
  <td >0.67 </td>
  <td >0.67 </td>
  <td >0.25 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100062</td>
  <td>blockbasenetwork/node</td>
  <td>https://github.com/blockbasenetwork/node/commit/623871e66669143c17ffa2e869c586c5b813d07c</td>
  <td >BlockBase.Network/Bl
  ockBase.Network.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >12</td>
  <td >63</td>
  <td >6</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >36</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >8</td>
  <td >9</td>
  <td >19</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >8</td>
  <td >-9</td>
  <td >-17</td>
  <td >-1</td>
  <td >0</td>
  <td >0</td>
  <td >1.14 </td>
  <td >1.14 </td>
  <td >0.67 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100063</td>
  <td>FitzyCodesThings/core-lms</td>
  <td>https://github.com/FitzyCodesThings/core-lms/commit/d9eb3833ee94f4fee466227ae53b29b81d4811b5</td>
  <td >CoreLMS.Web/CoreLM
  S.Web.csproj</td>
  <td>net5.0</td>
  <td >10</td>
  <td >145</td>
  <td >0</td>
  <td >1</td>
  <td >1</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >49</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >6</td>
  <td >9</td>
  <td >16</td>
  <td >130</td>
  <td >0</td>
  <td >3</td>
  <td >2</td>
  <td >3</td>
  <td >14</td>
  <td >-16</td>
  <td >81</td>
  <td >-3</td>
  <td >-3</td>
  <td >5</td>
  <td >0.54 </td>
  <td >0.33 </td>
  <td >0.11 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100064</td>
  <td>EasyAbp/Abp.TagHelperPlus</td>
  <td>https://github.com/EasyAbp/Abp.TagHelperPlus/commit/cd142ac218f8b5ee698d03bf627169872edc12ce</td>
  <td >host/EasyAbp.Abp.Tag
  HelperPlus.Web.Unified/EasyAbp.Abp.TagHelperPlus.Web.Unified.csproj</td>
  <td>net5.0</td>
  <td >25</td>
  <td >234</td>
  <td >0</td>
  <td >1</td>
  <td >1</td>
  <td >0</td>
  <td >11</td>
  <td >0</td>
  <td >0</td>
  <td >231</td>
  <td >0</td>
  <td >11</td>
  <td >0</td>
  <td >4</td>
  <td >24</td>
  <td >26</td>
  <td >276</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >3</td>
  <td >21</td>
  <td >-26</td>
  <td >45</td>
  <td >-11</td>
  <td >-1</td>
  <td >-3</td>
  <td >0.83 </td>
  <td >0.76 </td>
  <td >0.22 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100068</td>
  <td>pekkah/tanka-graphql-samples</td>
  <td>https://github.com/pekkah/tanka-graphql-samples/commit/20d0856841f0010b7a88051c2693c53335dfbdea</td>
  <td >src/Messages.Host/Me
  ssages.Host.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >9</td>
  <td >86</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >81</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >3</td>
  <td >8</td>
  <td >9</td>
  <td >84</td>
  <td >0</td>
  <td >1</td>
  <td >2</td>
  <td >3</td>
  <td >8</td>
  <td >-9</td>
  <td >3</td>
  <td >-3</td>
  <td >0</td>
  <td >0</td>
  <td >0.88 </td>
  <td >0.67 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100069</td>
  <td>Hona/TempusHub</td>
  <td>https://github.com/Hona/TempusHub/commit/8fdb10d746c640dddfb3e7371bf268912841acc0</td>
  <td >src/TempusHubBlazor/
  TempusHubBlazor.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >11</td>
  <td >131</td>
  <td >0</td>
  <td >1</td>
  <td >4</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >152</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >3</td>
  <td >10</td>
  <td >17</td>
  <td >130</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >12</td>
  <td >-17</td>
  <td >-22</td>
  <td >-1</td>
  <td >-2</td>
  <td >2</td>
  <td >0.40 </td>
  <td >0.31 </td>
  <td >0.31 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100070</td>
  <td>tom-englert/Equatable.Fody</td>
  <td>https://github.com/tom-englert/Equatable.Fody/commit/fa269dc00a1153b16ca7f407e29d40c25e358af4</td>
  <td >Tests/Tests.csproj</td>
  <td>.NETFramework4.6</td>
  <td >5</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >5</td>
  <td >5</td>
  <td >6</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >5</td>
  <td >-5</td>
  <td >1</td>
  <td >-2</td>
  <td >0</td>
  <td >0</td>
  <td >1.25 </td>
  <td >1.25 </td>
  <td >0.80 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100072</td>
  <td>waqaskhan540/QuestionAnswerApp</td>
  <td>https://github.com/waqaskhan540/QuestionAnswerApp/commit/34b4e42d618ed3afb146d92aa64a05f2b888df5d</td>
  <td >server/Server/QnA.Aut
  horization.Server/QnA.Authorization.Server.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >7</td>
  <td >129</td>
  <td >0</td>
  <td >2</td>
  <td >2</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >122</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >6</td>
  <td >15</td>
  <td >106</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >2</td>
  <td >14</td>
  <td >-15</td>
  <td >-16</td>
  <td >-2</td>
  <td >1</td>
  <td >8</td>
  <td >0.50 </td>
  <td >0.38 </td>
  <td >0.20 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100073</td>
  <td>dzimchuk/book-fast-docker</td>
  <td>https://github.com/dzimchuk/book-fast-docker/commit/8819f3a0e48418c0eabb77d2f337aeddaa29ca96</td>
  <td >BookFast.Web/BookFa
  st.Web.csproj</td>
  <td>net5.0</td>
  <td >6</td>
  <td >152</td>
  <td >0</td>
  <td >2</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >184</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >10</td>
  <td >137</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >1</td>
  <td >9</td>
  <td >-10</td>
  <td >-47</td>
  <td >-1</td>
  <td >1</td>
  <td >4</td>
  <td >0.83 </td>
  <td >0.57 </td>
  <td >0.38 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100074</td>
  <td>dzimchuk/book-fast-docker</td>
  <td>https://github.com/dzimchuk/book-fast-docker/commit/8ea811d249488461dc7f26896f1548f95930ca9e</td>
  <td >BookFast.Web/BookFa
  st.Web.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >6</td>
  <td >152</td>
  <td >0</td>
  <td >2</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >186</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >10</td>
  <td >137</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >1</td>
  <td >9</td>
  <td >-10</td>
  <td >-49</td>
  <td >-1</td>
  <td >1</td>
  <td >4</td>
  <td >0.83 </td>
  <td >0.57 </td>
  <td >0.38 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100075</td>
  <td>ghaagh/Sticky</td>
  <td>https://github.com/ghaagh/Sticky/commit/0ecb674a7f5f338319d5514b201958217e50599a</td>
  <td >Sticky.Services.KafkaCo
  nsumer/Sticky.Services.KafkaConsumer.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >7</td>
  <td >80</td>
  <td >1</td>
  <td >2</td>
  <td >5</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >79</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >5</td>
  <td >8</td>
  <td >11</td>
  <td >84</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >2</td>
  <td >10</td>
  <td >-11</td>
  <td >5</td>
  <td >-3</td>
  <td >-3</td>
  <td >2</td>
  <td >0.88 </td>
  <td >0.50 </td>
  <td >0.15 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100076</td>
  <td>ghaagh/Sticky</td>
  <td>https://github.com/ghaagh/Sticky/commit/0ecb674a7f5f338319d5514b201958217e50599a</td>
  <td >Sticky.Services.Respon
  seUpdater/Sticky.Services.ResponseUpdater.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >7</td>
  <td >15</td>
  <td >1</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >12</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >4</td>
  <td >7</td>
  <td >7</td>
  <td >19</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >2</td>
  <td >6</td>
  <td >-7</td>
  <td >7</td>
  <td >-3</td>
  <td >-2</td>
  <td >-1</td>
  <td >1.20 </td>
  <td >0.83 </td>
  <td >0.57 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100080</td>
  <td>jahanbinali1988/Sofa</td>
  <td>https://github.com/jahanbinali1988/Sofa/commit/48446e13b27666acfb6ee62443689f72b0fdcba9</td>
  <td >TestProjects/Sofa.Cour
  seManagement.IntegratedTest/Sofa.CourseManagement.IntegratedTest.csproj</td>
  <td>.NETCoreApp3.0</td>
  <td >18</td>
  <td >194</td>
  <td >6</td>
  <td >2</td>
  <td >8</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >159</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >5</td>
  <td >10</td>
  <td >23</td>
  <td >136</td>
  <td >2</td>
  <td >3</td>
  <td >0</td>
  <td >5</td>
  <td >13</td>
  <td >-23</td>
  <td >-23</td>
  <td >-4</td>
  <td >0</td>
  <td >3</td>
  <td >0.67 </td>
  <td >0.67 </td>
  <td >0.43 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100084</td>
  <td>paulbulman/ParkingRota</td>
  <td>https://github.com/paulbulman/ParkingRota/commit/017744d6e6e0daf33bc230e5ee3471a2cb2bda54</td>
  <td >ParkingRota.Business/
  ParkingRota.Business.csproj</td>
  <td>.NETCoreApp2.1</td>
  <td >7</td>
  <td >20</td>
  <td >2</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >7</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >5</td>
  <td >7</td>
  <td >7</td>
  <td >20</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >3</td>
  <td >4</td>
  <td >-7</td>
  <td >13</td>
  <td >-4</td>
  <td >-2</td>
  <td >-3</td>
  <td >0.80 </td>
  <td >0.50 </td>
  <td >0.50 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100087</td>
  <td>mcanerizci/TradingCat</td>
  <td>https://github.com/mcanerizci/TradingCat/commit/25582a45225f1c01a8f5a23273e201240082e4b5</td>
  <td >TradingCat/source/Ser
  vices/Order/Order.API/Order.API.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >5</td>
  <td >112</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >113</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >7</td>
  <td >111</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >0</td>
  <td >7</td>
  <td >-7</td>
  <td >-2</td>
  <td >-1</td>
  <td >0</td>
  <td >3</td>
  <td >0.57 </td>
  <td >0.57 </td>
  <td >0.38 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100088</td>
  <td>Lulubul/NeflixContainers</td>
  <td>https://github.com/Lulubul/NeflixContainers/commit/fe84fa90b40ecbfd9122f1e312ddd6acfe42abc2</td>
  <td >Marketing.API/Market
  ing.API.csproj</td>
  <td>.NETCoreApp2.2</td>
  <td >6</td>
  <td >99</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >111</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >2</td>
  <td >5</td>
  <td >7</td>
  <td >116</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >5</td>
  <td >-7</td>
  <td >5</td>
  <td >-1</td>
  <td >-1</td>
  <td >0</td>
  <td >0.60 </td>
  <td >0.33 </td>
  <td >0.14 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100093</td>
  <td>davidandradeduarte/simple-random-teams</td>
  <td>https://github.com/davidandradeduarte/simple-random-teams/commit/c8057e1fb8e7a485ba92bea3bf18be47efcbf371</td>
  <td >SimpleRandomTeams/
  SimpleRandomTeams.csproj��src/SimpleRandomTeams/SimpleRandomTeams.csproj</td>
  <td>net5.0</td>
  <td >9</td>
  <td >92</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >7</td>
  <td >0</td>
  <td >0</td>
  <td >84</td>
  <td >0</td>
  <td >7</td>
  <td >0</td>
  <td >5</td>
  <td >8</td>
  <td >8</td>
  <td >81</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >3</td>
  <td >6</td>
  <td >-8</td>
  <td >-3</td>
  <td >-7</td>
  <td >-2</td>
  <td >-2</td>
  <td >1.20 </td>
  <td >1.20 </td>
  <td >0.38 </td>
  <td ></td>
 </tr>
 <tr >
  <td >100098</td>
  <td>SkillsFundingAgency/das-providerapprenticeshipsservice</td>
  <td>https://github.com/SkillsFundingAgency/das-providerapprenticeshipsservice/commit/9e12083d0641a3ed9d9277f29197d1f6a4234000</td>
  <td >src/SFA.DAS.PAS.Acco
  unt.Api.ClientV2.UnitTests/SFA.DAS.PAS.Account.Api.ClientV2.UnitTests.csproj</td>
  <td>.NETStandard2.0</td>
  <td >8</td>
  <td >75</td>
  <td >2</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >78</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >7</td>
  <td >8</td>
  <td >77</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >2</td>
  <td >7</td>
  <td >-8</td>
  <td >-1</td>
  <td >-1</td>
  <td >1</td>
  <td >0</td>
  <td >0.86 </td>
  <td >0.63 </td>
  <td >0.44 </td>
  <td ></td>
 </tr>
 <tr >
  <td >1000103</td>
  <td>gmoreno90/webhookhub</td>
  <td>https://github.com/gmoreno90/webhookhub/commit/cd4cc30953a84aa582301b0660c2cd05a6f17b23</td>
  <td >WebHookHub/WebHo
  okHub.csproj</td>
  <td>net5.0</td>
  <td >10</td>
  <td >184</td>
  <td >0</td>
  <td >3</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >135</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >2</td>
  <td >9</td>
  <td >21</td>
  <td >159</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >1</td>
  <td >18</td>
  <td >-21</td>
  <td >24</td>
  <td >-1</td>
  <td >-1</td>
  <td >9</td>
  <td >0.44 </td>
  <td >0.44 </td>
  <td >0.21 </td>
  <td ></td>
 </tr>
 <tr >
  <td >1000108</td>
  <td>alexthissen/HealthMonitoring</td>
  <td>https://github.com/alexthissen/HealthMonitoring/commit/e4b854e6ecc0c67601c76ae5c03c72870ed9b7ed</td>
  <td >RetroGamingWebAPI/
  RetroGamingWebAPI.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >13</td>
  <td >182</td>
  <td >2</td>
  <td >3</td>
  <td >3</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >204</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >3</td>
  <td >13</td>
  <td >20</td>
  <td >122</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >1</td>
  <td >15</td>
  <td >-20</td>
  <td >-82</td>
  <td >-1</td>
  <td >-2</td>
  <td >2</td>
  <td >0.47 </td>
  <td >0.39 </td>
  <td >0.39 </td>
  <td ></td>
 </tr>
 <tr >
  <td >1000110</td>
  <td>equinor/procosys-preservation-api</td>
  <td>https://github.com/equinor/procosys-preservation-api/commit/7da9018fd78c912a1022a3b2956ba28a42f0a87d</td>
  <td >src/Equinor.Procosys.P
  reservation.WebApi/Equinor.Procosys.Preservation.WebApi.csproj</td>
  <td>net5.0</td>
  <td >19</td>
  <td >189</td>
  <td >5</td>
  <td >3</td>
  <td >7</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >199</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >4</td>
  <td >15</td>
  <td >25</td>
  <td >180</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >3</td>
  <td >18</td>
  <td >-25</td>
  <td >-19</td>
  <td >-1</td>
  <td >-1</td>
  <td >3</td>
  <td >0.67 </td>
  <td >0.67 </td>
  <td >0.30 </td>
  <td ></td>
 </tr>
 <tr >
  <td >1000113</td>
  <td>neuroglia-io/K8s.Eventing</td>
  <td>https://github.com/neuroglia-io/K8s.Eventing/commit/dbd556c3f1775e411fc18519e29c3456d78461df</td>
  <td >src/Gateway/Neurogli
  a.K8s.Eventing.Gateway.Infrastructure/Neuroglia.K8s.Eventing.Gateway.Infrastructure.csproj</td>
  <td>net5.0</td>
  <td >5</td>
  <td >91</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >90</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >3</td>
  <td >4</td>
  <td >8</td>
  <td >82</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >6</td>
  <td >-8</td>
  <td >-8</td>
  <td >-2</td>
  <td >-2</td>
  <td >2</td>
  <td >0.50 </td>
  <td >0.29 </td>
  <td >0.29 </td>
  <td ></td>
 </tr>
 <tr >
  <td >1000115</td>
  <td>sergey-rybalkin/StyleCopPlus</td>
  <td>https://github.com/sergey-rybalkin/StyleCopPlus/commit/0efc42dd9f991eab3a5dfa0abaa8bc9e5d7f41fb</td>
  <td >src/StyleCopPlus.Test/
  StyleCopPlus.Test.csproj</td>
  <td>.NETCoreApp2.0</td>
  <td >9</td>
  <td >88</td>
  <td >4</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >101</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >4</td>
  <td >7</td>
  <td >12</td>
  <td >101</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >2</td>
  <td >10</td>
  <td >-12</td>
  <td >0</td>
  <td >-1</td>
  <td >-2</td>
  <td >3</td>
  <td >0.45 </td>
  <td >0.45 </td>
  <td >0.45 </td>
  <td ></td>
 </tr>
 <tr >
  <td >1000116</td>
  <td>atomiv/atomiv-dotnet</td>
  <td>https://github.com/atomiv/atomiv-dotnet/commit/c580e41572331e67f012974158f95768178aad8a</td>
  <td >template/microservice
  /src/Web/Atomiv.Template.Web.RestApi/Atomiv.Template.Web.RestApi.csproj</td>
  <td>net5.0</td>
  <td >11</td>
  <td >146</td>
  <td >0</td>
  <td >1</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >145</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >11</td>
  <td >24</td>
  <td >146</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >20</td>
  <td >-24</td>
  <td >1</td>
  <td >-1</td>
  <td >-1</td>
  <td >9</td>
  <td >0.32 </td>
  <td >0.32 </td>
  <td >0.16 </td>
  <td ></td>
 </tr>
 <tr >
  <td >1000117</td>
  <td>pluto-arch/dotnet-project-template</td>
  <td>https://github.com/pluto-arch/dotnet-project-template/commit/267fc4ba8d0373a746daf8617424e7611b889eda</td>
  <td >template/content/src/
  PlutoNetCoreTemplate/PlutoNetCoreTemplate.csproj</td>
  <td>net5.0</td>
  <td >11</td>
  <td >142</td>
  <td >3</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >126</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >2</td>
  <td >10</td>
  <td >19</td>
  <td >136</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >2</td>
  <td >18</td>
  <td >-19</td>
  <td >10</td>
  <td >-2</td>
  <td >0</td>
  <td >8</td>
  <td >0.50 </td>
  <td >0.42 </td>
  <td >0.23 </td>
  <td ></td>
 </tr>
 <tr >
  <td >1000118</td>
  <td>seekdavidlee/Eklee-Azure-Functions-Http</td>
  <td>https://github.com/seekdavidlee/Eklee-Azure-Functions-Http/commit/05874438ef12aa232edaa9cad498dbde8c5c020c</td>
  <td >Eklee.Azure.Functions.
  Http/Eklee.Azure.Functions.Http.csproj</td>
  <td>.NETStandard2.1</td>
  <td >10</td>
  <td >51</td>
  <td >4</td>
  <td >0</td>
  <td >9</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >92</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >3</td>
  <td >9</td>
  <td >9</td>
  <td >94</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >2</td>
  <td >9</td>
  <td >-9</td>
  <td >2</td>
  <td >-2</td>
  <td >-1</td>
  <td >0</td>
  <td >1.29 </td>
  <td >1.00 </td>
  <td >0.45 </td>
  <td ></td>
 </tr>
 <tr >
  <td >1000119</td>
  <td>halomademeapc/ChatBeet</td>
  <td>https://github.com/halomademeapc/ChatBeet/commit/f62758e19ca9096e42bfcfae3f1105b364251a15</td>
  <td >ChatBeet/ChatBeet.cs
  proj</td>
  <td>net5.0</td>
  <td >32</td>
  <td >157</td>
  <td >4</td>
  <td >1</td>
  <td >6</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >172</td>
  <td >10</td>
  <td >3</td>
  <td >0</td>
  <td >8</td>
  <td >19</td>
  <td >41</td>
  <td >177</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >4</td>
  <td >24</td>
  <td >-41</td>
  <td >5</td>
  <td >-3</td>
  <td >-4</td>
  <td >5</td>
  <td >0.52 </td>
  <td >0.46 </td>
  <td >0.37 </td>
  <td ></td>
 </tr>
 <tr >
  <td >1000120</td>
  <td>halomademeapc/ChatBeet</td>
  <td>https://github.com/halomademeapc/ChatBeet/commit/7b9f141b5ca56e9247d2a52da331543dee0ff35e</td>
  <td >ChatBeet/ChatBeet.cs
  proj</td>
  <td>net5.0</td>
  <td >32</td>
  <td >157</td>
  <td >4</td>
  <td >1</td>
  <td >6</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >163</td>
  <td >6</td>
  <td >4</td>
  <td >0</td>
  <td >6</td>
  <td >18</td>
  <td >41</td>
  <td >177</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >4</td>
  <td >24</td>
  <td >-41</td>
  <td >14</td>
  <td >-4</td>
  <td >-2</td>
  <td >6</td>
  <td >0.54 </td>
  <td >0.48 </td>
  <td >0.43 </td>
  <td ></td>
 </tr>
 <tr >
  <td >1000124</td>
  <td>ops-ai/BeyondAuth</td>
  <td>https://github.com/ops-ai/BeyondAuth/commit/6a5de6939f7bcc586d214994503deaa60c78ea4d</td>
  <td >src/AuditServer/AuditS
  erver.csproj</td>
  <td>net5.0</td>
  <td >18</td>
  <td >234</td>
  <td >2</td>
  <td >3</td>
  <td >8</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >208</td>
  <td >2</td>
  <td >3</td>
  <td >0</td>
  <td >5</td>
  <td >16</td>
  <td >33</td>
  <td >222</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >2</td>
  <td >24</td>
  <td >-33</td>
  <td >14</td>
  <td >-3</td>
  <td >-3</td>
  <td >8</td>
  <td >0.32 </td>
  <td >0.32 </td>
  <td >0.19 </td>
  <td ></td>
 </tr>
 <tr >
  <td >1000125</td>
  <td>ops-ai/BeyondAuth</td>
  <td>https://github.com/ops-ai/BeyondAuth/commit/6a5de6939f7bcc586d214994503deaa60c78ea4d</td>
  <td >src/AuthorizationServe
  r/AuthorizationServer.csproj</td>
  <td>net5.0</td>
  <td >16</td>
  <td >205</td>
  <td >2</td>
  <td >1</td>
  <td >8</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >190</td>
  <td >4</td>
  <td >4</td>
  <td >0</td>
  <td >4</td>
  <td >13</td>
  <td >23</td>
  <td >153</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >2</td>
  <td >18</td>
  <td >-23</td>
  <td >-37</td>
  <td >-4</td>
  <td >-2</td>
  <td >5</td>
  <td >0.61 </td>
  <td >0.61 </td>
  <td >0.32 </td>
  <td ></td>
 </tr>
 <tr >
  <td >1000129</td>
  <td>ops-ai/BeyondAuth</td>
  <td>https://github.com/ops-ai/BeyondAuth/commit/6a5de6939f7bcc586d214994503deaa60c78ea4d</td>
  <td >src/PolicyServer/Policy
  Server.csproj</td>
  <td>net5.0</td>
  <td >16</td>
  <td >197</td>
  <td >2</td>
  <td >1</td>
  <td >8</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >184</td>
  <td >1</td>
  <td >1</td>
  <td >0</td>
  <td >3</td>
  <td >11</td>
  <td >21</td>
  <td >138</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >2</td>
  <td >14</td>
  <td >-21</td>
  <td >-46</td>
  <td >-1</td>
  <td >-1</td>
  <td >3</td>
  <td >0.64 </td>
  <td >0.64 </td>
  <td >0.44 </td>
  <td ></td>
 </tr>
 <tr >
  <td >1000138</td>
  <td>hbiarge/Experiments</td>
  <td>https://github.com/hbiarge/Experiments/commit/f826537c9de7ed4a0b82e27421828e1f38eac610</td>
  <td >Messaging/Rebus/Exte
  rnal/Acheve.External.Estimations/Acheve.External.Estimations.csproj</td>
  <td>net5.0</td>
  <td >6</td>
  <td >83</td>
  <td >0</td>
  <td >1</td>
  <td >4</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >97</td>
  <td >5</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >9</td>
  <td >97</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >8</td>
  <td >-9</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >3</td>
  <td >0.71 </td>
  <td >0.71 </td>
  <td >0.71 </td>
  <td ></td>
 </tr>
 <tr >
  <td >1000139</td>
  <td>hbiarge/Experiments</td>
  <td>https://github.com/hbiarge/Experiments/commit/f826537c9de7ed4a0b82e27421828e1f38eac610</td>
  <td >Messaging/Rebus/Exte
  rnal/Acheve.External.ImageProcess/Acheve.External.ImageProcess.csproj</td>
  <td>net5.0</td>
  <td >6</td>
  <td >83</td>
  <td >0</td>
  <td >1</td>
  <td >4</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >97</td>
  <td >4</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >9</td>
  <td >97</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >8</td>
  <td >-9</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >3</td>
  <td >0.71 </td>
  <td >0.71 </td>
  <td >0.71 </td>
  <td ></td>
 </tr>
 <tr >
  <td >1000140</td>
  <td>hbiarge/Experiments</td>
  <td>https://github.com/hbiarge/Experiments/commit/f826537c9de7ed4a0b82e27421828e1f38eac610</td>
  <td >Messaging/Rebus/Exte
  rnal/Acheve.External.Images/Acheve.External.Images.csproj</td>
  <td>net5.0</td>
  <td >6</td>
  <td >83</td>
  <td >0</td>
  <td >1</td>
  <td >4</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >97</td>
  <td >2</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >9</td>
  <td >97</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >8</td>
  <td >-9</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >3</td>
  <td >0.71 </td>
  <td >0.71 </td>
  <td >0.71 </td>
  <td ></td>
 </tr>
 <tr >
  <td >1000141</td>
  <td>hbiarge/Experiments</td>
  <td>https://github.com/hbiarge/Experiments/commit/f826537c9de7ed4a0b82e27421828e1f38eac610</td>
  <td >Messaging/Rebus/Exte
  rnal/Acheve.External.Notifications/Acheve.External.Notifications.csproj</td>
  <td>net5.0</td>
  <td >6</td>
  <td >83</td>
  <td >0</td>
  <td >1</td>
  <td >4</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >97</td>
  <td >2</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >9</td>
  <td >97</td>
  <td >2</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >8</td>
  <td >-9</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >3</td>
  <td >0.71 </td>
  <td >0.71 </td>
  <td >0.71 </td>
  <td ></td>
 </tr>
 <tr >
  <td >1000144</td>
  <td>flyingpianoman/TorrentGrease</td>
  <td>https://github.com/flyingpianoman/TorrentGrease/commit/f77ed49be04d149fc30870620db41dc913265dfe</td>
  <td >TorrentGrease.Server/
  TorrentGrease.Server.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >6</td>
  <td >25</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >23</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >5</td>
  <td >23</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >4</td>
  <td >-5</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >-1</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.60 </td>
  <td ></td>
 </tr>
 <tr >
  <td >1000145</td>
  <td>awaisa/AK</td>
  <td>https://github.com/awaisa/AK/commit/4f2b429dd7c299c3d7e0fbf6888935eb1ea44c5a</td>
  <td >ak/WebApi/WebApiCo
  re.csproj</td>
  <td>.NETCoreApp2.0</td>
  <td >49</td>
  <td >160</td>
  <td >58</td>
  <td >0</td>
  <td >8</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >155</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >29</td>
  <td >24</td>
  <td >36</td>
  <td >158</td>
  <td >0</td>
  <td >8</td>
  <td >0</td>
  <td >29</td>
  <td >29</td>
  <td >-36</td>
  <td >3</td>
  <td >-4</td>
  <td >0</td>
  <td >5</td>
  <td >0.73 </td>
  <td >0.55 </td>
  <td >0.45 </td>
  <td ></td>
 </tr>
 <tr >
  <td >1000147</td>
  <td>dr1rrb/smarthome.net</td>
  <td>https://github.com/dr1rrb/smarthome.net/commit/943a70c58726bf466c3e6e942be52bbd1464e115</td>
  <td >src/SmartHomeDotNet
  .Package/SmartHomeDotNet.Package.csproj</td>
  <td>.NETStandard2.0</td>
  <td >6</td>
  <td >24</td>
  <td >2</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >38</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >5</td>
  <td >6</td>
  <td >35</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >5</td>
  <td >-6</td>
  <td >-3</td>
  <td >-1</td>
  <td >0</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td ></td>
 </tr>
 <tr >
  <td >1000149</td>
  <td>dr1rrb/smarthome.net</td>
  <td>https://github.com/dr1rrb/smarthome.net/commit/646232e0a1c757b89a40c7ed25b9a54ee929506f</td>
  <td >src/SmartHomeDotNet
  .Package/SmartHomeDotNet.Package.csproj</td>
  <td>.NETStandard2.0</td>
  <td >6</td>
  <td >24</td>
  <td >2</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >38</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >5</td>
  <td >6</td>
  <td >35</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >5</td>
  <td >-6</td>
  <td >-3</td>
  <td >-1</td>
  <td >0</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td ></td>
 </tr>
 <tr >
  <td >1000152</td>
  <td>jernejk/EfCoreSamples.Logging</td>
  <td>https://github.com/jernejk/EfCoreSamples.Logging/commit/bfdaf92d4a9576f3ec42995ee6a851dea55669f6</td>
  <td >EfCoreSamples.Loggin
  g.Web/EfCoreSamples.Logging.Web.csproj</td>
  <td>net5.0</td>
  <td >13</td>
  <td >75</td>
  <td >7</td>
  <td >0</td>
  <td >7</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >130</td>
  <td >2</td>
  <td >5</td>
  <td >0</td>
  <td >5</td>
  <td >12</td>
  <td >22</td>
  <td >135</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >21</td>
  <td >-22</td>
  <td >5</td>
  <td >-5</td>
  <td >0</td>
  <td >9</td>
  <td >0.50 </td>
  <td >0.38 </td>
  <td >0.38 </td>
  <td ></td>
 </tr>
 <tr >
  <td >1000153</td>
  <td>jernejk/EfCoreSamples.Logging</td>
  <td>https://github.com/jernejk/EfCoreSamples.Logging/commit/1fa9b4196ee2d0ad59fcaba6f4b224685ffba087</td>
  <td >EfCoreSamples.Loggin
  g.Web/EfCoreSamples.Logging.Web.csproj</td>
  <td>net5.0</td>
  <td >13</td>
  <td >75</td>
  <td >7</td>
  <td >0</td>
  <td >7</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >0</td>
  <td >130</td>
  <td >4</td>
  <td >5</td>
  <td >0</td>
  <td >5</td>
  <td >12</td>
  <td >22</td>
  <td >135</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >21</td>
  <td >-22</td>
  <td >5</td>
  <td >-5</td>
  <td >0</td>
  <td >9</td>
  <td >0.50 </td>
  <td >0.38 </td>
  <td >0.38 </td>
  <td ></td>
 </tr>
 <tr >
  <td >1000154</td>
  <td>ztytotoro/Blog.Service</td>
  <td>https://github.com/ztytotoro/Blog.Service/commit/986442695af6e0a74fd74134955a472dc5e19657</td>
  <td >Blog.Service/Blog.Servi
  ce.csproj</td>
  <td>net5.0</td>
  <td >7</td>
  <td >119</td>
  <td >0</td>
  <td >2</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >101</td>
  <td >6</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >7</td>
  <td >15</td>
  <td >137</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >14</td>
  <td >-15</td>
  <td >36</td>
  <td >-1</td>
  <td >-1</td>
  <td >7</td>
  <td >0.43 </td>
  <td >0.43 </td>
  <td >0.18 </td>
  <td ></td>
 </tr>
 <tr >
  <td >1000155</td>
  <td>matteogarato/HellsGate</td>
  <td>https://github.com/matteogarato/HellsGate/commit/94ae32d5cf86a2fb60eb8a36f1f77621201cac38</td>
  <td >HellsGate.MVC/HellsG
  ate.MVC.csproj</td>
  <td>net5.0</td>
  <td >8</td>
  <td >137</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >146</td>
  <td >10</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >7</td>
  <td >8</td>
  <td >146</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >8</td>
  <td >-8</td>
  <td >0</td>
  <td >-1</td>
  <td >0</td>
  <td >1</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.56 </td>
  <td ></td>
 </tr>
 <tr >
  <td >1000159</td>
  <td>Christopher-Shi/Chris.Personnel.Management</td>
  <td>https://github.com/Christopher-Shi/Chris.Personnel.Management/commit/35fd5f86c0d3c8b65a7c146ed2a40e3eed7d5165</td>
  <td >Back-end-code/Chris.P
  ersonnel.Management.API/Chris.Personnel.Management.API.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >9</td>
  <td >101</td>
  <td >0</td>
  <td >1</td>
  <td >4</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >120</td>
  <td >4</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >7</td>
  <td >10</td>
  <td >107</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >7</td>
  <td >-10</td>
  <td >-13</td>
  <td >-2</td>
  <td >0</td>
  <td >0</td>
  <td >0.63 </td>
  <td >0.63 </td>
  <td >0.18 </td>
  <td ></td>
 </tr>
 <tr >
  <td >1000161</td>
  <td>attuo/MyWebAPITemplate</td>
  <td>https://github.com/attuo/MyWebAPITemplate/commit/121a6fe800313ddb6a090f20c70cfae87e2bc87b</td>
  <td >src/Web/Web.csproj</td>
  <td>net5.0</td>
  <td >12</td>
  <td >222</td>
  <td >2</td>
  <td >3</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >217</td>
  <td >4</td>
  <td >1</td>
  <td >0</td>
  <td >4</td>
  <td >10</td>
  <td >18</td>
  <td >191</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >11</td>
  <td >-18</td>
  <td >-26</td>
  <td >-1</td>
  <td >-4</td>
  <td >1</td>
  <td >0.36 </td>
  <td >0.36 </td>
  <td >0.27 </td>
  <td ></td>
 </tr>
 <tr >
  <td >1000166</td>
  <td>daxnet/abacuza</td>
  <td>https://github.com/daxnet/abacuza/commit/b0835392a2c65ea95793e23bc6ebb6a872383932</td>
  <td >src/services/jobs/Abac
  uza.Jobs.ApiService/Abacuza.Jobs.ApiService.csproj</td>
  <td>net5.0</td>
  <td >10</td>
  <td >142</td>
  <td >0</td>
  <td >3</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >110</td>
  <td >4</td>
  <td >1</td>
  <td >0</td>
  <td >2</td>
  <td >10</td>
  <td >14</td>
  <td >113</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >11</td>
  <td >-14</td>
  <td >3</td>
  <td >-1</td>
  <td >-2</td>
  <td >1</td>
  <td >0.58 </td>
  <td >0.46 </td>
  <td >0.46 </td>
  <td ></td>
 </tr>
 <tr >
  <td >1000168</td>
  <td>arditmezini/api-core</td>
  <td>https://github.com/arditmezini/api-core/commit/b465385d1e206966c37f806862073263fbe75fb5</td>
  <td >AspNetCoreApi.Api/As
  pNetCoreApi.Api.csproj</td>
  <td>net5.0</td>
  <td >25</td>
  <td >202</td>
  <td >2</td>
  <td >1</td>
  <td >3</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >0</td>
  <td >188</td>
  <td >2</td>
  <td >4</td>
  <td >0</td>
  <td >6</td>
  <td >20</td>
  <td >32</td>
  <td >186</td>
  <td >0</td>
  <td >4</td>
  <td >0</td>
  <td >4</td>
  <td >22</td>
  <td >-32</td>
  <td >-2</td>
  <td >-4</td>
  <td >-2</td>
  <td >2</td>
  <td >0.65 </td>
  <td >0.65 </td>
  <td >0.36 </td>
  <td ></td>
 </tr>
 <tr >
  <td >1000169</td>
  <td>shawnwildermuth/WilderBlog</td>
  <td>https://github.com/shawnwildermuth/WilderBlog/commit/9e828ffdc6e04c72a9a09253b738f83ad33b4a1d</td>
  <td >src/WilderBlog/Wilder
  Blog.csproj</td>
  <td>net5.0</td>
  <td >14</td>
  <td >176</td>
  <td >0</td>
  <td >3</td>
  <td >5</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >159</td>
  <td >4</td>
  <td >3</td>
  <td >0</td>
  <td >7</td>
  <td >14</td>
  <td >27</td>
  <td >160</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >3</td>
  <td >23</td>
  <td >-27</td>
  <td >1</td>
  <td >-3</td>
  <td >-4</td>
  <td >9</td>
  <td >0.40 </td>
  <td >0.30 </td>
  <td >0.25 </td>
  <td ></td>
 </tr>
 <tr >
  <td >1000174</td>
  <td>eventflow/EventFlow</td>
  <td>https://github.com/eventflow/EventFlow/commit/b1880a2a303362fa44b580a4a41e6e2368312506</td>
  <td >Source/EventFlow.Owi
  n.Tests/EventFlow.Owin.Tests.csproj</td>
  <td>.NETFramework4.7.2</td>
  <td >6</td>
  <td >6</td>
  <td >0</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >6</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >3</td>
  <td >5</td>
  <td >6</td>
  <td >6</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >1</td>
  <td >3</td>
  <td >-6</td>
  <td >0</td>
  <td >-2</td>
  <td >-2</td>
  <td >-2</td>
  <td >0.75 </td>
  <td >0.75 </td>
  <td >0.75 </td>
  <td ></td>
 </tr>
 <tr >
  <td >1000177</td>
  <td>yotkoKanchev/LetsSport</td>
  <td>https://github.com/yotkoKanchev/LetsSport/commit/9a6c034f48350798b66878017a821291ba08f045</td>
  <td >Web/LetsSport.Web/L
  etsSport.Web.csproj</td>
  <td>net5.0</td>
  <td >15</td>
  <td >152</td>
  <td >2</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >165</td>
  <td >8</td>
  <td >3</td>
  <td >0</td>
  <td >2</td>
  <td >14</td>
  <td >26</td>
  <td >184</td>
  <td >0</td>
  <td >5</td>
  <td >0</td>
  <td >1</td>
  <td >20</td>
  <td >-26</td>
  <td >19</td>
  <td >-3</td>
  <td >-1</td>
  <td >6</td>
  <td >0.45 </td>
  <td >0.45 </td>
  <td >0.38 </td>
  <td ></td>
 </tr>
 <tr >
  <td >1000178</td>
  <td>dzimchuk/book-fast-docker</td>
  <td>https://github.com/dzimchuk/book-fast-docker/commit/b379091a244426816bd6241b39cc1cbed3f57d77</td>
  <td >BookFast.Web/BookFa
  st.Web.csproj</td>
  <td>net5.0</td>
  <td >6</td>
  <td >152</td>
  <td >0</td>
  <td >2</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >184</td>
  <td >4</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >10</td>
  <td >137</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >1</td>
  <td >9</td>
  <td >-10</td>
  <td >-47</td>
  <td >-1</td>
  <td >1</td>
  <td >4</td>
  <td >0.83 </td>
  <td >0.57 </td>
  <td >0.38 </td>
  <td ></td>
 </tr>
 <tr >
  <td >1000179</td>
  <td>dzimchuk/book-fast-docker</td>
  <td>https://github.com/dzimchuk/book-fast-docker/commit/c359866d3efffde9adedc5dd2f41db3b1cb4e8aa</td>
  <td >BookFast.Web/BookFa
  st.Web.csproj</td>
  <td>.NETCoreApp3.1</td>
  <td >6</td>
  <td >152</td>
  <td >0</td>
  <td >2</td>
  <td >2</td>
  <td >0</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >179</td>
  <td >2</td>
  <td >1</td>
  <td >0</td>
  <td >0</td>
  <td >5</td>
  <td >10</td>
  <td >137</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >1</td>
  <td >9</td>
  <td >-10</td>
  <td >-42</td>
  <td >-1</td>
  <td >1</td>
  <td >4</td>
  <td >0.83 </td>
  <td >0.57 </td>
  <td >0.38 </td>
  <td ></td>
 </tr>
 <tr >
  <td >1000186</td>
  <td>I-Synergy/I-Synergy.Framework</td>
  <td>https://github.com/I-Synergy/I-Synergy.Framework/commit/38419792134ba7ae6a0a43e4c5eceb4e97cc21ed</td>
  <td >samples/ISynergy.Fra
  mework.UI.Sample/ISynergy.Framework.UI.Sample.Skia.Gtk/ISynergy.Framework.UI.Sample.Skia.Gtk.csproj��samples/ISynergy.Framework.UI/Sample.Skia.Gtk/Sample.Skia.Gtk.csproj</td>
  <td>net5.0</td>
  <td >5</td>
  <td >71</td>
  <td >0</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >70</td>
  <td >0</td>
  <td >3</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >4</td>
  <td >70</td>
  <td >0</td>
  <td >2</td>
  <td >0</td>
  <td >0</td>
  <td >3</td>
  <td >-4</td>
  <td >0</td>
  <td >-3</td>
  <td >0</td>
  <td >0</td>
  <td >1.00 </td>
  <td >1.00 </td>
  <td >0.33 </td>
  <td ></td>
 </tr>
 </tbody></table>
### USER STUDY DATASET

<a href="https://github.com/nufix-dependency-maze/nufix/blob/gh-pages/A Survey for dependency issue patches.zip?raw=true">A Survey for dependency issue patches.zip</a>
