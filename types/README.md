### VERS Type Definitions

This directory contains the machine-readable definitions of all currently
registered VERS types, one JSON file for each type. These JSON files serve as
the reference for VERS **type** specifications.

## Definitions

Each JSON file named `<vers-type>-definition.json` in this directory follows
the VERS Type Definition Schema standard. The goals are:

- Consistency across all VERS **types**.
- Machine-readability for validation and automation.
- Standardized structure defining 'constraints' including 'comparators' and
  'versions'.

## Usage

- These JSON files are the the authoritative source for defining, validating
  and testing VERS **types**.
- They should be referenced by tools, libraries, and documentation generators.

## Related files

The VERS **type** index provides a simple index of registered VERS types at:
[**vers-types-index.json**](https://github.com/package-url/vers-spec/blob/main/vers-types-index.json).

## Contributions

- Modifications must be made to these JSON files directly.
- The type definitions, tests and index are validated for consistency on
  commit.
- Documentation files are generated from these JSON files.
