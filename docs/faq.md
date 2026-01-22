# Frequently Asked Questions

## Why not reuse existing version range notations?

Most existing version range notations are tied to a specific version
string syntax and are therefore not readily applicable to other
contexts. For example, the use of elements such as tilde and caret
ranges in RubyGems, "npm" or Dart notations implies that a certain
structure exists in the version string ("semver" or "semver"- like). The
inclusion of these additional comparators is a result of the history and
evolution of a specific package ecosystem to address specific needs.

In practice, the unified and reduced set of comparators and syntax
defined for VERS has been designed such that all of the notations 
can be converted to a VERS notation and back from a VERS notation
to the original notation.

This conversion is not possible with existing notations. For instance,
the Python notation may not work with "npm" "semver" versions and
reciprocally.

There are likely a few rare cases where round tripping from and to
VERS may not be possible. In any case round tripping to and from a
VERS notation should produce equivalent results even if the results 
do not exactly match the original strings.

Another issue with existing version range notations is that they are
primarily designed for dependencies and not for vulnerable ranges. In
particular, a vulnerability may exist for multiple "version branches" of
a given package, such as with Django 2.x and 3.x. Several version range
notations have difficulties communicating these because typically all the
version constraints must be satisfied. In contrast, a vulnerability can
affect multiple disjoint version ranges of a package and any version
satisfying these constraints would be vulnerable. It may not be possible
to express this with a notation designed exclusively for dependent
version resolution.

Finally, one of the goals of the VERS specification is to provide a 
compact complement to PURL for version ranges. Some existing and closely
related notations designed for vulnerable ranges are verbose
because they were designed for use in an API with larger JSON documents.

### Why not use the OSV Ranges?

VERS and the OSSF OSV schema vulnerable ranges are equivalent and
VERS provides a compact range notation while OSV provides a more verbose
JSON notation. See: https://ossf.github.io/osv-schema/

VERS was informed by the OSV schema specification and its authors.

OSV uses a minimalist set of only three comparators:

- "=" to enumerate versions,
- ">=" for the version that introduced a vulnerability, and
- "<" for the version that fixed a vulnerability.

OSV Ranges support neither ">" nor "!=" comparators, making it
difficult to express some ranges that must exclude a version. While this may
not yet be an issue for most vulnerable ranges, the lack of support
for these comparators:

- makes it difficult or impossible to precisely express certain
  dependency and vulnerable ranges when a version must be excluded and
  the set of existing versions is not yet known.
- makes some ranges more verbose such as with the CVE v5 API
  range notation that can include their upper limit and would need
  two constraints.

Another high-level difference between VERS and OSV is the identifiers 
used to qualify a range package "ecosystem" value that resembles
closely the PURL package **type** used in VERS. VERS will
provide a strict mapping between the OSV ecosystem and the VERS
**version-scheme** values.

### Why not use CVE v5 API Ranges?

Version 5 of the CVE JSON data format defines version ranges with a
starting version, a **versionType**, and an upper limit for the version
range as lessThan, as lessThanOrEqual, or as an enumeration of versions.
The **versionType** and the package **collectionURL** values are only
indicative and left out of this specification. Both seem strictly
equivalent to the PURL **type** on the one hand and the VERS
**version-scheme** on the other hand.

See:
- https://github.com/CVEProject/cve-schema/blob/master/schema/v5.0/CVE_JSON_5.0_schema.json#L303
- https://github.com/CVEProject/cve-schema/blob/master/schema/v5.0/CVE_JSON_5.0_schema.json#L123

The semantics and expressiveness of each range are similar and VERS
provides a compact notation rather than a more verbose JSON notation.
VERS supports the strict conversion of any CVE v5 range to its
notation and further provides a concrete list of well known versioning
schemes. VERS design was informed by the CVE v5 API schema spec and
its authors.

When CVE v5 becomes active, this spec will provide a strict mapping
between the CVE versionType and the VERS versioning schemes values.
This specification and the Package-URL **types** should be 
updated accordingly to provide a mapping with the upcoming CVE
**collectionURL**.

An issue with CVE v5 is that it introduces a new trailing '*'
notation that does not exist in most version range notations and may
not be computable easily in many cases. The description of the
**lessThan** property is:

> The non-inclusive upper limit of the range. This is the least version NOT 
> in the range. The usual version syntax is expanded to allow a pattern to 
> end in an asterisk (\*), indicating an arbitrarily large number in the 
> version ordering. For example, {version: 1.0 lessThan: 1.\*} would describe
> the entire 1.X branch for most range kinds, and {version: 2.0, lessThan: \*} 
> describes all versions starting at 2.0, including 3.0, 5.1, and so on.

The conversion to VERS range should be:

- For version 1.0 and **lessThan**: '\*', the VERS equivalent is: '>=1.0'.

- For version 1.0 and **lessThan**: '.\*', the VERS equivalent can be
  computed for "semver" versions as '>=1.0|<2' but this is not accurate
  because the versioning schemes have different rules. For instance,
  pre-release may be treated in some cases as part of the v1. branch and in
  other cases as part of the v2. branch. For '<2.*' it is not clear whether
  CVE v5 spec means '<2' or something that excludes any version string that
  starts with '2'.
  Also for the expression **lessThan**: '2.\*' using a "semver" version,
  it is not clear if '2.0.0-alpha' is **lessThan**; "semver" sorts it
  before '2.0' and after '1.0', e.g., in "semver" '2.0.0-alpha' is "less
  than" '2'.

