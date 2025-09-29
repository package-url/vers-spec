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


## Users, adopters and links

See the [dedicated adopters list](ADOPTERS.md).


## License

This document is licensed under the MIT license.
