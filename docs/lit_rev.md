# Literature review

Remember: you are building an argument, not a library.

## Summary

Quickly summarize the literature you have found, followed by the most important or useful references.

## Articles

NV-Embed: Improved Techniques for Training LLMs as Generalist Embedding Models

- improves text embedding LLM model
- uses latent attention layer on top on decoder-only LLM
- improves MTEB benchmark
- NVIDIA project

Gecko: Versatile Text Embeddings Distilled from Large Language Models

- compact distilled text embedding LLM
- google deepmind project
- trained on range of tasks
- good MTEB performance

Scaling and evaluating sparse autoencoders

- openai project
- Sparse autoencoders provide a promising unsupervised approach for extracting in-
  terpretable features from a language model by reconstructing activations from a
  sparse bottleneck layer. 
- Training method for large sparse autoencoders, for finding circuits and concept features from LLMs

Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models

- These are causally implicated subnetworks of human-interpretable features
  for explaining language model behaviors
- LLM interpretability based on linear approximations of sparse features extracted from LLMs SAE

Toy Models of Superposition

- anthropic project
-  to investigate how and when models represent more features than they have dimensions. We call this phenomenon **superposition** 
- In our toy models, we are able to demonstrate that:
  - **Superposition is a real, observed phenomenon**.
  - **Both monosemantic and polysemantic neurons can form.**
  - **At least some kinds of computation can be performed in superposition.**
  - **Whether features are stored in superposition is** **governed by a phase change****.** 
  - **Superposition organizes features into geometric structures** such as digons, triangles, pentagons, and tetrahedrons.

Towards Monosemanticity: Decomposing Language Models With Dictionary Learning

- using SAE to learn monosemantic features from LLMs

Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet