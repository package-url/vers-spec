### VERS Type Definitions

This directory contains the machine-readable definitions of all currently
registered VERS `types` with one JSON file for each `type`. These JSON files
serve as the reference for VERS **type** specifications.

## Definitions

Each JSON file named `<vers-type>-definition.json` in this directory follows
the VERS Type Definition Schema. The goals are:

- Consistency across all VERS `types`
- Machine-readability for validation and automation
- Standardized structure defining 'constraints' including 'comparators' and
  'versions'

## Usage

- These JSON files are the authoritative source for defining, validating
  and testing VERS `types`.
- They should be referenced by tools, libraries, and documentation generators.

## Related files

There are two other places in this repository with important VERS `type` data:
- [`vers-types-index.json`](https://github.com/package-url/vers-spec/blob/main/vers-types-index.json):
  a simple index of registered VERS `types`.
- VERS `type`-specific tests. These test files are in the [`tests/`](https://github.com/package-url/vers-spec/tree/main/tests/)
  directory with the VERS `type` as the prefix to the test file name.

## PURL Type Tests
Each JSON file in the `vers-spec/tests/` directory is required to follow the
VERS Test Schema located at: [`schemas/vers-test.schema-0.2.json`](https://github.com/package-url/vers-spec/blob/main/schemas/vers-test.schema-0.2.json).
The goals for the VERS Test Schema are:
- Consistency across VERS `type` tests
- Machine-readability for automation such that tools can all use the same set
  of tests
- Two levels of tests (`test_group`): one for test cases that are required
  for conformance to the PURL specification and one for test cases that are
  recommended for tools to normalize or otherwise improve invalid input VERS
  data so that it can pass the required tests

NB: The VERS Test Schema is not currently included in the [ECMA-xxx-VERS](https://ecma-tc54.github.io/ECMA-427/)
standard. It is version 0.2 and is currently pending some significant
improvements.

## Contributions

Community contributions for VERS `type` definitions and tests are welcome.

- Registering a new VERS `type` requires an issue to document background
  information for the new `type`.
- Changing an existing VERS `type` requires an issue to explain the change
  unless the change is a minor editorial correction.
- Registering a new VERS `type` or changing an existing VERS `type` also
  requires a pull request.

See the Package-URL website [VERS types](https://www.packageurl.org/docs/vers/vers-types)
pages for more information.