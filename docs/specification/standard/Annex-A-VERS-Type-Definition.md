# Annex A (normative) VERS Type Definition
This Annex provides a copy of the current Version Range Specifier (VERS) Type Definition Schema. The format is JSON Schema version Draft 2020-12.

The schema shown below is available in electronic form at: https://packageurl.org/schemas/vers-type-definition.schema-0.2.json

~~~
{
  "$schema": "https://json-schema.org/draft/2020-12/schema#",
  "$id": "https://packageurl.org/schemas/vers-type-definition.schema-0.2.json",
  "title": "Version Range Specifier (VERS) Type Definition",
  "description": "Schema to define the structure of a VErsion Range Specifier (VERS) type.",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "$id",
    "type",
    "type_name",
    "description",
    "vers_examples"
  ],
  "properties": {
    "$schema": {
      "title": "JSON schema",
      "description": "URL of the JSON schema for VERS type definition.",
      "const": "https://packageurl.org/schemas/vers-type-definition.schema-0.2.json",
      "format": "uri"
    },
    "$id": {
      "title": "VERS type definition id",
      "description": "The unique identifier URI for this VERS type definition.",
      "type": "string",
      "pattern": "^https:\\/\\/packageurl\\.org/vers-types/[a-z0-9-]+-definition\\.json$"
    },
    "type": {
      "title": "VERS type",
      "description": "The type string for this VERS type.",
      "type": "string",
      "pattern": "^[a-z][a-z0-9-\\.]+$",
      "examples": [
        "semver",
        "maven",
        "pypi",
        "npm"
      ]
    },
    "type_name": {
      "title": "Type name",
      "description": "The name of this VERS type.",
      "type": "string",
      "examples": [
        "Apache Maven Dependency Version Requirement",
        "npm version range"
      ]
    },
    "description": {
      "title": "Description",
      "description": "The description of this VERS type.",
      "type": "string",
      "examples": [
        "Apache Maven dependency version requirement as defined in a Maven POM.",
        "npm dependencies version range as defined in a package.json.",
        "RubyGems version requirement restrictions using restriction operators."
      ]
    },
    "vers_examples": {
      "title": "VERS examples",
      "description": "Examples of valid VERS notations for this VERS type.",
      "type": "array",
      "uniqueItems": true,
      "minItems": 1,
      "items": {
        "type": "string",
        "pattern": "^vers:[a-z][a-z0-9-\\.]+/.*$"
      },
      "examples": [
        [
          "vers:npm/1.223",
          "vers:semver/<1.2.2|>2.0.0|=7.0.0"
        ]
      ]
    },
    "native_range_and_vers_equivalent_examples": {
      "title": "Examples of native version ranges and their VERS equivalents.",
      "description": "Optional list of examples of native version ranges mapped to their corresponding VERS syntax.",
      "type": "array",
      "uniqueItems": true,
      "minItems": 1,
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "native_range",
          "vers"
        ],
        "properties": {
          "native_range": {
            "title": "Native range example",
            "description": "Native range example for this VERS type.",
            "type": "string"
          },
          "vers": {
            "title": "Corresponding VERS notation",
            "description": "Corresponding VERS notation for this VERS type.",
            "type": "string"
          },
          "note": {
            "title": "Note",
            "description": "Optional note about this example.",
            "type": "string"
          },
          "reference_url": {
            "title": "Reference URL",
            "description": "Optional reference URL for this native range example.",
            "type": "string",
            "format": "uri"
          }
        }
      }
    },
    "note": {
      "title": "Note",
      "description": "Note about this VERS type.",
      "type": "string"
    },
    "reference_urls": {
      "title": "Reference URLs",
      "description": "List of informational reference URLs about this VERS type, such as specifications or reference code.",
      "type": "array",
      "uniqueItems": true,
      "minItems": 1,
      "items": {
        "type": "string",
        "format": "uri"
      },
      "examples": [
        "https://maven.apache.org/pom.html#dependency-version-requirement-specification",
        "https://github.com/npm/node-semver",
        "https://docs.npmjs.com/cli/v12/configuring-npm/package-json#dependencies",
        "https://github.com/ruby/ruby/blob/d1c079751b80352d347452c8d134ffb177838adb/lib/rubygems/requirement.rb#L6"
      ]
    }
  }
}
~~~
