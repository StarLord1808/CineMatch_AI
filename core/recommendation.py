from services.search import SearchService
from services.ranking import RankingService
from typing import List, Dict

class RecommendationEngine:
    """
    Core engine for generating movie recommendations.
    """
    def __init__(self):
        self.search_service = SearchService()
        self.ranking_service = RankingService()

    def get_recommendations(self, prompt: str, top_k: int = 5) -> List[Dict]:
        """
        Get recommendations for a user prompt.
        
        Args:
            prompt: User's natural language query.
            top_k: Number of movies to recommend.
            
        Returns:
            List of recommended movies (metadata + reason).
        """
        # 1. Search (Fetch more than k to allow for deduplication)
        # Fetching 3x top_k to ensure we have enough after deduplication
        raw_results = self.search_service.search(prompt, k=top_k * 3)
        
        # 2. Re-rank / Deduplicate
        deduped_results = self.ranking_service.deduplicate_by_movie(raw_results)
        
        # 3. Limit to top_k
        final_results = deduped_results[:top_k]
        
        return final_results

if __name__ == "__main__":
    # Quick CLI test
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", type=str, required=True)
    args = parser.parse_args()
    
    engine = RecommendationEngine()
    recs = engine.get_recommendations(args.query)
    
    print(f"\nTop Recommendations for: '{args.query}'\n")
    for i, rec in enumerate(recs, 1):
        print(f"{i}. {rec['metadata'].get('movie_title')} ({rec['metadata'].get('year')})")
        print(f"   Reason (Snippet): {rec['content'][:150]}...")
        print(f"   Distance: {rec['distance']:.4f}\n")
