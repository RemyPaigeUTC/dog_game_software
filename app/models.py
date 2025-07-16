from sqlalchemy import ForeignKey, String
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timezone
from typing import Optional, List
# general purpose database functions and classes such as types and query building helpers
import sqlalchemy as sa
# provides the support for using models
import sqlalchemy.orm as so
from app import db, login
from flask_login import UserMixin
from sqlalchemy import Integer, ForeignKey, Column, Table
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.orm import mapped_column, relationship

class DogInfo:
    registered_name: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True, unique=True)
    call_name: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    gender: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    living_status: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    breed: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    muzzle_length: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    muzzle_depth: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    dewlap: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    brow_ridge: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    brow_profile: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    bite: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    skull: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    head_width: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    stop: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    head_carriage: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    ear_length: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    ear_width: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    ear_carriage: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    eye_size: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    eye_shape: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    bone: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    build: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    back_length: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    back_shape: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    topline: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    neck_length: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    croup: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    chest_depth: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    chest_width: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    tuck: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    wrinkle: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    leg_length: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    front_angulation: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    rear_angulation: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    reach: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    drive: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    pasterns: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    feet: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    hind_dew_claws: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    tail_shape: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    tail_length: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    tail_set: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    tail_carriage: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    hairless: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    coat_length: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    furnishings: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    topknot: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    ear_fringe_type: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    ear_fringe_length: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    neck_ruff: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    body_coat: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    leg_feather: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    tail_plume: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    coat_curl: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    texture: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    undercoat: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    coat_lay: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    ridge: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    shedding: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    coat_type_genotype: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    eye_colour: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    pigment: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    nose_colour: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    coat_colour_genotype: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    coat_colour: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    immune_mediated_haemolytic_anaemia: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    dilated_cardiomyopathy: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    cardiomyopathy: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    endocardiosis: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    mitral_valve_dysplasia: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    patent_ductus_arteriosus: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    pulmonic_stenosis: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    ventricular_septal_defect: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    addisons_disease: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    autoimmune_thyroid_disease: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    diabetes_mellitus: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    cataracts_hereditary: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    corneal_dystrophy: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    distichiasis: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    entropion: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    keratoconjunctivitis_sicca: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    microphthalmia: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    persistent_pupillary_membranes: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    progressive_retinal_atrophy: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    retinal_dysplasia: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    vitreous_degeneration: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    chronic_hepatitis: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    exocrine_pancreatic_insufficiency: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    protein_losing_enteropathy: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    cervical_spondylomyelopathy: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    chondrodystrophy: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    elbow_dysplasia: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    hip_dysplasia: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    legg_calve_perthes_disease: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    muscular_dystrophy: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    myotonia_congenita: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    patellar_luxation: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    chiari_malformation: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    deafness_congenital: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    degenerative_myelopathy: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    epilepsy: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    hydrocephalus: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    cleft_palate: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    atopy: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    demodicosis: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    ichthyosis: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    cryptorchidism: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    primary_glomerulopathy: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    renal_dysplasia: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    umbilical_hernia: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    urolithiasis: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    haemophilia: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    von_willebrands_disease: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    portosystemic_shunt: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    choroidal_hypoplasia: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    optic_nerve_hypoplasia: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    primary_glaucoma: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    primary_lens_luxation: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    selective_iga_deficiency: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    craniomandibular_osteopathy: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    osteochondritis_dissecans: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    cerebellar_abiotrophy: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    exercise_induced_collapse: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    myasthenia_gravis: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    neuroaxonal_dystrophy: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    sensory_neuropathy: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    tracheal_collapse: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)
    follicular_dysplasia: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True)

@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))

followers = sa.Table(
    'followers',
    db.metadata,
    sa.Column('follower_id', sa.Integer, sa.ForeignKey('user.id'),
              primary_key=True),
    sa.Column('followed_id', sa.Integer, sa.ForeignKey('user.id'),
              primary_key=True)
)

