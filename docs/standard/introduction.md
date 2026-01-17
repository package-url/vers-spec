# Introduction

This specification is a new syntax for dependency and vulnerable version
ranges.

## Context

Software package version ranges and version constraints are essential:

- When resolving the dependencies of a package to express which subset
  of the versions are supported. For instance a dependency or
  requirement statement such as "I require package foo, version 2.0 or
  later versions" defines a range of acceptable foo versions.
- When stating that a known vulnerability or bug affects a range of
  package versions. For instance a security advisory such as
  "vulnerability 123 affects package bar, version 3.1 and version 4.2
  but not version 5" defines a range of vulnerable "bar" package
  versions.

Version ranges can be replaced by a list enumerating all the versions of
interest. But in practice, all the versions may not yet exist when
defining an open version range such as "v2.0 or later".

Therefore, a version range is a necessary, compact and practical way to
reference multiple versions rather than listing all the versions.

## Problem

Several version range notations exist and have evolved separately to
serve the specific needs of each package ecosystem, vulnerability
databases and tools.

There is no (mostly) universal notation for version ranges and there is
no universal way to compare two versions, even though the concepts that
exist in most version range notations are similar.

Each package type or ecosystem may define their own ranges notation and
version comparison semantics for dependencies. And for security
advisories, the lack of a portable and compact notation for vulnerable
package version ranges means that these ranges may be either ambiguous
or hard to compute and may be best replaced by complete enumerations of
all impacted versions, such as in the [NVD CPE Match
feed](https://nvd.nist.gov/vuln/data-feeds#cpeMatch).

Because of this, expressing and resolving a version range is often a
complex, error prone task.

In particular the need for common notation for version has emerged based
on the usage of Package-URLs referencing vulnerable package version
ranges such as in vulnerability databases like
[VulnerableCode](https://github.com/nexB/vulnerablecode/).

## Solution

A solution to the many version range syntaxes is to design a new
simplified notation to unify them all with:

- a mostly universal and minimalist, compact notation to express
  version ranges from many different package types and ecosystems.
- the package type-specific definitions to normalize existing range
  expressions in this common notation.
- the designation of which algorithm or procedure to use when
  comparing two versions such that it is possible to resolve if a
  version is within or outside of a version range.

We call this solution "VErsion Range Specifier" or VERS and it is
described in this document.
