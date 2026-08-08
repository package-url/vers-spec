# Conformance

A conforming implementation of Version Range Specifier (VERS) shall fully
implement and support all elements defined within this Standard, including the
syntax, components, and semantic requirements for constructing and
interpreting valid VERS notations.

A conforming implementation of VERS shall adhere to the syntax defined in this
Standard, ensuring that all VERS notations are constructed, parsed, and
validated according to the prescribed rules. The implementation shall provide
full support for ecosystem-agnostic behaviour, enabling VERS to function
consistently and reliably across diverse environments.

All required components of a VERS notation - **scheme**, **type**, and
**constraints** - shall be present and validated according to the rules
defined in this Standard.

Implementations shall ensure that equivalent VERS notations are consistently
resolved to the same canonical representation. This includes strict adherence
to normalisation and equivalence rules. Furthermore, implementations shall
process URI encoding and decoding for VERS components according to the
standards outlined in RFC 3986.

Invalid VERS notations that fail to conform to the specification shall be
identified and rejected by any conforming implementation. This guarantees the
integrity and reliability of VERS notations in all supported contexts.

A conforming implementation of VERS may extend its functionality by providing
ecosystem-specific validation, processing, or metadata handling, as long as
these extensions do not violate the core specification. Additionally,
implementations may offer auxiliary tools or features, such as utilities for
constructing or validating VERS notations, provided they align with the
Standard's requirements.

A conforming implementation shall not redefine or alter the core syntax,
components, or semantics defined by this Standard. Any prohibited
extensions explicitly identified in the specification shall not be
implemented. Furthermore, behaviours that compromise the interoperability of
VERS across tools, platforms, or ecosystems are strictly disallowed.