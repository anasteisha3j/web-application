from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Image
from . import db
import json
from io import BytesIO
from PIL import Image as PILImage
#import base64

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
         image_file = request.files.get('image')  
         if image_file:
            img = PILImage.open(image_file)
            img = img.convert("RGB")

            img = img.crop((0, 0, 200, 200))

            img_byte_arr = BytesIO()
            img.save(img_byte_arr, format='JPEG')
            img_byte_arr.seek(0)

            new_image = Image(picture=img_byte_arr.read(), user_id=current_user.id)
            db.session.add(new_image)
            db.session.commit()
            flash('Image uploaded!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-img', methods=['POST'])
def delete_img():
    img_data = json.loads(request.data) 
    img_id = img_data['imgID']
    image = Image.query.get(img_id)
    
    if image:
        if image.user_id == current_user.id:
            db.session.delete(image)
            db.session.commit()
            flash('Image deleted!', category='success')

    return jsonify({})  
