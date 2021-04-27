# NuFix Introduction 

.NET is an open-source development platform for building projects and sharing packages among them. As at March 2021, there are nine actively used and updated .NET platform variations available in 220 versions. A .NET package is often designed to assume a set of dependencies, which correspond to specific versions of .NET platforms and additional depended packages. These dependencies change as the .NET platforms and packages evolve, inducing compatibility issues. We call such issues Dependency Maze (DM) issues. We observe that multiple types of DM issues often occur in building a .NET project. Fixing a DM issue tends to introduce new DM issues. As a result, many fixes involve a set of changes made to a project's dependencies. Identifying these changes is challenging due to the large search space of finding possible dependency combinations.
 
To help .NET developers tackle the DM issues, we empirically studied a set of real DM issues, learning their common fixing strategies and developers' preferences in adopting these strategies. Based on these findings, we develop NuFix, an automated technique to repair DM issues. NuFix formulates the repair task as a binary integer linear optimization problem to effectively derive an optimal fix in line with the learnt developers' preferences. We applied NuFix to our benchmark containing 354 real DM issues with documented fixes. The evaluation results show that NuFix successfully generates fixes for all these DM issues.  The generated fixes are highly similar to the documented ones. Besides, we invited ten .NET experts to manually validate NuFix's generated fixes. Their feedback indicates that the fixes meet developers' desired properties for the build management of .NET projects.

# Empirical Study Dataset (RQ1-2)

 <a href="https://github.com/nufix-dependency-maze/nufix/blob/gh-pages/Benchmark.zip?raw=true">Empirical Study Dataset.xlsx</a>

# Benchmark (RQ3)

 <a href="https://github.com/nufix-dependency-maze/nufix/blob/gh-pages/Benchmark.zip?raw=true">Benchmark.zip</a>

# Expert Validation (RQ4)

<a href="https://github.com/nufix-dependency-maze/nufix/blob/gh-pages/A Survey for dependency issue patches.zip?raw=true">Expert feedback.zip</a>

# Expert Validation (RQ4)
![Octocat](https://raw.githubusercontent.com/nufix-dependency-maze/nufix/gh-pages/assets/images/download_png.png)
