# VERS specification

## Version range specifier

A version range specifier (aka. VERS) is a URI string using the VERS
URI-scheme composed of three components:

    vers:<versioning-scheme>/<version-constraint>

The `<version-constraint>` component may be repeated as many times as needed
to accurately reflect the intended range(s) with this syntax:

    vers:<versioning-scheme>/<version-constraint>|<version-constraint>|...

*[JMH: The following table needs to be fleshed out to adequately name and
describe the components.]*

Table 1 —  Components of a VERS

| Component  | Requirement | Description|
| ---------- | ----------- |:------------------------------------------------------ |
| scheme     | Required    | The URL scheme with the constant value of "vers". |
| versioning-scheme       | Required    | The version specification or "scheme" such as "semver", "npm", "deb", etc. |
| version-constraint  | Required    | [To come]. |

*[JMH: the following VERS example seems to interpret the 1st pipe as "or" and
the 2nd pipe as "but" -- why an inconsistent use of the pipe, rather than some
not-yet-used character/symbol?  In any event, we need a clear and complete
description of the separators and their respective uses.]*

For example, to define a set of versions that contains either version
"1.2.3", or any versions greater than or equal to "2.0.0" but less than
"5.0.0" using the "node-semver" versioning scheme used with the "npm"
PURL **type**, the version range specifier will be:

    vers:npm/1.2.3|>=2.0.0|<5.0.0

VERS is the URI-scheme and is an acronym for "VErsion Range
Specifier". It has been selected because it is short, obviously about
version and available for a future formal URI-scheme registration at
IANA.

The pipe "|" is used as a simple separator between
`<version-constraint>`. Each `<version-constraint>` in this
pipe-separated list contains a comparator and a version:

    <comparator:version>

This list of `<version-constraint>` components is a signpost in the version
timeline of a package that specifies version intervals.

*[JMH: what does `<version>` refer to in the following sentence -- a
component, something else?]*

A `<version>` satisfies a version range specifier if it is contained
within any of the intervals defined by these `<version-constraint>`
components.

### Using version range specifiers

VERS primary usage is to test if a version is within a range.

A version is within a version range if falls in any of the intervals
defined by a range. Otherwise, the version is outside of the version
range.

Some important usages derived from this include:

- **Resolving a version range specifier to a list of concrete versions.**
  In this case, the input is one or more known versions of
  a package. Each version is then tested to check if it lies within or
  outside the range. For example, given a vulnerability and the VERS
  describing the vulnerable versions of a package, this process is
  used to determine if an existing package version is vulnerable.
- **Selecting one of several versions that are within a range.** In
  this case, given several versions that are within a range and
  several packages that express package dependencies qualified by a
  version range, a package management tool will determine and select
  the set of package versions that satisfy all the version range
  constraints of all dependencies. This usually requires deploying
  heuristics and algorithms (possibly complex such as sat solvers)
  that are ecosystem- and tool-specific and outside of the scope for
  this specification; yet VERS could be used in tandem with PURL
  to provide an input to this dependencies resolution process.

*[JMH: What are the "sat solvers" referred to in the 2nd bullet above?]*

### Examples

A single version in an "npm" package dependency:

- originally seen as a dependency on version "1.2.3" in a `package.json`
  manifest
- the version range spec is: `vers:npm/1.2.3`

A list of versions, enumerated:

- `vers:pypi/0.0.0|0.0.1|0.0.2|0.0.3|1.0|2.0pre1`

A complex statement about a vulnerability in a "maven" package that
affects multiple branches, each with their own fixed versions at
https://repo1.maven.org/maven2/org/apache/tomee/apache-tomee/. Note how
the constraints are sorted:

*[JMH: The link cited above does not contain the version values in the list
below.  What is the connection between the link contents and the list below?]*

- "affects Apache TomEE 8.0.0-M1 - 8.0.1, Apache TomEE 7.1.0 - 7.1.2,
  Apache TomEE 7.0.0-M1 - 7.0.7, Apache TomEE 1.0.0-beta1 - 1.7.5."
- a normalized version range spec is:
  `vers:maven/>=1.0.0-beta1|<=1.7.5|>=7.0.0-M1|<=7.0.7|>=7.1.0|<=7.1.2|>=8.0.0-M1|<=8.0.1`
- alternatively, four VERS express the same range, using one VERS
  for each of the vulnerable "branches":
    - `vers:tomee/>=1.0.0-beta1|<=1.7.5`
    - `vers:tomee/>=7.0.0-M1|<=7.0.7`
    - `vers:tomee/>=7.1.0|<=7.1.2`
    - `vers:tomee/>=8.0.0-M1|<=8.0.1`

Converting RubyGems custom syntax for dependency on gem. Note how the
pessimistic version constraint is expanded

*[JMH the 1st bullet below does not include the "<2.3.0" contained in the 2nd
bullet.]*:

- `'library', '~>2.2.0', '!=2.2.1'`
- the version range spec is: `vers:gem/>=2.2.0|!=2.2.1|<2.3.0`

### URI scheme

The VERS URI scheme is an acronym for "VErsion Range Specifier". It
has been selected because it is short, obviously about version and
available for a future formal registration for this URI-scheme at the
IANA registry.

The URI scheme is followed by a colon ":".

