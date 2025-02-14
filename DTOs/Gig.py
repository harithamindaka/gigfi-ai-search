class GigDTO:
    def __init__(self, gigId, sellerId, title, duration, description, rating, price, score=0):
        self.gigId = gigId
        self.sellerId = sellerId
        self.title = title
        self.duration = duration
        self.description = description
        self.rating = rating
        self.price = price
        self.score = score
        

    def to_dict(self):
        """Convert DTO to dictionary"""
        return {
            "gig_id": self.gigId,
            "seller_id": self.sellerId,
            "title": self.title,
            "duration": self.duration,
            "description": self.description,
            "rating": self.rating,
            "price": self.price,
            "score": self.score
        }


    def set_score(self, score):
        self.score = score
        return 
    
    def get_result_dict(self):
        return {
            "gig_id": self.gigId,
            "seller_id": self.sellerId,
            "title": self.title,
            "duration": self.duration,
            "description": self.description,
            "rating": self.rating,
            "price": self.price,
            "score": self.score
        }


    @classmethod
    def from_dict(cls, data: dict):
        """Create DTO from dictionary"""
        return cls(
            gigId=data.get("gig_id"),
            sellerId=data.get("seller_id"),
            title=data.get("title"),
            duration = data.get("duration"),
            description = data.get("description"),
            rating = data.get("rating"),
            price = data.get("price"),
            score = data.get("score"),
        )
