---
id: test-schema-changes
title: VERS test schema v0.2 changes
sidebar_label: Test schema changes
hide_table_of_contents: true
---

# VERS test schema v0.2 changes
The VERS test schema was updated to: https://packageurl.org/schemas/vers-test.schema-0.2.json
on August 4, 2026. This update includes an automated update to all of the VERS
test suite files at: `vers-spec/tests/`. See a summary of the changes below.

The original VERS test suite files for the [VERS test schema v0.1](https://packageurl.org/schemas/vers-test.schema-0.1.json)
remain available under [vers-spec v1.0.2](https://github.com/package-url/vers-spec/releases/tag/v1.0.2).

### Test groups
**Change**: Renamed
- 'base' to 'required'
- 'advanced' to 'recommended'

This change removes the ambiguity of the **test group** names from the v0.1
VERS test schema by using names that map to Ecma conformance terminology.

### Test messages
**Change**: Renamed **expected_failure_reason** to **expected_message**

The terminology of the v0.1 VERS test schema did not provide a
way to provide a test case message for the use case:
- When an **input** contains an unregistered VERS **type**. This applies to
  all **test types**. It seems important to document that a VERS **type**
  is not registered because this means that the VERS **type** is effectively
  unknown across the tools and databases that implement VERS.

### Test types
**Change**: Renamed **test type** 'roundtrip' to 'validate'.

The general meaning of a "roundtrip" test was to confirm that a VERS
tool can parse a canonical VERS into its components and then build a canonical
VERS from those components - these functions are also known as deserialization
and serialization. The former 'roundtrip' **test type** did not provide much
value because the input and output are required to be the same - a VERS tool
can easily test this "roundtrip" behavior without a test case.

There is a high degree of similarity between the 'parse' and 'validate'
**test types** in terms of the functions a VERS tool performs. The key
difference is that the **expected output** from a 'parse' test case is
an object composed of decoded VERS components and the **expected output**
from a 'validate' test case is a VERS string. The 'validate' **test type**
does not require the input VERS string to be in canonical form.