class User(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True,
                                                unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True,
                                             unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    posts: so.WriteOnlyMapped['Post'] = so.relationship(
        back_populates='author')
    following: so.WriteOnlyMapped['User'] = so.relationship(
        secondary=followers, primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        back_populates='followers')
    followers: so.WriteOnlyMapped['User'] = so.relationship(
        secondary=followers, primaryjoin=(followers.c.followed_id == id),
        secondaryjoin=(followers.c.follower_id == id),
        back_populates='following')
    def __repr__(self):
        return '<User {}>'.format(self.username)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    def follow(self, user):
        if not self.is_following(user):
            self.following.add(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.following.remove(user)

    def is_following(self, user):
        query = self.following.select().where(User.id == user.id)
        return db.session.scalar(query) is not None

    def followers_count(self):
        query = sa.select(sa.func.count()).select_from(
            self.followers.select().subquery())
        return db.session.scalar(query)

    def following_count(self):
        query = sa.select(sa.func.count()).select_from(
            self.following.select().subquery())
        return db.session.scalar(query)

class Post(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    body: so.Mapped[str] = so.mapped_column(sa.String(140))
    timestamp: so.Mapped[datetime] = so.mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc))
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id),
                                               index=True)

    author: so.Mapped[User] = so.relationship(back_populates='posts')

    def __repr__(self):
        return '<Post {}>'.format(self.body)
# followers = sa.Table(
#     'followers',
#     db.metadata,
#     sa.Column('follower_id', sa.Integer, sa.ForeignKey('user.id'),
#               primary_key=True),
#     sa.Column('followed_id', sa.Integer, sa.ForeignKey('user.id'),
#               primary_key=True)
# )
relationships = sa.Table(
    'relationships',
    db.metadata,
    sa.Column('parent_to_dog_id', sa.Integer, sa.ForeignKey('dog.id'),
              primary_key=True),
    sa.Column('child_of_dog_id', sa.Integer, sa.ForeignKey('dog.id'),
              primary_key=True)
)
# followers = parent_to = follower
# following = child_of = followed
class Dog(db.Model, DogInfo):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    # following: so.WriteOnlyMapped['User'] = so.relationship(
    #     secondary=followers,
    #     primaryjoin=(followers.c.follower_id == id),
    #     secondaryjoin=(followers.c.followed_id == id),
    #     back_populates='followers')
    # followers: so.WriteOnlyMapped['User'] = so.relationship(
    #     secondary=followers,
    #     primaryjoin=(followers.c.followed_id == id),
    #     secondaryjoin=(followers.c.follower_id == id),
    #     back_populates='following')
    child_of: so.WriteOnlyMapped['Dog'] = so.relationship(
        secondary=relationships,
        primaryjoin=(relationships.c.parent_to_dog_id == id),
        secondaryjoin=(relationships.c.child_of_dog_id == id),
        back_populates='parent_to')
    parent_to: so.WriteOnlyMapped['Dog'] = so.relationship(
        secondary=relationships,
        primaryjoin=(relationships.c.child_of_dog_id == id),
        secondaryjoin=(relationships.c.parent_to_dog_id == id),
        back_populates='child_of')


    def become_parent_to(self, dog):
        if not self.is_parent_to(dog):
            self.parent_to.add(dog)

    def set_child_of(self, dog):
        self.child_of.add(dog)

    def undo_become_parent_to(self, dog):
        if self.is_parent_to(dog):
            self.parent_to.remove(dog)

    def is_parent_to(self, dog):
        query = self.parent_to.select().where(Dog.id == dog.id)
        return db.session.scalar(query) is not None

    def count_children(self):
        query = sa.select(sa.func.count()).select_from(
            self.parent_to.select().subquery())
        return db.session.scalar(query)

    def count_parents(self):
        query = sa.select(sa.func.count()).select_from(
            self.child_of.select().subquery())
        return db.session.scalar(query)

    def list_children(self):
        query = self.parent_to.select()
        return db.session.execute(query).all()
    def list_parents(self):
        query = self.child_of.select()
        return db.session.execute(query).all()



