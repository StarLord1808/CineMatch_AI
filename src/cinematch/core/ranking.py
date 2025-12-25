from typing import List, Dict

class RankingService:
    """
    Service to re-rank, filter, and deduplicate search results.
    """
    
    @staticmethod
    def deduplicate_by_movie(results: List[Dict]) -> List[Dict]:
        """
        Ensures only one result per movie is returned (the best matching review).
        
        Args:
            results: List of search results from SearchService.
            
        Returns:
            Deduplicated list of results.
        """
        seen_movies = set()
        unique_results = []
        
        for result in results:
            movie_title = result['metadata'].get('movie_title')
            
            # If movie_title is missing, treat as unique review
            if not movie_title:
                unique_results.append(result)
                continue
                
            if movie_title not in seen_movies:
                seen_movies.add(movie_title)
                unique_results.append(result)
        
        return unique_results

    @staticmethod
    def filter_by_score(results: List[Dict], threshold: float = 0.5) -> List[Dict]:
        """
        Filter out results that are too far (large L2 distance).
        Note: For L2 distance, lower is better. 
        So we filter where distance > threshold.
        Adjust threshold based on empirical testing.
        """
        # TODO: Calibrate threshold for L2 vs Cosine. 
        # For now, let's just return all, or implement a soft cut-off.
        return [r for r in results if r['distance'] < threshold]
