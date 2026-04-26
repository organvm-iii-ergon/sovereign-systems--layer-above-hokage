# Pillar 3: Algorithmic Interface

## Purpose

To build the knowledge extraction, embedding, and retrieval system that powers Sovereign.

**Core Questions**:
1. How do we extract relevant clips from session transcripts?
2. How do we embed and retrieve knowledge?
3. How do we evaluate the interface?

---

## Reading Ladder (Progressive Depth)

### Level 1: Foundations (Weeks 1-2)

| Source | Author | Year | Core Concept | Time |
|-------|--------|------|---|---|
| *Attention Is All You Need* | Vaswani et al. | 2017 | Transformer architecture | 8h |
| *BERT* | Devlin et al. | 2019 | Pre-training + fine-tuning | 4h |
| *Sentence Transformers* | Reimers & Gurevych | 2019 | SBERT | 4h |
| *CLIP* | Radford et al. | 2021 | Vision-language alignment | 6h |

**Total**: 22 hours

**Deliverable**: Your first embedding pipeline

### Level 2: Retrieval Methods (Weeks 3-4)

| Source | Author | Year | Core Concept | Time |
|-------|--------|------|---|---|
| *Dense Passage Retrieval* | Karpukhin et al. | 2020 | DPR | 6h |
| *ColBERT* | Khattab & Zaher | 2020 | Late interaction | 6h |
| *ANCE* | Xiong et al. | 2021 | Approximate nearest neighbor | 6h |
| *BPR* | Yoo et al. | 2022 | Bi-encoder reranking | 4h |

**Total**: 22 hours

**Deliverable**: Working retrieval system

### Level 3: Evaluation (Weeks 5-6)

| Source | Author | Year | Core Concept | Time |
|-------|--------|------|---|---|
| *BEIR* | Thakur et al. | 2021 | Retrieval benchmarks | 4h |
| *MTEB* | Muennighoff et al. | 2022 | Embedding benchmarks | 4h |
| *LoTTE* | Santos et al. | 2023 | Long-tail evaluation | 4h |
| *MARCO* | Nguyen et al. | 2016 | Ranking metrics deep dive | 4h |

**Total**: 16 hours

**Deliverable**: Evaluation framework

---

## Experiment Templates

### Template 1: Clip Extraction

```yaml
# experiment-templates/clip-extraction.yaml
name: sovereign_clip_extraction
type: semantic_extraction
version: "1.0"

purpose: >
  Extract relevant clips from session transcripts

input:
  transcript:
    format: markdown
    source: session logs
  
  query:
    type: question or keyword_list

processing:
  chunking:
    method: sliding_window
    chunk_size: 512
    overlap: 50
  
  embedding:
    model: bge-large-en-v1.5
    normalize: true
    batch_size: 32

retrieval:
  method: cosine_similarity
  top_k: 5
  threshold: 0.7

output:
  clips:
    - text
    - score
    - context_window

metrics:
  - relevance_precision_at_k
  - coverage
  - redundancy_rate
```

### Template 2: Embedding Similarity

```yaml
# experiment-templates/embedding-similarity.yaml
name: sovereign_embedding_similarity
type: embedding_evaluation
version: "1.0"

purpose: >
  Evaluate embedding quality on knowledge tasks

datasets:
  - name: session_qa
    source: historical_sessions
    size: 1000
    splits: [train, test]
  
  - name: domain_similarity
    source: domain_pairs
    size: 500

models:
  - bge-large-en-v1.5
  - bge-base-en-v1.5
  - e5-large-v2
  - sentence-transformers/all-MiniLM-L6-v2

metrics:
  semantic_similarity:
    - spearman_corr
    - pearson_corr
  
  task_performance:
    - retrieval_ndcg@10
    - classification_f1
    - clustering_ari

analysis:
  - per-domain_breakdown
  - failure_modes
  - embedding_distribution
```

### Template 3: Retrieval Evaluation

```yaml
# experiment-templates/retrieval-evaluation.yaml
name: sovereign_retrieval_eval
type: retrieval_benchmark
version: "1.0"

purpose: >
  Evaluate retrieval system on Sovereign queries

corpus:
  sessions_from: 2024-01-01
  size: 10000
  indexing: milvus

queries:
  - vacuum_detection_queries
  - coordination_queries
  - operator_queries

metrics:
  retrieval:
    - recall@1
    - recall@5
    - recall@10
    - ndcg@10
    - mrr
  
  reranking:
    - precision@1
    - diversity@k

baselines:
  - bm25
  - dpr
  - colbert
  - ours
```

---

## Algorithmic Core

### CLIP-Based Clip Extraction

```python
# clip_extraction.py
import numpy as np
from sentence_transformers import SentenceTransformer
from dataclasses import dataclass

@dataclass
class ExtractedClip:
    text: str
    score: float
    position: tuple[int, int]  # start, end

class ClipExtractor:
    """
    Extract relevant clips from transcripts using embeddings.
    """
    
    def __init__(
        self, 
        model_name: str = "bge-large-en-v1.5",
        chunk_size: int = 512,
        overlap: int = 50
    ):
        self.model = SentenceTransformer(model_name)
        self.chunk_size = chunk_size
        self.overlap = overlap
    
    def extract(
        self,
        transcript: str,
        query: str,
        top_k: int = 5,
        score_threshold: float = 0.7
    ) -> list[ExtractedClip]:
        """Extract top-k relevant clips."""
        
        # 1. Chunk transcript
        chunks = self._chunk_transcript(transcript)
        
        # 2. Embed query and chunks
        query_emb = self.model.encode(query)
        chunk_embs = self.model.encode(chunks)
        
        # 3. Compute similarities
        similarities = self._cosine_similarity(query_emb, chunk_embs)
        
        # 4. Get top-k
        top_indices = np.argsort(similarities)[-top_k:]
        
        # 5. Build clips
        clips = []
        for idx in top_indices:
            if similarities[idx] >= score_threshold:
                clips.append(ExtractedClip(
                    text=chunks[idx],
                    score=similarities[idx],
                    position=(idx, idx + len(chunks[idx]))
                )
        
        return sorted(clips, key=lambda x: x.score, reverse=True)
    
    def _chunk_transcript(self, transcript: str) -> list[str]:
        """Chunk transcript into overlapping segments."""
        words = transcript.split()
        chunks = []
        
        for i in range(0, len(words), self.chunk_size - self.overlap):
            chunk = ' '.join(words[i:i + self.chunk_size])
            if chunk:
                chunks.append(chunk)
        
        return chunks
    
    def _cosine_similarity(
        self, 
        a: np.ndarray, 
        b: np.ndarray
    ) -> np.ndarray:
        """Compute cosine similarity."""
        a_norm = a / np.linalg.norm(a)
        b_norm = b / np.linalg.norm(b, axis=1, keepdims=True)
        return np.dot(b_norm, a_norm)
```

### Late Interaction Retrieval (ColBERT-style)

```python
# late_interaction.py
import torch
import torch.nn.functional as F

class LateInteractionRetriever:
    """
    ColBERT-style late interaction retrieval.
    Each token gets a context vector, 
    interaction happens at query time.
    """
    
    def __init__(self, model_name: str = "colbert-ir/colbertv2"):
        self.model = SentenceTransformer(model_name)
        self.dim = self.model.get_sentence_embedding_dimension()
    
    def index(self, documents: list[str]) -> np.ndarray:
        """Index documents as token-level embeddings."""
        
        # Get token embeddings
        token_embs = self.model.encode(
            documents, 
            convert_to_tensor=True,
            tokenize=True
        )
        
        # [num_docs, max_tokens, dim]
        return token_embs
    
    def score(
        self, 
        query_embs: torch.Tensor,
        doc_embs: torch.Tensor
    ) -> torch.Tensor:
        """
        MaxSim: max similarity over query tokens.
        """
        # [1, query_len, dim] -> [query_len, 1, dim]
        # [num_docs, doc_len, dim] -> [1, doc_len, dim]
        
        # Similarity matrix
        sim = torch.matmul(
            query_embs.unsqueeze(0),
            doc_embs.unsqueeze(1)
        )
        
        # Max over doc tokens for each query token
        max_sim = sim.max(dim=2).values
        
        # Mean over query tokens
        scores = max_sim.mean(dim=1)
        
        return scores
```

---

## ROS Specification

### What We Need to Prove

| Claim | Evidence Required | Method |
|-------|----------------|--------|
| Clips capture meaning | Human eval of relevance | Validation |
| Retrieval finds gaps | Vacuum detection hits | A/B test |
| Embeddings are stable | Bootstrap CI | Repeated embedding |
| Interface is fast | Latency < 100ms | Load test |

### Quality Gates

| Gate | Threshold |
|---|---|
| Retrieval recall@10 | > 0.80 |
| NDCG@10 | > 0.70 |
| Latency P99 | < 100ms |
| Relevance score | Human eval > 4/5 |

---

## Decision Log

| Date | Decision | Rationale |
|---|---|---|
| 2026-04-26 | Algorithmic interface as pillar 3 | Knowledge extraction |
| 2026-04-26 | CLIP extraction | Semantic matching |
| 2026-04-26 | Late interaction | Better reranking |
| 2026-04-26 | MTEB benchmarks | Standard evaluation |

---

*Every query needs a proven answer. Every answer needs a citation.*