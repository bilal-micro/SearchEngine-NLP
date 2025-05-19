from sentence_transformers import SentenceTransformer
import numpy as np
import csv
from sklearn.metrics.pairwise import cosine_similarity



class Engine:
    vectors_np = []
    products_vector = []   
    model = None

    @staticmethod
    def train():
        vectors = []
        try:
            Engine.model = SentenceTransformer("intfloat/multilingual-e5-small")
            with open("product_vectors.txt", "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split(',')
                    pid = parts[0]
                    name = parts[1]
                    vector = np.array([float(x) for x in parts[2].split()])
                    Engine.products_vector.append((int(pid), name))
                    vectors.append(vector)
            Engine.vectors_np = np.stack(vectors)
            print("✅ Loaded embeddings from product_vectors.txt")
        except:
            # print("Error.")
            return
        
    @staticmethod
    def train_all(file_path):
        products = []
        if Engine.model is None:
            return
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if row:
                    pid = row[0]
                    name = f"{row[1]} {row[2]} {row[3]}"
                    products.append((pid, name))

        product_names = [name for _, name in products]
        embeddings = Engine.model.encode(product_names, convert_to_numpy=True)
        with open("product_vectors.txt", "w", encoding="utf-8") as f:
            for (pid, name), vector in zip(products, embeddings):
                vector_str = " ".join([f"{v:.6f}" for v in vector])
                f.write(f"{pid},{name},{vector_str}\n")

    @staticmethod
    def add_new_product(product):
        if Engine.model is None:
            return
        embedding = Engine.model.encode([product.title], convert_to_numpy=True)  
        embedding_str = " ".join([f"{v:.6f}" for v in embedding[0]])
        with open("product_vectors.txt", "a", encoding="utf-8") as f:
            f.write(f"{product.id},{product.title},{embedding_str}\n")

    @staticmethod
    def remove_product(product_id):
        lines_kept = []
        removed = False
        if Engine.model is None:
            return
        with open("product_vectors.txt", "r", encoding="utf-8") as f:
            for line in f:
                if line.strip().startswith(f"{product_id},"):
                    removed = True
                    continue
                lines_kept.append(line)
        if removed:
            with open("product_vectors.txt", "w", encoding="utf-8") as f:
                f.writelines(lines_kept)
        return removed
    
    @staticmethod
    def search_product(data , k = 5):
        if Engine.model is None:
            return []
        try:
            query_vec = Engine.model.encode([data], convert_to_numpy=True)

            similarities = cosine_similarity(query_vec, Engine.vectors_np)[0]  

            top_k = k * 2
            # * 2 to get same user requestd number
            top_indices = similarities.argsort()[-top_k:][::-1]

            results = []
            for idx in top_indices:
                pid, name = Engine.products_vector[idx]
                results.append(pid)
            
            return results
        except:
            return []