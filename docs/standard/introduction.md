# Introduction

This specification is a new syntax for dependency and vulnerable version
ranges.

## Context

Software package version ranges and version constraints are essential
for:

- Resolving the dependencies of a package to express which subset
  of versions are supported. For instance a dependency or
  requirement statement such as "I require package foo, version 2.0 or
  later versions" defines a range of acceptable "foo" versions.
- Stating that a known vulnerability or bug affects a range of
  package versions. For instance a security advisory such as
  "vulnerability 123 affects package bar, version 3.1 and version 4.2
  but not version 5" defines a range of vulnerable "bar" package
  versions.

Version ranges can be replaced by a list enumerating all versions of
interest for a package, but such a list cannot cover versions that do 
not exist when you create the list for an open version range such as 
"v2.0 or later". A version range is a necessary, compact, and practical 
way to reference multiple versions rather than listing all versions.

## Problem

Several version range notations exist and have evolved independently to
serve the specific needs of a package ecosystem, vulnerability
database or tools.

There is no universal notation for version ranges and there is
no universal way to compare two versions, even though the concepts in
most version range notations are similar.

Each package type or ecosystem may define its own range notation and
version comparison semantics for dependencies. For security
advisories, the lack of a portable and compact notation for vulnerable
package version ranges means that these ranges may be ambiguous
or hard to compute and may be replaced by complete enumerations of
all impacted versions, such as in the [NVD CPE Match
feed](https://nvd.nist.gov/vuln/data-feeds#cpeMatch). 

Expressing and resolving a version range is often a complex and error 
prone task because of the ambiguity and the use of enumerations of 
impacted versions that may require frequent updates.

This specfication for a common notation for version ranges emerged 
from the use of Package-URLs to reference vulnerable package version
ranges in vulnerability databases like
[VulnerableCode](https://github.com/nexB/vulnerablecode/).

*[I think the URL ^ should be https://github.com/aboutcode-org/vulnerablecode]*

## Solution

A solution to the many version range notation systems is to design 
a new simplified notation to unify them with:

- A mostly universal and minimalist, compact notation to express
  version ranges from many different package types and ecosystems.
- Package type-specific definitions to normalize existing range
  expressions in this common notation.
- The designation of which algorithm or procedure to use when
  comparing two versions so that it is possible to resolve whether
  a version is within or outside of a version range.

We call this solution "VErsion Range Specifier" or VERS.
