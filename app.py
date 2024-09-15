from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory storage for FAQs
faqs = [
    {"id": 1, "question": "What is an apple?", "answer": "An apple is a fruit."},
    {"id": 2, "question": "What is a banana?", "answer": "A banana is a fruit."}
]

# Get all FAQs
@app.route('/faqs', methods=['GET'])
def get_faqs():
    return jsonify(faqs)

# Get FAQ by ID
@app.route('/faqs/<int:faq_id>', methods=['GET'])
def get_faq(faq_id):
    faq = next((f for f in faqs if f['id'] == faq_id), None)
    if faq:
        return jsonify(faq)
    return jsonify({"error": "FAQ not found"}), 404

# Create a new FAQ
@app.route('/faqs', methods=['POST'])
def create_faq():
    data = request.json
    new_faq = {
        "id": len(faqs) + 1,
        "question": data['question'],
        "answer": data['answer']
    }
    faqs.append(new_faq)
    return jsonify(new_faq), 201

# Update FAQ by ID
@app.route('/faqs/<int:faq_id>', methods=['PUT'])
def update_faq(faq_id):
    faq = next((f for f in faqs if f['id'] == faq_id), None)
    if faq:
        data = request.json
        print(f"Received data for update: {data}")  # Debug print
        faq['question'] = data.get('question', faq['question'])
        faq['answer'] = data.get('answer', faq['answer'])
        return jsonify(faq)
    return jsonify({"error": "FAQ not found"}), 404

# Delete FAQ by ID
@app.route('/faqs/<int:faq_id>', methods=['DELETE'])
def delete_faq(faq_id):
    print(f"Attempting to delete FAQ with ID: {faq_id}")  # Debug print
    global faqs
    faq = next((f for f in faqs if f['id'] == faq_id), None)
    if faq:
        faqs = [f for f in faqs if f['id'] != faq_id]
        return jsonify({"message": "FAQ deleted"}), 200
    return jsonify({"error": "FAQ not found"}), 404

if __name__ == '_main_':
    app.run(debug=True)