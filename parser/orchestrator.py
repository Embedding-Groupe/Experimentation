import sys
import os
import extract_non_keywords
import split_identifiers
import get_word_presence

def main():
    if len(sys.argv) < 2:
        print("Usage: python orchestrator.py <path_to_python_script>")
        return

    input_script = sys.argv[1]
    
    if not os.path.exists(input_script):
        print(f"Error: File {input_script} not found.")
        return

    # 1. Extraction
    print(f"--- Step 1: Extracting non-keywords from {input_script} ---")
    # extract_non_keywords.main() expects the python file path. 
    # It creates a json file with the same basename.
    extract_non_keywords.main(input_script)
    
    # Determine the output JSON path
    # extract_non_keywords uses os.path.splitext(target_file)[0] + ".json"
    json_output = os.path.splitext(input_script)[0] + ".json"
    
    if not os.path.exists(json_output):
        print(f"Error: Expected output file {json_output} was not created.")
        return

    # 2. Splitting
    print(f"--- Step 2: Splitting identifiers in {json_output} ---")
    split_identifiers.main(json_output)

    # 3. Frequency
    print(f"--- Step 3: Calculating word frequencies in {json_output} ---")
    get_word_presence.main(json_output)

    print(f"\nPipeline complete. Results saved in {json_output}")

if __name__ == "__main__":
    main()
