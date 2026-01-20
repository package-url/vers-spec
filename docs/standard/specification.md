# VERS specification

VERS stands for "VErsion Range Specifier. A VERS is an ASCII URI string composed of
three components:

    scheme:version-scheme/version-constraint|version-constraint|version-constraint|

Components are separated by a specific character for unambiguous parsing.

Table 1 —  Components of a VERS

| Component           | Requirement | Description|
| ------------------- | ----------- |:------------------------------------------------------ |
| scheme              | Required    | The URL scheme with the constant value of "vers". |
| version-scheme      | Required    | The version specification or "scheme" such as "semver", "npm", "deb", etc. |
| version-constraints | Required    | Version constraints may be repeated as many times as needed to accurately reflect the intended range(s)|

**Example 1 (Informative): npm**

    vers:npm/1.2.3|>=2.0.0|<5.0.0

**Example 2 (Informative): gem**

    vers:gem/>=2.2.0|!=2.2.1|<2.3.0`

## A VERS is a URI scheme

A VERS is a valid URI scheme that conforms to URI definitions or specifications at:
- https://tools.ietf.org/html/rfc3986

## VERS components

### Scheme
- The **scheme** is a constant with the value "pkg".
- The **scheme** shall be followed by an unencoded colon ':'.

### **Version-scheme**
- The **version-scheme** shall be composed only of ASCII letters and numbers, period '.', and dash '-'.
- The **version-scheme** shall start with an ASCII letter.
- The **version-scheme** shall not be percent-encoded.
- The **version-scheme** is case insensitive. The canonical form is lowercase.
- The **version-scheme** shall be followed by a slash '/'.

The **version-scheme** defines:

- the specific notation and conventions used for a version string
  encoded in this scheme.
  A **version-scheme** often specifies a version
  segment separator and the meaning of each version segment, such as
  [major.minor.patch] in "semver".
- how two versions are compared to determine if a version is inside
  or outside a range.
- how a **version scheme**-specific range notation can be transformed
  into VERS notation.

By convention a **version scheme** should be the same as the
PURL **type** for a given package ecosystem. It is acceptable to
define a **version-scheme** that does not match an existing PURL **type**
such as a scheme that is specifically for a single package or project.

The **version-scheme** is followed by a slash '/'.

### **Version-constraints**
- The **version-constraints** component shall be preceded by an unencoded
  '/' slash separator when not empty.
- Each instance of the ** version-constraints** component is composed of either a single
  **version** or the combination of a **comparator** and a **version**.
- Multiple **version-constrain** instances strings shall be separated by an unencoded
  pipe '|'. The pipe "|" has no special meaning other than being a separator.

*[JMH: the next sentence refers to "this list" -- what list?]*

*[JMH: what is meant below by `<version>`?]*

Each **version-constraint** component of this list is either a single
`<version>` as in `1.2.3` for example or the combination of a `<comparator>`
and a `<version>` as in `>=2.0.0` using this syntax:

    <comparator><version>

A single version means that a version equal to this version
satisfies the range spec. Equality is based on the equality of two
normalized version strings according to their version scheme. For
most schemes, this is a simple string equality. But schemes can specify
normalization and rules for equality such as "pypi" with PEP 440.

The special star "/*" comparator matches any version. It must be
used **alone** exclusive of any other constraint and must not be followed
by a version. For example, `vers:deb/*` represents all the versions of a
Debian package. This includes past, current and possible future
versions.

Otherwise, the **comparator** is one of these comparison operators:

- "!=": Version exclusion or inequality comparator. This means a
  version must not be equal to the provided version that must be
  excluded from the range. For example: `!=1.2.3` means that version
  "1.2.3" is excluded.
- "<", "<=": Less than or less-or-equal version comparators
  point to all versions less than or equal to the provided version.
  For example `<=1.2.3` means less than or equal to "1.2.3".
- ">", ">=": Greater than or greater-or-equal version comparators
  point to all versions greater than or equal to the provided version.
  For example `>=1.2.3` means greater than or equal to "1.2.3".

The **version-scheme** defines:

- how to compare two version strings using these comparators, and
- the structure (if any) of a version string such as "1.2.3". For
  instance, the "semver" specification for version numbers defines a
  version as composed primarily of three dot-separated numeric
  segments named "major", "minor" and "patch".

A pipe "|" is used as a simple separator between
**version-constraints**. Each **version-constraint** in this
pipe-separated list contains a Comparator and a Version.

A package version satisfies a set of **versions-constraints** if it is 
contained within any of the intervals defined by the **version-constraints**.

### Comparator characters
A Comparator is composed of these ASCII characters: 
- the Equals character: '=' (equals)
- the Not Equal Sign characters: '!=' (exclamation mark, equals)
- the Greater Than character: '>' (greater than)
- the Greater Than or Equals characters: '>=' (greater than, equals)
- the Less Than character: '<' (less than)
- the Less Than or Equals characters: '<=' (less than, equals)

### Version
A Version is an ASCII string.

## Separator characters
This is how each of the Separator Characters is used:
- ':' (colon) is the separator between **scheme** and **version-scheme**
- '/' (slash) is the separator between **version-scheme** and "**version-constraints**
- '!' (pipe) is the separator between **version-constraints**

## Normalized, canonical representation and validation

The construction and validation rules are designed such that a VERS is
easy to read and understand by humans and straightforward to process
by tools, attempting to avoid the creation of empty or impossible
version ranges.

- Spaces are not significant and are removed in a canonical form. For
  example `<1.2.3|>=2.0` and ` < 1.2. 3 | > = 2 . 0` are equivalent.
- A version range specifier contains only printable ASCII letters,
  digits and punctuation.
- The URI scheme and version scheme are always lowercase as in
  `vers:npm`.
- Versions are case-sensitive, and a **version-scheme** may specify
  its own case sensitivity.
- If a version in a **version-constraint** contains separator or
  comparator characters (i.e., ">", "<", "=", "!", "*", "|"), it must be
  quoted using the URL quoting rules. This should be rare in practice.

*[JMH: what is meant by `version` in the last bullet above?  (This is used
elsewhere as well.)]*

The list of **version-constraint** components of a range are signposts in the
version timeline of a package. With these few and simple validation
rules, we can avoid the creation of most empty or impossible version
ranges:

- **Constraints are sorted by version**. The canonical ordering is the
  versions order. The ordering of **version-constraint** components is not
  significant otherwise but this sort order is needed when checking if a
  version is contained in a range.
- **Versions are unique**. Each `version` must be unique in a range
  and can occur only once in any **version-constraint** component of a range
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

### Using version range specifiers

The primary VERS use case is to test if a version is within a range. 
A version is within a version range if falls in any of the intervals
defined by a range. Otherwise, the version is outside of the version
range.

Some important use cases derived from this include:

- **Resolve a version range specifier to a list of specific versions.**

  In this case, the input is one or more known versions of
  a package. Each version is then tested to check if it lies inside or
  outside the range. For example, given a vulnerability and the VERS
  describing the vulnerable versions of a package, this process is
  used to determine if an existing package version is vulnerable.
  
- **Select one of several versions that are within a range.**

  In this case, with the input of several versions that are within a
  range and several packages that express package dependencies
  qualified by a version range, a package management tool will
  determine and select the set of package versions that satisfy
  the version range constraints of all of the dependencies. This
  usually requires deploying heuristics and algorithms (possibly
  as complex as SAT solvers) that are ecosystem- and tool-specific
  and outside of the scope for this specification. VERS could
  be used in tandem with PURL to provide an input to this dependencies
  resolution process.


### Examples


For example, to define a set of versions that contains either version
"1.2.3", or any versions greater than or equal to "2.0.0" but less than
"5.0.0" using the "node-semver" version scheme used with the "npm"
PURL **type**, the version range specifier will be:

    vers:npm/1.2.3|>=2.0.0|<5.0.0

*[JMH/MJH: the following VERS example seems to interpret the 1st constraint as "or" versus
"and" for the second and third constraints. 1.2.3 we need a clear and complete
description of the separators and their respective uses.]*

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
