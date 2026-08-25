<!--  NOTE: Auto-generated from the JSON VERS type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# VERS Type Definition: pypi

- **Type Name:** pypi versioning
- **Description:** pypi versioning version ranges.
- **Schema ID:** `https://packageurl.org/vers-types/pypi-definition.json`

## VERS Examples

- `vers:pypi/<=1.3.0|3.0.0`
- `vers:pypi/>=1.0.0|<=2.0.0`
- `vers:pypi/>=3.0.0|2.0.3`
- `vers:pypi/>=3.0.0|!=2.0.3`
- `vers:pypi/0.0.2|0.0.6|>=3.0.0|0.0.1|0.0.4|0.0.5|0.0.3`

## Native Range to VERS Examples

| Native Range | VERS Range | Note |
|--------------|------------|------|
| `>= 1.0` | `vers:pypi/>=1.0` |  |
| `<2.1.0` | `vers:pypi/<2.1.0` |  |
| `!=5` | `vers:pypi/!=5` |  |
| `>=1.0a1,<1.0.5\|\|>=1.1b1,<1.1.1` | `vers:pypi/>=1.0a1\|<1.0.5\|>=1.1b1\|<1.1.1` |  |
| `>=5.0.0,<5.0.12\|\|>=6.0.0,<6.0.5\|\|>=6.1.0,<6.2.2` | `vers:pypi/>=5.0.0\|<5.0.12\|>=6.0.0\|<6.0.5\|>=6.1.0\|<6.2.2` |  |
| `<21.2.3\|\|>=22.0.0,<22.2.3\|\|>=23.0.0,<23.0.3` | `vers:pypi/<21.2.3\|>=22.0.0\|<22.2.3\|>=23.0.0\|<23.0.3` |  |
| `==2.3.0\|\|==3.0.0` | `vers:pypi/2.3.0\|3.0.0` |  |

## Reference URLs

- `https://www.python.org/dev/peps/pep-0440/`
