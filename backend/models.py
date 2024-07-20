class User(db.Model):
    """User Model"""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)  # Increased length
    name = db.Column(db.String(120), nullable=False)
    user_type = db.Column(db.String(50))  # "individual" or "company"
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))  # New field

    def set_password(self, password):
        """Set hashed password."""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.name}>'

class Company(db.Model):
    """Company Model"""
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(120), unique=True, nullable=False)
    contact_email = db.Column(db.String(120), unique=True, nullable=False)
    contact_number = db.Column(db.String(20))
    users = db.relationship('User', backref='company', lazy=True)

    def __repr__(self):
        return f'<Company {self.company_name}>'