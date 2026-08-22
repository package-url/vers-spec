#!/usr/bin/env python
import json
from pathlib import Path

"""
Generate Markdown documents, one for each VERS type definition JSON document.
"""


def get_yes_no(value):
    """Return a human-readable yes/no from a boolean value"""
    return "Yes" if value else "No"


def generate_documentation(definition) -> str:
    """
    Return documentation for a VERS type definition.
    """
    lines = []
    lines.append("<!--  NOTE: Auto-generated from the JSON VERS type definition.")
    lines.append("Do not manually edit this file. Edit the JSON type definition instead. -->")
    lines.append("")
    lines.append(f"# VERS Type Definition: {definition['type']}")
    lines.append("")
    lines.append(f"- **Type Name:** {definition['type_name']}")
    lines.append(f"- **Description:** {definition['description']}")
    lines.append(f"- **Schema ID:** `{definition['$id']}`")
    lines.append("")

    # VERS Examples
    lines.append("## VERS Examples")
    lines.append("")
    for example in definition["vers_examples"]:
        lines.append(f"- `{example}`")
    lines.append("")

    # Native <-> VERS example mappings (optional)
    if native_examples := definition.get("native_and_vers_examples"):
        lines.append("## Native Range to VERS Examples")
        lines.append("")
        lines.append("| Native Range | VERS Range | Note |")
        lines.append("|--------------|------------|------|")
        for ex in native_examples:
            native_range = ex["native_range"]
            vers_range = ex["vers_range"]
            note = ex.get("note", "")
            lines.append(f"| `{native_range}` | `{vers_range}` | {note} |")
        lines.append("")

    # Top-level reference URLs (optional)
    if reference_urls := definition.get("reference_urls"):
        lines.append("## Reference URLs")
        lines.append("")
        for url in reference_urls:
            lines.append(f"- `{url}`")
        lines.append("")

    # Top-level note (optional)
    if note := definition.get("note"):
        lines.append("## Note")
        lines.append("")
        lines.append(note)
        lines.append("")

    return "\n".join(lines)


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 2:
        selected_types = f"{sys.argv[1]}-definition.json"
    else:
        selected_types = "*-definition.json"

    types = []
    types_dir = Path("types")
    for filepath in types_dir.glob(selected_types):
        data = json.loads(filepath.read_text())
        vtype = data["type"]
        types.append(vtype)
        md = generate_documentation(data)
        mddoc = Path("docs/types/definitions") / f"{vtype}-definition.md"
        mddoc.parent.mkdir(parents=True, exist_ok=True)
        mddoc.write_text(md, newline="\n")
        print(f"VERS Type Documentation generated for {mddoc}")

    idxdoc = Path("vers-types-index.json")
    idx = json.dumps(sorted(types), indent=2) + "\n"
    idxdoc.write_text(idx, newline="\n")
    print(f"VERS Types Index generated at {idxdoc}")
