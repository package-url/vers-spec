# 5 VERS specification

VERS stands for "VErsion Range Specifier. A VERS is an ASCII URI string
composed of three components:

    scheme:type/constraints|

Components are separated by a specific character for unambiguous parsing.

**Table 1 —  Components of a VERS**

| Component           | Requirement | Description|
| ------------------- | ----------- |:------------------------------------------------------ |
| scheme              | Required    | The URL scheme with the constant value of "vers". |
| type                | Required    | The version specification type such as "semver", "npm", "deb", etc. |
| constraints         | Required    | Version constraints may be repeated as many times as needed to accurately reflect the intended range. The separator between constraints is a single pipe '\|'. |

## 5.1 Separator characters
This is how each of the Separator Characters is used:
- ':' (colon) is the separator between **scheme** and **type**
- '/' (slash) is the separator between **type** and **constraints**
- '|' (pipe) is the separator between **constraints**

**Example 1 (Informative): npm**

    vers:npm/1.2.3|>=2.0.0|<5.0.0

**Example 2 (Informative): gem**

    vers:gem/>=2.2.0|!=2.2.1|<2.3.0`

## 5.2 A VERS is a URI scheme

A VERS is a valid URI scheme that conforms to URI definitions or
specifications at: - https://tools.ietf.org/html/rfc3986

## 5.3 VERS components

### 5.3.1 Scheme
- The **scheme** is a constant with the value "vers".
- The **scheme** shall be followed by an unencoded colon ':'.

### 5.3.2 Type
- The **type** shall be composed only of ASCII letters and numbers,
  period '.', and dash '-'.
- The **type** shall start with an ASCII letter.
- The **type** shall not be percent-encoded.
- The **type** is case insensitive and lowercase.
- The **type** shall be followed by a slash '/'.

A **type** defines:

- the specific notation and conventions used for a version string encoded
  according to this **type**
- how two versions are compared to determine if a version is inside or
  outside a range
- how a **type**-specific range notation can be transformed into VERS
  notation
- how to compare two version strings using **comparators**
- the structure (if any) of a **version** string such as "1.2.3". For
  example, the "semver" specification for version numbers defines a version as
  composed primarily of three dot-separated numeric segments named "major",
  "minor" and "patch".

By convention a **type** should be the same as the PURL **type** for a given
package or software ecosystem. It is, however, allowed to define a **type**
that does not match an existing PURL **type** such as a version scheme that
applies to a single package or project or a general purpose version scheme
like 'semver-2.0.0'.

This Standard includes the VERS Definition Schema but it does not include the
set of current "registered" VERS type (JSON format) definition files because
there are ongoing additions and changes to these files. The set of current "registered" VERS type definition files are located at: https://www.packageurl.org/vers-types/. Registration refers to the Package-URL community process for
adding a new VERS type.

There are two rules related to the set of registered VERS type definitions for conforming tools to validate the VERS type component of a VERS notation:

- If a VERS **type** is registered, then a VERS notation is invalid if it does
  not conform to all of the rules for the corresponding VERS **type**
  definition.
- If a VERS **type** is not registered, then the **type** component is valid
  if it conforms to the rules stated in the **type** component rules in this
  Clause of the Standard. In this case a tool should report a warning that the
  VERS type is not registered.

### 5.3.3 Constraints
- The **constraints** component shall be preceded by an unencoded
  '/' slash separator when not empty.
- Each instance of the **constraints** component is called a **constraint**.
  Each **constraint** is composed of either a single **version** as in
  '1.2.3' or the combination of a **comparator** and a **version** as in
  '>=2.0.0'.
- A **comparator** always precedes the **version** with no characters allowed
  between the **comparator** and the **version**.
- Multiple **constraints** shall be separated by an unencoded
  pipe '|'. The pipe "|" has no special meaning other than being a separator.

#### 5.3.1 Comparators
A **comparator** is composed of these ASCII characters:
- the Equals character: '=' (equals, '=')
- the Not Equals character: '!' (exclamation mark, '!')
- the Greater Than character: '>' (greater than, '>')
- the Less Than character: '<' (less than, '<')
- the Asterisk character: '\*' (asterisk, '*')

A **comparator** shall be one of the following:
- '!=' is the Inequality **comparator**. This means that a version shall not
  be equal to the provided version and it shall be excluded from the range.
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
- The special Asterisk '\*' **comparator** matches any version. It shall be
  used alone and exclusive of any other constraint and shall not be followed
  by a version. For example, 'vers:deb/\*' represents all versions of a
  Debian package. This includes past, current and possible future versions.

There is no Equality **comparator** (equals, '=') because a **version**
without a **comparator** asserts equality. For example `vers:npm/1.2.3` means
that the **version** is equal to "1.2.3". If a **constraint** string starts
with '=', tools shall report an error.

#### 5.3.2 Version**
A **version** is an ASCII string.

A single **version** in a **constraint** string means that a version
equal to this version satisfies the range specification. Equality is based on
the equality of two normalised version strings according to the applicable
**type**. For most schemes, this is a simple string equality. A
**type** may, however, define normalisation and other rules for
equality such as the "pypi" rules from PEP 440.

A package version satisfies a set of **constraints** if it is
contained within any of the intervals defined by the **constraints**.

## 5.4 VERS validation rules

VERS validation rules are designed such that a VERS notation is easy for a
human to read and understand, and straightforward for tools to process. The
rules are also designed to prevent the creation of empty or impossible version
ranges.

- Tools shall report an error for an invalid VERS string.
- A version range specifier contains only printable ASCII letters,
  digits and punctuation.
- ASCII whitespace is not permitted in a VERS string. Tools shall report an
  error if any Whitespace character, for example SPACE (0x20), TAB (0x09), or
  LF (0x0A), is used.
- The VERS **scheme** and **type** are always lowercase as in 'vers:npm'.
- Versions are case-sensitive. A **type** may specify
  case sensitivity for that **type**.
- If a version in a **constraint** string contains any of these characters:
  '>', '<', '=', '!', '*', '|', '%', these characters shall be
  percent-encoded using URI percent-encoding rules.
- Tools shall report an error for invalid percent-encoded sequences.

The list of **constraint** strings represent distinct intervals in the version
timeline of a a package. The separators do not mean "and" or "or". They are
separators in a sequence of **constraints**.

With a few simple validation rules, we can avoid the creation of most empty or
impossible version ranges. These rules are:

- **Constraints** shall be sorted by version order. The ordering of the
  **constraint** instances is significant for validity: tools shall report
  an error for invalid ordering.
- Versions are unique. Each version shall be unique in a **constraints**
  string and can occur only once in any **constraint**, regardless of the **comparators**. Tools shall report an error for duplicated versions.
- There can be only one asterisk in a **constraints** string: '\*' shall occur
  only once and alone in a **constraints** string.

Starting from a de-duplicated and sorted list of **constraints**, the
following rules apply to the **comparators** of any two contiguous
**constraints**:

- A constraint using the '!=' **comparator** can be followed by a constraint
  using any **comparator** (any of '=', '!=', '>', '>=', '<', '<=') or no
  constraint.
- Ignoring all **constraints** with the '!=' **comparator**, an equality
  **constraint** shall be followed only by a **constraint** with
  one of **comparators**: '=', '>', or '>=' or no **constraint**.
- Ignoring all constraints with a '=' or '!=' **comparator**, the sequence
  of **constraints** shall be an alternation of Greater-than and Lesser-than
  **comparators**:
- A constraint using '\<' and '\<=' shall be followed by one of '>' or '>='
  (or no constraint).
- A constraint using '>' and '>=' shall be followed by one of '\<' or '\<='
  (or no constraint).

Tools shall report an error for an invalid sequence of **constraints**.

