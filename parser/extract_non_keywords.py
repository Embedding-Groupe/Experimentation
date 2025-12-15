import sys
import os
import json
import tree_sitter_python as tspython
from tree_sitter import Language, Parser

def main(target_file: str):
    """
    Ce script analyse un fichier Python spécifié en utilisant `tree-sitter` 
    pour en extraire les éléments non-mots-clés. Il identifie les identifiants, 
    les chaînes de caractères, les entiers, les flottants, les booléens et `None`.
    Les éléments extraits sont ensuite sauvegardés dans un fichier JSON 
    portant le même nom que le fichier source, avec une extension `.json`.    
    """

    # permet l'appel du script en ligne de commande
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
    main("test.py")
