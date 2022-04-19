from docutils.nodes import image, reference, TextElement, Element
from sphinx.application import Sphinx
from sphinx.writers.html5 import HTML5Translator


# Base from sphinx.writers.html5.HTML5Translator.visit_reference
def visit_reference(self, node: Element):
    atts = {"class": "reference"}
    if node.get("internal") or "refuri" not in node:
        atts["class"] += " internal"
    else:
        atts["class"] += " external"
        # overwritten
        atts["target"] = "_blank"
        atts["rel"] = "noreferrer"
    if "refuri" in node:
        atts["href"] = node["refuri"] or "#"
        if self.settings.cloak_email_addresses and atts["href"].startswith("mailto:"):
            atts["href"] = self.cloak_mailto(atts["href"])
            self.in_mailto = True
    else:
        assert "refid" in node, 'References must have "refuri" or "refid" attribute.'
        atts["href"] = "#" + node["refid"]
    if not isinstance(node.parent, TextElement):
        assert len(node) == 1 and isinstance(node[0], image)
        atts["class"] += " image-reference"
    if "reftitle" in node:
        atts["title"] = node["reftitle"]
    if "target" not in node:
        pass
    elif "target" in atts:
        atts["target"] += " " + node["target"]
    else:
        atts["target"] = node["target"]
    self.body.append(self.starttag(node, "a", "", **atts))

    if node.get("secnumber"):
        self.body.append(
            ("%s" + self.secnumber_suffix) % ".".join(map(str, node["secnumber"]))
        )


def setup(app: Sphinx):
    app.add_node(
        reference, True, html=(visit_reference, HTML5Translator.depart_reference)
    )
