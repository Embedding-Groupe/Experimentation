import sys
import os
import json
import tree_sitter_python as tspython
from tree_sitter import Language, Parser

def main():
    target_file = "test.py"
    if len(sys.argv) > 1:
        target_file = sys.argv[1]
    
    if not os.path.exists(target_file):
        print(f"File {target_file} not found.")
        return

    try:
        PY_LANGUAGE = Language(tspython.language())
        parser = Parser(PY_LANGUAGE)
    except Exception as e:
        print(f"Error initializing parser: {e}")
        # Fallback or older API handling if needed, but 0.22+ uses this
        return

    with open(target_file, "rb") as f:
        source_code = f.read()

    tree = parser.parse(source_code)
    root_node = tree.root_node

    non_keywords = []
    
    # Types to keep
    KEEP_TYPES = {
        "identifier",
        "string",
        "integer", 
        "float",
        "true",
        "false",
        "none"
    }

    def traverse(node):
        # We check the type
        # For strings, we want the whole string literal including quotes
        if node.type == "string":
            text = source_code[node.start_byte:node.end_byte].decode("utf8")
            non_keywords.append(text)
            return # Do not traverse inside string
        
        if node.type in KEEP_TYPES:
            text = source_code[node.start_byte:node.end_byte].decode("utf8")
            non_keywords.append(text)
        
        for child in node.children:
            traverse(child)

    traverse(root_node)

    output_filename = os.path.splitext(target_file)[0] + ".json"
    
    with open(output_filename, "w", encoding="utf8") as f:
        json.dump(non_keywords, f, indent=4, ensure_ascii=False)
        
    print(f"Successfully extracted {len(non_keywords)} items to {output_filename}")

if __name__ == "__main__":
    main()
