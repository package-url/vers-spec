---
id: test-schema
title: VERS test schema
sidebar_label: Test schema
hide_table_of_contents: true
---

# VERS test schema

The VERS Test Schema is a [JSON Schema](https://json-schema.org/) that
provides the structure for tools to conform to the VERS specification for tool
functions such as:

- Build a VERS string from a native ecosystem data source;
- Merge an array of VERS strings into a canonical VERS string;
- Parse a VERS string to determine if a version is contained within a range;
- Validate a VERS string,

The structure of test cases used in VERS test files is defined in a JSON
schema. The current VERS Test Schema is [version 0.2](https://packageurl.org/vers-schemas/vers-test.schema-0.2.json).
The VERS Test Schema v0.2 implements [JSON Schema version "Draft 2020-12"](https://json-schema.org/draft/2020-12).

## VERS Test Schema v0.2 changes
The VERS test schema was updated to [version 0.2](https://packageurl.org/vers-schemas/vers-test.schema-0.2.json) on August 4, 2026. This update
included an automated update to all of the VERS test suite files at:
`vers-spec/tests/`. A summary of these changes is:

### Test groups
**Change**: Renamed
- 'base' to 'required'
- 'advanced' to 'recommended'

This change removes the ambiguity of the **test group** names from the v0.1
VERS test schema by using names that map to Ecma conformance terminology.

### Test messages
**Change**: Renamed **expected_failure_reason** to **expected_message**

The terminology of the version 0.1 VERS test schema did not provide a
way to provide a test case message for conditions other than failure. Some
use cases are:
- When an **input** contains an unregistered VERS **type**. It is important to
  document that a VERS **type** is not registered because this means that the
  VERS **type** is effectively unknown across tools and databases that
  implement VERS.
- If a test case normalizes test case **input**, then a tool should report a
  message documenting the change.

### Test types
**Change**: Renamed **test type** 'roundtrip' to 'validate'.

The general meaning of a "roundtrip" test was to confirm that a VERS
tool can parse a canonical VERS into its components and then build a canonical
VERS from those components. These functions are also known as deserialization
and serialization. The former 'roundtrip' **test type** did not provide much
value because the input and output are required to be the same - a VERS tool
can easily test this "roundtrip" behavior without a test case.

There is a high degree of similarity between the 'parse' and 'validate'
**test types** in terms of the functions a VERS tool performs. The key
difference is that the **expected output** from a 'parse' test case is
an object composed of decoded VERS components and the **expected output**
from a 'validate' test case is a VERS string. The 'validate' **test type**
does not require the input VERS string to be in canonical form.

## VERS Test Schema v0.1

The VERS Test Schema v0.1 is available at: https://packageurl.org/schemas/vers-test.schema-0.1.json.

There is also an <a href="/interactive_schemas/vers-test.schema-0.2.html" target="_blank">Interactive HTML</a> `↗`
presentation of the v0.1 VERS Test Schema.

The original VERS test suite files for the v0.1 VERS Test Schema are available
under the [vers-spec v1.0.2 release](https://github.com/package-url/vers-spec/releases/tag/v1.0.2).









