# Version schemes

## Package ecosystem version schemes

To better understand the package versioning problem, here are 
some of the many notations and conventions in use:

- [semver](https://semver.org/) is a popular specification to
  structure version strings, but does not provide a way to express
  version ranges.
- RubyGems strongly suggests using "semver" for versioning but does not
  enforce it. As a result some gems use "semver" while several popular
  packages do not use strict "semver". RubyGems uses their own notation
  for version ranges which looks like the "node-semver" notation with
  some subtle differences. See:
  https://guides.rubygems.org/patterns/#semantic-versioning
- "node-semver" ranges are used in npm at
  https://github.com/npm/node-semver#ranges with range semantics
  that are specific to "semver" versions and npm.
- The Dart pub versioning scheme is similar to "node-semver". Version
  resolution uses its own algorithm. See: https://dart.dev/tools/pub/versioning 
- Python uses its own version and version range notation with notable
  peculiarities for how pre-release and post-release suffixes are used.
  See: https://www.python.org/dev/peps/pep-0440/
- Debian and Ubuntu use their own notation and are known for
  their use of "epochs' to disambiguate versions. See:
  https://www.debian.org/doc/debian-policy/ch-relationships.html
- RPM distros use their own range notation and use "epochs" like Debian.
  See: https://rpm-software-management.github.io/rpm/manual/dependencies.html
- Perl CPAN defines its own version range notation similar to VERS
  with two-segment versions. See:
  https://metacpan.org/pod/CPAN::Meta::Spec#Version-Ranges
- Apache Maven and NuGet use similar math interval notation using
  brackets. See: https://en.wikipedia.org/wiki/Interval_(mathematics)
    - Apache Maven
      http://maven.apache.org/enforcer/enforcer-rules/versionRanges.html
    - NuGet
      https://docs.microsoft.com/en-us/nuget/concepts/package-versioning#version-ranges
- gradle uses Apache Maven notation with some extensions. See:
  https://docs.gradle.org/current/userguide/single_versions.html
- Gentoo and Alpine Linux use comparison operators similar to VERS:
    - Gentoo https://wiki.gentoo.org/wiki/Version_specifier
    - Alpine linux
      https://gitlab.alpinelinux.org/alpine/apk-tools/-/blob/master/src/version.c
- Arch Linux https://wiki.archlinux.org/title/PKGBUILD#Dependencies
  uses its own simplified notation for its PKGBUILD depends array and
  uses a modified RPM version comparison.
- Go modules use "semver" versions with specific version resolution algorithms.
  See: https://golang.org/ref/mod#versions
- The Haskell Package Versioning Policy   provides a notation similar to VERS
  based on a modified "semver" with extra notations such as star and caret.
  See:  https://pvp.haskell.org/
- The NVD defines CPE ranges as lists of version start and end versions
  either including or excluding the start or end version. NVD also provides
  an enumeration of the available ranges as a daily feed.
  See: https://nvd.nist.gov/vuln/data-feeds#cpeMatch
- Version 5 of the CVE JSON data format defines version ranges with a
  **starting version**, a **versionType**, and an upper limit for the
  version range as 'lessThan' or 'lessThanOrEqual'; or as an enumeration
  of versions. The **versionType** is defined as "The version numbering
  system used   for specifying the range. This defines the exact semantics
  of the comparison (less-than) operation on versions, which is required
  to understand the range itself".
  A **versionType** resembles closely the Package-URL package **type**.
  See: https://github.com/CVEProject/cve-schema/blob/master/schema/v5.0/CVE_JSON_5.0.schema#L303
- The OSSF OSV schema defines vulnerable ranges with version events using
  "introduced", "fixed" and "limit" fields and an optional enumeration of all
  versions in these ranges, except for "semver"-based versions. A range may be
  ecosystem-specific based on a provided package "ecosystem" value
  that resembles the Package-URL package "type". See: https://ossf.github.io/osv-schema/ 

The way two versions are compared as equal, less than or greater than is a
closely related topic:

- Each package ecosystem may have evolved its own specific version
  string conventions, semantics and comparison procedure. For instance,
  "semver" is a prominent specification in this domain but it is just
  one of the many ways to structure a version string.
- Debian, RPM, PyPI, RubyGems, and Composer have their own subtly
  different approaches to determine how two versions are compared
  as equal, greater than or less than.

## PURL Type version schemes

The following tables lists the known versioning schemes for some common Package-URL
**types** (aka. "ecosystem").

| PURL type | Description   | Reference URL      |                                                                                                                                                                                                         
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| deb       | Debian and Ubuntu use these comparators: <, <=, =, >= and >>   | [https://www.debian.org/doc/debian-policy/ch-relationships.html](https://www.debian.org/doc/debian-policy/ch-relationships.html) |
| rpm       | RPM distros. A simplified rmpvercmp version comparison routine is used by Arch Linux Pacman. | https://rpm-software-management.github.io/rpm/manual/dependencies.html |
| gem       | RubyGems uses a version scheme that is similar to "node-semver" for its syntax, but it does not use "semver" versions. | https://guides.rubygems.org/patterns/#semantic-versioning |
| npm       | npm uses "node-semver" which is based on "semver" with its own  range notation. Several other package types  use "node-semver"-like ranges, but most of these related version schemes do not implement "node-semver". | https://github.com/npm/node-semver#ranges 
| cargo     | Cargo for Rust uses a version scheme that is similar to "node-semver". |  https://doc.rust-lang.org/cargo/reference/specifying-dependencies.html  |
| composer  | Composer for PHP  | https://getcomposer.org/doc/articles/versions.md |
| pypi      | PyPI for Python   | https://www.python.org/dev/peps/pep-0440/   |
| cpan      | CPAN              | https://perlmaven.com/how-to-compare-version-numbers-in-perl-and-for-cpan-modules  |
| golang    | Go modules use "semver" versions with a specific minimum version resolution algorithm.   | https://golang.org/ref/mod#versions|
| maven     | Apache Maven supports a math interval notation which is rarely used elsewhere. | http://maven.apache.org/enforcer/enforcer-rules/versionRanges.html  |
| nuget     | Nuget and Apache Maven follow a similar approach with a math-derived interval syntax as in https://en.wikipedia.org/wiki/Interval_(mathematics)  | https://docs.microsoft.com/en-us/nuget/concepts/package-versioning#version-ranges |
| gentoo    | Gentoo Linux  | https://wiki.gentoo.org/wiki/Version_specifier |   
| alpine    | Alpine Linux uses Gentoo-like conventions. | https://gitlab.alpinelinux.org/alpine/apk-tools/-/blob/master/src/version.c |

## Generic version schemes

These are generic schemes, to be used sparingly for special cases:

- **generic**: a generic version comparison algorithm (which will be
  specified later, likely based on a split on any wholly alpha or
  wholly numeric segments and dealing with digit and string
  comparisons, similar to libversion)
- **none**: a generic versioning scheme for a range containing no
  versions. 'vers:none/*' is the only valid VERS form for this scheme.
- **all**: a generic versioning scheme for a range containing all
  versions. 'vers:all/*' is the only valid VERS form for this scheme.
- **intdot**: a generic versioning scheme that allows version
  components to be specified as integers separated by dots, e.g.
  '10.234.5.12'. Versions specified in this scheme consist of ASCII
  digits only, formatted with only non-negative integers, and ignoring
  leading zeros. Interpretation of the version should stop at the
  first character that is not a digit or a dot.
- **lexicographic**: a generic versioning scheme that compares
  versions based on lexicographic order, interpreted as UTF-8. Strings
  should be compared bytewise as unsigned bytes without normalization.
  UTF-8 encoding is defined in https://datatracker.ietf.org/doc/html/rfc3629.
- **semver**: a generic scheme that uses the same syntax as `semver`.
  It follows the MAJOR.MINOR.PATCH format and is defined in the
  Semantic Versioning Specification 2.0.0. See
  https://semver.org/spec/v2.0.0.html.
- **datetime**: a generic scheme that uses a timestamp for comparison.
  The timestamp must adhere to RFC3339, section 5.6. See
  https://www.rfc-editor.org/rfc/rfc3339#section-5.6.
