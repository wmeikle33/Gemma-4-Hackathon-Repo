from dataclasses import dataclass
from pathlib import Path


@dataclass
class KnowledgeResult:
    source: str
    content: str
    score: int


class LocalKnowledgeBase:
    def __init__(self, knowledge_dir: Path) -> None:
        self.knowledge_dir = knowledge_dir

    def search(self, query: str, limit: int = 2) -> list[KnowledgeResult]:
        query_terms = set(query.lower().split())
        results: list[KnowledgeResult] = []

        for path in self.knowledge_dir.glob("*.md"):
            content = path.read_text(encoding="utf-8")
            content_terms = set(content.lower().split())
            score = len(query_terms & content_terms)

            if score > 0:
                results.append(
                    KnowledgeResult(
                        source=path.name,
                        content=content,
                        score=score,
                    )
                )

        return sorted(
            results,
            key=lambda result: result.score,
            reverse=
