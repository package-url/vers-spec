# Introduction

There is no universal notation for software package version ranges and
there is no universal way to compare two versions of a package even though the
 concepts in many version range notations are similar. Each package type or 
 ecosystem may define its own version range notation and version comparison 
 semantics for dependencies.

For security advisories, the lack of a portable and compact notation for 
vulnerable package version ranges means that these ranges may be ambiguous
or hard to compute and may be replaced by complete enumerations of all 
impacted versions. Expressing and resolving a version range is often a complex 
and error prone task because of the ambiguity and the use of enumerations of 
impacted versions is an appproach that may require frequent updates. A version 
range is a necessary, compact, and practical way to reference multiple versions rather than listing all versions.

VErsion Range Specifier (VERS) introduces a standard URI-based syntax to 
define package version ranges and the semantics (algorithm or procedure) to 
interpret each version range notation. This standardization provides ensures 
more accurate and consistent analysis of package version dependencies and the 
impact of known vulnerabilities or bugs on a package. VERS was developed in 
concert with the Package-URL (PURL) specification standardized with [ECMA-427](https://ecma-tc54.github.io/ECMA-427/).

Challenges addressed by VERS:
- **Ambiguity of package dependencies**: With diverse version range notations 
across ecosystems, accurately and consistently identifying software package 
dependencies is a long-standing problem. VERS eliminates this ambiguity by 
creating a universal version range notation with a predictable structure.
- **Ambiguity of package versions affected by a vulnerability**: With diverse 
version range notations across ecosystems, accurately and consistently 
identifying software package versions affected by a vulnerability or bug is
extremely difficult. VERS eliminates this ambiguity by creating a universal 
version range notation with a predictable structure.
- **Tooling and Automation**: By standardizing version range analysis, VERS 
simplifies tooling development, automation, and integration for tasks such as 
software composition analysis and software vulnerability management.

As software supply chain security becomes a global priority, formalizing VERS
as an international standard supports its adoption and consistent 
implementation. Standardization under Ecma International Technical Committee
54 (TC54) positions VERS as a foundational building block for secure, 
transparent, and efficient software ecosystems worldwide.

By enabling a universally recognized and implementable specification, VERS 
aligns with global efforts to improve the security, reliability, and 
accountability of software supply chains. Its adoption ensures that 
organizations and developers can rely on a common way to specify and interpret
package version ranges for managing package dependency resolution and software
vulnerability analysis and mitigation.
