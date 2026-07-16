# VERS types

There is a very wide range of software version schemes. For the development of
the VERS specification, we are focused on three categories of VERS **types**:

- Package ecosystem VERS **types**: Our initial focus is to define VERS 
**types** for packages with a registered [PURL (Package-URL) **type**](https://package-url.github.io/www.packageurl.org/docs/purl/purl-spec-purl-types#registered-purl-types).
- Special VERS **types** : These "generic" version schemes should be reserved 
for special cases.

## Package ecosystem VERS types
Most software package ecosystems have a version scheme. Some variation of 
[SemVer](https://semver.org/) is the most popular approach to structure a 
version string, but it does not provide a way to express version ranges.

The following table lists versioning schemes for some common registered [PURL 
(Package-URL) **types**](https://package-url.github.io/www.packageurl.org/docs/purl/purl-spec-purl-types#registered-purl-types). If there is a registered PURL 
**type** for a package ecosystem, the PURL type will also be the name for the 
VERS **type**.

| type | Description   | Reference URL      |            
| --------- | --------------| ------------------ |
| alpm   | Arch Linux uses its own simplified notation for its PKGBUILD depends array and uses a modified RPM version comparison. | https://wiki.archlinux.org/title/PKGBUILD#Dependencies|
| apk    | Alpine Linux uses comparison operators similar to VERS.              | https://gitlab.alpinelinux.org/alpine/apk-tools/-/blob/master/src/version.c|
| cargo     | Cargo for Rust uses a version scheme that is similar to "node-semver". |  https://doc.rust-lang.org/cargo/reference/specifying-dependencies.html |
| composer  | Composer for PHP  | https://getcomposer.org/doc/articles/versions.md |
| cpan      | Perl CPAN defines its own version range notation similar to VERS with two-segment versions. |  https://metacpan.org/pod/CPAN::Meta::Spec#VERSION-NUMBERS <br> https://perlmaven.com/how-to-compare-version-numbers-in-perl-and-for-cpan-modules  |
| dart | The Dart pub versioning scheme is similar to "node-semver". Version resolution uses its own algorithm. | https://dart.dev/tools/pub/versioning |
| deb       | Debian and Ubuntu use their own native notation and are known for their use of "epochs" to disambiguate versions. Their native comparators are '<<', '<=', '=', '>=' and '>>'. As '<<' and '>>' are not allowed as comparators in VERS, tools should translate '<<' to '<' and '>>' to '>' when converting Debian ranges. | https://www.debian.org/doc/debian-policy/ch-relationships.html |
| gem       | RubyGems strongly suggests using SemVer for versioning but does not enforce it. As a result some popular packages do not use strict Semver. RubyGems uses their own notation for version ranges which is similar to the "node-semver" notation with some subtle differences. | https://guides.rubygems.org/patterns/#semantic-versioning |
| golang    | Go modules use SemVer versions with a specific minimum version resolution algorithm.   | https://golang.org/ref/mod#versions|
| hackage | The Haskell Package Versioning Policy provides a notation similar to VERS based on a modified SemVer with extra notations such as star and caret.   | https://pvp.haskell.org/  |
| maven     | Apache Maven uses a [math interval notation](https://en.wikipedia.org/wiki/Interval_(mathematics)) with brackets. | http://maven.apache.org/enforcer/enforcer-rules/versionRanges.html  |
| nuget     | Nuget uses a [math interval notation](https://en.wikipedia.org/wiki/Interval_(mathematics)) with brackets. | https://docs.microsoft.com/en-us/nuget/concepts/package-versioning#version-ranges |
| npm       | npm uses "node-semver" which is based on SemVer with its own  range notation. Several other package types use "node-semver"-like ranges, but most of these related version schemes do not implement "node-semver". | https://github.com/npm/node-semver#ranges |
| pypi      | Python uses its own version and version range notation with notable peculiarities for how pre-release and post-release suffixes are used. | https://www.python.org/dev/peps/pep-0440/   |
| rpm       | RPM distros use their own range notation and they use "epochs" like Debian. | https://rpm-software-management.github.io/rpm/manual/dependencies.html |

## Special VERS types

There are special "generic" VERS **types** to be used sparingly for special 
cases:

- **all**: a generic VERS **type** for a range containing all
versions. 'vers:all/*' is the only valid VERS form for this **type**.
- **datetime**: a generic VERS **type** that uses a timestamp for comparison.
The timestamp must adhere to RFC3339, section 5.6. See
https://www.rfc-editor.org/rfc/rfc3339#section-5.6.
- **generic**: a generic VERS **type** using a comparison algorithm which 
 will be specified later, likely based on a split on any wholly alpha or
 wholly numeric segments and dealing with digit and string
 comparisons, similar to libversion.
- **intdot**: a generic VERS **type** that allows version components to be 
specified as integers separated by dots, e.g. '10.234.5.12'. Versions 
specified in this scheme consist of ASCII digits only, formatted with only 
non-negative integers, and ignoring leading zeros. Interpretation of the 
version should stop at the first character that is not a digit or a dot.
- **lexicographic**: a generic VERS **type** that compares versions based on 
lexicographic order, interpreted as UTF-8. Strings should be compared 
byte-wise as unsigned bytes without normalization. UTF-8 encoding is defined 
in https://datatracker.ietf.org/doc/html/rfc3629.
- **none**: a generic VERS **type** for a range containing no versions. 
'vers:none/*' is the only valid VERS form for this scheme.
- **semver**: a VERS **type** that uses the same syntax as SemVer. It follows 
the MAJOR.MINOR.PATCH format and is defined in the Semantic Versioning 
Specification 2.0.0. See https://semver.org/spec/v2.0.0.html.

## Version comparison conventions

The way two versions are compared as equal, less than or greater than is 
closely related to VERS **types**.

- Each package ecosystem may have evolved its own specific version
  string conventions, semantics and comparison procedure. For instance,
  "semver" is a prominent specification in this domain but it is just
  one of the many ways to structure a version string.
- Debian, RPM, PyPI, RubyGems, and Composer have their own subtly
  different approaches to determine how two versions are compared
  as equal, greater than or less than.

