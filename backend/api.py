# Eclipse CHE Project , i love you xixix
import redis
from flask import Flask
from flask_restful import Resource, Api

# Instantiate the app
app = Flask(__name__)
api = Api(app)
data = [
    {
        "id": "2baf70d1-42bb-4437-b551-e5fed5a87abe",
        "title": "Castle in the Sky",
        "description": "The orphan Sheeta inherited a mysterious crystal that links her to the mythical sky-kingdom of Laputa. With the help of resourceful Pazu and a rollicking band of sky pirates, she makes her way to the ruins of the once-great civilization. Sheeta and Pazu must outwit the evil Muska, who plans to use Laputa's science to make himself ruler of the world.",
        "director": "Hayao Miyazaki",
        "producer": "Isao Takahata",
        "release_date": "1986"
    },
    {
        "id": "12cfb892-aac0-4c5b-94af-521852e46d6a",
        "title": "Grave of the Fireflies",
        "description": "In the latter part of World War II, a boy and his sister, orphaned when their mother is killed in the firebombing of Tokyo, are left to survive on their own in what remains of civilian life in Japan. The plot follows this boy and his sister as they do their best to survive in the Japanese countryside, battling hunger, prejudice, and pride in their own quiet, personal battle.",
        "director": "Isao Takahata",
        "producer": "Toru Hara",
        "release_date": "1988"
    }
]
class Product(Resource):
    def get(self):
        encoding = 'utf-8'
        # here host can use the docker-compose defined service name or the docker network ip address
        # r = redis.Redis(host='redis', port=6379)
        # r = redis.Redis(host='192.168.16.4', port=6379)
        r = redis.Redis(host='devkeliuredis2.marathon.l4lb.thisdcos.directory', port=6379)
        ke = dict()
        ke['id'] = r.get('keliu').decode(encoding)
        ke['title'] = "ke's testing"
        ke['description'] = r.get('keliu').decode(encoding)
        data.append(ke)
        return data

# Create routes
api.add_resource(Product, '/mymovies/')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)