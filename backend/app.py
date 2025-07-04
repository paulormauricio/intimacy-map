from flask import Flask, request, jsonify
from database import init_db, db
from models import Account, Stakeholder, Product, AccountProduct, Opportunity


def create_app():
    app = Flask(__name__)
    app.config['DATABASE_URI'] = 'postgresql://sam:sam@db:5432/sam'
    init_db(app)

    @app.route('/accounts', methods=['POST'])
    def create_account():
        data = request.json
        account = Account(name=data['name'], notes=data.get('notes',''))
        db.session.add(account)
        db.session.commit()
        return jsonify({'id': account.id, 'name': account.name}), 201

    @app.route('/accounts', methods=['GET'])
    def list_accounts():
        accounts = Account.query.all()
        return jsonify([{'id': a.id, 'name': a.name, 'health_score': a.health_score} for a in accounts])

    @app.route('/accounts/<int:account_id>/stakeholders', methods=['POST'])
    def add_stakeholder(account_id):
        data = request.json
        sh = Stakeholder(account_id=account_id, name=data['name'], role=data.get('role'),
                         influence=data.get('influence'), strength=data.get('strength'))
        db.session.add(sh)
        db.session.commit()
        return jsonify({'id': sh.id}), 201

    @app.route('/accounts/<int:account_id>/stakeholders', methods=['GET'])
    def list_stakeholders(account_id):
        stakeholders = Stakeholder.query.filter_by(account_id=account_id).all()
        return jsonify([{'id': s.id, 'name': s.name, 'role': s.role,
                        'influence': s.influence, 'strength': s.strength} for s in stakeholders])

    @app.route('/accounts/<int:account_id>/white_space', methods=['GET'])
    def white_space(account_id):
        products = Product.query.all()
        matrix = []
        for product in products:
            ap = AccountProduct.query.filter_by(account_id=account_id, product_id=product.id).first()
            matrix.append({'product': product.name, 'adopted': bool(ap and ap.adopted)})
        return jsonify(matrix)

    @app.route('/accounts/<int:account_id>/ai_insights', methods=['GET'])
    def ai_insights(account_id):
        # Placeholder for AI engine
        account = Account.query.get_or_404(account_id)
        insight = f"Consider engaging more stakeholders for {account.name}."
        return jsonify({'next_best_action': insight})

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0')
