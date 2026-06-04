import os
from openai import OpenAI
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -----------------------------
# Configuration
# -----------------------------
DATA_FOLDER = "../Data"
OPENAI_MODEL = "gpt-3.5-turbo"

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# -----------------------------
# Load documents
# -----------------------------
def load_documents(folder_path):
    documents = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            full_path = os.path.join(folder_path, filename)
            with open(full_path, "r", encoding="utf-8") as f:
                text = f.read()
                documents.append({
                    "filename": filename,
                    "content": text
                })
    return documents

# -----------------------------
# Chunk documents
# -----------------------------
def chunk_text(text, chunk_size=300):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])
    return chunks

# -----------------------------
# Build knowledge base
# -----------------------------
def build_knowledge_base(documents):
    chunk_records = []

    for doc in documents:
        chunks = chunk_text(doc["content"])
        for chunk in chunks:
            chunk_records.append({
                "source": doc["filename"],
                "text": chunk
            })

    texts = [record["text"] for record in chunk_records]
    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(texts)

    return chunk_records, vectorizer, matrix

# -----------------------------
# Retrieve relevant chunks
# -----------------------------
def retrieve_chunks(query, chunk_records, vectorizer, matrix, top_k=3):
    query_vec = vectorizer.transform([query])
    scores = cosine_similarity(query_vec, matrix)[0]

    ranked_indices = scores.argsort()[::-1][:top_k]

    results = []
    for idx in ranked_indices:
        results.append(chunk_records[idx])
    return results

# -----------------------------
# LLM answer without retrieval
# -----------------------------
def answer_without_retrieval(query):
    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an AI Portfolio Copilot for a wealth manager. "
                    "Answer professionally. If information is missing, say so."
                )
            },
            {"role": "user", "content": query}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content

# -----------------------------
# LLM answer with retrieval
# -----------------------------
def answer_with_retrieval(query, retrieved_chunks):
    context = "\n\n".join([
        f"Source: {chunk['source']}\n{chunk['text']}"
        for chunk in retrieved_chunks
    ])

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an AI Portfolio Copilot for a wealth manager. "
                    "Use only the provided context. "
                    "If the context is insufficient, explicitly say so. "
                    "Do not fabricate portfolio facts."
                )
            },
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion: {query}"
            }
        ],
        temperature=0.2
    )
    return response.choices[0].message.content

# -----------------------------
# Main
# -----------------------------
def main():
    documents = load_documents(DATA_FOLDER)
    chunk_records, vectorizer, matrix = build_knowledge_base(documents)

    test_questions = [
        "Why did this portfolio underperform last quarter?",
        "Is this portfolio suitable for a moderate-risk client?",
        "What should I discuss with the client in the next review meeting?",
        "What is the gold allocation in this portfolio?"
    ]

    print("Phase 4 - Retrieval Augmented Portfolio Copilot")
    print("=" * 70)

    for question in test_questions:
        print(f"\nQUESTION: {question}")
        print("-" * 70)

        print("WITHOUT RETRIEVAL:")
        answer1 = answer_without_retrieval(question)
        print(answer1)

        print("\nRETRIEVED CHUNKS:")
        retrieved = retrieve_chunks(question, chunk_records, vectorizer, matrix, top_k=3)
        for i, chunk in enumerate(retrieved, start=1):
            print(f"\nChunk {i} | Source: {chunk['source']}")
            print(chunk["text"])

        print("\nWITH RETRIEVAL:")
        answer2 = answer_with_retrieval(question, retrieved)
        print(answer2)

        print("\n" + "=" * 70)

if __name__ == "__main__":
    main()