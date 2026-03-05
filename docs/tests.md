---
id: tests
title: VERS test overview
sidebar_label: VERS test overview
hide_table_of_contents: true
---

# VERS test overview

## Tests

The VErsion Range Specifier (VERS) specification provides a JSON Schema and 
test files to support language-neutral testing of VERS implementations. The
objectives for the VERS test schema and test files are to enable tools to 
conform to the VERS specification for tool functions such as:
- validate a VERS string
- parse a VERS string to determine if a version is contained within a range

The test files are available at: [`vers-spec/tests/`](https://github.com/package-url/vers-spec/tree/main/tests). Each test file is in JSON format with 
a naming convention based on: `<version-scheme>_<range OR version>_<test-type>_test.json.`

Two key properties in the VERS test JSON Schema are:
- Test groups
- Test types

### Test groups

There are two VERS test groups:
- **base**: Test group for base conformance tests. Base tests are pass/fail.
- **advanced**: Test group for advanced tests. Advanced tests are more 
permissive than base tests. They may correct some errors.

### Test types

There are nine VERS test types:
- **build**: A test to build a canonical VERS string from decoded VERS 
components.
- **comparison**: A test to sort an input version string array using the applicable **version-scheme** rules.
- **containment**: A test to determine whether a bare version string is 
contained within the range of a VERS string.
- **equality**: A test to check if two input versions strings are equal using 
the applicable **version-scheme** rules.
- **from_native**: A test to construct a canonical VERS string from a native ecosystem data source.
- **invert**: A test to invert a VERS string into a canonical VERS string.
- **merge**: A test to merge an array of VERS strings into a canonical VERS string.
- **parse**: A test to parse a VERS string into a decoded **version-scheme** 
and a **version-constraints** list.
- **roundtrip**: A test to parse a VERS input string and build a canonical 
VERS output string.