### Why not use the NVD CPE Ranges?

The version range notation defined in the JSON schema of the CVE API
payload uses four fields: **versionStartIncluding**,
**versionStartExcluding**, **versionEndIncluding** and
**versionEndExcluding**. For example:

    "versionStartIncluding": "7.3.0",
    "versionEndExcluding": "7.3.31",
    "versionStartExcluding" : "9.0.0",
    "versionEndIncluding" : "9.0.46",

See:
- https://nvd.nist.gov/vuln/vulnerability-detail-pages#divRange
- https://nvd.nist.gov/developers/vulnerabilities#divResponse
- https://csrc.nist.gov/schema/nvd/feed/1.1/nvd_cve_feed_json_1.1.schema

In addition to these ranges, the NVD publishes a list of CPEs
with versions resolved for a range with daily updates at
https://nvd.nist.gov/vuln/data-feeds#cpeMatch

Note that the NVD CVE configuration is a complex specification that goes
well beyond version ranges and is used to match comprehensive
configurations across multiple products and version ranges. The VERS focus
is exclusively on versions but VERS supports the conversion of any CPE range.

### Why not use node-semver ranges?

The **node-semver** tool is similar to but more complex than VERS.
The use of AND and OR constraints in **node-semver** presents some practical 
issues:

- A space means "AND" and therefore white spaces are significant. Having
  significant white spaces in a string makes normalization more
  complicated and may be a source of confusion if you remove the
  spaces from the string. VERS avoids the ambiguity of spaces by
  ignoring them.
- The advanced range syntax has grown to be rather complex using
  hyphen ranges, star ranges, carets and tilde constructs that are
  all tied to the JavaScript and npm methods for handling versions in
  their ecosystem and are bound to the "semver" semantics
  and its "npm" implementation. These are not reusable elsewhere.
  The multiple comparators and modifiers make the notation grammar
  more complex to parse and process for a machine and harder to read
  for a human.

See: https://github.com/npm/node-semver#ranges

Notations that are directly derived from node-semver as used in Rust and
PHP Composer have the same issues.

### Why not use Python PEP 440 ranges?

The Python PEP 440 "Version Identification and Dependency
Specification" provides a comprehensive specification for Python package
versioning and a notation for "version specifiers" to express the
version constraints of dependencies.

See: https://www.python.org/dev/peps/pep-0440/#version-specifiers

This specification is similar to the VERS spec, with more operators
and aspects specific to the versions used only in the Python ecosystem.

- In particular PEP 440 uses tilde, triple equal and wildcard star
  operators that are specific to how two Python versions are compared.
- The comma separator between constraints is a logical "AND" rather
  than an "OR". The "OR" does not exist in the syntax making some
  version ranges harder to express, in particular for vulnerabilities
  that may affect several exact versions or ranges for multiple
  parallel release branches. Ranges such as "Django 1.2 or later, or
  Django 2.2 or later or Django 3.2 or later" are difficult to express
  without "OR" logic.

### Why not use RubyGems requirements notation?

The RubyGems specification suggests but does not enforce using semver.
It uses operators similar to **node-semver** with the difference
that RubyGems uses the "~>" aka. pessimistic operator instead of the 
plain "\~" tilde used in **node-semver**. This operator implies some 
semver-like versioning, yet gem versions are not strictly semver. This
makes the notation complex to implement and impractical to reuse in 
places that do not use the same Ruby-specific semver-like semantics.

See: https://guides.rubygems.org/patterns/#declaring-dependencies

### Why not use fewer comparators with only =, >= and <?

For instance, the OSV schema adopts a reduced set of only three
comparators:

- "=" is implied when used to enumerate vulnerable versions
- ">=" (greater or equal) is for the version that introduces a
  vulnerability
- "<" (lesser) is for the version that fixes a vulnerability

This approach is simpler and works well for most vulnerable ranges but
it faces limitations when converting from other notations:

- ">" cannot be converted reliably to ">=" unless you know all the
  versions and these will never change.
- "<=" cannot be converted reliably to "<" unless you know all the
  versions and these will never change.
- "!=" cannot be converted reliably: there is no ">" comparator to
  create an unequal equivalent of "><"; and a combo of ">=" and
  "<" is not equivalent to inequality unless you know all the
  versions and these will never change.

### Why not use richer comparators such as tilde, caret and star?

Some existing notations such as those for npm, gem, python, or composer
provide a syntactic shorthand such as:

- a "pessimistic operator" using tilde, ~> or =\~ as in "\~1.3" or
  "~>1.2.3"
- a caret ^ prefix as in "^ 1.2"
- using a star in a version segment as in "1.2.*"
- dash-separated ranges as in "1.2 - 1.4"
- arbitrary string equality such as "===1.2"

Most of these notations can be converted without loss to the VERS
notation. These notations typically assume a well defined
version string structure specific to their package ecosystem and are not
reusable in another ecosystem that would not use the exact same version
conventions.

For instance, the tilde and caret notations demand that you can reliably
infer the next version (aka. "bump") from a given version; this is
possible only if the versioning scheme supports this operation reliably
for all its accepted versions.

### Why not use mathematical interval notation for ranges?

Apache Maven and NuGet use a mathematical interval notation with
comma-separated "[", "]", "(" and ")" to declare version ranges.

Most other known range notations use the more common ">", "<", and "="
as comparators. VERS adopts the more common approach.
