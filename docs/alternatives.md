# Implementations and alternatives

[Since we did not bring over lines 627-640 from `VERSION-RANGE-SPEC.md`, we
might want to change the top heading and dispense with the second-level
heading below.]

## Related efforts and alternative

- CUDF defines a generic range notation similar to Debian and integer
  version numbers from the sequence of versions for universal
  dependencies resolution https://www.mancoosi.org/cudf/primer/
- OSV is an "Open source vulnerability DB and triage service." It
  defines vulnerable version range semantics using a minimal set of
  comparators for use with package "ecosystem" and version range
  "type". https://github.com/google/osv
- libversion is a library for general purpose version comparison using
  a unified procedure designed to work with many package types.
  https://github.com/repology/libversion
- unified-range is a library for uniform version ranges based on the
  Maven version range spec. It supports Apache Maven and npm ranges
  https://github.com/snyk/unified-range
- dephell specifier is a library to parse and evaluate version ranges
  and "work with version specifiers (can parse PEP 440, SemVer, Ruby,
  NPM, Maven)" https://github.com/dephell/dephell_specifier

*[JMH: Do we want the entities named in these bullets ^ highlighted, e.g.,
backticks, bold, double quotes?]*
