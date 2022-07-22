from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)


video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required")
video_put_args.add_argument("views", type=int, help="views of the video")
video_put_args.add_argument("likes", type=int, help="likes of the video")

videos = {}

class Video(Resource):
    def get(self, video_id):
        return videos[video_id], 200
    
    def put(self, video_id):
        print(request.form)
        args = video_put_args.parse_args()
        # videos[video_id] = args
        return {"videos_id": args}

api.add_resource(Video, "/video/<int:video_id>")
                                # could be in or array
# api.add_resource(HelloWorld, "/helloworld/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)