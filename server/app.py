#!/usr/bin/env python3

from flask import request, jsonify
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

import os
from config import create_app, db, api
from models import Book, BookSchema

env = os.getenv("FLASK_ENV", "dev")
app = create_app(env)

class Books(Resource):
    def get(self):
        # Get pagination parameters from query string, with defaults
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 5, type=int)

        # paginate method
        pagination = Book.query.paginate(page=page, per_page=per_page, error_out=False)
        books = BookSchema(many=True).dump(pagination.items)

        # repsonse with metadata
        response = {
            "page": page,
            "per_page": per_page,
            "total": pagination.total,
            "total_pages": pagination.pages,
            "items": books
        }
        return response, 200

api.add_resource(Books, '/books', endpoint='books')

if __name__ == '__main__':
    app.run(port=5555, debug=True)