#!/usr/bin/env python3
"""Parse the saved HTML files for parameter tables. Extract operation name + params."""
import json, re
from pathlib import Path
from html.parser import HTMLParser

ROOT = Path("/Users/sklee01/tourism-service-lab-v2")
SRC = ROOT/"scripts/detail-pages"
OUT = ROOT/"scripts/parsed-params.json"

class TableScraper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tables = []
        self.cur_table = None
        self.cur_row = None
        self.cur_cell = None
        self.depth = 0
        self.tag_stack = []
        self.attr_stack = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.tag_stack.append(tag)
        self.attr_stack.append(a)
        if tag == "table":
            self.cur_table = {"attrs": a, "rows": []}
        elif tag == "tr" and self.cur_table is not None:
            self.cur_row = []
        elif tag in ("td", "th") and self.cur_row is not None:
            self.cur_cell = []

    def handle_endtag(self, tag):
        if self.tag_stack and self.tag_stack[-1] == tag:
            self.tag_stack.pop()
            self.attr_stack.pop()
        if tag == "table" and self.cur_table is not None:
            self.tables.append(self.cur_table)
            self.cur_table = None
        elif tag == "tr" and self.cur_row is not None and self.cur_table is not None:
            self.cur_table["rows"].append(self.cur_row)
            self.cur_row = None
        elif tag in ("td", "th") and self.cur_cell is not None and self.cur_row is not None:
            self.cur_row.append("".join(self.cur_cell).strip())
            self.cur_cell = None

    def handle_data(self, data):
        if self.cur_cell is not None:
            self.cur_cell.append(data)


def parse_html_for_params(html):
    """Return list of {op, params: [...]}"""
    # find operation blocks via comments or headings
    # detail page has tabular sections; let's try simpler regex on .paramTbody
    # We look for patterns: <tbody class="...paramTbody..." id="paramTbody_XX">...</tbody>
    ops = []

    # Method 1: find operation list with names and ids
    # detail/spec list has rows like: <td>1</td><td>tatsCnctrRatedList ...</td>...
    op_names = re.findall(r"<td[^>]*>([a-zA-Z][a-zA-Z0-9_]+List[12]?[a-zA-Z]*)\s*</td>", html)
    op_names = list(dict.fromkeys(op_names))

    # Method 2: tbody.paramTbody blocks
    bodies = re.findall(r'<tbody[^>]*(?:id|class)="[^"]*paramTbody[^"]*"[^>]*>(.*?)</tbody>',
                        html, flags=re.DOTALL|re.IGNORECASE)
    # also tbody ids with paramTbody_NN
    bodies2 = re.findall(r'<tbody[^>]*id="paramTbody[_0-9]*"[^>]*>(.*?)</tbody>',
                         html, flags=re.DOTALL|re.IGNORECASE)
    all_bodies = bodies + bodies2

    parsed = []
    for body in all_bodies:
        # extract rows
        rows = re.findall(r"<tr[^>]*>(.*?)</tr>", body, flags=re.DOTALL)
        params = []
        for r in rows:
            cells = re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", r, flags=re.DOTALL)
            text_cells = [re.sub(r"<[^>]+>", "", c).strip() for c in cells]
            text_cells = [re.sub(r"\s+", " ", c) for c in text_cells]
            if len(text_cells) >= 2 and re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", text_cells[0]):
                params.append({"name": text_cells[0], "sample": text_cells[1] if len(text_cells)>1 else "",
                               "desc": text_cells[2] if len(text_cells)>2 else "",
                               "required": "필수" in " ".join(text_cells)})
        if params:
            parsed.append(params)

    return {"op_names": op_names, "param_groups": parsed}


out = {}
for f in sorted(SRC.glob("*.html")):
    html = f.read_text(encoding="utf-8")
    out[f.stem] = parse_html_for_params(html)

OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
for k, v in out.items():
    print(f"\n== {k}")
    print(f"  ops: {v['op_names'][:10]}")
    print(f"  param groups: {len(v['param_groups'])}")
    for g in v['param_groups'][:3]:
        print(f"    {[(p['name'], p['sample']) for p in g[:6]]}")
