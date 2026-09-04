---
id: how-to-parse
title: How to parse and validate VERS
sidebar_label: How to parse and validate VERS
hide_table_of_contents: false
---

# How to parse and validate VERS

## Terminology
In this document we use terminology from [Clause 5 VERS Specification of the
proposed Ecma VERS Standard](https://github.com/package-url/vers-spec/blob/main/docs/specification/standard/Clause-5-VERS-Specification.md)
The defined terms are in **bold** following Ecma style. The specific terms
are:
- **type** and **constraints** are standard VERS components
- **constraint**: refers to one instance of a constraint within a sequence of
  constraints (the **constraints** component)
- Each **constraint" is composed of a **comparator** and a
  **version**
- **comparator**: a set of characters defined in Clause 5
- **version**: the version string within a single **constraint**

## Parsing VERS

- Check that the VERS string is valid.
- Tools shall report an error if the VERS string contains any literal ASCII
  whitespace character (including SPACE, TAB, or LF).
- ASCII whitespace that is part of a **version** shall be represented by a
  percent-encoded SPACE ('%20'). Other ASCII whitespace, such as TAB or LF,
  is not permitted. The resulting version is percent-decoded exactly once
  during parsing.
- Start from the left and split once on colon ':'.
- The left-hand side is the URI scheme, which shall be lowercase.
    - Tools shall validate that the URI scheme value is 'vers'.
- The right-hand side is the "specifier".
- Split the "specifier" from the left once on a slash '/'.
- The left-hand side is the **type** component, which shall be lowercase.
  Tools should validate that the **type** is a registered **type** and report
  a warning message if the **type** is not currently registered.
- The right-hand side is the **constraints** component. Tools
  shall validate that the **constraints** component is not empty after
  splitting.
- If the string is equal to '\*', the **constraints** value is an asterisk
  ('*'). Parsing is done and no further processing is needed for this VERS.
  A tool shall report an error if there are characters other than '\*'.
- Tools shall report an error if the **constraints** component has a leading
  or trailing pipe '|'.
- Split the **constraints** string on pipe '|'. The result is a sequence of
  **constraint** strings. Tools shall report an error if consecutive
  pipes ('|') are present.
- For each **constraint** string determine:
    - If the **constraint** string starts with no **comparator** value then
      this is the implicit equality condition and the remaining string is the
      **version**.
    - If the **constraint** string starts with '=', tools shall
      report an error: the equality condition is implicit and shall be
      represented by a bare version without a leading '='.
   -  If the **constraint** string starts with one of the two-character
      **comparator** values ('>=', '<=', '!=') or with one of the
      one-character **comparator** values ('<', '>') and:
        - If it starts with '>=', then the **comparator** is '>='.
        - If it starts with '<=', then the **comparator** is '<='.
        - If it starts with '!=', then the **comparator** is '!='.
        - If it starts with '<', then the **comparator** is '<'.
        - If it starts with '>', then the **comparator** is '>'.
      Remove the **comparator** from beginning of a **constraint** string.
      The remaining string is the **version**.
    - Tools shall validate and report an error if the **version** is
      empty.
    - If the **version** contains a percent '%' character, tools shall
      validate that each '%' starts a valid percent-encoded triplet.
    - Tools shall apply percent-decoding exactly once to the **version**
      string.
      Tools shall report an error for invalid percent-encoded sequences.
    - Append the parsed **constraint** strings to the **constraints**.
- The results are the **type** and the **constraints** components.

Tools shall validate and simplify **constraints** after parsing is complete
by:

- Sorting and validating the sequence of **constraint** strings.

Tools shall report an error if the parsed **constraints** component is
invalid, including invalid ordering, duplicate versions, or invalid
**comparator** sequences. Tools shall not correct or normalise invalid input
during parsing.

### Simplifying constraints

Tools can simplify the **constraints** component using the following approach.

These pairs of contiguous **constraint** strings with these **comparators**
are valid:

- '!=' followed by anything
- '<', or '<=' followed by '!=', '>', '>=' or no **comparator** value
  (equality)
- '>', or '>=' followed by '!=', '<', or '<='

The following pairs of contiguous **constraints** with these **comparators**
are redundant and invalid (ignoring any instances of '!=' because this
**comparator** can appear anywhere):

- no **comparator** value (equality), '<' or '<=' followed by '<' or '<=:'
  this is the same as '<' or '<='
- '>' or '>=' followed by no **comparator** value (equality), '>' or '>=:'
  this is the same as '>' or '>='

A procedure to remove redundant **constraints** is:

- Start from a **constraints** string sorted by **version** where each
  **version** occurs only once in any **constraint**.

- If the **constraints** component contains only a single **constraint**
  (asterisk equal or other) return this **constraint** and simplification is
  finished.

- Split the **constraints** component into two sub lists:

    - an "unequal constraints list" where the comparator is '!='
    - a "remainder constraints list" where the comparator is not
      '!='

- If the "remainder constraints list" is empty, return the "unequal
  constraints" list and simplification is finished.

- Iterate over the **constraints** component, considering the current and next
  contiguous **constraint** strings, and the previous **constraint** string
  (e.g., before current) if it exists:

    - If the current **comparator** is '>' or '>=' and the next **comparator**
      is '>' or '>=', discard the next **constraint**.
    - If the current **comparator** is no value (equality), '<' or '<=' and
      the next **comparator** is '<' or '<=', discard the current
      **constraint**. The previous **constraint** becomes the current
      **constraint** if it exists.
    - If there is a previous **constraint**:
        - If the previous **comparator** is '>' or '>=' and the current
          **comparator** is no value (equality), '>' or '>=', discard the
          current **constraint**.
        - If the previous **comparator** is no value (equality), '<' or '<='
          and the current **comparator** is '<' or '<=', discard the previous
          **constraint**.

- Concatenate the "unequal constraints list" and the "remainder constraints
  list"

- Sort by version and return.

### Checking if a version is contained within a range

To check if a "tested version" is contained within a version range:

- Start from a parsed VERS with:

    - **type**
    - **constraints** sorted by **version** where each **version** occurs only
      once in any **constraint**

- If the **constraints** contain only one **constraint** and the
  **comparator** is '*', then the "tested version" is IN the range. The
  version check is finished.

- Select the version equality and comparison procedures suitable for
  this VERS **type** and use these for all version comparisons
  performed below.

- If the "tested version" is equal to any of the **constraint**
  **versions** where the **comparator** is for equality (any of no value,
  '<=', or '>=') then the "tested version" is IN the range. The version check
  is finished.

- If the "tested version" is equal to any of the **constraint**
  **versions** where the **constraint** **comparator**  is '!=' then the
  "tested version" is NOT IN the range. The version check is finished.

- Split the **constraints** component into two sub lists:

    - a first list where the **comparator** is no value (equality) or '!='
    - a second list where the **comparator** is neither no value (equality)
      nor '!='

- Iterate over the current and next contiguous **constraint** pairs (aka.
  pairwise) in the second list.

- For each current and next **constraint**:

    - If this is the first iteration and the current **comparator** is '<'
      or <=' and the "tested version" is less than the current
      **version** then the "tested version" is IN the range. The version check
      is finished.
    - If this is the last iteration and the next **comparator** is '>' or
      '>=' and the "tested version" is greater than the next **version**
      then the "tested version" is IN the range. The version check is
      finished.
    - If the current **comparator** is '>' or '>=' and the next **comparator**
      is '<' or '<=' and the "tested version" is greater than the
      current version and the "tested version" is less than the next
      version then the "tested version" is IN the range. The version check is
      finished.
    - If the current **comparator** is '<' or '<=' and next **comparator** is
      '>' or '>=' then these versions are NOT IN the range. Continue
      to the next iteration.

- Reaching here without having finished the version check means that the
  "tested version" is NOT IN the range.

### Notes

- Comparing **versions** from VERS with a different **type** is an
  error. Even though there may be some similarities between the "semver"
  version for an 'npm' package and the 'deb' version for its Debian packaging,
  the way **versions** are compared for each **type** may be different. Tools
  shall report an error in this case.
- All references to sorting or ordering of **constraints** means
  sorting by **version**. And sorting by **version** always means using the
  VERS **type**-specified **version** for comparison and ordering.
