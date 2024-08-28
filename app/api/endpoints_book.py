from flask_restx import Namespace, Resource, fields
from flask import request
from app.models import Book
from app.api.serializers_book import BookSchema
from app.extensions import db


api = Namespace('books', description='Operações relacionadas a livros')

book_model = api.model('Book', {
    'id': fields.Integer(readOnly=True),
    'name': fields.String(required=True),
    'description': fields.String(required=True),
    'author': fields.String(required=True),
    'rate': fields.Float(required=True),
    'image': fields.String(required=False),
})

book_schema = BookSchema()
books_schema = BookSchema(many=True)

@api.route('/')
class BookListResource(Resource):
    @api.doc('list_books')
    @api.marshal_list_with(book_model)
    def get(self):
        """
        Retorna uma lista de livros
        """
        return book_schema.dump(Book.query.all())
    
    @api.expect(book_model)
    @api.marshal_with(book_model, code=201)
    def post(self):
        """ 
        Cria um novo livro
        """
        data = request.get_json()
        book_data = book_schema.load(data)
        new_book = Book(**book_data)
        db.session.add(new_book)
        db.session.commit()
        return book_schema.dump(new_book), 201
    
@api.route('/<int:book_id>')
class BookResource(Resource):
    @api.doc('get_book')
    @api.marshal_with(book_model)
    def get(self, id):
        """
        Retorna um livro pelo id
        """
        return book_schema.dump(Book.query.get_or_404(id))
    
    @api.expect(book_model)
    @api.marshal_with(book_model)
    def put(self, id):
        """
        Atualiza um livro pelo id
        """
        book = Book.query.get_or_404(id)
        data = request.get_json()
        book_data = book_schema.load(data, instance=book, partial=True)
        for key, value in book_data.items():
            setattr(book, key, value)
        db.session.commit()
        return book_schema.dump(book)
    
    @api.response(204, 'Book deleted')
    def delete(self, id):
        """
            Deleta um livro pelo id
        """
        book = Book.query.get_or_404(id)
        db.session.delete(book)
        db.session.commit()
        return '', 204
    
