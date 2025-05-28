import xml.dom.minidom as minidom
import xml.sax
import time

# DOM implementation
def analyze_go_terms_dom(xml_file):
    start = time.time()
    
    dom_tree = minidom.parse(xml_file)
    terms = dom_tree.getElementsByTagName("term")

    # Store max <is_a> counts per namespace with a list of IDs
    max_terms = {
        "biological_process": [[], 0],
        "molecular_function": [[], 0],
        "cellular_component": [[], 0]
    }

    for term in terms:
        namespace = term.getElementsByTagName("namespace")[0].firstChild.nodeValue
        go_id = term.getElementsByTagName("id")[0].firstChild.nodeValue
        is_a_count = len(term.getElementsByTagName("is_a"))

        if namespace in max_terms:
            if is_a_count > max_terms[namespace][1]:
                max_terms[namespace] = [[go_id], is_a_count]
            elif is_a_count == max_terms[namespace][1]:
                max_terms[namespace][0].append(go_id)

    end = time.time()
    duration = end - start

    print("DOM Results:")
    for ns, (ids, count) in max_terms.items():
        print(f"{ns}: {ids} with {count} <is_a>")
    print(f"DOM processing time: {duration:.4f} seconds\n")
    
    return duration


# SAX handler class
class GOSaxHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_tag = ""
        self.namespace = ""
        self.go_id = ""
        self.is_a_count = 0

        self.max_terms = {
            "biological_process": [[], 0],
            "molecular_function": [[], 0],
            "cellular_component": [[], 0]
        }

    def startElement(self, tag, attrs):
        self.current_tag = tag
        if tag == "term":
            self.namespace = ""
            self.go_id = ""
            self.is_a_count = 0
        elif tag == "is_a":
            self.is_a_count += 1

    def characters(self, content):
        if self.current_tag == "namespace":
            self.namespace += content.strip()
        elif self.current_tag == "id":
            self.go_id += content.strip()

    def endElement(self, tag):
        if tag == "term":
            if self.namespace in self.max_terms:
                if self.is_a_count > self.max_terms[self.namespace][1]:
                    self.max_terms[self.namespace] = [[self.go_id], self.is_a_count]
                elif self.is_a_count == self.max_terms[self.namespace][1]:
                    self.max_terms[self.namespace][0].append(self.go_id)
        self.current_tag = ""


# SAX implementation
def analyze_go_terms_sax(xml_file):
    start = time.time()
    
    handler = GOSaxHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(xml_file)

    end = time.time()
    duration = end - start

    print("SAX Results:")
    for ns, (ids, count) in handler.max_terms.items():
        print(f"{ns}: {ids} with {count} <is_a>")
    print(f"SAX processing time: {duration:.4f} seconds\n")
    
    return duration


# Main function to run both analyses and compare speed
if __name__ == "__main__":
    xml_file = "go_obo.xml"  # Make sure this file is in the same directory or use full path

    dom_time = analyze_go_terms_dom(xml_file)
    sax_time = analyze_go_terms_sax(xml_file)

    if dom_time < sax_time:
        print("# DOM was faster")
    elif sax_time < dom_time:
        print("# SAX was faster")
    else:
        print("# Both methods took the same time")
