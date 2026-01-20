# How to parse and validate VERS

## Parsing and validating VERS notation

To parse a VERS string:

- Remove all spaces and tabs.
- Start from left, and split once on colon ':'.
- The left hand side is the URI-scheme that shall be lowercase.
    - Tools shall validate that the URI-scheme value is VERS.
- The right hand side is the specifier.
- Split the specifier from left once on a slash '/.
- The left hand side is the **version-scheme** that shall be
  lowercase. Tools should validate that the **version-scheme** is a
  known scheme.
- The right hand side is a list of one or more constraints. Tools 
  validate that this **version-constraints** string is not empty
  ignoring spaces.
- If the string is equal to '\*', the **version-constraints** value is
 '*'. Parsing is done and no further processing is needed for this VERS.
  A tool should report an error if there are characters other than'\*'.
- Strip leading and trailing pipes '|' from the constraints string.
- Split the constraints on pipe '|'. The result is a list of
  **version-constraints** strings. Consecutive pipes shall be treated as one.
  Leading and trailing pipes are ignored.
- For each **version-constraints** string:
    - Determine if the **version-constraints** string starts with one of the
     two **comparators**: [what does this mean? 2 versus a list of 5]
        - If it starts with '>=', then the comparator is '>='.
        - If it starts with '<=', then the comparator is '<='.
        - If it starts with '!=', then the comparator is '!='.
        - If it starts with '<', then the comparator is '<'.
        - If it starts with '>', then the comparator is '>'.
        - Remove the comparator from **version-constraints** string
          start. The remaining string is the version.
    - Otherwise the version is the full **version-constraints** string
      (which implies an equality comparator of '=')
    - Tools should validate and report an error if the version is
      empty.
    - If the version contains a percent '%' character, apply URL
      quoting rules to unquote this string.
    - Append the parsed **version-constraints** strings to the
      constraints list.

Finally:

- The results are the **version-scheme** and the list of
  **version-constraints** strings.

Tools should optionally validate and simplify the list of 
**version-contraints** strings once parsing is complete by:

- sorting and validating the list of constraints
- Simplifying the list of constraints

### Version-constraints simplification

Tools can simplify a list of **version-constraints** strings using this approach:

These pairs of contiguous constraints with these **comparators** are valid:

- '!=' followed by anything
- '=', '<', or '<=' followed by '=', '!=', '>', or '>='
- '\>', or '>=' followed by '!=', '<', or '<='

These pairs of contiguous constraints with these **comparators** are
redundant and invalid (ignoring any '!=; because it they can show up
anywhere):

- '=', '<' or '<=' followed by '<' or '<=:' this is the same as '<' or '<='
- '\>' or '>=' followed by '=', '>' or '>=:' this is the same as '>' or '>='

A procedure to remove redundant constraints can be:

- Start from a list of constraints of **comparator** and **version**, sorted
  by **version** where each **version** occurs only once in any
  constraint.

- If the constraints list contains a single constraint (star, equal or
  anything) return this list and simplification is finished.

- Split the constraints list in two sub lists:

    - a list of "unequal constraints" where the comparator is '!='
    - a remainder list of "constraints" where the comparator is not
      '!='

- If the remainder list of "constraints" is empty, return the "unequal
  constraints" list and simplification is finished.

- Iterate over the constraints list, considering the current and next
  contiguous constraints, and the previous constraint (e.g., before
  current) if it exists:

    - If current comparator is '>' or '>=' and next comparator is
      '=', '>' or '>=', discard the next constraint
    - If current comparator is '=', '<' or '<=' and the next
      comparator is '<' or '<=', discard current constraint.
      The previous constraint becomes current if it exists.
    - If there is a previous constraint:
        - If previous comparator is '>' or '>=' and current
          comparator is '=', '>' or '>=', discard the current
          constraint
        - If previous comparator is '=', '<' or '<=' and current
          comparator is '<' or '<=', discard the previous constraint

- Concatenate the "unequal constraints" list and the filtered
  "constraints" list

- Sort by version and return.

### Checking if a version is contained within a range

To check if a "tested version" is contained within a version range:

- Start from a parsed a version range specifier with:

    - a **version-scheme**
    - a list of constraints of **comparator** and **version**, sorted by
      version and where each version occurs only once in any
      constraint.

- If the constraint list contains only one item and the comparator is
  '*', then the "tested version" is IN the range. Check is finished.

- Select the version equality and comparison procedures suitable for
  this versioning scheme and use these for all version comparisons
  performed below.

- If the "tested version" is equal to the any of the constraint
  versions where the constraint comparator is for equality (any of '=',
  '<=', or '>=') then the "tested version" is in the range. Check is
  finished.

- If the "tested version" is equal to the any of the constraint
  versions where the constraint comparator is '!=' then the "tested
  version" is NOT in the range. Check is finished.

- Split the constraint list in two sub lists:

    - a first list where the comparator is '=' or '!='
    - a second list where the comparator is neither '=' nor '!='

- Iterate over the current and next contiguous constraint pairs (aka.
  pairwise) in the second list.

- For each current and next constraint:

    - If this is the first iteration and current comparator is '<'
      or <=' and the "tested version" is less than the current
      version then the "tested version" is IN the range. Check is
      finished.
    - If this is the last iteration and next comparator is '>' or
      '>=' and the "tested version" is greater than the next version
      then the "tested version" is IN the range. Check is finished.
    - If current comparator is '>' or '>=' and next comparator is
      '<' or '<=' and the "tested version" is greater than the
      current version and the "tested version" is less than the next
      version then the "tested version" is IN the range. Check is
      finished.
    - If current comparator is '<' or '<=' and next comparator is
      '>' or '>=' then these versions are out the range. Continue
      to the next iteration.

- Reaching here without having finished the check before means that
  the "tested version" is NOT in the range.

### Notes and caveats

- Comparing versions from VERS notations with a different
  **version-scheme** is an error. Even though there may be some
  similarities between the "semver" version for an "npm" and the
  "deb" version for its Debian packaging, the way versions are
  compared for each **version-scheme** may be different. Tools should
  report an error in this case.
- All references to sorting or ordering of version constraints mean
  sorting by version. And sorting by versions always implies using the
  **version-scheme**-specified version comparison and ordering.
