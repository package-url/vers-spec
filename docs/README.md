This README explains the organization of documentation files for the VERS
specification.

## VERS specification documentation
The files stored in `vers-spec/docs/specification/standard/` are expected to 
be used in the VERS standard which we plan to submit to Ecma International as
a new standard in 2026.

The other files in the `vers-spec/docs/specification/` folder are also 
specification documentation, but we are not planning to include them in the 
(future) Ecma VERS standard. Most of these documents provide information to 
support implementation of the VERS Specification in software tools or 
databases.

## VERS tests documentation
The files stored in `vers-spec/docs/tests/` provide documentation that 
explains the structure of the VERS test suite, how a VERS implementation tool
can use the test suite (future), and how to create VERS test cases (future).

## VERS types documentation
The files stored in `vers-spec/docs/types/` provide documentation for the 
definition and usage of VERS types:
- One file for each VERS type generated from the corresponding JSON definition
  file (future)
- Files that explain the semantics for version range interpretation for a 
  VERS type including especially how to compare two versions (future)

**NB:** Some files in the `docs` folder contain "front matter" that
is used for publishing the content on the www.packageurl.org website.
The "front matter" layout is:

|                        |       |
| ---------------------- | ----- |
| id                     |       |
| title                  |       |
| sidebar_label          |       |
| hide_table_of_contents |       |
