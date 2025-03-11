import langgraph.graph as lg
from docx import Document  # ✅ Import python-docx
from app.services.srs_parser import parse_srs
from app.services.er_diagram_parser import analyze_er_diagram
from app.services.validator import validate_schemas
from app.services.storage import store_extracted_data

# Define workflow
workflow = lg.Graph()

workflow.add_node("parse_srs", parse_srs)
workflow.add_node("analyze_er_diagram", analyze_er_diagram)
workflow.add_node("validate_schemas", validate_schemas)
workflow.add_node("store_results", store_extracted_data)

workflow.set_entry_point("parse_srs")
workflow.add_edge("parse_srs", "analyze_er_diagram")
workflow.add_edge("analyze_er_diagram", "validate_schemas")
workflow.add_edge("validate_schemas", "store_results")

# Compile the workflow
graph = workflow.compile()

def process_files(srs_filename, er_filename):
    """Run the workflow when new files are uploaded."""
    try:
        # ✅ Use `python-docx` to read DOCX properly
        doc = Document(srs_filename)
        srs_content = "\n".join([paragraph.text for paragraph in doc.paragraphs])

        inputs = {
            "srs_filename": srs_filename,
            "er_filename": er_filename,
            "srs_content": srs_content
        }

        return graph.invoke(inputs)

    except Exception as e:
        raise Exception(f"❌ Error processing files: {str(e)}")
