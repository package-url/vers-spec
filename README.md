# Context

We build and release software by massively consuming and producing software
packages such as npms, RPMs, Rubygems, etc.


## Problem

Each package manager, platform, type or ecosystem has

- its own conventions and protocols to identify, locate and provision
  software packages and
- another set of conventions to define dependent version ranges and how to
  compare two package versions.

When tools, APIs and databases process or store multiple package types, it is
difficult to reference the same software package across tools in a uniform
way. This is a problem that Package-URL (PURL) tries to solve.

The problem of versions and version ranges is what this Version Range
Specifier (VERS) tries to solve. VERS grew from PURL and complements PURL.


## Specification details

The VERS specification consists of

- a core syntax definition and versioning scheme definitions stored in a
  single document:

  - [VERS core](VERSION-RANGE-SPEC.md): Defines the format, syntax, and rules
    used to represent and validate VERS

  and

- a collection of JSON test data stored in the /tests directory


## Adopters

VERS (VErsion Range Specifier) has been adopted by other specifications and is supported by many tools. The details are available on the [Package-URL website](https://www.packageurl.org/).
- See [Specifications](https://www.packageurl.org/#:~:text=PURL%20Adoption%20%2D%20Specifications) 
for the list of these specifications.
- See [Tools](https://www.packageurl.org/#:~:text=PURL%20v1.0-,Software%20Tools) 
for the list of these tools.

If you want to add a tool or specification that supports VERS please create an issue in the [Package-URL website repository](https://github.com/package-url/www.packageurl.org/issues). 
There are separate issue templates for 'Add a Tool' and 'Add a Specification" because the data fields are different.

**NB** There is a "staging website" for Package-URL at: https://package-url.github.io/www.packageurl.org/ 
that will have the most recent information about specifications and tools that
 have adopted PURL. We normally update the "production" website 
 at: https://www.packageurl.org/ weekly.


## License

This document is licensed under the MIT license.
