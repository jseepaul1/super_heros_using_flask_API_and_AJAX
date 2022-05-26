from flask_app.config.mysqlconnection import connectToMySQL
my_db ="superheroes"

class Superhero:
    def __init__(self, superhero_data):
        self.id = superhero_data['id']
        self.name = superhero_data['name']
        self.created_at = superhero_data['created_at']
        self.updated_at = superhero_data['updated_at']

    @classmethod
    def search_superhero(cls, data):
        query = "INSERT INTO superheroes (name) VALUES (%(name)s);"
        return connectToMySQL(my_db).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM superheroes;"

        superhero_results = connectToMySQL(my_db).query_db(
            query
        )
        superheroes = []
        for superhero in superhero_results:
            superheroes.append(cls(superhero))
        return superheroes