### `<versioning-scheme>`

The `<versioning-scheme>` (such as "npm", "deb", etc.) determines:

- the specific notation and conventions used for a version string
  encoded in this scheme. Versioning schemes often specify a version
  segments separator and the meaning of each version segment, such as
  [major.minor.patch] in "semver".
- how two versions are compared as greater or lesser to determine if a
  version is within or outside a range.
- how a versioning scheme-specific range notation can be transformed
  in the VERS simplified notation defined here.

By convention the versioning scheme **should** be the same as the
PURL package type for a given package ecosystem. It is OK to
have other schemes beyond the PURL type. A scheme could be specific to a
single package name.

The `<versioning-scheme>` is followed by a slash "/".

### `<version-constraint>`

After the `<versioning-scheme>` and "/" there are one or more
`<version-constraint>` components separated by a pipe "|". The pipe "|" has
no special meaning beside being a separator.

*[JMH: Re the pipe "has no special meaning" -- as noted re one example above,
the pipe is used in that example as both "or" and "but".  Why the
inconsistency?  Won't that confuse people? ]*

*[JMH: the next sentence refers to "this list" -- what list?]*

*[JMH: what is meant below by `<version>`?]*

Each `<version-constraint>` component of this list is either a single
`<version>` as in `1.2.3` for example or the combination of a `<comparator>`
and a `<version>` as in `>=2.0.0` using this syntax:

    <comparator><version>

A single version means that a version equal to this version
satisfies the range spec. Equality is based on the equality of two
normalized version strings according to their versioning scheme. For
most schemes, this is a simple string equality. But schemes can specify
normalization and rules for equality such as "pypi" with PEP 440.

The special star "\*" comparator matches any version. It must be
used **alone** exclusive of any other constraint and must not be followed
by a version. For example, `vers:deb/*` represents all the versions of a
Debian package. This includes past, current and possible future
versions.

Otherwise, the `<comparator>` is one of these comparison operators:

- "!=": Version exclusion or inequality comparator. This means a
  version must not be equal to the provided version that must be
  excluded from the range. For example: `!=1.2.3` means that version
  "1.2.3" is excluded.
- "\<", "\<=": Less than or less-or-equal version comparators
  point to all versions less than or equal to the provided version.
  For example `<=1.2.3` means less than or equal to "1.2.3".
- ">", ">=": Greater than or greater-or-equal version comparators
  point to all versions greater than or equal to the provided version.
  For example `>=1.2.3` means greater than or equal to "1.2.3".

The `<versioning-scheme>` defines:

- how to compare two version strings using these comparators, and
- the structure (if any) of a version string such as "1.2.3". For
  instance, the "semver" specification for version numbers defines a
  version as composed primarily of three dot-separated numeric
  segments named "major", "minor" and "patch".

## Normalized, canonical representation and validation

The construction and validation rules are designed such that a VERS is
easy to read and understand by humans and straightforward to process
by tools, attempting to avoid the creation of empty or impossible
version ranges.

- Spaces are not significant and are removed in a canonical form. For
  example `<1.2.3|>=2.0` and ` < 1.2. 3 | > = 2 . 0` are equivalent.
- A version range specifier contains only printable ASCII letters,
  digits and punctuation.
- The URI scheme and versioning scheme are always lowercase as in
  `vers:npm`.
- The versions are case-sensitive, and a versioning scheme may specify
  its own case sensitivity.
- If a `version` in a `<version-constraint>` contains separator or
  comparator characters (i.e., ">", "<", "=", "!", "*", "|"), it must be
  quoted using the URL quoting rules. This should be rare in practice.

*[JMH: what is meant by `version` in the last bullet above?  (This is used
elsewhere as well.)]*

The list of `<version-constraint>` components of a range are signposts in the
version timeline of a package. With these few and simple validation
rules, we can avoid the creation of most empty or impossible version
ranges:

- **Constraints are sorted by version**. The canonical ordering is the
  versions order. The ordering of `<version-constraint>` components is not
  significant otherwise but this sort order is needed when checking if a
  version is contained in a range.
- **Versions are unique**. Each `version` must be unique in a range
  and can occur only once in any `<version-constraint>` component of a range
  specifier, irrespective of its comparators. Tools must report an
  error for duplicated versions.
- **There is only one star**: "*" must only occur once and alone in a
  range, without any other constraint or version.

Starting from a de-duplicated and sorted list of constraints, these
extra rules apply to the comparators of any two contiguous constraints
to be valid:

- "!=" constraint can be followed by a constraint using any
  comparator, i.e., any of "=", "!=", ">", ">=", "<", "<=" as
  comparator (or no constraint).

*[JMH: I don't fully understand the next two points. Examples would be
helpful.]*

Ignoring all constraints with "!=" comparators:

- A "=" constraint must be followed only by a constraint with one of
  "=", ">", ">=" as comparator (or no constraint).

And ignoring all constraints with "=" or "!=" comparators, the sequence
of constraint comparators must be an alternation of greater and lesser
comparators:

- "\<" and "\<=" must be followed by one of ">", ">=" (or no
  constraint).
- ">" and ">=" must be followed by one of "\<", "\<=" (or no
  constraint).

Tools must report an error for such invalid ranges.
