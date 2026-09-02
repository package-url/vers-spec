# VERS use cases

A primary VERS use case is to test if a package version is contained with a
**constraints** sequence. A package version is within VERS **constraints** if it
falls within any of the intervals defined by the **constraints**.  Otherwise,
the package version is outside of the **constraints**.

Some important use cases derived from this include:

- **Resolve a version range specifier to a list of specific versions.**

  In this use case, the input is one or more known versions of
  a package. Each version is then tested to check if it lies inside or
  outside the **constraints**. For example, given a vulnerability and the VERS
  describing the vulnerable versions of a package, this process is
  used to determine if a specific package version is vulnerable.

- **Select one of several versions that are within a range.**

  In this use case, with the input of several package versions that are within
  a range and several packages that express package dependencies qualified by
  a version range, a package management tool will determine and select the set
  of package versions that satisfy the **constraints** of all of the
  dependencies. This usually requires deploying heuristics and algorithms
  (possibly as complex as SAT solvers) that are ecosystem- and tool-specific
  and outside of the scope of this specification. VERS can be used in tandem
  with PURL to provide an input to this dependency resolution process.

## Examples

For example, to define a set of versions that contains either version
"1.2.3", or any versions greater than or equal to "2.0.0" but less than
"5.0.0" using the "node-semver" version scheme for the "npm" PURL **type**,
the VERS will be:

    vers:npm/1.2.3|>=2.0.0|<5.0.0

This is an example of how to read a **constraints** string in version
order from left to right to determine the versions that are included in a
VERS. In this case you process in order:
- Include a single version "1.2.3"
- Include versions that are ">=2.0.0"
- Stop including versions when you reach the constraint "<5.0.0"

Other examples are:

### A single version in an "npm" package dependency:
For a package dependency originally seen as a dependency on version "1.2.3" in
a `package.json` manifest file the VERS is:

    vers:npm/1.2.3

### A list of versions, enumerated:
    vers:pypi/0.0.0|0.0.1|0.0.2|0.0.3|1.0|2.0pre1

### A complex statement about a vulnerability in a "maven" package:
For a Maven package vulnerability that affects multiple branches,
each with its own fixed version: `affects Apache TomEE 8.0.0-M1 - 8.0.1,
Apache TomEE 7.1.0 - 7.1.2, Apache TomEE 7.0.0-M1 - 7.0.7,
Apache TomEE 1.0.0-beta1 - 1.7.5.`

- A normalised VERS is:

      vers:maven/>=1.0.0-beta1|<=1.7.5|>=7.0.0-M1|<=7.0.7|>=7.1.0|<=7.1.2|>=8.0.0-M1|<=8.0.1

- An alternative is to use four VERS notations to cover the same range using
  one VERS for each of the vulnerable "branches":

      vers:tomee/>=1.0.0-beta1|<=1.7.5
      vers:tomee/>=7.0.0-M1|<=7.0.7
      vers:tomee/>=7.1.0|<=7.1.2
      vers:tomee/>=8.0.0-M1|<=8.0.1

  See also: https://repo1.maven.org/maven2/org/apache/tomee/apache-tomee/

### Converting RubyGems custom syntax for dependencies:
Note how the pessimistic version **constraint** is expanded for the RubyGems
dependency expression: `'library', '~>2.2.0', '!=2.2.1', '<2.3.0'`

- The VERS is:

      vers:gem/>=2.2.0|!=2.2.1|<2.3.0
