# 1 Scope
This Standard defines the Version Range Specifier (VERS) syntax for specifying
a software version range notation as a compact alternative to enumerating a
list of software versions. The primary use cases for VERS are identifying
software package versions that are impacted by a vulnerability and analyzing
software package version dependencies.

A VERS notation is a valid URI composed of two components to identify a
software package. The VERS type component defines the ecosystem-specific
structure and meaning for the VERS constraints component. This Standard
specifies the syntax for VERS and the schema for defining VERS types, but it
does not include any specific VERS type definitions.

This edition of the Standard supports linear versioning where the software
versions do not branch to form a tree of versions. For tree-based versioning
with branches, a possible solution is to use multiple VERS until direct
support for tree use cases is implemented in a future version of the Standard.