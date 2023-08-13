import sys
import os
import markdown

def convert_markdown_to_html(input_file, output_file):
    with open(input_file, 'r') as markdown_file:
        markdown_content = markdown_file.read()
        html_content = markdown.markdown(markdown_content, extensions=['extra'])

    with open(output_file, 'w') as html_file:
        html_file.write(html_content)

if len(sys.argv) < 3:
    sys.stderr.write("Usage: ./markdown2html.py <input_file> <output_file>\n")
    sys.exit(1)

input_filename = sys.argv[1]
output_filename = sys.argv[2]

if not os.path.exists(input_filename):
    sys.stderr.write(f"Missing {input_filename}\n")
    sys.exit(1)

convert_markdown_to_html(input_filename, output_filename)
sys.exit(0)
