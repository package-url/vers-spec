---
id: test-overview
title: VERS test overview
sidebar_label: Test overview
hide_table_of_contents: true
---

# VERS test overview

The Version Range Specifier (VERS) specification provides test files to
support language-neutral testing of VERS implementations. The objectives for
the VERS test suite is to:
- Enable tools to demonstrate conformance with the VERS specification as
  defined in the [VERS Core Specification](https://packageurl.org/docs/vers/specification)
  or in registered VERS **type** definitions.
- Help tools identify and fix common problems in VERS data.

The structure of test cases used in VERS test files is defined in a JSON
schema that is available at: https://packageurl.org/schemas/vers-test.schema-0.2.json.

## Conformance
Since the primary goal for the VERS test suite is to help VERS tools achieve
and demonstrate conformance with the VERS specification, it is important to
state what we mean by conformance. Conformance for VERS is defined in the
VERS specification files at: https://github.com/package-url/vers-spec/tree/main/docs/specification/standard.

A  summary is: "A conforming implementation of Version Range Specifier (VERS)
shall fully implement and support all elements defined within this Standard,
including the syntax, components, and semantic requirements for constructing
and interpreting valid VERS notations."

Other VERS documentation such as "How to parse and validate VERS" is important
but not part of the VERS Standard for conformance purposes.

Some common words have a very specific meaning for Ecma conformance:
- "canonical form" means a VERS string or a set of VERS components in the
  format that matches the Standard for a string or components respectively
- "normalization" means the process of structuring, standardizing, or
  converting data to conform to a standard format - i.e. canonical form.
- "shall" indicates a requirement (Ecma & ISO definition)
- "should" indicates a recommendation (Ecma & ISO definition)

The VERS Standard requires that:
- A VERS string is in canonical form or
- Each VERS component in a set (object) conforms to the VERS Standard.

## Terminology
Some key terminology for VERS tests is:

| Term            | Definition                                              |
|-----------------|---------------------------------------------------------|
| VERS component  | One of the 3 components of a VERS string  |
| VERS data       | Summary term for a VERS string or an object composed of VERS components |
| VERS Standard   | Refers to the VERS Core Specification                    |
| VERS tool       | A software program that implements one or more VERS functions such as building or parsing a VERS notation or determining whether a version is contained within VERS **constraints** |
| VERS type registration | Means that there is a VERS type definition file (JSON) in the `vers-spec` repository |
| test case       | Is a single test example within a *test file*         |
| test file       | Is a set of *test cases*                              |
| test suite      | Is the entire set of current VERS *test files*        |

