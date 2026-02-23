# VERS specification

VERS stands for "VErsion Range Specifier. A VERS is an ASCII URI string composed of
three components:

    scheme:version-scheme/version-constraints|

Components are separated by a specific character for unambiguous parsing.

**Table 1 —  Components of a VERS**

| Component           | Requirement | Description|
| ------------------- | ----------- |:------------------------------------------------------ |
| scheme              | Required    | The URL scheme with the constant value of "vers". |
| version-scheme      | Required    | The version specification or "scheme" such as "semver", "npm", "deb", etc. |
| version-constraints | Required    | Version constraints may be repeated as many times as needed to accurately reflect the intended range. The separator between version-constraints is a single pipe '\|'. |

## Separator characters
This is how each of the Separator Characters is used:
- ':' (colon) is the separator between **scheme** and **version-scheme**
- '/' (slash) is the separator between **version-scheme** and 
**version-constraints**
- '|' (pipe) is the separator between **version-constraints**

**Example 1 (Informative): npm**

    vers:npm/1.2.3|>=2.0.0|<5.0.0

**Example 2 (Informative): gem**

    vers:gem/>=2.2.0|!=2.2.1|<2.3.0`

## A VERS is a URI scheme

A VERS is a valid URI scheme that conforms to URI definitions or 
specifications at: - https://tools.ietf.org/html/rfc3986

## VERS components

### Scheme
- The **scheme** is a constant with the value "vers".
- The **scheme** shall be followed by an unencoded colon ':'.

### **Version-scheme**
- The **version-scheme** shall be composed only of ASCII letters and numbers,
  period '.', and dash '-'.
- The **version-scheme** shall start with an ASCII letter.
- The **version-scheme** shall not be percent-encoded.
- The **version-scheme** is case insensitive. The canonical form is lowercase.
- The **version-scheme** shall be followed by a slash '/'.

A **version-scheme** defines:

- the specific notation and conventions used for a version string encoded in 
this scheme
- how two versions are compared to determine if a version is inside or 
outside a range
- how a version-scheme-specific range notation can be transformed into VERS 
notation

A **version-scheme** also defines:
- how to compare two version strings using **comparators**
- the structure (if any) of a **version** string such as "1.2.3". For
example, the "semver" specification for version numbers defines a version as 
composed primarily of three dot-separated numeric segments named "major", 
"minor" and "patch".

By convention a **version-scheme** should be the same as the
PURL **type** for a given package ecosystem. It is, however, allowed to
define a **version-scheme** that does not match an existing PURL **type**
such as a scheme that applies to a single package or project.

### **Version-constraints**
- The **version-constraints** component shall be preceded by an unencoded
'/' slash separator when not empty.
- Each instance of the **version-constraints** component is composed of either
a single **version** as in '1.2.3' or the combination of a **comparator** and
a **version** as in '>=2.0.0'.
- A **comparator** always precedes the **version** with no characters allowed
between the **comparator** and the **version**
- Multiple **version-constraints** strings shall be separated by an unencoded
pipe '|'. The pipe "|" has no special meaning other than being a separator.

#### Comparator characters
A **comparator** is composed of these ASCII characters: 
- the Equals character: '=' (equals, '=')
- the Not Equals character: '!' (exclamation mark, '!')
- the Greater Than character: '>' (greater than, '>')
- the Less Than character: '<' (less than, '<')
- the Asterisk character: '\*' (asterisk, '*')

A **comparator** must be one of the following:
- '=' is the Equality **comparator**. This means a version must be equal to
the provided version.
- '!=' is the Inequality **comparator**. This means that a version must not be
equal to the provided version and it must be excluded from the range.
For example: '!=1.2.3' means that version   "1.2.3" is excluded.
- '<' is the Less-than **comparator**. This includes all versions less than
the provided version. 
- '<=': is the Less-or-equal **comparator**. This includes all versions less
than or equal to the provided version. For example '<=1.2.3' means
less than or equal to "1.2.3".
- '>' is the Greater-than **comparator**. This includes all versions greater
than the provided version.
- '>=' is the Greater-or-equal **comparator**. This includes all versions
greater than or equal to the provided version. For example '>=1.2.3'
means greater than or equal to "1.2.3".
- The special asterisk '\*' **comparator** matches any version. It must be
used alone and exclusive of any other constraint and must not be followed
by a version. For example, 'vers:deb/\*' represents all versions of a
Debian package. This includes past, current and possible future versions.

#### Version strings
A Version is an ASCII string.

A single **version** in a **version-constraints** string means that a version 
equal to this version satisfies the range specification. Equality is based on 
the equality of two normalized version strings according to the applicable
**version-scheme**. For most schemes, this is a simple string equality. A 
**version-scheme** may, however, define normalization and other rules for 
equality such as the "pypi" rules from PEP 440.

A package version satisfies a set of **version-constraints** if it is 
contained within any of the intervals defined by the **version-constraints**.

## Normalized, canonical representation and validation

VERS construction and validation rules are designed such that a VERS is
easy to read and understand by humans and straightforward to process
with tools. The rules are designed to prevent the creation of empty or 
impossible version ranges.

- Spaces are not significant and are removed in a canonical form. For
example '|<1.2.3|>=2.0|' and '|< 1 . 2 . 3 | > = 2 . 0 |' are equivalent.
- A version range specifier contains only printable ASCII letters,
digits and punctuation.
- The VERS **scheme** and **version-scheme** are always lowercase as in
'vers:npm'.
- Versions are case-sensitive. A **version-scheme** may specify
its own case sensitivity.
- If a version in a **version-constraints** string contains **separator** or
**comparator** characters (i.e., '>', '<', '=', '!', '*', '|'), the version
shall be quoted using the URL quoting rules. This should be rare in practice.

The list of **version-constraints** strings for a range are like a set of 
signposts in the version timeline of a package. With a few simple validation 
rules, we can avoid the creation of most empty or impossible version ranges. 
These rules are:

- Constraints are sorted by version. The canonical ordering is the
version order. The ordering of **version-constraints** components
is not significant but this sort order is needed when checking
if a version is contained within a range.
- Versions are unique. Each version must be unique in a range
and can occur only once in any **version-constraints** component of
VERS, regardless of the **comparators**. Tools shall report an
error for duplicated versions.
- There can be only one asterisk: if used, '\*' must occur only once and alone
in a range, without any other constraint or version.

Starting from a de-duplicated and sorted list of constraints, these
extra rules apply to the **comparators** of any two contiguous constraints:

- A constraint using the '!=' **comparator** can be followed by a constraint
using any **comparator** (any of '=', '!=', '>', '>=', '<', '<=') or no
constraint.

Ignoring all constraints with the '!=' **comparator**:

- A constraint using the '=' **comparator** must be followed only by a constraint 
with one of   '=', '>', or '>=' as the **comparator** or no constraint.

Ignoring all constraints with a '=' or '!=' **comparator**, the sequence
of constraints must be an alternation of Greater-than and Lesser-than
**comparators**:
- A constraint using '\<' and '\<=' must be followed by one of '>' or '>=' 
(or no constraint).
- A constraint using '>' and '>=' must be followed by one of '\<' or '\<=' 
(or no constraint). 

Tools must report an error for such invalid ranges.

### Using version range specifiers

The primary VERS use case is to test if a version is within a range. 
A version is within a version range if it falls within any of the intervals
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
"5.0.0" using the "node-semver" version scheme for the "npm" PURL **type**, 
the version range specifier will be:

    vers:npm/1.2.3|>=2.0.0|<5.0.0

[comment]: # (JMH/MJH: the preceding VERS example seems  to interpret the 
separator between the 1st and 2nd constraints as "or" versus the separator 
between the 2nd and 3rd constraints as "and". . We need a clear description 
of the separator(s) and its/their respective uses.)   

Other examples are:

#### A single version in an "npm" package dependency:
For a package dependency originally seen as a dependency on version "1.2.3" in
a `package.json` manifest file the version range specification is:

    vers:npm/1.2.3

#### A list of versions, enumerated:
    vers:pypi/0.0.0|0.0.1|0.0.2|0.0.3|1.0|2.0pre1

#### A complex statement about a vulnerability in a "maven" package:
For a "maven" package vulnerability that affects multiple branches, 
each with its own fixed version: `affects Apache TomEE 8.0.0-M1 - 8.0.1, 
Apache TomEE 7.1.0 - 7.1.2, Apache TomEE 7.0.0-M1 - 7.0.7, 
Apache TomEE 1.0.0-beta1 - 1.7.5.`

- A normalized VERS notation is:

      vers:maven/>=1.0.0-beta1|<=1.7.5|>=7.0.0-M1|<=7.0.7|>=7.1.0|<=7.1.2|>=8.0.0-M1|<=8.0.1
  
- An alternative is to use four VERS notations to cover the same range, using one VERS
  for each of the vulnerable "branches":

      vers:tomee/>=1.0.0-beta1|<=1.7.5
      vers:tomee/>=7.0.0-M1|<=7.0.7
      vers:tomee/>=7.1.0|<=7.1.2
      vers:tomee/>=8.0.0-M1|<=8.0.1

  See also: https://repo1.maven.org/maven2/org/apache/tomee/apache-tomee/

#### Converting RubyGems custom syntax for dependencies:
Note how the pessimistic version constraint is expanded for the RubyGems dependency
expression: `'library', '~>2.2.0', '!=2.2.1'`:

- The VERS notation is:

      vers:gem/>=2.2.0|!=2.2.1|<2.3.0

*[JMH the dependency expression does not include the "<2.3.0" constraint in 
the VERS notation.]*:
