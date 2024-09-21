# tests/unit/test_rag_pipeline.py

import unittest
from ragstack.rag.pipeline import RAGPipeline
from ragstack.vectorstores.inmemory import InMemoryVectorStore
from ragstack.llm.dummy import DummyLLM

class TestRAGPipeline(unittest.TestCase):
    def test_rag_pipeline_run(self):
        vector_store = InMemoryVectorStore()
        llm = DummyLLM()
        pipeline = RAGPipeline(vector_store, llm, "{query}\n\nContext: {context}")

        query = "Test query"
        response = pipeline.run(query)
        self.assertIsNotNone(response)
        self.assertIn(query, response)

if __name__ == '__main__':
    unittest.main()