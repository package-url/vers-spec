---
id: test-suite
title: VERS test suite
sidebar_label: Test suite
hide_table_of_contents: false
---

# VERS test suite
The VERS test suite is intended to help a VERS implementation tool demonstrate
conformance with the VERS specification. The primary objective is to provide
clarity about whether a VERS string or a set of VERS components is in
canonical form.

## Test files
Each VERS test file is a collection of test cases whose structure is defined
by the VERS test schema. The current VERS test schema is located at: https://packageurl.org/schemas/.

The VERS test files are currently organized in the folder: https://github.com/package-url/vers-spec/tree/main/tests. Most test file names follow the pattern of VERS **type**
concatenated with **test type**.


## Test cases
The basic structure of a VERS **test case** is:
- `description`: string
- `test_group`: 'required' or 'recommended'
- `test_type`: see list below
- `input`: A VERS string or an object of VERS components that is the test case
  input. The "input" is not required to be in canonical form.
- `expected_output`: A VERS string or a set of decoded components (canonical
  form) that is the test case output.
- `expected_failure`: boolean
- `expected_message`: string

Each test case is granular such that an expected failure condition covers only
one error. This means that a test case should only cover an error for a single
VERS component or a single parsing error related to separator characters. This
is necessary to keep test cases simple. It is not intended to constrain error
message handling implemented by a VERS tool.

### description
The test case **description** should succinctly describe the test case scope
and purpose.

### test_group
There are two VERS **test groups**:
- 'required': A test case to demonstrate conformance with the VERS
  specification.
- 'recommended': A test case that is recommended to identify common problems
  in VERS data and how to remediate or normalize them in order to pass the
  'required' tests. The use of 'recommended' test cases is always optional.

The terminology of 'required' vs 'recommended' matches the use of "shall" vs
"should" for Ecma conformance. A "shall" statement means 'required'; a
"should" statement means 'recommended'.

### test_type
There are nine VERS **test types**:

- 'build': A test case for the function of building a canonical VERS output
  string from an input of decoded VERS components.
- 'comparison': A test case to sort an input version string array
  using the applicable VERS type rules.
- 'containment': A test case to determine if a bare version string is
  contained within the range of a VERS string.
- 'equality': A test case to check if two input version strings are equal
  using the applicable VERS type rules.
- 'from_native': A test case to construct a canonical VERS string from a native
  ecosystem data source.
- 'invert': A test case to invert a VERS string into a canonical VERS string.
- 'merge': A test case to merge an array of VERS strings into a canonical VERS
  string.
- 'parse': A test case to parse a VERS string into a decoded VERS type and a
  constraints list.
- 'validate': A test case for the function of validating a VERS input
  string. The input is a VERS string (in canonical form or not) and the output
  is a VERS string in canonical form.

See [`/docs/how-to-parse.md`](https://packageurl.org/docs/vers/how-to-parse#parsing-and-validating-vers-notation) for more information about
the 'containment', 'parse', and 'validate' **test types**.

### input
- **input** may be a VERS string or an object containing VERS components.
- **input** does not need to be in canonical form, but a test case with
  non-canonical input shall fail when the **test group** is 'required'.

### expected_output
**expected output** is either a canonical VERS string or an object containing
a set of decoded VERS components.
- If **expected_failure** is true, then **expected output** is null.
- If **expected failure** is false, then **expected output** is required.

### expected_failure
**expected failure** is true if the test **input** is expected to fail
according to the function defined by the **test type**.

### expected_message
**expected message** either documents the reason that a test case results in a
failure or provides information about the result of the test case. It should
be descriptive without duplicating the test case **description**.
- If **expected failure** is true, then **expected message** is
  required.
- If **expected failure** is false, then **expected message** is not required,
  but is recommended when an **input** contains an unregistered VERS **type**.
  It is important to document that a VERS **type** is not registered because
  this means that the VERS **type** is effectively unknown across the tools
  and databases that implement VERS.

The VERS specification does not mandate how a VERS tool natively reports
the success or failure of a test. Implementation languages that throw
exceptions or return typed results should return typed errors, i.e.
a syntactically invalid VERS and a VERS input that fails VERS
**type**-specific validation should result in different types or enum values.