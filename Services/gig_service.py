from DTOs.Gig import GigDTO

class GigService:
    def __init__(self):
        self.results = []

    def extract_results(self, results):
        formatted_results = []
        for result in results:
            formatted_result = {
                "score": result["@search.reranker_score"],
                "title": result["Title"],
                "description": result["Description"],
                "rating": result["Rating"],
                "price": result["Price"],
                "gig_id": result["Gig_ID"],
                "seller_id": result["Seller_ID"],
                "duration": result["Duration"],
                "tags": result["Tags"]
            }

            # captions = result["@search.captions"]
            # if captions:
            #     caption = captions[0]
            #     if caption.highlights:
            #         formatted_result["caption"] = caption.highlights
            #     else:
            #         formatted_result["caption"] = caption.text
            # formatted_results.append(formatted_result)

            result_dto = GigDTO.from_dict(formatted_result)
            self.results.append(result_dto)
        
        return self.results

    def get_results_as_dict(self):
        return [result.get_result_dict() for result in self.results]