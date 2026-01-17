# Version schemes

## Package ecosystem version schemes

To better understand the problem, here are some of the many notations
and conventions in use:

- `semver` https://semver.org/ is a popular specification to
  structure version strings, but does not provide a way to express
  version ranges.
- RubyGems strongly suggests using `semver` for version but does not
  enforce it. As a result some gems use semver while several popular
  packages do not use strict semver. RubyGems uses their own notation
  for version ranges which looks like the `node-semver` notation with
  some subtle differences. See
  https://guides.rubygems.org/patterns/#semantic-versioning
- `node-semver` ranges are used in npm at
  https://github.com/npm/node-semver#ranges with range semantics
  that are specific to `semver` versions and npm.
- Dart pub versioning scheme is similar to `node-semver` and the
  documentation at https://dart.dev/tools/pub/versioning provides a
  comprehensive coverage of the topic of versioning. Version
  resolution uses its own algorithm.
- Python uses its own version and version ranges notation with notable
  peculiarities on how pre-release and post-release suffixes are used
  https://www.python.org/dev/peps/pep-0440/
- Debian and Ubuntu use their own notation and are remarkable for
  their use of `epochs` to disambiguate versions.
  https://www.debian.org/doc/debian-policy/ch-relationships.html
- RPM distros use their own range notation and use epochs like Debian.
  https://rpm-software-management.github.io/rpm/manual/dependencies.html
- Perl CPAN defines its own version range notation similar to this
  specification and uses two-segment versions.
  https://metacpan.org/pod/CPAN::Meta::Spec\#Version-Ranges
- Apache Maven and NuGet use similar math intervals notation using
  brackets https://en.wikipedia.org/wiki/Interval_(mathematics)
    - Apache Maven
      http://maven.apache.org/enforcer/enforcer-rules/versionRanges.html
    - NuGet
      https://docs.microsoft.com/en-us/nuget/concepts/package-versioning#version-ranges
- gradle uses Apache Maven notation with some extensions
  https://docs.gradle.org/current/userguide/single_versions.html
- Gentoo and Alpine Linux use comparison operators similar to this
  specification:
    - Gentoo https://wiki.gentoo.org/wiki/Version_specifier
    - Alpine linux
      https://gitlab.alpinelinux.org/alpine/apk-tools/-/blob/master/src/version.c
- Arch Linux https://wiki.archlinux.org/title/PKGBUILD#Dependencies
  uses its own simplified notation for its PKGBUILD depends array and
  uses a modified RPM version comparison.
- Go modules https://golang.org/ref/mod#versions use `semver`
  versions with specific version resolution algorithms.
- Haskell Package Versioning Policy https://pvp.haskell.org/
  provides a notation similar to this specification based on a
  modified semver with extra notations such as star and caret.
- The NVD https://nvd.nist.gov/vuln/data-feeds#cpeMatch defines CPE
  ranges as lists of version start and end either including or
  excluding the start or end version. And also provides a concrete
  enumeration of the available ranges as a daily feed.
- The version 5 of the CVE JSON data format at
  https://github.com/CVEProject/cve-schema/blob/master/schema/v5.0/CVE_JSON_5.0.schema#L303
  defines version ranges with a starting version, a versionType, and
  an upper limit for the version range as lessThan or lessThanOrEqual;
  or an enumeration of versions. The versionType is defined as `"The
  version numbering system used for specifying the range. This defines
  the exact semantics of the comparison (less-than) operation on
  versions, which is required to understand the range itself"`. A
  "versionType" resembles closely the Package-URL package "type".
- The OSSF OSV schema https://ossf.github.io/osv-schema/ defines
  vulnerable ranges with version events using "introduced", "fixed"
  and "limit" fields and an optional enumeration of all the versions
  in these ranges, except for semver-based versions. A range may be
  ecosystem-specific based on a provided package "ecosystem" value
  that resembles closely the Package-URL package "type".

The way two versions are compared as equal, lesser or greater is a
closely related topic:

- Each package ecosystem may have evolved its own peculiar version
  string conventions, semantics and comparison procedure.
