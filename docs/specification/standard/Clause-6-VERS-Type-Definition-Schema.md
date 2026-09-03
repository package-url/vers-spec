# 6 VERS Type Definition Schema

The VERS Type Definition JSON Schema is the reference data model that is used
to define VERS **types** in a structured way. Each VERS **type** is specified
in a JSON document that matches this schema. These JSON documents are then
used to generate VERS **type** documentation and to support VERS tools and
libraries so that they can more easily build, parse, and validate PURLs by
**type** in a consistent and standardized manner across programming languages
and technology stacks.

## 6.1 JSON Schema

The VERS Type Definition Schema is formally specified by a Draft 2020-12 JSON
Schema. Each published version of this specification is accompanied by a
versioned meta-schema at a stable URI:

https://packageurl.org/schemas/vers-type-definition.schema-<major>.<minor>.json

**Location:** /

**Type:** Object

Schema to specify a Version Range Specifier (VERS) type as a structured definition.

**Table 2: Properties for the root object**

| **Property**          | **Type** | **Requirement** | **Description**         |
| --------------------- | -------- | ---------------- | ------|
| type                  | String   | Required        | The type string for this VERS type.                                                                     |
| type_name             | String   | Required        | The name for this VERS type.                                                                           |
| description           | String   | Required        | The description of this VERS type.                                                                     |
| vers_examples         | Array    | Required        | Examples for valid VERS ranges for this VERS type.                                                     |
| native_and_vers_equivalent_examples | Array  | Optional | List of examples of valid, native version ranges mapped to their corresponding VERS syntax.        |
| note                  | String   | Optional        | Note about this VERS type.                                                                         |
| reference_urls        | Array    | Optional        | List of informational reference URLs about this VERS type, such as specifications or reference code. |

## 6.2 VERS type

**Location:** /type

**Property:** type (Required)

**Type:** String

**Pattern Constraint:** ^\[a-z\]\[a-z0-9-\\.\]+\$

The type string for this VERS type.

**Example 1 (Informative)**

    maven

*Example 2 (Informative)**

    npm

**Example 3 (Informative)**

    pypi

## 6.3 Type name

**Location:** /type_name

**Property:** type_name (Required)

**Type:** String

The name for this VERS type.

**Example 1 (Informative)**

    Apache Maven Dependency Version Requirement

**Example 2 (Informative)**

    npm version range

## 6.4 Description


**Property:** description (Required)

**Type:** String

The description of this VERS type.

## 6.5 VERS examples

**Location:** /vers_examples

**Property:** vers_examples (Required)

**Type:** Array (of String)

**Pattern Constraint:** ^vers:[a-z][a-z0-9-\\.]+/.*$

Examples of valid VERS ranges for this VERS type.

_All items shall be unique._

## 6.6 Native range and VERS equivalent examples

**Location:** /native_range_and_vers_equivalent_example

**Property:** native_range_and_vers_equivalent_examples (Optional)

**Type:** Object

The definition of native and VERS range equivalents for a VERS type. This
information is optional for a VERS type.

**Table 3: Properties for the native_and_vers_equivalent_examples object**

| **Property**           | **Type** | **Requirement** | **Description**                                              |
| ---------------------- | -------- | --------------- | ------------------------------------------------------------ |
| native_range           | String   | Required        | Native range example for this VERS type.                     |
| vers                   | String   | Required        | Corresponding VERS notation for this VERS type.              |
| note                   | String   | Optional        | Optional note about this example.                            |
| reference_url          | URI as specified in RFC 3986 | Optional | Optional reference URL for this native range example. |

## 6.7 Note

**Location:** /note

**Property:** note (Optional)

**Type:** String

Note about this VERS type.

## 6.8 Reference URLs

**Location:** /reference_urls

**Property:** reference_urls (Optional)

**Type:** array (of String)

**Format:** URI as specified in [RFC 3986](https://www.ietf.org/rfc/rfc3986.html)

Optional list of informational reference URLs about this VERS type. Each item of this array shall be a string.

_All items shall be unique._
