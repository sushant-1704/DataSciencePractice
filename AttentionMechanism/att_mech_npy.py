import numpy as np

# Create/Open the file in write mode
with open("attention_results.txt", "w") as f:

    # ----- Step 1: Create dummy Query, Key, Value -----
    np.random.seed(42)  # for reproducibility

    # Example: 1 query, 3 keys/values, dimension=4
    Q = np.random.rand(1, 4)   # shape (1, d_k)
    K = np.random.rand(3, 4)   # shape (n_k, d_k)
    V = np.random.rand(3, 4)   # shape (n_k, d_v)

    f.write("Query (Q):\n{}\n\n".format(Q))
    f.write("Keys (K):\n{}\n\n".format(K))
    f.write("Values (V):\n{}\n\n".format(V))

    # ----- Step 2: Calculate QK^T -----
    scores = np.dot(Q, K.T)
    f.write("Step 1 - Raw Scores (QK^T):\n{}\n\n".format(scores))

    # ----- Step 3: Scale scores by sqrt(d_k) -----
    d_k = K.shape[1]
    scaled_scores = scores / np.sqrt(d_k)
    f.write("Step 2 - Scaled Scores:\n{}\n\n".format(scaled_scores))

    # ----- Step 4: Apply softmax -----
    def softmax(x):
        exp_x = np.exp(x - np.max(x))  # stability trick
        return exp_x / np.sum(exp_x, axis=1, keepdims=True)

    attention_weights = softmax(scaled_scores)
    f.write("Step 3 - Attention Weights (Softmax):\n{}\n\n".format(attention_weights))

    # ----- Step 5: Multiply weights by V -----
    output = np.dot(attention_weights, V)
    f.write("Step 4 - Final Output:\n{}\n\n".format(output))

print("✅ Results saved to 'attention_results.txt' . It’s the summary the model will use for the next step in making predictions.")