- For instance, `semver` is a prominent specification in this domain
  but this is just one of the many ways to structure a version string.
- Debian, RPM, PyPI, RubyGems, and Composer have their own subtly
  different approach to determine how two versions are compared
  as equal, greater or lesser.

## PURL Type version schemes

## Some of the known versioning schemes

These are a few known versioning schemes for some common Package-URL
<span class="title-ref">types</span> (aka. `ecosystem`).

- **deb**: Debian and Ubuntu
  https://www.debian.org/doc/debian-policy/ch-relationships.html
  Debian uses these comparators: \<\<, \<=, =, \>= and \>\>.
- **rpm**: RPM distros
  https://rpm-software-management.github.io/rpm/manual/dependencies.html
  A simplified rmpvercmp version comparison routine is used by
  Arch Linux Pacman.
- **gem**: RubyGems
  https://guides.rubygems.org/patterns/#semantic-versioning which is
  similar to `node-semver` for its syntax, but does not use semver
  versions.
- **npm**: npm uses node-semver which is based on semver with its own
  range notation https://github.com/npm/node-semver#ranges A similar
  but different scheme is used by Rust
  https://doc.rust-lang.org/cargo/reference/specifying-dependencies.html
  and several other package types may use `node-semver`-like ranges.
  But most of these related schemes are not strictly the same as what
  is implemented in `node-semver`. For instance PHP `composer` may
  need its own scheme as this is not strictly `node-semver`.
- **composer**: PHP https://getcomposer.org/doc/articles/versions.md
- **pypi**: Python https://www.python.org/dev/peps/pep-0440/
- **cpan**: Perl
  https://perlmaven.com/how-to-compare-version-numbers-in-perl-and-for-cpan-modules
- **golang**: Go modules https://golang.org/ref/mod#versions use
  `semver` versions with a specific minimum version resolution
  algorithm.
- **maven**: Apache Maven supports a math interval notation which is
  rarely seen in practice
  http://maven.apache.org/enforcer/enforcer-rules/versionRanges.html
- **nuget**: NuGet
  https://docs.microsoft.com/en-us/nuget/concepts/package-versioning#version-ranges
  Note that Apache Maven and NuGet are following a similar approach
  with a math-derived intervals syntax as in
  https://en.wikipedia.org/wiki/Interval_(mathematics)
- **gentoo**: Gentoo https://wiki.gentoo.org/wiki/Version_specifier
- **alpine**: Alpine linux
  https://gitlab.alpinelinux.org/alpine/apk-tools/-/blob/master/src/version.c
  which is using Gentoo-like conventions.

## Generic version schemes

These are generic schemes, to use sparingly for special cases:

- **generic**: a generic version comparison algorithm (which will be
  specified later, likely based on a split on any wholly alpha or
  wholly numeric segments and dealing with digit and string
  comparisons, like is done in libversion)
- **none**: a generic versioning scheme for a range containing no
  version. `vers:none/*` is the only valid vers form for this scheme.
- **all**: a generic versioning scheme for a range containing all
  versions. `vers:all/*` is the only valid vers form for this scheme.
- **intdot**: a generic versioning scheme that allows version
  components to be specified as integers separated by dots, e.g.
  `10.234.5.12`. Versions specified in this scheme consist of ASCII
  digits only, formatted with only non-negative integers, and ignoring
  leading zeros. Interpretation of the version should stop at the
  first character that is not a digit or a dot.
- **lexicographic**: a generic versioning scheme that compares
  versions based on lexicographic order, interpreted as UTF-8. Strings
  should be compared bytewise as unsigned bytes without normalization.
  UTF-8 encoding is defined in https://datatracker.ietf.org/doc/html/rfc3629.
- **semver**: a generic scheme that uses the same syntax as `semver`.
  It follows the MAJOR.MINOR.PATCH format and is defined in the
  Semantic Versioning Specification 2.0.0, see
  https://semver.org/spec/v2.0.0.html.
- **datetime**: a generic scheme that uses a timestamp for comparison.
  The timestamp must adhere to RFC3339, section 5.6, see
  https://www.rfc-editor.org/rfc/rfc3339#section-5.6.
