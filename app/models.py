from app import db
from datetime import datetime

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    # Add other project-specific fields here

    # Relationships
    measurements = db.relationship('Measurement', backref='project', lazy=True)

    def __repr__(self):
        return f'<Project {self.name}>'

class Measurement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    footings_lf = db.Column(db.Float)
    foundation_lf = db.Column(db.Float)
    garage_sf = db.Column(db.Float)
    basement_sf = db.Column(db.Float)
    living_area_sf = db.Column(db.Float)
    garage_wall_lf = db.Column(db.Float)
    outside_wall_lf = db.Column(db.Float)
    common_wall_lf = db.Column(db.Float)
    plumbing_wall_lf = db.Column(db.Float)
    interior_wall_lf = db.Column(db.Float)
    outside_wall_sf = db.Column(db.Float)
    gable_sf = db.Column(db.Float)
    roof_perimeter_lf = db.Column(db.Float)
    roof_sf = db.Column(db.Float)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # Relations
    project = db.relationship('Project', backref=db.backref('measurements', lazy=True))

    def __repr__(self):
        return f'<Measurement for Project ID {self.project_id}>'

# You can define more models here as needed
